# Watch-o-Matic

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/apeskinian/p3_watch-o-matic)](https://github.com/apeskinian/p3_watch-o-matic/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/apeskinian/p3_watch-o-matic)](https://github.com/apeskinian/p3_watch-o-matic/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/apeskinian/p3_watch-o-matic)](https://github.com/apeskinian/p3_watch-o-matic)

The Watch-o-Matic is a handy tool to keep track of your watch collection. As watch enthusiast's collection is never complete, you can also keep track of your wishlist to plan your future purchases! Each list can be added to when you either treat yourself to a new watch or find one that you want to add to the wishlist. The make, model and movement type of each watch are clearly displayed when either the collection or wishlist is requested.

![WOM Mockup](documentation/screenshots/wom_mockups.png)

Source: [Techsini Multi Device Website Mockup Generator](http://techsini.com/multi-mockup/?url=https://apeskinian-watch-o-matic-8cd45839ba26.herokuapp.com/)

## UX

🛑🛑🛑🛑🛑🛑🛑🛑🛑START OF NOTES (to be deleted)

In this section, you will briefly explain your design processes.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Stories

### New Site Users

- As a new site user, I would like to add all my watches to the app, so that I can see all the watches I own.
- As a new site user, I would like to add a new watch that I've bought to the app, so that I can see that it's in my collection.
- As a new site user, I would like to add a new watch to my wishlist, so that I can see what I want to buy in the future.

### Returning Site Users

- As a returning site user, I would like to view my current watch collection, so that I can keep track of the watches I own.
- As a returning site user, I would like to view my wishlist, so that I can decide whether it's time to buy a new watch.
- As a returning site user, I would like to add a new watch that I've bought to the app, so that I can see that it's in my collection.
- As a returning site user, I would like to add a new watch to my wishlist, so that I can see what I want to buy in the future.

## Features

- ### Main Menu
  This is where the user is greeted and given the options for what they can do in the app. View their current collection, view their wishlist or add a watch to one of the lists. The user is prompted for a choice which is then validated to make sure one of the options was entered and then taken to their choice action.

  ![Features - Main Menu](documentation/features/wom_feature_main_menu.png "Main Menu")

- ### Viewing current collection
  The user is shown their current collection in a table which is ordered alphabetically. This is paginated if the collection has more than 10 watches. Each page is shown as a number out of the total with a prompt to press ENTER to see the next page. When the last page is being shown or there is only one page the option to continue and perform another action is given. If y is entered the user is taked back to the main menu. If n is chosen the app gives a thank you message and ends.

  ![Features - View Collection](documentation/features/wom_feature_collection_01.png "Viewing Collection 1")
  ![Features - View Collection](documentation/features/wom_feature_collection_02.png "Viewing Collection 2")
  ![Features - Add watch](documentation/features/wom_feature_close.png "App closing")

- ### Viewing wishlist
  The user is shown their watch wishlist in a table which is ordered alphabetically. This is paginated if the wishlist has more than 10 watches. Each page is shown as a number out of the total with a prompt to press ENTER to see the next page. When the last page is being shown or there is only one page the option to continue and perform another action is given. If y is entered the user is taked back to the main menu. If n is chosen the app gives a thank you message and ends.

  ![Features - View Collection](documentation/features/wom_feature_wishlist.png "Viewing Wishlist")
  ![Features - Add watch](documentation/features/wom_feature_close.png "App closing")

- ### Adding a watch to either the collection or wishlist
  The user can add a new watch to their collection or their wishlist. They are prompted to choose which option they want which is validated. They can add a watch to their chosen list by entering the required details in the following steps:

  1. User is prompted to enter the make of the watch, this is then double checked with the user who can confirm and move on to the next step or go back and re enter the detail.
  2. User is prompted to enter the model of the watch, this is then double checked with the user who can confirm and move on to the next step or go back and re enter the detail.
  3. User is prompted to choose the movement of the watch from three options:
     - Quartz
     - Manual
     - Automatic
  
     When a valid option is given the user is taken to the next step.
  4. The user is presented with an overview of the watch to be added. They now have two options:
     - Confirm the addition: this will add the watch details to the google sheet and show them the updated collection or wishlist.
     - Cancel the addition: this will them give them the option to start again, go back to the main menu or quit the app.
  
  | Step | Screenshot |
  | --- | --- |
  | Choosing which list to add to: | ![Features - Add watch](documentation/features/wom_feature_add_menu.png "Add a new watch option") |
  | Prompt user for watch make: | ![Features - Add watch](documentation/features/wom_feature_add_collection_make_prompt.png "Prompt for make of watch") |
  | User confirmation of make: | ![Features - Add watch](documentation/features/wom_feature_add_collection_make_confirm.png "Confirm make of watch") |
  | Prompt user for watch model: | ![Features - Add watch](documentation/features/wom_feature_add_collection_model_prompt.png "Prompt for model of watch") |
  | User confirmation of model: | ![Features - Add watch](documentation/features/wom_feature_add_collection_model_confirm.png "Confirm model of watch") |
  | Prompt user for movement choice: | ![Features - Add watch](documentation/features/wom_feature_add_movement_prompt.png "Choosing watch movement") |
  | Overview of proposed new addition: | ![Features - Add watch](documentation/features/wom_feature_add_collection_final_prompt.png "Overview confirmation") |
  | Confirmation of addition to collection: | ![Features - Add watch](documentation/features/wom_feature_add_collection_show.png "Showing updated collection") |
  | Confirmation of addition to wishlist: | ![Features - Add watch](documentation/features/wom_feature_add_wishlist_show.png "Showing updated wishlist") |
  | Options given when addition is cancelled: | ![Features - Add watch](documentation/features/wom_feature_add_cancelled.png "Addition cancelled menu") |

- ### User input validation

  #### Invalid inputs
  Everytime the user is asked for input it is validated against preset acceptable parameters for each questions. When the app is given an invalid response it will alert the user and show them what they entered highlighted in red. It will then prompt them to try again reminding them of the options that are expected. This will repeat until a valid answer is given.

  | Invalid numeric entry | Invalid alphanumeric entry |
  | --- | --- |
  | ![Features - validation](documentation/features/wom_feature_validation_mm_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_mm_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_viewcoll_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_viewcoll_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_viewwish_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_viewwish_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_addmenu_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_addmenu_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_movement_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_movement_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_overview_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_overview_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_cancel_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_cancel_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_confirmmake_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_confirmmake_alpha.png "Invalid alphanumeric") |
  | ![Features - validation](documentation/features/wom_feature_validation_confirmmodel_num.png "Invalid numeric") | ![Features - validation](documentation/features/wom_feature_validation_confirmmodel_alpha.png "Invalid alphanumeric") |

  #### No inputs
  If the user does not input anything and presses enter they are informed this and asked to try again.

  | Non input validation | Non input validation | Non input validation |
  | --- | --- | --- |
  | ![Features - validation](documentation/features/wom_feature_validation_noinput_mm.png "No input main menu") | ![Features - validation](documentation/features/wom_feature_validation_noinput_viewcoll.png "No input viewing collection") | ![Features - validation](documentation/features/wom_feature_validation_noinput_viewwish.png "No input viewing wishlist") |
  | ![Features - validation](documentation/features/wom_feature_validation_noinput_addmenu.png "No input add watch menu") | ![Features - validation](documentation/features/wom_feature_validation_noinput_makeconfirm.png "No input make confirm") | ![Features - validation](documentation/features/wom_feature_validation_noinput_modelconfirm.png "No input model confirm") |
  | ![Features - validation](documentation/features/wom_feature_validation_noinput_movement.png "No input movement") | ![Features - validation](documentation/features/wom_feature_validation_noinput_overview.png "No input overview") | ![Features - validation](documentation/features/wom_feature_validation_noinput_cancel.png "No input cancel") |
  
  #### Self validation
  The only exception to this validation is when entering make and model details for a new watch. As there are virtually endless possibilities for watch makes and names the user is prompted to validate their own input. They have two chances to validate, once when they enter each detail and again before the watch is added.
  
  | User Self Validation for details | User self validation for overview |
  | --- | --- |
  | ![Feature - user validation](documentation/features/wom_feature_add_wishlist_make_confirm.png "User detail self validation") | ![Feature - user validation](documentation/features/wom_feature_add_wishlist_final_prompt.png "User overview self validation") |


### Future Features

- I would like to add the feature that if you're add a watch to the collection, it looks to see if it's in the wishlist and if so, asks if the user wants to remove it from the wishlist.
- Being able to move a watch from the wishlist to the collection. This is similar to the above feature but acts on the basis that the user remembers it was in the wishlist so doesn't have to enter the details.
- Being able to remove watches from either list. This would be useful if the user sold a watch and no longer owns it.
- Having user specific collections that can be accessed securely.

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- ⚠️⚠️ IDE: CHOOSE ONLY ONE <-- delete me ⚠️⚠️
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Google Sheets](https://img.shields.io/badge/Google_Sheets-grey?logo=googlesheets&logoColor=34A853)](https://docs.google.com/spreadsheets) used for storing data from my Python app.
- [![Lucid](https://img.shields.io/badge/Lucidchart-grey?logo=lucid&logoColor=FF9E0F)](https://www.lucidchart.com/pages) used for creating the flowchart for the apps logic.


## Data Model

### Flowchart

To follow best practice, a flowchart was created for the app's logic,
and mapped out before coding began using a free version of
[Lucidchart](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning) and/or [Draw.io](https://www.draw.io).

Below is the flowchart of the main process of this Python program. It shows the entire cycle of the program.

![screenshot](documentation/flowchart.png)

### Classes & Functions

The program uses classes as a blueprint for the project's objects (OOP). This allows for the object to be reusable.

```python
class Person:
    """ Insert docstring comments here """
    def __init__(self, name, age, health, inventory):
        self.name = name
        self.age = age
        self.health = health
        self.inventory = inventory
```

The primary functions used on this application are:

- `get_sales_data()`
    - Get sales figures input from the user.
- `validate_data()`
    - Converts all string values into integers.
- `update_worksheet()`
    - Update the relevant worksheet with the data provided.
- `calculate_surplus_data()`
    - Compare sales with stock and calculate the surplus for each item type.
- `get_last_5_entries_sales()`
    - Collects columns of data from sales worksheet.
- `calculate_stock_data()`
    -  Calculate the average stock for each item type, adding 10%.
- `main()`
    - Run all program functions.

### Imports

I've used the following Python packages and/or external imported packages.

- `gspread`: used with the Google Sheets API
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `time`: used for adding time delays
- `os`: used for adding a `clear()` function
- `colorama`: used for including color in the terminal
- `random`: used to get a random choice from a list

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://apeskinian-watch-o-matic-8cd45839ba26.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: node index.js > Procfile`

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/apeskinian/p3_watch-o-matic) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/apeskinian/p3_watch-o-matic.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/apeskinian/p3_watch-o-matic)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/apeskinian/p3_watch-o-matic)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Credits

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Content

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [W3Schools](https://www.w3schools.com/css/css3_variables.asp) | entire site | how to use CSS :root variables |
| [Flexbox Froggy](https://flexboxfroggy.com/) | entire site | modern responsive layouts |
| [Grid Garden](https://cssgridgarden.com) | entire site | modern responsive layouts |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [YouTube](https://www.youtube.com/watch?v=YL1F4dCUlLc) | leaderboard | using `localStorage()` in JS for high scores |
| [YouTube](https://www.youtube.com/watch?v=u51Zjlnui4Y) | PP3 terminal | tutorial for adding color to the Python terminal |
| [strftime](https://strftime.org) | CRUD functionality | helpful tool to format date/time from string |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |

### Media

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution to any supports that helped, encouraged, or supported you throughout the development stages of this project.
A few examples have been provided below to give you some ideas.

⚠️⚠️ EXAMPLES ONLY - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner (John/Jane), for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.
