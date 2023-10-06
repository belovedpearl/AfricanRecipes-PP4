**Table of Contents:**
---
---
 * [Scope](#scope)  
 * [Background](#background)
 * [Target Audience](#target-audience)
 * [Wireframes](#wireframes)
    * [Wireframe 1](#wireframe-1-the-landing-page)
    * [Wireframe 2](#wireframe-2-the-recipe-detail-page)
* [User Stories](#user-stories)
    * [Admin User Story](#admin-user-story)
    * [General User User Story](#general-user-user-story)
    * [Unregistered users User Story](#unregistered-user-user-story)
    * [Registered users User Story](#registered-user-user-story)
* [Features](#features)
    * [Base Template](#base-template)
        * [Header and Navbar](#header-and-navbar)
        * [A Section for the Messages](#a-section-for-the-messages)
        * [Footer](#footer)
    * [Landing Page](#landing-page)
        * [Recipes](#recipes)
        * [Pagination](#pagination)
        * [Recipe by Country](#recipe-by-country)
---
# SCOPE
---



The scope of this project is to create a website using Python Django framework, tailored to showcase a diverse collection of authentic African recipes.

Key features will include:

**User Authentication:** The website will use the Django AllAuth library to enable user account creation and login functionality. Once registered and logged in, users gain access to the website's full suite of features.

**Recipe Management:** Registered users will have the capability to contribute their own recipes. Additionally, they can update their recipes over time to keep the content fresh and relevant.

**User Engagement:** Users can express their appreciation for recipes by liking them. They can also express their dislikes if a particular recipe does not align with their taste.

**Recipe Deletion:** Registered users will have the ability to delete their own recipes, providing them with control over their contributed content.

**Country-Based Navigation:** The website will offer a user-friendly way for visitors to search recipes from specific African countries. Users can either click on a country's name or utilize the dropdown menu featuring a list of african countries.

By implementing these features, 'Mama's Kitchen' aims to foster an engaging community for African food enthusiasts, where users can share, discover, and appreciate the rich heritage of African kitchen.

---
# Background
---

This project is inspired by the Code Institute 'I think there for I Blog' walkthrough project. As an African, I have always had a concern for African heritage which is not well preserved and  adequately transferred to the next generation.

I have taught of a way to preserve and promote the African culture especially providing a means whereby users of this platform can have access to different African traditional food from across the globe.

As it is well known that one of the factors for decline in active transfer ia the modernization and also immigration which has made different people forget or have little or no knowledge about their root.

This project seeks to be a store house for African Trditional meals where individuals can access different foods thereby promoting and preserving the heritage to generations.


---
# Target Audience
---

This project is tailored for a vibrant community of Africans, both at home and abroad, eager to delve deeper into the richness of African cuisine. The platform offers a delightful exploration of diverse African recipes. Whether an aspiring home chef or simply curious about the flavors of the continent.

---
# Wireframes
---

While conceiving the project the following were the wireframes were used to represent the home and details page.

All wireframes are made with Balsamiq

Link for the wireframe pictures can be found ![here](static/images/wireframes/)

---

## Wireframe 1: The Landing page

### Desktop and Laptop

![Desktop and Laptop](static/images/wireframes/mama's%20kitchenhomepagedesktop&Laptop.webp)

### Mobile

![Mobile](static/images/wireframes/mama'skitchenhomepagemobile.webp)

---

## Wireframe 2: The Recipe Detail page

### Desktop and Laptop
![Desktop and Laptop](static/images/wireframes/mama'skitchendetailsdesktop&laptop.webp)


### Mobile

![Mobile](static/images/wireframes/mama'skitchendetailmobile.webp)

---

# User Stories

Below are the User Stories used to guide the development of Mama's Kitchen.

## Admin User Story

The Admin user User Stories were used as a guide to determine what Admin Superusers that have access to the Admin panel should be able to do.

As an Admin user I can..

Navigate to the admin sign-in page, so that I can sign in to the admin panel.

View all recipe posts submitted by users, so that I can view and edit posts if needed.

Filter and sort recipe posts easily, so that I can see all of the posts that needs to be approved.

Approve any number of selected recipes post so that they can be be visible on the site.

Delete any number of selected recipe, so that they no longer take up memory in the database especially the ones that are not on line with the platform ideas.

Make posts with rich text and images, so that I can improve the quality of posts.

Add a recipe post, so that I do not have to use the add post page on the front-end

Filter and sort all comments easily, so that I can see all recipes posts that fulfil certain criteria

---


## General User User Story

Generally, as a user I can ..

Immediately determine the purpose of the application on first visit, so that I can quickly decide whether its of interest or not.

Have a positive user experience irrespective of the means of access, so that I can access the application from enjoy the platform from any device

View all recipe posts so that I can choose one to read in detail.

Sort recipe posts by country name so that I can see only the recipe post of intrested countries.

If my search  by country returned no results, have a message displayed informing me of no posts related to my country search.

---
## Unregistered-user-User-Story

These user stories were outlined to determine specifically, what unregistered user should be able to do.

Sign-up and create an account, so that I can access the detailed functionality of the application.
Sign-in to that created account, so that I can access the detailed functionality of the application.

---

## Registered user User Story

These user stories helped to determine what registered users specifically should be able to do.

As a registered user I can ...

* Sign in to an already existing account, so that I can access the full functionality of the application.

* Edit recipe posts I created so that I can improve or modify the content.

* Delete recipe posts I created so that I know that I have the control of the content I created.

* Change the password for that account, so that it becomes more memorable.

* Sign-out easily, when already signed-in, so that I can be sure that my session was closed securely.

* Have my sign-in status reflected back to me, so that I can be sure that I have signed-in.

* Add a recipe post easily so that I can share food recipe on the website.

* Apply rich text formatting to the content of my recipe, so that I can better express myself and provide additional structure to my recipe.

* Upload an image to my recipe, so that I can show other users what the recipe looks like.

* If there is no recipe when searching by countrry, have that reflected back to me so that I know that there is no recipe for the selected country.

* Allow for confirmation of delete recipe befor deletion, so that I cannot accidentally delete any recipe post.

* Be alerted when I have posted a recipe, so that I can be assured that I have submitted the recipe.

* Be informed when I have successfully signed in, so that I can be assured that I have submitted the right details.

* Be informed when I have updated a recipe, so that I can be assured that I have updated the recipe.

* Be informed when I have deleted a recipe, so that I can be assured that I have deleted the recipe.

* When viewing a recipe detail, like the page , so that I can express my thoughts of the recipe.

* When viewing a recipe detail, dislike the page , so that I can express my thoughts of the recipe.

---
# Features

---
This section discusses the features and pages of the project 'Mama's Kitchen', the design choices made, discussion of the HTML and CSS codes. Where appropriate, the views and forms used to render those pages are also discussed.

---

## Base Template

Mama's Kitchen uses a single base template file extended to every other page, this is to provide a consistent user experience and promote uniformity across the website. Codes from the other templates are injected in=between the center element ({insert block content} & {end block content}) to relay the specificity of each page.
The base template is made up of the following;

### Header and Navbar

The navbar provides navigation to other pages of Mama's Kitchen. The navbar was created using a standard Bootstrap navbar and its responsive on different screen sizes. Each list item in the navbar is a link that changes color when hovered notifying user of mouse movement over the link.
Active pages are styled with custom CSS by a background color, border radius of 10px with black text. This was included to inform user about the page they are currently on.

All users have access to the default landing page (index page) by clicking either the bolded Mama'sKitchen icon or the Home Link. 
All users can search recipes by countries using the dropdown on the country link or clicking on their preferred country name on each recipe. A click on the country name filters the database by the recipe of the country, if there is no recipe for the country, the user is informed, more details will be discussed in the 'countries page' section.

If the user is signed out or has not yet created an account, navigation options after the above are either Log-in to an existing account or Register a new account. A user may create an account by clicking on the Sign Up link, or Sign in to an existing account by clicking on the Sign In link.

If the user is signed-in, navigation options are to either Sign-out or Add a new Recipe. The user may click on the Add Recipe link to be directed to a page where they may create and upload a recipe of choice.

On the right end of the navbar, unregistered users are presented with the statement 'Tasty African Recipe' while registered signed in users are presented with the caption 'Signed in as <username>'. This section  has two functions; first, it identifies the specific logged in user by displaying their name. The username also acts as a link where users can edit their profile information.


### A section for the messages
Messages if available are relayed to the users here. This message can be as a result of actions like login, logout, updating a profile, submitting a recipe. They all assure the user of the completion of their actions.

### Footer 
Links to various social media platforms are featured here with a copyright caption.


---

## Landing Page
---

This is the template rendered to the users when visiting the deployed site (Mama'sKitchen). The landing page is rendered from templates/index.html using the RecipeView view.
This view inherits from the Django [ListView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/) class. It uses the model Recipe and queries the database for approved posts. It paginates by 6 recipes per page allowing users navugatre to other page to view more recipes.
In order to provide additional context-data a function was defined to return the url_name and the country list as part of the rendered template. 

Landing page screenshot:



### Recipes

Each recipe card presents a brief overview of a particular recipe. Allowing thw user to view the image, local name, post author, country, likes and dislikes, date posted. A user click on the local name directs the user to a page containing more details (cook-time, instructions, ingredients) about the recipe.

The details page with its view is discussed below.

Recipe Screenshot:


### Pagination

The landing page is set to display recipes in batches of 6. Other recipes are paginated. The pagination allows users  to move in a variety of ways that intrest the user. Users can choose to move to the first page to view the first 6 recipes, move to the previous page from where they are currently on, move to the next page from where they are currently on, move to the last page of available recipes. By clicking on the button **First**, **Previous**, **Next**, **Last** respectively.

Users can access any particular pagination page by clicking on the appropriate numbered square. If any of the first, last, previous or last options are not available, then the button still displays, but is greyed-out and has no active href attribute. This was implemented to provide a consistent style as the user navigates the recipes paginated pages.

Including the pagination will help users to have a smooth scroll through to different pages of the site.

Pagination bar:


### Recipe by Country

Due to the nature of the project and its targets, I initially considered allowing users to filter the recipes available by country name. Users can access this function by either clicking on their desired country name on each post or by using the country dropdown in the navbar to select their choiced country.

If there are no recipe posted for such country, users are given a feedback informing them of no recipe posted for their country of choice. Users are then ebcouraged to add recipe for such country.

Dropdown picture of Afrcican Countries:






