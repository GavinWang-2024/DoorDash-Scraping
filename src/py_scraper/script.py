import asyncio

from scrapybara import Scrapybara
from undetected_playwright.async_api import async_playwright
from dotenv import load_dotenv
import os

load_dotenv()
async def get_scrapybara_browser():
    api_key = os.getenv("SCRAPYBARA_API_KEY")
    client = Scrapybara(api_key=api_key)
    instance = client.start_browser()
    return instance

async def retrieve_menu_items(instance, start_url: str) -> list[dict]:
    """
    :args:
    instance: the scrapybara instance to use
    url: the initial url to navigate to

    :desc:
    this function navigates to {url}. then, it will collect the detailed
    data for each menu item in the store and return it.
    
    (hint: click a menu item, open dev tools -> network tab -> filter for
            "https://www.doordash.com/graphql/itemPage?operation=itemPage")

    one way to do this is to scroll through the page and click on each menu
    item.

    determine the most efficient way to collect this data.

    :returns:
    a list of menu items on the page, represented as dictionaries
    """
    cdp_url = instance.get_cdp_url().cdp_url
    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp(cdp_url)
        page = await browser.new_page()

        await page.goto(start_url)


        # browser automation ...
        await page.wait_for_load_state("networkidle") #waits until no network connections for 500 ms (API, AJAX reqs)
        
        while True: #scroll through page to load all items
            prev_height = await page.evaluate("document.body.scrollHeight") #get height of page
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await asyncio.sleep(2)
            new_height = await page.evaluate("document.body.scrollHeight")
            if new_height == prev_height:
                break
        
        
        #get menu items
        menu_items = await page.evaluate('''
            () => {
                const jsonData = JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent);
                const menuSections = jsonData.hasMenu.hasMenuSection;
                const menuItems = [];

                // Iterate over menu sections and gather all menu items
                menuSections.forEach(section => {
                    section.forEach(itemSection => {
                        menuItems.push(...itemSection.hasMenuItem);
                    });
                });
                
                return menuItems;
            }''')
        
        if menu_items:
            print(f"Found {len(menu_items)} Panda Express items:\n")
            categories = {
                "Most Ordered": range(1, 13),
                "Bowl": [13],
                "Plate": [14],
                "Bigger Plate": [15],
                "Panda Club Meal": range(16, 20),
                "5 Person Family Meal": [20],
                "Appetizers and More": range(21, 25),
                "A La Carte": range(25, 41),
                "Drinks": range(41, 62),
                "Catering": range(62, 68),
                "Apple Pie Roll": [68],
                "Requests": range(69, 71),
                "Condiments": range(71, 76)
            }

            for title, indices in categories.items():
                print(f"\n--- {title} ---")
                
                for idx in indices:
                    if idx - 1 < len(menu_items):
                        item = menu_items[idx - 1]
                        
                        name = item.get('name', 'No name available').replace("&amp;", "&")
                        description = item.get('description', "").replace("&amp;", "&")
                        price = item['offers'].get('price', None)

                        output = f"Item {idx}: Name: {name}"
                        if description:
                            output += f" | Description: {description}"
                        if price:
                            output += f" | Price: {price}"

                        print(output)

        else:
            print("No menu items found.")
        return menu_items
       
async def main():
    instance = await get_scrapybara_browser()

    try:
        await retrieve_menu_items(
            instance,
            "https://www.doordash.com/store/panda-express-san-francisco-980938/12722988/?event_type=autocomplete&pickup=false",
        )
    finally:
        # Be sure to close the browser instance after you're done!
        instance.stop()


if __name__ == "__main__":
    asyncio.run(main())
