#!/usr/bin/env python3
"""
Test different methods to bypass Cloudflare Turnstile on KenPom.

Methods tested:
1. playwright-stealth
2. Custom browser context with realistic fingerprint
3. Slower interaction timing
"""
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

def test_playwright_stealth():
    """Test using playwright-stealth to bypass Cloudflare."""
    print("\n" + "="*80)
    print("METHOD 1: playwright-stealth")
    print("="*80)

    try:
        from playwright.sync_api import sync_playwright
        from playwright_stealth import stealth_sync
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        print("Install with: pip install playwright-stealth")
        return False

    username = os.getenv("KENPOM_USERNAME")
    password = os.getenv("KENPOM_PASSWORD")

    if not username or not password:
        print("❌ KENPOM_USERNAME or KENPOM_PASSWORD not set in .env")
        return False

    print(f"Testing with username: {username[:3]}***")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        )
        page = context.new_page()

        # Apply stealth
        stealth_sync(page)

        print("1. Navigating to KenPom with stealth...")
        page.goto("https://kenpom.com/", wait_until="domcontentloaded", timeout=30000)

        # Wait for page to load
        page.wait_for_timeout(3000)

        # Check for challenge
        title = page.title()
        print(f"   Page title: {title}")

        if "Just a moment" in title or "Verify you are human" in page.content():
            print("   ❌ Still blocked by Cloudflare Turnstile")
            page.screenshot(path="kenpom_stealth_blocked.png")
            browser.close()
            return False

        # Look for login form
        email_input = page.locator("input[name='email']")
        email_count = email_input.count()
        print(f"   Email inputs found: {email_count}")

        if email_count == 0:
            print("   ❌ No login form found")
            browser.close()
            return False

        print("   ✅ Login form is visible!")

        # Try to login
        print("2. Filling login form...")
        email_input.first.fill(username)
        page.wait_for_timeout(500)

        password_input = page.locator("input[name='password']")
        password_input.first.fill(password)
        page.wait_for_timeout(500)

        print("3. Submitting form...")
        submit_button = page.locator("input[type='submit']")
        submit_button.first.click()

        # Wait for navigation
        print("4. Waiting for login...")
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except:
            pass

        page.wait_for_timeout(2000)

        # Check for success
        data_link = page.locator("a:has-text('data')")
        if data_link.count() > 0:
            print("   ✅ Login successful! Found 'data' link")

            # Get cookies
            cookies = context.cookies("https://kenpom.com/")
            cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
            print(f"   ✅ Got {len(cookies)} cookies")

            browser.close()
            return True
        else:
            print("   ❌ Login failed - no 'data' link found")
            page.screenshot(path="kenpom_stealth_after_login.png")
            browser.close()
            return False


def test_realistic_browser_context():
    """Test using realistic browser context and timing."""
    print("\n" + "="*80)
    print("METHOD 2: Realistic Browser Context")
    print("="*80)

    from playwright.sync_api import sync_playwright

    username = os.getenv("KENPOM_USERNAME")
    password = os.getenv("KENPOM_PASSWORD")

    if not username or not password:
        print("❌ KENPOM_USERNAME or KENPOM_PASSWORD not set")
        return False

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
            ]
        )

        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            locale='en-US',
            timezone_id='America/New_York',
            permissions=['geolocation'],
            geolocation={'latitude': 40.7128, 'longitude': -74.0060},
            color_scheme='light',
            has_touch=False,
            is_mobile=False,
            extra_http_headers={
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Upgrade-Insecure-Requests': '1',
            }
        )

        page = context.new_page()

        # Remove webdriver flag
        page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            // Override permissions
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );

            // Override chrome property
            window.chrome = {
                runtime: {}
            };
        """)

        print("1. Navigating with realistic context...")
        page.goto("https://kenpom.com/", wait_until="domcontentloaded", timeout=30000)

        # Wait like a real user
        page.wait_for_timeout(3000)

        # Check page
        title = page.title()
        print(f"   Page title: {title}")

        if "Just a moment" in title:
            print("   ❌ Still blocked by Cloudflare")
            browser.close()
            return False

        # Look for login form
        email_count = page.locator("input[name='email']").count()
        print(f"   Email inputs found: {email_count}")

        if email_count > 0:
            print("   ✅ Login form is visible!")
            browser.close()
            return True
        else:
            print("   ❌ No login form")
            browser.close()
            return False


def test_wait_for_challenge():
    """Test waiting for Cloudflare challenge to auto-resolve."""
    print("\n" + "="*80)
    print("METHOD 3: Wait for Turnstile Auto-Solve")
    print("="*80)

    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # Run visible to see what happens
            slow_mo=100
        )
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()

        print("1. Navigating to KenPom (visible browser)...")
        page.goto("https://kenpom.com/", wait_until="domcontentloaded")

        print("2. Waiting for Cloudflare challenge...")
        # Wait up to 30 seconds for challenge to resolve
        for i in range(30):
            page.wait_for_timeout(1000)

            # Check if login form appeared
            if page.locator("input[name='email']").count() > 0:
                print(f"   ✅ Challenge passed after {i+1} seconds!")
                browser.close()
                return True

            # Check if still on challenge page
            if "Just a moment" in page.title():
                print(f"   [{i+1}s] Still waiting for challenge...")
            else:
                # Page changed, check what we got
                break

        email_count = page.locator("input[name='email']").count()
        if email_count > 0:
            print("   ✅ Login form visible!")
            browser.close()
            return True
        else:
            print("   ❌ Challenge did not resolve")
            browser.close()
            return False


if __name__ == "__main__":
    results = {}

    print("Testing KenPom Cloudflare Bypass Methods")
    print("="*80)

    # Test Method 1: playwright-stealth
    try:
        results['stealth'] = test_playwright_stealth()
    except Exception as e:
        print(f"Method 1 failed with error: {e}")
        results['stealth'] = False

    # Test Method 2: Realistic browser context
    try:
        results['realistic'] = test_realistic_browser_context()
    except Exception as e:
        print(f"Method 2 failed with error: {e}")
        results['realistic'] = False

    # Test Method 3: Wait for auto-solve (only if others fail)
    if not any(results.values()):
        try:
            results['auto_solve'] = test_wait_for_challenge()
        except Exception as e:
            print(f"Method 3 failed with error: {e}")
            results['auto_solve'] = False

    # Summary
    print("\n" + "="*80)
    print("RESULTS SUMMARY")
    print("="*80)
    for method, success in results.items():
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{method:20s}: {status}")

    if any(results.values()):
        print("\n✅ At least one method works! Update the workflow to use it.")
        sys.exit(0)
    else:
        print("\n❌ All methods failed. Cloudflare detection is very strong.")
        print("Recommendation: Use manual CSV upload method.")
        sys.exit(1)
