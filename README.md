# Setup

1. Create Scrapybara instance
2. Download/Install Rye: https://rye.astral.sh/guide/installation/
3. Setup Rye: rye init 
5. rye add scrapybara
6. rye add undetected-playwright-patch
7. rye add python-dotenv
8. add api key to .env as SCRAPYBARA_API_KEY = ...

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


# Bonus Question

1. Extract before-state, after-state, and transition descriptions.
2. Construct formatted strings for before-state and after-state.
3. Define generate_playwright_script to generate Playwright script.
4. Extract subtasks from trajectory decomposition data.
5. Loop through subtasks and extract action descriptions.
6. Retrieve corresponding transition descriptions.
7. Format transition details using format_transition_description.
8. Construct prompts combining actions and transition descriptions.
9. Join prompts into a single structured prompt.
10. Call OpenAI API with the structured prompt.
11. Retrieve response from OpenAI API.
12. Extract and return Playwright script from API response.


# Input Generated for AI

```text
Action: URL navigation to https://www.ubereats.com/
Before State:
Website: Uber Eats
Overview: The loading page of Uber Eats where users can order food.
Functional Analysis: This page is designed for users to enter their delivery address and access food delivery options.
Functional Actions: Enter delivery address, Sign in

After State:
Website: Uber Eats
Overview: The Uber Eats homepage after loading, showing a location permission request modal.
Functional Analysis: The page now includes a modal prompting the user to allow location access for a more personalized experience by showing nearby restaurants.
Functional Actions: Allow location access, Enter delivery address instead, Sign in

Transition Description: A modal appears prompting the user to allow location access, enhancing the food ordering experience by potentially showing nearby restaurants.

---
Action: Click on the close button of location access modal.
Before State:
Website: Uber Eats
Overview: The loading page of Uber Eats where users can order food.
Functional Analysis: This page is designed for users to enter their delivery address and access food delivery options.
Functional Actions: Enter delivery address, Sign in

After State:
Website: Uber Eats
Overview: The Uber Eats homepage after loading, showing a location permission request modal.
Functional Analysis: The page now includes a modal prompting the user to allow location access for a more personalized experience by showing nearby restaurants.
Functional Actions: Allow location access, Enter delivery address instead, Sign in

Transition Description: A modal appears prompting the user to allow location access, enhancing the food ordering experience by potentially showing nearby restaurants.

---
Action: Click on the delivery address input field.
Before State:
Website: Uber Eats
Overview: The home page for Uber Eats, prompting users to enter a delivery address to view restaurants.
Functional Analysis: This page allows users to enter a delivery address to explore nearby restaurants for food delivery. Users can also see options to sign 
in or log in to their accounts.
Functional Actions: Enter delivery address, Log in, Sign up

After State:
Website: Uber Eats
Overview: The home page for Uber Eats shows options for inputting delivery address and searching for food without location permission.
Functional Analysis: The page now prominently displays a field to enter a delivery address and buttons for immediate delivery options. The previous location permission prompt is no longer visible, allowing users to search directly.
Functional Actions: Enter delivery address, Deliver now, Search here, Log in, Sign up

Transition Description: The location permission modal was closed after the user clicked the close button, allowing the main content page to display options 
for directly entering a delivery address and searching for food.

---
Action: Type '2390 el camino real' into the delivery address input field.
Before State:
Website: Uber Eats
Overview: The home page for Uber Eats, prompting users to enter a delivery address to view restaurants.
Functional Analysis: This page allows users to enter a delivery address to explore nearby restaurants for food delivery. Users can also see options to sign 
in or log in to their accounts.
Functional Actions: Enter delivery address, Log in, Sign up

After State:
Website: Uber Eats
Overview: The home page for Uber Eats shows options for inputting delivery address and searching for food without location permission.
Functional Analysis: The page now prominently displays a field to enter a delivery address and buttons for immediate delivery options. The previous location permission prompt is no longer visible, allowing users to search directly.
Functional Actions: Enter delivery address, Deliver now, Search here, Log in, Sign up

Transition Description: The location permission modal was closed after the user clicked the close button, allowing the main content page to display options 
for directly entering a delivery address and searching for food.

---
Action: Click on the suggested address '2390 El Camino Real'.
Before State:
Website: Uber Eats
Overview: The home page for Uber Eats, prompting users to enter a delivery address to view restaurants.
Functional Analysis: This page allows users to enter a delivery address to explore nearby restaurants for food delivery. Users can also see options to sign 
in or log in to their accounts.
Functional Actions: Enter delivery address, Log in, Sign up

After State:
Website: Uber Eats
Overview: The home page for Uber Eats shows options for inputting delivery address and searching for food without location permission.
Functional Analysis: The page now prominently displays a field to enter a delivery address and buttons for immediate delivery options. The previous location permission prompt is no longer visible, allowing users to search directly.
Functional Actions: Enter delivery address, Deliver now, Search here, Log in, Sign up

Transition Description: The location permission modal was closed after the user clicked the close button, allowing the main content page to display options 
for directly entering a delivery address and searching for food.

---
Action: Click on Chipotle Mexican Grill to view its menu and details.
Before State:
Website: Uber Eats
Overview: The homepage allows users to order food delivery and enter their delivery address.
Functional Analysis: This page is primarily used for ordering food from local restaurants. It features an address input field, delivery options, and sign-in options.
Functional Actions: Enter delivery address, Choose delivery time, Search for restaurants, Sign in, Sign up

After State:
Website: Uber Eats
Overview: The homepage allows users to order food delivery and enter their delivery address.
Functional Analysis: This page is primarily used for ordering food from local restaurants. It features an address input field, delivery options, and sign-in options.
Functional Actions: Enter delivery address, Choose delivery time, Search for restaurants, Sign in, Sign up

Transition Description: The input field for entering the delivery address was clicked, resulting in the element being active, which may allow for user interaction such as typing an address.

---
Action: Scroll to explore featured items.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

---
Action: Click on the '#1 most liked' item to view details.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

---
Action: Close the detailed view of the Burrito Bowl.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

---
Action: Click on the '2nd most liked' item to view details.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

---
Action: Close the detailed view of the Burrito.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

---
Action: Click on the '#3 most liked' item to view details.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

---
Action: Closed the Quesadilla details view.
Before State:
Website: Uber Eats
Overview: The homepage of Uber Eats featuring a food delivery interface.
Functional Analysis: This page allows users to enter their delivery address to find available food delivery options nearby.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up

After State:
Website: Uber Eats
Overview: The homepage of Uber Eats with search results for a delivery address.
Functional Analysis: The page now shows suggested delivery addresses based on the user input.
Functional Actions: Enter delivery address, Select delivery time, Search for food, Sign in or sign up, Clear search selection

Transition Description: After typing '2390 el camino real' into the delivery address input field, a dropdown list appears showing multiple address suggestions related to the input, including '2390 El Camino Real, Palo Alto, CA', along with other nearby locations. This change allows users to select a suggested address for more efficient searching.

Generate a complete Playwright script based on the above actions and descriptions in Python.
```




