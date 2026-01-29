#!/usr/bin/env python3
"""
Test KenPom login locally to debug GitHub Actions issue.
"""
import os
import sys
from playwright.sync_api import sync_playwright

# Get credentials from .env or environment
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("KENPOM_USERNAME")
password = os.getenv("KENPOM_PASSWORD")

if not username or not password:
    print("ERROR: KENPOM_USERNAME or KENPOM_PASSWORD not set in .env")
    print("Please create a .env file with these variables.")
    sys.exit(1)

print(f"Testing KenPom login with username: {username[:3]}***")

def fill_first(page, selectors, value, field_name="field"):
    """Try multiple selectors and fill the first one that works."""
    for selector in selectors:
        try:
            locator = page.locator(selector)
            count = locator.count()
            print(f"  Trying {selector}: {count} found")
            if count > 0:
                locator.first.fill(value)
                print(f"  ✓ Filled {field_name} using {selector}")
                return True
        except Exception as e:
            print(f"  ✗ Error with {selector}: {e}")
            continue
    print(f"  ✗ Could not find {field_name} with any selector")
    return False

with sync_playwright() as p:
    # Use headless=False to see what's happening
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    print("\n1. Navigating to KenPom...")
    page.goto("https://kenpom.com/", wait_until="domcontentloaded")
    
    # IMPORTANT: Wait for the login form to be visible
    print("\n2. Waiting for login form...")
    try:
        page.wait_for_selector("input[name='email']", timeout=10000, state="visible")
        print("  ✓ Login form is visible")
    except Exception as e:
        print(f"  ✗ Login form not visible: {e}")
        page.screenshot(path="kenpom_error.png")
        print("  Screenshot saved to kenpom_error.png")
        browser.close()
        sys.exit(1)
    
    print("\n3. Filling email field...")
    email_selectors = ["input[name='email']", "input[type='email']"]
    if not fill_first(page, email_selectors, username, "email"):
        page.screenshot(path="kenpom_error.png")
        browser.close()
        sys.exit(1)
    
    print("\n4. Filling password field...")
    password_selectors = ["input[name='password']", "input[type='password']"]
    if not fill_first(page, password_selectors, password, "password"):
        page.screenshot(path="kenpom_error.png")
        browser.close()
        sys.exit(1)
    
    print("\n5. Submitting form...")
    submitted = False
    submit_selectors = [
        "input[type='submit']", 
        "button[type='submit']", 
        "input[value*='Login']", 
        "button:has-text('Login')"
    ]
    
    for selector in submit_selectors:
        try:
            locator = page.locator(selector)
            count = locator.count()
            print(f"  Trying {selector}: {count} found")
            if count > 0:
                locator.first.click()
                print(f"  ✓ Clicked submit using {selector}")
                submitted = True
                break
        except Exception as e:
            print(f"  ✗ Error with {selector}: {e}")
            continue
    
    if not submitted:
        print("  → Trying keyboard Enter as fallback...")
        page.keyboard.press("Enter")
    
    print("\n6. Waiting for navigation...")
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
        print("  ✓ Page loaded")
    except Exception:
        print("  → Timeout waiting for networkidle (may be OK)")
    
    print("\n7. Checking login success...")
    # Look for "data" link which appears after successful login
    data_link = page.locator("a:has-text('data')")
    data_link_count = data_link.count()
    print(f"  'data' links found: {data_link_count}")
    
    if data_link_count > 0:
        print("  ✓ Login successful!")
        href = data_link.first.get_attribute("href")
        if href:
            if href.startswith("http"):
                data_url = href
            else:
                data_url = f"https://kenpom.com/{href.lstrip('/')}"
            print(f"  Data URL: {data_url}")
    else:
        print("  ✗ Login may have failed - no 'data' link found")
        page.screenshot(path="kenpom_after_login.png")
        print("  Screenshot saved to kenpom_after_login.png")
    
    print("\n8. Getting cookies...")
    cookies = context.cookies("https://kenpom.com/")
    cookie_str = "; ".join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    
    if cookie_str:
        print(f"  ✓ Got {len(cookies)} cookies")
        print(f"  Cookie preview: {cookie_str[:100]}...")
    else:
        print("  ✗ No cookies found!")
    
    browser.close()
    
    print("\n✅ Test complete!")
