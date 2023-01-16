# TIMEKEEPER: Simple Time Keeping Software 

**Developer: Christopher Jimerson**

[Visit Live Site](https://time-keeper.herokuapp.com/)

![Site Image](imgs/feat/landing-main.png)
## About
This project is a simple time management software that helps a user view, change, edit, and calculate hours for employees.


## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Easily view the data for the employees stored in the database
- Easily move through the application with clear response to correct, or incorrect use
- Understand what is asked of me for each part of the application

### Site Owner Goals

- Create an easy to use system for a user to navigate and utilize
- Provide feedback on what a user does, correct or otherwise
- Give examples of data formats that are needed to use the system

## User Experience

### Target Audience

- This is targeted at users that have a small team and need to have an easy way to manage the times of their teams work

### User Requirements and Expectations

- A straight forward and error absent application
- Easy to understand navigation
- Clear purposes to each function
- Feedback from user input

### User Manual

<details><summary>For a more details view of the instructions on how-to-use, click here</summary>

### Landing-Authentication
<br>
When the program starts the user finds themselves on a landing page. This page is requesting the user to log-in. For testing purposes, we only have one current user credentials. The username and password are as follows:<br>
username: Admin<br>
password: letMein<br>

Note: The entry is case sensitive and must<br>

Once entered correctly, the user is directed to the Employee Select screen.
<br>
### Employee Select
<br>
On this screen the user is asked to provide the employee, by name, whose data they wish to access.<br>
The input again is case sensitve and must match the provided names.<br>
Once correct, the user will be taken to the main menu.<br>
<br>
### Main Menu
<br>
The main menu provides the user with five options, each one listed numerically in order.<br>
<br>
1. View "employee name" Hour<br>
2. Edit "employee name" Hours<br>
3. Add Entry to "employ name" Hours<br>
4. Calculate "employee name" Current Total Hours<br>
5. Retrun to Employee Select<br>
<br>
The user is asked which menu they would like to visit and the bottom of the page shows the requested input to be the chosen menu number.<br>
Once chosen, and correct, the user will be taken to the menu of choice.<br>
<br>
### Menu One
<br>
This menu is simply a view of the selected employees total hours, organized in chronological order.<br>
When the user is done, they simply should press enter to return to the main menu.<br>
<br>
### Menu Two
<br>
This menu allows the user to select an entry, by using the instance number in the far left column, to edit.<br>
Once selected, the user is then taken to a submenu, which is the choice edit menu.<br>
This menu shows the user their selected entry at the top and then provides the input format for the date and times.<br>
The user must then input the correct date and clock-in and clock-out.<br>
Once done, they are given an status update of the success, or failure, of their upload, and then redirected back to menu two.<br>
<br>
### Menu Three
<br>
This menu allows users to add a brand new entry to the employee.<br>
The user is presented with the correct format that their new data should be in<br>
Users must input the correct format for a date, clock-in and clock-out.<br>
Once done the user will be provided a status update of the success, or failure, of their upload and then redirected back to the main menu.<br>
<br>
### Menu Four
<br>
This menu displays to the user the total hours for the selected employee currently in the database.<br> 
It will display the total for a few seconds, and then redirect the user back to the main men.<br> 
<br>
### Menu Five
This menu navigates the user back to the employee select screen where they are able to choose the which employee they want to access. 

</details>

<br>

[Back to Table Of Contents](#table-of-contents)

## User Stories

### Users

As a user...

1. I want to easily see employee working hours 
2. I want to know what menus are available
3. I want to see what employees are in our database
4. I want the software protected from just having anyone use it
5. I want to be able to edit existing data
6. I want to add new data for an employee
7. I want to know how many total hours are in the database for each of our employees
8. I want to easily navigate back to the beginning
9. I want feedback on my data input
10. I want to know that my changes have been successful

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Flowchart




## Technologies Used

### Languages
- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools
- [Git](https://git-scm.com/) was used for version control within VSCode to push the code to GitHub
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Google Cloud Platform](https://cloud.google.com/cloud-console/) was used to manage access and permissions to the Google Services such as Google auth, sheets etc.
- [Google Sheets](https://www.google.co.uk/sheets/about/) were used to store players details
- [Code Institute PEP8](https://pep8ci.herokuapp.com//) was used to check my code against Python conventions
- [Heroku](https://www.heroku.com/) was used to deploy this project to a live environment


### Libraries

#### Python Libraries
- datetime - used for date validation
- re - used for time format validation
- os - used to clear terminal
- time - used to displayed delayed messages in the terminal
#### Third Party Libraries
- [gspread](https://docs.gspread.org/en/latest/) - JUSTIFICATION: I used gspread as a mock database to hold the employee data, and list of employees and thus; used the database to read and write from my application.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - JUSTIFICATION: this allows the connection between my application and Google API so that it has the credentials and authorization  to access, and edit, my database(Google sheet)
- [colorama](https://pypi.org/project/colorama/) - JUSTIFICATION: I used this library to add color to the terminal and provide easy visual feedback to the user based on either accepted data entry(green text) or errors(red text)

[Back to Table Of Contents](#table-of-contents)

## Features

### Landing-Authentication
- Provides user with title and welcome
- Gives request to sign-in
- Requests username and password
- User stories covered: 4 

<details>
    <summary>Landing Screen Shot</summary>

![Landing-Authentication](imgs/feat/landing-main.png)
</details>

### Employee Select
- Provides list of current employees in database
- Requests users to choose from current list to progress
- User stories covered: 3

<details>
    <summary>Employee Select Screen Shot</summary>

![Employee Select](imgs/feat/employee_request.png)
</details>

### Main Menu
- Provides list of the menus the user has access to
- Request menu choice
- User stories covered: 2
<details>
    <summary>Screen Shot</summary>

![Main Menu](imgs/feat/main_menu.png)
</details>

### Menu One
- Displays all entries for selected employee
- Data is organized chronologically
- User stories covered: 1

<details>
    <summary>Menu One Screen Shot</summary>

![Menu One](imgs/feat/menu_one.jpg)
</details>


### Menu Two
- Displays all entries for selcted employee
- This list is organized by instance of addition, not chronological
- Once entry is selected, user may edit the date, clock-in, and clock-out
- User stories covered: 5
<details>
    <summary>Menu Two Screen Shot</summary>

![Menu Two](imgs/feat/menu_two.jpg)
</details>
<details>
    <summary>Menu Two Submenu Screen Shot</summary>

![Menu Two-Submenu](imgs/feat/menu_two_edit_menu.jpg)
</details>

### Menu Three
- Allows users to add new entry to selected employee database
- Requests the date, clock-in, and clock-out of the new entry
- User stories covered: 6
<details>
    <summary>Menu Three Screen Shot</summary>

![Menu Three](imgs/feat/menu_three.jpg)
</details>

### Menu Four
- Calculates and displays total hours in the database for given employee
- User stories covered: 7
<details>
    <summary>Menu Four Screen Shot</summary>

![Menu Four](imgs/feat/menu_four.jpg)
</details>

### Menu Five
- Navigates the user back to the employee select screen
- User stories covered: 8

<details>
    <summary>Menu Five Screen Shot</summary>

![Menu Five](imgs/feat/menu_five.jpg)
</details>

### User Input Validation
- For every input requested from the user we provide validation
- Green text with success messages display
- Red text with failure messages display
- User stories covered: 9, 10
<details>
    <summary>Landing Page Username and Password</summary>

![Username Fail ](imgs/input/landing_un_fail.png)
![Username Success ](imgs/input/landing_un_correct.png)
![Password Fail ](imgs/input/landing_pw_fail.png)
![Password Success ](imgs/input/landing_pw_correct.png)
</details>

<details>
    <summary>Employee Select Name Input</summary>

![Employee Select Fail ](imgs/input/employee_request_failure.png)
![Employee Select Success ](imgs/input/employee_request_correct.png)
</details>

<details>
    <summary>Main Menu Selection</summary>

![Main Menu Fail ]((imgs/input/main_menu_selection_fail.jpg)
![Main Menu Success ]((imgs/input/main_menu_selection_correct.jpg)
</details>

<details>
    <summary>Menu One Return</summary>

![Menu One Return Fail ]((imgs/input/menu_one_failed_input.jpg)
</details>

<details>
    <summary>Menu Two Selection</summary>

![Menu Two Selection Fail]((imgs/input/menu_two_edit_menu_input_fail.jpg)
![Menu Two Selection Success]((imgs/input/menu_two_edit_menu_input_ok.jpg)
</details>

<details>
    <summary>Date Input</summary>

![Date Input Fail ]((imgs/input/menu_two_edit_menu_date_fail.jpg)
![Date Input Success ]((imgs/input/menu_two_edit_menu_date_ok.jpg)
</details>

<details>
    <summary>Time Input</summary>

![Time Input Fail]((imgs/input/menu_two_edit_menu_timein_fail.jpg)
![Time Input Success]((imgs/input/menu_two_edit_menu_timein_ok.jpg)
</details>

#### Clock-Out
<br>
When the user enters the clock-out time, either through menu three or two, the clock-out must be later than the clock-in. The format must be correct as well, as with the Time Input feature
<details>
    <summary>Clock-out Input</summary>

![ Clock-out Input Fail]((imgs/input/menu_two_edit_menu_timeout_fail_format_ok.jpg)
</details>

<details>
    <summary>Input Update</summary>

![Menu Three Update ]((imgs/input/menu_three_success.jpg)
</details>




[Back to Table Of Contents](img_directory_here)

## Validation

[Code Institute PEP8 Validation Service](https://pep8ci.herokuapp.com//) was used to check the code for PEP8 requirements. All the code passes with no errors and no warnings to show.

<details><summary>PEP8 Heroku App check for run.py</summary>
<img src=imgs/val/validation_py.jpg>
</details>

<details><summary>PEP8 Heroku App check for color.py</summary>
<img src=imgs/val/color_validation.jpg>
</details>


## Testing

The testing approach for this code was primarily manual testing of user stories<br>

1. I want to easily see employee working hours 

| **Feature**   | **Action**                    | **Expected Result**            | **Actual Result** |
| ------------- | ----------------------------- | -------------------------------| ----------------- |
| Menu One | Selection Main Menu Option 1 | Display organized list of data | Works as expected |


<details><summary>Screenshot</summary>
<img src="imgs/testing/menu_one_sorted.jpg">
</details><br>

2. I want to know what menus are available

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main Menu | Navigate to Main Menu | Display list of Menu Options | Work as expected |

<details><summary>Screenshot</summary>
<img src="imgs/testing/main_menu_selection.png">
</details><br>

3. I want to see what employees are in our database

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Employee Select | Navigate to Employee Select Screen | View a list of names | Work as expected|


<details><summary>Screenshot</summary>
<img src="imgs/testing/employee_request_list.png">
</details><br>

4. I want the softrware protected from just having anyone use it

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Landing-Authentication | Start Program | Be required to enter valid username/password | Works as expected |


<details><summary>Screenshots</summary>
<img src="imgs/testing/landing_un_request.png">
<img src="imgs/testing/landing_pw_request.png">
</details><br>

5. I want to be able to edit existing data 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>

6. I want to add new data for an employee 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>

7. I want to know how many total hours are in the database for each of our employees

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>

8. I want to easily navigate back to the beginning 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>

9. I want feedback on my data input 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>

10. I want to know that my changes have been successful 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>

Number. 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
|  | | | |
|  | | | |

<details><summary>Screenshot</summary>
<img src="">
</details>


[Back to Table Of Contents](#table-of-contents)
## Bugs



## Deployment

### Heroku
This application has been deployed from Github using Heroku. Here's how:
1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

### Forking the GitHub Repository
1. Go to the GitHub repository
2. Click on Fork button in top right corner
3. You will then have a copy of the repository in your own GitHub account.
   
### Making a Local Clone
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it
3. Highlight the "HTTPS" button to clone with HTTPS and copy the link
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone <span>https://</span>github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone

[Back to Table Of Contents](#table-of-contents)

## Credits

### Code


## Acknowledgements
