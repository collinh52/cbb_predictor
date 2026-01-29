#!/usr/bin/env python3
"""
Improved KenPom login that bypasses Cloudflare Turnstile.

Uses realistic browser context and fingerprinting to avoid detection.
"""
import os
import sys
from playwright.sync_api import sync_playwright


def login_to_kenpom(username: str, password: str, verbose: bool = True) -> dict:
    """
    Login to KenPom and return cookies and data URL.

    Args:
        username: KenPom email
        password: KenPom password
        verbose: Print progress messages

    Returns:
        dict with keys: 'success', 'cookies', 'data_url', 'error'
    """
    if not username or not password:
        return {
            'success': False,
            'error': 'Username or password not provided',
            'cookies': None,
            'data_url': None
        }

    if verbose:
        print(f"Logging into KenPom as {username[:3]}***")

    with sync_playwright() as p:
        # Launch with anti-detection arguments
        browser = p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
            ]
        )

        # Create realistic browser context
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            locale='en-US',
            timezone_id='America/New_York',
            color_scheme='light',
            has_touch=False,
            is_mobile=False,
            java_script_enabled=True,
            extra_http_headers={
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Upgrade-Insecure-Requests': '1',
            }
        )

        page = context.new_page()

        # Remove webdriver flag and other automation markers
        page.add_init_script("""
            // Remove webdriver flag
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            // Mock permissions
            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );

            // Add chrome object
            window.chrome = {
                runtime: {},
                loadTimes: function() {},
                csi: function() {},
                app: {}
            };

            // Mock plugins
            Object.defineProperty(navigator, 'plugins', {
                get: () => [1, 2, 3, 4, 5]
            });

            // Mock languages
            Object.defineProperty(navigator, 'languages', {
                get: () => ['en-US', 'en']
            });
        """)

        try:
            if verbose:
                print("1. Navigating to KenPom...")

            # Navigate with realistic wait
            page.goto("https://kenpom.com/", wait_until="domcontentloaded", timeout=30000)

            # Wait like a real user
            page.wait_for_timeout(2000)

            # Check if we got through Cloudflare
            title = page.title()
            if "Just a moment" in title or "Verify you are human" in page.content():
                return {
                    'success': False,
                    'error': 'Cloudflare challenge not bypassed',
                    'cookies': None,
                    'data_url': None
                }

            if verbose:
                print("   ✓ Bypassed Cloudflare")

            # Wait for login form
            if verbose:
                print("2. Waiting for login form...")

            try:
                page.wait_for_selector("input[name='email']", timeout=10000, state="visible")
            except:
                return {
                    'success': False,
                    'error': 'Login form not found',
                    'cookies': None,
                    'data_url': None
                }

            if verbose:
                print("   ✓ Login form loaded")

            # Fill email
            if verbose:
                print("3. Filling credentials...")

            email_input = page.locator("input[name='email']")
            email_input.first.fill(username)
            page.wait_for_timeout(500)  # Human-like delay

            # Fill password
            password_input = page.locator("input[name='password']")
            password_input.first.fill(password)
            page.wait_for_timeout(500)

            if verbose:
                print("4. Submitting form...")

            # Submit
            submit_button = page.locator("input[type='submit']")
            submit_button.first.click()

            # Wait for navigation
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except:
                pass  # Timeout is ok

            page.wait_for_timeout(2000)

            if verbose:
                print("5. Verifying login...")

            # Check for successful login
            data_link = page.locator("a:has-text('data')")
            if data_link.count() == 0:
                # Check if login failed
                if "login" in page.url.lower():
                    return {
                        'success': False,
                        'error': 'Login failed - incorrect credentials or blocked',
                        'cookies': None,
                        'data_url': None
                    }

            # Get data URL
            data_url = None
            if data_link.count() > 0:
                href = data_link.first.get_attribute("href")
                if href:
                    if href.startswith("http"):
                        data_url = href
                    else:
                        data_url = f"https://kenpom.com/{href.lstrip('/')}"

            # Get cookies
            cookies = context.cookies("https://kenpom.com/")
            cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])

            if not cookie_str:
                return {
                    'success': False,
                    'error': 'No cookies received',
                    'cookies': None,
                    'data_url': None
                }

            if verbose:
                print(f"   ✓ Got {len(cookies)} cookies")
                if data_url:
                    print(f"   ✓ Data URL: {data_url}")

            browser.close()

            return {
                'success': True,
                'cookies': cookie_str,
                'data_url': data_url,
                'error': None
            }

        except Exception as e:
            browser.close()
            return {
                'success': False,
                'error': str(e),
                'cookies': None,
                'data_url': None
            }


if __name__ == "__main__":
    import argparse
    from dotenv import load_dotenv

    load_dotenv()

    parser = argparse.ArgumentParser(description="Login to KenPom and export cookies")
    parser.add_argument("--username", help="KenPom email (or use KENPOM_USERNAME env var)")
    parser.add_argument("--password", help="KenPom password (or use KENPOM_PASSWORD env var)")
    parser.add_argument("--export-env", help="Export to GitHub Actions GITHUB_ENV file")
    parser.add_argument("--quiet", action="store_true", help="Minimal output")

    args = parser.parse_args()

    username = args.username or os.getenv("KENPOM_USERNAME")
    password = args.password or os.getenv("KENPOM_PASSWORD")

    if not username or not password:
        print("ERROR: KENPOM_USERNAME and KENPOM_PASSWORD must be provided")
        sys.exit(1)

    result = login_to_kenpom(username, password, verbose=not args.quiet)

    if result['success']:
        print("\n✅ Login successful!")

        # Export to GitHub Actions if requested
        if args.export_env and os.path.exists(args.export_env):
            with open(args.export_env, "a") as f:
                f.write(f"KENPOM_COOKIE={result['cookies']}\n")
                if result['data_url']:
                    f.write(f"KENPOM_DATA_URL={result['data_url']}\n")
            print(f"✓ Exported to {args.export_env}")

        sys.exit(0)
    else:
        print(f"\n❌ Login failed: {result['error']}")
        sys.exit(1)
