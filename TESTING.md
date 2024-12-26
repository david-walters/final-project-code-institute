# My Django Project: Cass Galaar — Testing

![My Flask Project shown on a variety of screen sizes](events_list/static/images/home-page.png)

Visit the deployed site: [Events List UK](https://events-list-uk-6cbca1177466.herokuapp.com/)

---

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [W3C Validator](#w3c-validator)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Testing User Stories](#testing-user-stories)
  - [Full Testing](#full-testing)
  - [Browser and Device Testing](#browser-and-device-testing)
  - [Manual Feature Testing](#manual-feature-testing)

Testing was ongoing throughout the entire build of this project. During development I made use of the console inside VS-Code to read about the errors that occurred in order to correct them.

I have gone through each page using google chrome developer tools & Firefox inspector tool to ensure that each page is responsive on a variety of different screen sizes and devices and to ensure that the keyframes also work on different browsers.

---

## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS.

- [Home page (base.html, index.html, modal-add-event.html)](events_list/static/images/w3c-home-page.png) - Passed/No-errors
- [see-details.html](events_list/static/images/w3c-details-page.png) - Passed/No-errors
- [edit-event.html](events_list/static/images/w3c-edit-page.png) - Passed/No-errors
- [delete-event.html](events_list/static/images/w3c-delete-page.png) - Passed/No-errors
- [guidelines.html](events_list/static/images/w3c-guidelines-page.png) - Passed/No-errors
- [styles.css](events_list/static/images/w3c-css.png) - Passed/No-errors

All python files were tested using `pylint`. All pages scored 10/10 except for the init file which is to be ignored as the import is meant to be at the bottom to prevent circular imports.

- [pylint](events_list/static/images/pylint.png)

My JS file was tested using JSHint and returened with zero errors.

- [JSHint](events_list/static/images/jshint.png)

---

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website.

#### Desktop Results

All pages of the site are achieving a score of 100 for accessibility, performance, best practices, and SEO — Perfect results.

![Home page (base.html, index.html, modal-add-event.html)](events_list/static/images/lighthouse-dt-home.png)
![see-details.html](events_list/static/images/lighthouse-dt-details.png)
![edit-event.html](events_list/static/images/lighthouse-dt-edit.png)
![delete-event.html](events_list/static/images/lighthouse-dt-delete.png)
![guidelines.html](events_list/static/images/lighthouse-dt-guidelines.png)

#### Mobile Results

Each page is achieving a score of 100 for accessibility, best practices and SEO. The performance category is achieving a score of 97 or more.

![Home page (base.html, index.html, modal-add-event.html)](events_list/static/images/lighthouse-mb-home.png)
![see-details.html](events_list/static/images/lighthouse-mb-details.png)
![edit-event.html](events_list/static/images/lighthouse-mb-edit.png)
![delete-event.html](events_list/static/images/lighthouse-mb-delete.png)
![guidelines.html](events_list/static/images/lighthouse-mb-guidelines.png)

---

## MANUAL TESTING

### Testing User Stories

#### First Time Visitor Goals

| Goals                                                                      | How are they achieved?                                                                                                                                           |
| :------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I want to see what events are taking place in the UK.                      | The homepage immediately lists all events happening in different cities, making it easy for users to browse through events taking place across the UK.           |
| I want to be able to add an event to the list for people to know about it. | The 'Add Event' button allows users to submit new events through a simple form, which is then added to the event list for others to see once submitted.          |
| I want to be able to edit or delete my added event.                        | Each event has an 'Edit' and 'Delete' button visible to the user who created it, allowing them to easily update event details or remove the event from the list. |

#### Returning Visitor Goals

| Goals                                                           | How are they achieved?                                                                                                                            |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| I want to see if any new events have been added.                | When returning to the homepage, users can see any newly added events listed in chronological order, helping them stay updated on upcoming events. |
| I want to see if any events I'm interested in have any updates. | The 'See Details' page for each event allows users to check for updated event information, such as changes in the event description or date.      |

---

### Browser and Device Testing

Full testing was performed on the following devices and more on Google dev tools:

![Device list](events_list/static/images/device-list.png)

The site was tested using the following browsers:

- Google Chrome
- Microsoft IE
- Firefox

Additional testing was taken by friends and family on a variety of devices and screen sizes. They reported no issues when visiting and navigating.

### Manual Feature Testing

#### Header/Nav Items

| Feature                | Expected Outcome                                                                    | Testing Performed                        | Result                                                   | Pass/Fail |
| ---------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------- | --------- |
| Logo - href to Home    | Clicking on the logo should direct the user to the home page                        | Clicked on the logo                      | The user is successfully directed to the home page       | Pass      |
| Nav item - Home        | Clicking on the "Home" nav item should direct the user to the home page             | Clicked on the "Home" nav item           | The user is successfully directed to the home page       | Pass      |
| Nav item - Guidelines  | Clicking on the "Guidelines" nav item should direct the user to the guidelines page | Clicked on the "Guidelines" nav item     | The user is successfully directed to the guidelines page | Pass      |
| Nav items' hover state | On hover, the scale should increase except for the active one                       | Hovered over each nav item in the header | The hover state is applied except for the active one     | Pass      |

#### Main Page Buttons

| Feature            | Expected Outcome                                                                              | Testing Performed                                     | Result                                                                               | Pass/Fail |
| ------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------ | --------- |
| Add Event button   | Opens a modal pop-up where users can fill in event details                                    | Clicked on the "Add Event" button                     | The modal for adding an event appears                                                | Pass      |
| See Details button | Redirects to the "See Details" page showing the correct information for the selected event    | Clicked the "See Details" button for a specific event | Redirected to the event’s detail page, displaying all relevant information           | Pass      |
| Edit button        | Opens a form pre-filled with the selected event's details, allowing the user to edit and save | Clicked the "Edit" button for a specific event        | A form with pre-filled details of the event is displayed, allowing updates           | Pass      |
| Delete button      | Redirects to a confirmation page to delete the selected event                                 | Clicked the "Delete" button for a specific event      | Redirected to the delete confirmation page for that event, with an option to confirm | Pass      |

#### CRUD Functionality

| Feature                    | Expected Outcome                                                                                             | Testing Performed                                                                   | Result                                                                                             | Pass/Fail |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------- |
| Add Event functionality    | Submits event information from modal, redirects to the home page, displays the new event and a flash message | Filled in event details, submitted the form, checked the home page                  | The event is added, appears on the home page, and a flash message confirms successful addition     | Pass      |
| Edit Event functionality   | Submits edited event information, redirects to the home page, shows updated event with flash message         | Edited event details, submitted the form, and checked the home page                 | The event is updated, appears with new details on the home page, and a flash message confirms edit | Pass      |
| Delete Event functionality | Deletes the event, redirects to the home page, and displays a flash message confirming deletion              | Clicked the "Delete" button, confirmed the action, and checked the home page        | The event is removed from the home page, and a flash message confirms successful deletion          | Pass      |
| See Details functionality  | Displays the event details on the details page, with a button to go back to the main page                    | Viewed event details and clicked the "Back to Main" button                          | Redirected to the home page with the table of events displayed                                     | Pass      |
| Close Modal Button         | Closes the Add Event modal without submitting or saving                                                      | Opened the Add Event modal, clicked the "Close" button                              | The modal closes without submitting or saving any information                                      | Pass      |
| Cancel Edit Button         | Redirects back to the home page without saving changes                                                       | Opened the Edit page, clicked the "Cancel" button                                   | Redirected to the home page, and no changes were saved                                             | Pass      |
| "No" Button on Delete Page | Redirects to the home page without deleting the event                                                        | Clicked the "Delete" button on an event, then clicked "No" in the confirmation page | Redirected to home page, and the event remains on the home page                                    | Pass      |

#### Form Validation

| Feature                            | Expected Outcome                                                                                           | Testing Performed                                                     | Result                                                                   | Pass/Fail |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------- |
| Event Name field (max length 50)   | User is prevented from typing more than 50 characters in the Event Name field                              | Tried entering more than 50 characters in the Event Name field        | Input stopped after 50 characters                                        | Pass      |
| Event Name field (required)        | Displays an error if the field is left empty or filled with white spaces upon submission                   | Submitted the form with an empty or whitespace-only Event Name field  | An error alert prevents the form from submitting                         | Pass      |
| Town Name field (max length 30)    | User is prevented from typing more than 30 characters in the Town Name field                               | Tried entering more than 30 characters in the Town Name field         | Input stopped after 30 characters                                        | Pass      |
| Town Name field (required)         | Displays an error if the field is left empty or filled with white spaces upon submission                   | Submitted the form with an empty or whitespace-only Town Name field   | An error alert prevents the form from submitting                         | Pass      |
| Description field (max length 700) | User is prevented from typing more than 700 characters in the Description field                            | Tried entering more than 700 characters in the Description field      | Input stopped after 700 characters                                       | Pass      |
| Description field (required)       | Displays an error if the field is left empty or filled with white spaces upon submission                   | Submitted the form with an empty or whitespace-only Description field | An error alert prevents the form from submitting                         | Pass      |
| Date field validation (required)   | Displays an error if the date is left empty or a past date is selected                                     | Tried submitting with no date or a past date                          | The form is prevented from submitting, and an error message is displayed | Pass      |
| No white spaces as valid input     | White spaces alone should not be considered valid input for any field, and an error is shown on submission | Entered white spaces only in all fields and tried to submit the form  | An error alert appeared, preventing form submission                      | Pass      |
| Date validation (no past dates)    | Prevents past dates from being selected in the date field                                                  | Tried selecting a date before the current date                        | The form is prevented from submitting, and an error message is displayed | Pass      |
