12/12/2021 <br>
Testing was performed on a continuous basis throughout the entirety of this project.

All codes used will be put through the relevant code validators once all user testing and fixes have been complete.

## Table of Contents

- [Code Validation](#code-validation) <br>
- [User Stories](#user-stories) <br>
- [Manual Testing](#manual-testing) <br>
- [Site Responsiveness](#site-responsiveness) <br>
- [Bugs Encountered](#bugs-encountered) <br>
- [Outstanding Bugs](#outstanding-bugs) <br>


## Code Validation

- CSS passed through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) with no Errors found

- HTML passed through [W3C HTML Validator](https://validator.w3.org/nu/?doc=http%3A%2F%2Fms3-frugaol.herokuapp.com%2Foffers) with alt image errors and src being blank for image preview issue. Alt image errors fixed however, src is to remain blank as image preview will not work without. See below error
![Src_blank_issue](testing_img_docs/business_signup_src_error.png) 

- Javascript passed through [JS Hint](https://jshint.com/). All errors presented have now been fixed. 

- Python passed through [PEP8 Validator](http://pep8online.com/checkresult). All python code is now PEP8 compliant


## User Stories

New User:
- As a new user I want to be able to:
    -   know the exactly with this website is about
    ![N_User_abhaile](testing_img_docs/user_stories/signup.png) 

    -   know the layout of the app easily so that I can navigate the app with ease and avoid frustration
    ![N_User_navigate_app](testing_img_docs/user_stories/signup.png) 

    -   know what the different elements mean so that I can make an informed decision on what element I want to subscribe to
    ![N_User_elements](testing_img_docs/user_stories/signup.png) 

    -   know why I should sign up and decide whether this is the app for me
    ![N_User_element](testing_img_docs/user_stories/signup.png) 

    -   browse the online store easily so that I can purchase something I like. 
    ![N_User_online_store](testing_img_docs/user_stories/signup.png) 

    -   of the health risks involved so that I don’t die 
    ![N_User_disclaimer](testing_img_docs/user_stories/signup.png) 


Existing User:
- As an existing user I want to:
    - have my info saved so that I can purchase items from site without needing to fill out my info again
    ![E_User_info](testing_img_docs/user_stories/signup.png)

    - know about the different breathworks and the benefits associated with them
    ![E_diff_bws_bens](testing_img_docs/user_stories/signup.png)

    - be guided through my breathwork so that I can better understand and learn the different breathing techniques in an engaging environment. 
    ![E_user_focused_breath](testing_img_docs/user_stories/signup.png) 

    - be able to search appropriately so that I can better navigate and find the items I need. 
    ![E_user_search](testing_img_docs/user_stories/signup.png) 

    - be able to access my own profile and update my information as I see fit. 
    ![E_User_update_info](testing_img_docs/user_stories/signup.png) 

    - be able to access my own profile and see my previous order history 
    ![E_user_order_hist](testing_img_docs/user_stories/signup.png) 



Admin User:
- As an Admin user I want to:
    - be able to add products to the site
    ![A_User_add_prod](testing_img_docs/user_stories/signup.png) 

    - be able to edit products on the site
    ![A_User_edit_prod](testing_img_docs/user_stories/signup.png) 

    - be able to see preview images of products I am adding before submitting on edit/add products forms
    ![A_User_pre_image_prod](testing_img_docs/user_stories/signup.png) 

    - be able to add exercises to the site
    ![A_User_add_exer](testing_img_docs/user_stories/signup.png) 

    - be able to edit exercises on the site
    ![A_User_edit_exer](testing_img_docs/user_stories/signup.png) 

    - be able to see preview images of exercises I am adding before submitting on edit/add exercises forms
    ![A_User_pre_image_exer](testing_img_docs/user_stories/signup.png) 


## Manual Testing
- App has been tested extensively by friends and I and no reported or noticable issues or faults present. 

## Site Responsiveness
- App was passed through [Responsive Design Checker](https://responsivedesignchecker.com/) with no notable issues coming back

## Bugs Encountered
12/12/2021: <br>
Project Abhaile was deployed today and sent out to friends and family to test and break. 

This is what has comeback:

#### Profile Image Issue
![Willy-prof_img_issue](testing_img_docs/willy-profimg_issue.png)

- Logo saved not appearing on business profile.
- After testing further the issue is that image uploaded had spaces in filename which has caused an issue materializng from DB. 
- Fix: Have introduced new if statement that initiates flash message telling user that filenames must not include any gaps. Tested and working.

#### Offer Image Extension not allowed
![Willy-offer_img_issue](testing_img_docs/willy-offerimg_extensionnotallowed.png)

- Offer image extension not permitted. Meaning that attempted upload extension was not a recognised extension from the ALLOWED_IMAGE_EXTENSIONS in app.py. 
- After testing further the issue is that extension was .webp
- Fix: Have added .webp extension to ALLOWED_IMAGE_EXTENSIONS in app.py. 


#### Business Sign Up - No Filename
![Colm-no_filename_issue](testing_img_docs/colm-no_filename_issue.jpg)

- User attempted to sign up without uploading image. 
- Fix: Have made flash message easier to understand requesting that user must add logo for sign up. 
- Have also introduced h6 heading above image upload to inform user that logo upload is required for sign up


#### Text Align Issue - Business Profile
![Colm-text_align_issue](testing_img_docs/colm-text_align_issue.jpg)

- Text has not scaled down properly for mobile and circles surrounding social media icons have gone wonky.  
- Fix: Above issues have been fixed through better grid management and centering a div


#### Text Overlap Issue - Offer Profile
![Colm-text_overlap_issue](testing_img_docs/colm-text_overlap.jpg)

- Text has not scaled down properly for mobile and causing overlap. 
- Fix: Now fixed. Better implemented the grid system for materialize to fix

#### File Upload Nothing Appearing - Business/Consumer/Offer Create
![file_upload_no_appear](testing_img_docs/imgfilename_notappearing.png)

- Nothing showing to user when they upload image
- Fix: Now fixed. Have introduced image preview window so user can see image they have selected

## Outstanding Bugs:
- Unfortunately could not find a way to allow files with gap in name to be uploaded to the app. Have included if statement that if this occurs the user will be prompted to rename file.

- Initial plans was to have both Business users and Consumer users login through the same portal however was unable to crack this. System (and me most likely) were unable to distinguish between the different users. To counteract this I made 2 seperate login portals for each user to login through (see below)
![login_portal_issue](testing_img_docs/user_stories/login.png)