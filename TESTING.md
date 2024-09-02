# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/apeskinian/p3_watch-o-matic/main/run.py) | ![screenshot](documentation/validation/wom_pep8.png "PEP8 Python Validation") | |

## Browser Compatibility

| Browser | Home | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/wom_browsers_chrome.png "Chrome compatibility") | Works as expected |
| Firefox | ![screenshot](documentation/browsers/wom_browsers_firefox.png "Firefox compatibility") | Works as expected |
| Edge | ![screenshot](documentation/browsers/wom_browsers_edge.png "Edge compatibility") | Works as expected |
| Safari | ![screenshot](documentation/browsers/wom_browsers_safari.png "Safari compatibility") | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive/wom_responsive_devtools_mobile.png "Responsive test Mobile DevTools") | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive/wom_responsive_devtools_tablet.png "Responsive test Tablet DevTools") | Works as expected |
| 4K Monitor (DevTools)| ![screenshot](documentation/responsive/wom_responsive_devtools_4kmonitor.png "Responsive test 4K DevTools") | Noticeable scaling issues |
| iPhone 15 Pro | ![screenshot](documentation/responsive/wom_responsive_iphone15pro.png "Responsive test iPhone 15 Pro") | Does not resize to fit width and keyboard does not input |
| iPad Mini | ![screenshot](documentation/responsive/wom_responsive_ipadmini.png "Responsive test iPad Mini") | Does not resize to fit width and keyboard does not input |
| MacBook Air M3 | ![screenshot](documentation/responsive/wom_responsive_macbookairm3.png "Responsive test Macbook Air M3") | Works as expected |
| 2K Desktop Monitor | ![screenshot](documentation/responsive/wom_responsive_2kdesktop.png "Responsive test 2K Desktop Monitor") | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Main | ![screenshot](documentation/lighthouse/wom_lighthouse_mobile.png "Lighthouse mobile") | ![screenshot](documentation/lighthouse/wom_lighthouse_desktop.png "Lighthouse desktop") | Some minor warnings |

## Defensive Programming

| Page | Test | Expectation | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Main Menu |  |  |  |  |  |
|  | Testing valid input of 1 | User should be shown the current collection | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_valid_1.gif "Valid input of 1") |
|  | Testing valid input of 2 | User should be shown the wishlist | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_valid_2.gif "Valid input of 2") |
|  | Testing valid input of 3 | The process of adding a watch should start | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_valid_3.gif "Valid input of 3") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/mm/wom_dp_mm_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| View Collection |  |  |  |  |  |
|  | Testing valid input of ENTER for pagination | User should be shown the next page of the list | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_valid_pag.gif "Valid ENTER input") |
|  | Testing invalid inputs for pagination prompt | The app should not show any inputs, effectively ignoring everything until ENTER is pressed | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_pag.gif "Invalid non ENTER inputs") |
|  | Testing valid input of y for y/n prompt | User should be shown the main menu | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_valid_y.gif "Valid input of y") |
|  | Testing valid input of n for y/n prompt | User should be shown the app exit message and app ends | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs for y/n prompt | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs for y/n prompt | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key for y/n prompt | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs for y/n prompt  | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| View Wishlist |  |  |  |  |  |
|  | Testing valid input of ENTER for pagination | User should be shown the next page of the list | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_valid_pag.gif "Valid ENTER input") |
|  | Testing invalid inputs for pagination prompt | The app should not show any inputs, effectively ignoring everything until ENTER is pressed | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_pag.gif "Invalid non ENTER inputs") |
|  | Testing valid input of y for y/n prompt | User should be shown the main menu | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_valid_y.gif "Valid input of y") |
|  | Testing valid input of n for y/n prompt | User should be shown the app exit message and app ends | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs for y/n prompt  | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs for y/n prompt  | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key for y/n prompt | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs for y/n prompt  | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch - list selection |  |  |  |  |  |
|  | Testing valid input of 1 | User should be taken to the input screen for Watch make with a confirmation message adding to collection | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_valid_1.gif "Valid input of 1") |
|  | Testing valid input of 2 | User should be taken to the input screen for Watch make with a confirmation message adding to Wishlist | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_valid_2.gif "Valid input of 2") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch -  user input confirmation for make |  |  |  |  |  |
|  | Testing user input | User should be prompted to validate their input with y/n response | Test successful | ![screenshot](documentation/defensive/aw2/wom_dp_aw2_standard.gif "Testing user input") |
|  | Testing no input and pressing ENTER | User should be made aware that no input was given and prompted to validate this input with y/n response | Test successful | ![screenshot](documentation/defensive/aw2/wom_dp_aw2_none.gif "Testing blank user input") |
| Add watch -  user input validation for make |  |  |  |  |  |
|  | Testing valid input of y | User should be taken to the watch model input | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_valid_y.gif "Valid input of y") |
|  | Testing valid input of n | User should be prompted to re enter the watch make | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch -  user input confirmation for model |  |  |  |  |  |
|  | Testing user input | User should be prompted to validate their input with y/n response | Test successful |  |
|  | Testing no input and pressing ENTER | User should be made aware that no input was given and prompted to validate this input with y/n response | Test successful |  |
| Add watch -  user input validation for model |  |  |  |  |  |
|  | Testing valid input of y | User should be taken to the watch movement input | Test successful |  |
|  | Testing valid input of n | User should be prompted to re enter the watch model | Test successful |  |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful |  |
| Add watch -  watch addition overview input validation |  |  |  |  |  |
|  | Testing valid input of y | Watch should be added to the google sheet and user informed of success before being shown the updated table | Test successful |  |
|  | Testing valid input of n | User should be given the menu for watch addition cancellation, google sheet should not be updated | Test successful |  |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful |  |
| Watch addition cancelled |  |  |  |  |  |
|  | Testing valid input of 1 | User should be taken to the beginning of the add watch section | Test successful |  |
|  | Testing valid input of 2 | User should be taken to the main menu | Test successful |  |
|  | Testing valid input of 3 | User should be shown the app exit message and app ends | Test successful |  |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful |  |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful |  |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to add all my watches to the app, so that I can see all the watches I own. | ![screenshot](documentation/features/wom_feature_add_collection_final_prompt.png) |
| As a new site user, I would like to add a new watch that I've bought to the app, so that I can see that it's in my collection. | ![screenshot](documentation/features/wom_feature_add_collection_final_prompt.png) |
| As a new site user, I would like to add a new watch to my wishlist, so that I can see what I want to buy in the future. | ![screenshot](documentation/features/wom_feature_add_wishlist_final_prompt.png) |
| As a returning site user, I would like to view my current watch collection, so that I can keep track of the watches I own. | ![screenshot](documentation/features/wom_feature_collection_01.png) |
| As a returning site user, I would like to view my wishlist, so that I can decide whether it's time to buy a new watch. | ![screenshot](documentation/features/wom_feature_wishlist.png) |
| As a returning site user, I would like to add a new watch that I've bought to the app, so that I can see that it's in my collection. | ![screenshot](documentation/features/wom_feature_add_collection_final_prompt.png) |
| As a returning site user, I would like to add a new watch to my wishlist, so that I can see what I want to buy in the future. | ![screenshot](documentation/features/wom_feature_add_wishlist_final_prompt.png) |

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
