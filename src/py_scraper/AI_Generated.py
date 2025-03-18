#changed some parts of the AI generated script to work

from playwright.async_api import async_playwright
import asyncio

async def run(playwright):
    # Launch the browser
    print("Launching browser...")
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()

    # Open a new page
    print("Opening a new page...")
    page = await context.new_page()

    # Navigate to Uber Eats homepage
    print("Navigating to Uber Eats homepage...")
    await page.goto("https://www.ubereats.com/")

    # Wait until the location permission modal appears and close it
    # Timeout added to wait for any potential delays
    print("Checking for location permission modal...")
    if await page.is_visible("button[aria-label='Close']", timeout=5000):
        # Click the button with aria-label="Close"
        print("Closing location permission modal...")
        await page.click("button[aria-label='Close']")

    # Enter delivery address
    print("Entering delivery address...")
    await page.click("input[placeholder='Enter delivery address']")
    await page.fill("input[placeholder='Enter delivery address']", "2390 El Camino Real")

    # Wait and select the suggested address
    print("Selecting suggested address...")
    await page.wait_for_selector("ul[role='listbox']", timeout=2000)
    await page.click("ul[role='listbox'] li:first-child")
    
    print("Searching for Chipotle link")
    await asyncio.sleep(4)

    previous_height = await page.evaluate('document.body.scrollHeight') #initial height

    while True:
        h3_elements = await page.query_selector_all("h3")
        chipotle_link = None

        for h3 in h3_elements:  # Find the Chipotle h3
            text_content = await h3.text_content()
            if 'Chipotle Mexican Grill' in text_content:
                chipotle_link = await h3.evaluate('h3 => h3.closest("a").href')
                break
        
        if chipotle_link:
            await page.goto(chipotle_link)
            break
        
        else:
            print("Chipotle link not found. Scrolling down for more restaurants...")
            
            await page.evaluate("window.scrollBy(0, window.innerHeight)")
            await asyncio.sleep(4)

            new_height = await page.evaluate('document.body.scrollHeight')
            if new_height == previous_height:
                print("Reached the bottom of the page. No more restaurants to load.")
                break
            previous_height = new_height

            show_more_btn = await page.query_selector("button:has-text('Show more')")
            if show_more_btn:
                await show_more_btn.click()
            else:
                print("No more restaurants to load.")
                break
            
    
    
    # IF CHIPOTLE IS CLOSED, A SCHEDULE DELIVERY POPUP WILL APPEAR -> CLICK CANCEL
    print("Waiting for Chipotle page to load...")
    await page.wait_for_selector("h1:has-text('Chipotle Mexican Grill')")
    
    # Scroll to featured items
    print("Scrolling to featured items...")
    while True:
        featured_items = await page.query_selector("h3:has-text('Featured items')")
        if featured_items and await featured_items.is_visible():
            print("Featured items section found.")
            break
        await page.evaluate("window.scrollBy(0, 100)")
        await asyncio.sleep(1)
    
    # Interact with quick add buttons
    print("Interacting with quick add buttons...")
    buttons = await page.query_selector_all("button[data-testid='quick-add-button']")
    
    await buttons[0].click()  # open #1 item
    print("Opening first featured item...")
    await page.click("button[aria-label='Close']")  # close #1 item
    print("Closing first featured item...")

    await buttons[1].click()  # open #2 item
    print("Opening second featured item...")
    await page.wait_for_selector("button[aria-label='Close']", state='visible')
    await page.click("button[aria-label='Close']")  # close #2 item
    print("Closing second featured item...")

    await buttons[2].click()  # open #3 item
    print("Opening third featured item...")
    await page.wait_for_selector("button[aria-label='Close']", state='visible')
    await page.click("button[aria-label='Close']")  # close #3 item
    print("Closing third featured item...")
    await asyncio.sleep(3)
    print("Closing context and browser...")
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == "__main__":
    asyncio.run(main())
