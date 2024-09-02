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

| Page | Test | Expectation | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Main Menu |  |  |  |  |
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
|  | Testing valid input of y for y/n prompt | User should be shown the main menu | Test successful (capital Y also accepted) | ![screenshot](documentation/defensive/vc/wom_dp_vc_valid_y.gif "Valid input of y") |
|  | Testing valid input of n for y/n prompt | User should be shown the app exit message and app ends | Test successful (capital N also accepted) | ![screenshot](documentation/defensive/vc/wom_dp_vc_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs for y/n prompt | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs for y/n prompt | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key for y/n prompt | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs for y/n prompt  | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/vc/wom_dp_vc_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| View Wishlist |  |  |  |  |  |
|  | Testing valid input of ENTER for pagination | User should be shown the next page of the list | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_valid_pag.gif "Valid ENTER input") |
|  | Testing invalid inputs for pagination prompt | The app should not show any inputs, effectively ignoring everything until ENTER is pressed | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_pag.gif "Invalid non ENTER inputs") |
|  | Testing valid input of y for y/n prompt | User should be shown the main menu | Test successful (capital Y also accepted) | ![screenshot](documentation/defensive/vw/wom_dp_vw_valid_y.gif "Valid input of y") |
|  | Testing valid input of n for y/n prompt | User should be shown the app exit message and app ends | Test successful (capital N also accepted) | ![screenshot](documentation/defensive/vw/wom_dp_vw_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs for y/n prompt  | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs for y/n prompt  | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key for y/n prompt | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs for y/n prompt  | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/vw/wom_dp_vw_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch - List selection |  |  |  |  |  |
|  | Testing valid input of 1 | User should be taken to the input screen for Watch make with a confirmation message adding to collection | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_valid_1.gif "Valid input of 1") |
|  | Testing valid input of 2 | User should be taken to the input screen for Watch make with a confirmation message adding to Wishlist | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_valid_2.gif "Valid input of 2") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw1/wom_dp_aw1_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch -  User input confirmation for watch make |  |  |  |  |  |
|  | Testing user input | User should be prompted to validate their input with y/n response | Test successful | ![screenshot](documentation/defensive/aw2/wom_dp_aw2_standard.gif "Testing user input") |
|  | Testing no input and pressing ENTER | User should be made aware that no input was given and prompted to validate this input with y/n response | Test successful | ![screenshot](documentation/defensive/aw2/wom_dp_aw2_none.gif "Testing blank user input") |
| Add watch -  User input validation for watch make |  |  |  |  |  |
|  | Testing valid input of y | User should be taken to the watch model input | Test successful (capital Y also accepted) | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_valid_y.gif "Valid input of y") |
|  | Testing valid input of n | User should be prompted to re enter the watch make | Test successful (capital N also accepted) | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw3/wom_dp_aw3_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch -  User input confirmation for watch model |  |  |  |  |  |
|  | Testing user input | User should be prompted to validate their input with y/n response | Test successful | ![screenshot](documentation/defensive/aw4/wom_dp_aw4_standard.gif "Testing user input") |
|  | Testing no input and pressing ENTER | User should be made aware that no input was given and prompted to validate this input with y/n response | Test successful | ![screenshot](documentation/defensive/aw4/wom_dp_aw4_none.gif "Testing blank user input") |
| Add watch -  User input validation for watch model |  |  |  |  |  |
|  | Testing valid input of y | User should be taken to the watch movement input | Test successful (capital Y also accepted) | ![screenshot](documentation/defensive/aw5/wom_dp_aw5_valid_y.gif "Valid input of y") |
|  | Testing valid input of n | User should be prompted to re enter the watch model | Test successful (capital N also accepted) | ![screenshot](documentation/defensive/aw5/wom_dp_aw5_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw5/wom_dp_aw5_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw5/wom_dp_aw5_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw5/wom_dp_aw5_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw5/wom_dp_aw5_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch -  Movement selection |  |  |  |  |  |
|  | Testing valid input of 1 | User should be taken to the watch addition overview with Quartz as the selected movement | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_valid_1.gif "Valid input of 1") |
|  | Testing valid input of 2 | User should be taken to the watch addition overview with Manual as the selected movement | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_valid_2.gif "Valid input of 2") |
|  | Testing valid input of 3 | User should be taken to the watch addition overview with Automatic as the selected movement | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_valid_3.gif "Valid input of 3") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw6/wom_dp_aw6_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Add watch -  New watch details overview |  |  |  |  |  |
|  | Testing valid input of y | Watch should be added to the google sheet and user informed of success before being shown the updated table | Test successful (capital Y also accepted) | ![screenshot](documentation/defensive/aw7/wom_dp_aw7_valid_y.gif "Valid input of y") |
|  | Testing valid input of n | User should be given the menu for watch addition cancellation, google sheet should not be updated | Test successful (capital N also accepted) | ![screenshot](documentation/defensive/aw7/wom_dp_aw7_valid_n.gif "Valid input of n") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw7/wom_dp_aw7_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw7/wom_dp_aw7_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw7/wom_dp_aw7_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw7/wom_dp_aw7_invalid_multi.gif "Multiple invalid inputs followed by valid input") |
| Watch addition cancelled |  |  |  |  |  |
|  | Testing valid input of 1 | User should be taken to the beginning of the add watch section | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_valid_1.gif "Valid input of 1") |
|  | Testing valid input of 2 | User should be taken to the main menu | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_valid_2.gif "Valid input of 2") |
|  | Testing valid input of 3 | User should be shown the app exit message and app ends | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_valid_3.gif "Valid input of 3") |
|  | Testing invalid numeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_invalid_num.gif "Invalid numeric input") |
|  | Testing invalid alphanumeric inputs | Validation should fail and user be informed that they entered an invalid input showing them what was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_invalid_alpha.gif "Invalid alphanumeric input") |
|  | Testing no input and just pressing the ENTER key | Validation should fail and user be informed that no input was entered. They should be reminded of the accepted inputs and prompted to try again | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_invalid_enter.gif "No input and ENTER pressed") |
|  | Testing multiple invalid inputs | Validation should continue to fail for each invalid input giving the correct response until a valid input is entered at which point the app should proceed to the relevant point | Test successful | ![screenshot](documentation/defensive/aw8/wom_dp_aw8_invalid_multi.gif "Multiple invalid inputs followed by valid input") |

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

| Decription | Bug | Solution | Result |
| --- | --- | --- | --- |
| The PrettyTable was showing some odd behaviour when the content width was larger than the deployment terminal. To fix this, I added the max-width parameters to the table so that if the content was longer the table would start to wrap text to the rwo below and stop the strange display behaviour. | ![screenshot](documentation/bugs/wom_bug_table_glitch.png "Table display behaviour") | ![screenshot](documentation/bugs/wom_bug_table_solution.png "Code to define the max-width of the columns") | ![screenshot](documentation/bugs/wom_bug_table_fixed.png "Table now displays correctly with long entries") |

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
