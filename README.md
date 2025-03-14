# Setup

1. Create Scrapybara instance
2. Download/Install Rye: https://rye.astral.sh/guide/installation/
3. Setup Rye: rye init 
5. rye add scrapybara
6. rye add undetected-playwright-patch
7. rye add python-dotenv


*If you encounter permission errors, may need to give permissions for playwright (I did ```sudo chmod -R 755 /Users/gavin/Desktop/DoorDash-Scraping/```)


# Process

1. Initialize Scrapybara – Start an instance for browser automation.
2. Load environment variables – Retrieve API keys and configurations.
3. Connect to Scrapybara instance – Obtain the CDP URL for remote control.
4. Launch Playwright browser – Connect to Scrapybara's Chromium instance.
5. Navigate to the target URL – Open the DoorDash restaurant page.
6. Wait for network activity to settle – Ensure all content is loaded.
7. Scroll to the bottom – Load all menu items dynamically.
8. Extract menu items – Parse and retrieve structured JSON data.
9. Format and categorize data – Organize menu items by category.
10. Display results – Print menu items with name, description, and price.
11. Close Scrapybara instance – Shut down the remote-controlled browser.



Found the HTML Elements to scrape with this JS:

```javascript
const jsonData = JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent);
const menuSections = jsonData.hasMenu.hasMenuSection;
const menuItems = [];

menuSections.forEach(section => {
section.forEach(itemSection => {
    menuItems.push(...itemSection.hasMenuItem);
    });
});

console.log(menuItems);
```