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

- HTML passed through [W3C HTML Validator](https://validator.w3.org/) with all errors being fixed. Checker brought back warnings due to jinja but cant do anything to resolve this.

- Javascript passed through [JS Hint](https://jshint.com/). All errors presented have now been fixed. 

- Python code passed through [PEP8 Validator](http://pep8online.com/checkresult) and Flake8 validator. Some errors cannot be fixed like "Avoid using null=True on string-based fields such CharField" and similar. Also brought up issues with migration lengths that cannot be fixed either. 


## User Stories

New User:
- As a new user I want to be able to:
    -   know the layout of the app easily so that I can navigate the app with ease and avoid frustration
    ![N_User_navigate_app](testing_media/user_stories/homepage_nav.png) 

    -   know the exactly with this app/website is about
    ![N_User_abhaile](testing_media/user_stories/homepage.png) 

    -   know what the different elements mean so that I can make an informed decision on what element I want to subscribe to
    ![N_User_elements](testing_media/user_stories/element_hover.png) 

    -   know why I should sign up and decide whether this is the app for me
    ![N_User_element](testing_media/user_stories/water_el_pg_full.png) 

    -   easily sign up
    ![N_User_signup](testing_media/user_stories/sign_up.png) 

    -   follow along to video of exercise in case I do not understand
    ![N_User_video](testing_media/user_stories/yt_link.png) 

    -   browse the online store easily so that I can purchase something I like. 
    ![N_User_online_store](testing_media/user_stories/water_prods_pg_full.png) 

    -   better view the product on offer through multiple images so I know what I am buying. 
    ![N_User_prod_deetz](testing_media/user_stories/water_prod_page_full.png) 

    -   view cart prior to checking out
    ![N_view_cart](testing_media/user_stories/cart_pg_full.png) 

    -   of the health risks involved in exercises so that I don’t die 
    ![N_User_disclaimer](testing_media/user_stories/safety_warning.png) 

<br>

Existing User:
- As an existing user I want to:
    - have my info saved so that I can purchase items from site without needing to fill out my info again
    ![E_User_info](testing_media/user_stories/checkout_pg_full.png)

    - know about the different breathworks and the benefits associated with them
    ![E_diff_bws_bens](testing_media/user_stories/fire_exercise_full_page.png)

    - be guided through my breathwork so that I can better understand and learn the different breathing techniques in an engaging environment. 
    ![E_user_focused_breath](testing_media/user_stories/earth_bubble_in_motion_cropped.png) 

    - be able to search appropriately so that I can better navigate and find the items I need. 
    ![E_user_search](testing_media/user_stories/search.png) 

    - be able to filter appropriately so that I can better navigate and find what I need. 
    ![E_user_filter](testing_media/user_stories/prod_filter.png)

    - be able to access my own profile and update my information as I see fit. 
    ![E_User_update_info](testing_media/user_stories/profile_page_full.png) 

    - be able to access my own profile and see my previous order history 
    ![E_user_order_hist](testing_media/user_stories/order_hist.png) 

<br>

Admin User:
- As an Admin user I want to:
    - be able to add products to the site
    ![A_User_add_prod](testing_media/user_stories/add_prod_full.png) 

    - be able to edit products on the site
    ![A_User_edit_prod](testing_media/user_stories/edit_prod_full_pg.png) 

    - be able to see preview images of products I am adding before submitting on edit/add products forms
    ![A_User_pre_image_prod](testing_media/user_stories/add_prod_in_action_img.png) 
    ![A_User_pre_image_prod2](testing_media/user_stories/edit_prod_full_img.png) 

    - be able to add exercises to the site
    ![A_User_add_exer](testing_media/user_stories/add_exer_in_action.png) 

    - be able to edit exercises on the site
    ![A_User_edit_exer](testing_media/user_stories/edit_exer_full.png) 

    - be able to see preview images of exercises I am adding before submitting on edit/add exercises forms
    ![A_User_pre_image_exer](testing_media/user_stories/edit_exer_pg.png) 

    - be able to restrict access to certain parts of site to incentivise new sign ups 
    ![A_User_restrict](testing_media/user_stories/exer_page_not_avail.png) 

## Manual Testing
- App has been tested extensively by friends and I and no reported or noticable issues or faults present. 

## Site Responsiveness
- App was passed through [Responsive Design Checker](https://responsivedesignchecker.com/) with no notable issues coming back

## Bugs Encountered
12/12/2021: <br>
Project Abhaile was deployed today and sent out to friends and family to test and break. 

This is what has comeback:

### Element Page issue (mobile)
![overlap_issue](testing_media/testing/overlap.jpg)

- Element product and exercise buttons going over text on mobile.
- After testing further the issue is that when user is not Abhaile member, request for user to sign up is bigger than buttons involved, pushing container into above div. 
- Fix: Have introduced more marginning to help space out affected divs.


### Breath Sync not starting. 
![breath_sync_not_working](testing_media/testing/breathe_rd_issue_nostart.png)

- Since round dropdown inclusion, breath focus on exercise pages not working
- After testing further the issue is that the default value on "Choose Your Rounds" selection was set to 0 so when user attempted to start exercise, round was 0 so couldnt start
- Fix: Have now set default value to "1" so that when user doesnt select round, the exercise still starts. 


### Hold timer/Postround timer on Breath Sync not initiating at end of round
![timer_no_start](testing_media/testing/timernostart.png)

- Hold countdown timer not initiating post end of round. 
- After testing further the issue is that the Sleep JS function used at round end to pause exercise stopped entire app and so hold timer start event couldnt start.
- Fix: Have remvoved this Sleep function and instead added a new animation to mimic end round functionality. In addition, hold timer starts one rep before this hold animation starts allowing holdtimer to initiate at same time of end round pause. 


### Sort Box Issue (Resize)- Mobile display issue 
![sort_box_resize_issue](testing_media/testing/sort_resize.jpg)
![sort_box_resize_issue_prod](testing_media/testing/sortboxissue.png)

- On mobile, sort boxes not scaled down correctly. 
- Fix: Fixed by targetting select elements and bringing down font size


### Prod Image Scale - Mobile display issue
![prod_img_selector_mob](testing_media/testing/prod_img_off_screen.jpg)

- Image container on product pages overflowing on mobile. 
- Fix: Now fixed. Introduced media queries and vh and vw sizes to better adapt to all devices


### Admin Issue - Edit/Add buttons for Products not scaling down properly
![admin_issue_edit_add_mob](testing_media/testing/editadd_mob.jpg)

- On mobile, edit and add buttons not showing properly and overlapping down to items below
- Fix: Now fixed. Have introduced better grid structure. Edit & Delete now appearing on own row


### Cart Page Issue - Cart items appearing messy on mobile
![cart_issue_mob](testing_media/testing/cart_pg_messy.png)

- On mobile, items in cart not scaling down correctly on mobile. 
- Fix: Now fixed. Have introduced better media queries to account for adjusting sizes



- Common complaint that has come back is that yellow color for air pages is hard to distinguish against the white. Have added a snow color instead throughout site to combat this. 



<br>

## Outstanding Bugs and Encountered problems with no fix:
- The focused breath system was fully developed by me and through the use of keyframe animations, await/async and getProperty functionality was able to get this working for the most part. Unfortunately I was unable to integrate staggered breathing functions ie, one inhale leads to 10 exhales, or,inhale for 2 sec, inhale for 3 sec, inhale 2 sec, exhale for 2, exhale for 3, exhale for 2 etc. This will be looked into more post MS4 and try find a pattern that I can replicate in Javascript

- Have attempted to introduce a subscription system, spending over a week and countless hours trying to implement, but was unable to blend a sub system into the existing product system and checkout due to stripe restrictions. In hindsight, the better solution to implement both might have been to introduce the subscription system first and then blend the ecom store into it that way. Due to time and knowledge constraints I have been regretfully forced to abandon this but am eager post MS4 to get this going. 