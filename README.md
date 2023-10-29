# Mama'sKitchen - *African food recipes*

[View code here](https://github.com/belovedpearl/AfricanRecipes-PP4)

![Responsiveness](screenshots/live_site/responsive.webp)

[View site responsiveness here](https://ui.dev/amiresponsive?url=https://africanrecipes-95e71e30ded1.herokuapp.com/)

---


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
    * [Admin Section](#admin-section)
    * [Landing Page](#landing-page)
        * [Recipes](#recipes)
        * [Pagination](#pagination)
        * [Recipe by Country](#recipe-by-country)
    * [Details Page](#details-page)
    * [Add Recipe Page](#add-recipe-page)
    * [Update Recipe](#update-recipe)
    * [Delete Recipe](#delete-recipe)
    * [Share Post](#share-post)
    * [Countries Page](#countries-page)
    * [Edit User Page](#edit-user-page)
    * [Sign-In, Sign-Out, Sign-Up Pages](#sign-in-sign-out-sign-up-pages)
    * [Messages](#messages)
    * [Error Pages](#error-pages)
* [Database Model](#database-model)
     * [Recipe Class](#recipe-class)
         * [Recipe Class Method](#recipe-class-methods)
     * [Country Class](#country-class)
          * [Country Class Methods](#country-class-methods)
* [Recipes Views](#recipe-views)
     * [Landing Page View](#landing-page-view)
     * [Details Page View](#details-page-view)
     * [Likes and Dislike View](#likes-and-dislike-views)
     * [Add Recipe View](#add-recipe-view)
     * [Update Recipe View](#update-recipe-view)
     * [Delete Recipe View](#delete-recipe-view)
     * [Country View](#country-view)
     * [Edit User View](#edit-user-view)
     * [Change Password View](#change-password-view)
* [Recipe Forms](#recipe-forms)
     * [Recipe Form](#recipe-forms)
     * [Edit Profile Form](#edit-profile-form)
     * [Change Password Form](#change-password-form)
* [Mama'sKitchen Url](#mamaskitchen-url)
* [Mama'sKitchen Admin](#mamaskitchen-admin)
* [Future Features](#future-features)
* [Bugs](#bugs)
     * [Requirements File Bug](#requirements-file-bug)
     * [Active Link Bug](#active-link-bug)
     * [Add Recipe Page Bug](#add-recipe-page-bug)
     * [Country Page Bug](#country-page-bug)
     * [Update Recipe Image Input](#update-recipe-image-input)
     * [Missing Navbar Toggler](#missing-navbar-toggler)
     * [Image Size Bug](#image-size-bug)
     * [Likes and Dislike Message Bug](#likes-and-dislike-message-bug)
     * [Flash Messages](#flash-messages)
     * [Country Dropdown List](#country-dropdown-list)
     * [Home Page Validation Bug](#home-page-validation-bug)
     * [First Project Error and Restart](#first-project-error-and-restart)
     * [Tab Duplication Bug](#tab-duplication-bug)
     * [Heroku Deployment Bug](#heroku-deployment-bug)
* [Design Choices](#design-choices)
    * [Font](#font)
    * [Color Scheme](#color-scheme)
    * [Favicon](#favicon)
* [Accessibility](#accessibility)
* [Technology Used](#technology-used)
    * [Languages](#languages)
    * [Python Modules and Packages Used](#python-modules-packages-used)
* [Framework and Tools](#frameworks-and-tools)
* [Development and Deployment](#development-and-deployment)
* [How to Fork](#how-to-fork)
* [How to Clone](#how-to-clone)
* [Testing](#testing)
* [Tools](#tools)
* [Credits](#credits)
* [Acknowledgement](#acknowledgement)


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

By implementing these features, 'Mama'sKitchen' aims to foster an engaging community for African food enthusiasts, where users can share, discover, and appreciate the rich heritage of African kitchen.

---

# Background

---

This project is inspired by the Code Institute's 'I think there for I Blog' walkthrough project. As an African, I have always had a concern for African heritage which is not well preserved and  adequately transferred to the next generation.

I have taught of a way to preserve and promote the African culture especially providing a means whereby users of this platform can have access to different African traditional food from across the globe.

As it is well known that one of the factors responsible for decline in active transfer of heritage is the modernization and also immigration which has made different people forget or have little or no knowledge about their root.

This project seeks to be a store house for African Trditional meals where individuals can access different foods thereby promoting and preserving the heritage to generations.


---

# Target Audience

---

This project is tailored for a vibrant community of Africans, both at home and abroad, eager to delve deeper into the richness of African cuisine. The platform offers a delightful exploration of diverse African food recipes, whether an aspiring home chef or simply curious about the flavors of the continent.


---

# Wireframes

---

While conceiving the project the following were the wireframes were used to represent the home and details page.

All wireframes are made with Balsamiq

Link for the wireframe pictures can be found ![here](wireframes/)

---

## Wireframe 1: The Landing page

### Desktop and Laptop

![Desktop and Laptop](wireframes/mama's_kitchen_homepage_desktop&Laptop.webp)

### Mobile

![Mobile](wireframes/mama's_kitchen_homepage_mobile.webp)

---

## Wireframe 2: The Recipe Detail page

### Desktop and Laptop
![Desktop and Laptop](wireframes/mama's_kitchen_details_desktop&laptop.webp)


### Mobile

![Mobile](wireframes/mama's_kitchen_detail_mobile.webp)

---

# User Stories

Below are the User Stories used to guide the development of Mama'sKitchen.

## Admin User Story

The Admin user User Stories were used as a guide to determine what Admin Superusers that have access to the Admin panel should be able to do.

As an Admin user I can..

* Navigate to the admin sign-in page, so that I can sign in to the admin panel.

* View all recipe posts submitted by users, so that I can view and edit posts if needed.

* Filter and sort recipe posts easily, so that I can see all of the posts that needs to be approved.

* Approve recipes post so that they can be be visible on the site.

* Delete any number of selected recipe, so that they no longer take up memory in the database especially the ones that are not on line with the platform ideas.

* Make posts with rich text and images, so that I can improve the quality of posts.

* Add a recipe post, so that I do not have to use the add post page on the front-end

* Filter and sort all comments easily, so that I can see all recipes posts that fulfil certain criteria

---


## General User User Story

Generally, as a user I can ..

* Immediately determine the purpose of the application on first visit, so that I can quickly decide whether its of interest or not.

* Have a positive user experience irrespective of the means of access, so that I can access the application from enjoy the platform from any device

* View all recipe posts so that I can choose one to read in detail.

* Sort recipe posts by country name so that I can see only the recipe post of intrested countries.

* If my search  by country returned no results, have a message displayed informing me of no posts related to my country search.

---

## Unregistered-user-User-Story

These user stories were outlined to determine specifically, what unregistered user should be able to do.

* Sign-up and create an account, so that I can access the detailed functionality of the application.

* Sign-in to that created account, so that I can access the detailed functionality of the application.

---

## Registered user User Story

These user stories helped to determine what registered users specifically should be able to do.

As a registered user I can ...

* Sign in to an already existing account, so that I can access the full functionality of the application.

* Add a recipe post easily so that I can share food recipe on the website.

* Edit recipe posts I created so that I can improve or modify the content.

* Delete recipe posts I created so that I know that I have the control of the content I created.

* Change the password for that account, so that it becomes more memorable.

* Sign-out easily, when already signed-in, so that I can be sure that my session was closed securely.

* Have my sign-in status reflected back to me, so that I can be sure that I have signed-in.


* Apply rich text formatting to the content of my recipe, so that I can better express myself and provide additional structure to my recipe.

* Upload an image to my recipe, so that I can show other users what the recipe looks like.

* If there is no recipe when searching by countrry, have that reflected back to me so that I know that there is no recipe for the selected country.

* Allow for confirmation of delete recipe before deletion, so that I cannot accidentally delete any recipe post.

* Be alerted when I have posted a recipe, so that I can be assured that I have submitted the recipe.

* Be informed when I have successfully signed in, so that I can be assured that I have submitted the right details.

* Be informed when I have updated a recipe, so that I can be assured that I have updated the recipe.

* Be informed when I have deleted a recipe, so that I can be assured that I have deleted the recipe.

* When viewing a recipe detail, like the page , so that I can express my thoughts of the recipe.

* When viewing a recipe detail, dislike the page , so that I can express my thoughts of the recipe.

---

# Features

---
This section discusses the features and pages of the project 'Mama'sKitchen', the design choices made, discussion of the HTML and CSS codes. Where appropriate, the views and forms used to render those pages are also discussed.

---

## Base Template

Mama's Kitchen uses a single base template file extended to every other page, this is to provide a consistent user experience and promote uniformity across the website. Codes from the other templates are injected inbetween the center element ({insert block content} & {end block content}) to relay the specificity of each page.

The base template is made up of the following;

### Header and Navbar

The navbar provides navigation to other pages of Mama's Kitchen. The navbar was created using a standard Bootstrap navbar and its responsive on different screen sizes. Each list item in the navbar is a link that changes color when hovered notifying user of mouse movement over the link.
Active pages are styled with custom CSS by a background color, border radius of 10px with black text. This was included to inform user about the page they are currently on.

All users have access to the default landing page (index page) by clicking either the bolded Mama'sKitchen icon or the Home Link. 
All users can search recipes by countries using the dropdown on the country link or clicking on their preferred country name on each recipe. A click on the country name filters the database by the recipe of the country, if there is no recipe for the country, the user is informed, more details will be discussed in the 'countries page' section.

If the user is signed out or has not yet created an account, navigation options after the above are either Log-in to an existing account or Register a new account. A user may create an account by clicking on the Sign Up link, or Sign in to an existing account by clicking on the Sign In link.

If the user is signed-in, navigation options are to either Sign-out or Add a new Recipe. The user may click on the Add Recipe link to be directed to a page where they may create and upload a recipe of choice.

On the right end of the navbar, unregistered users are presented with the statement 'Tasty African Recipe' while registered signed in users are presented with the caption **'Signed in as <username>'**. This section  has two functions; first, it identifies the specific logged in user by displaying their name. The username also acts as a link where users can edit their profile information.

<details>
<summary>Header and Navbar Picture for Registered Users</summary>
<img src="screenshots/live_site/navbar-reg.webp" width="80%">
</details>

<details>
<summary>Header and Navbar Picture for Non-Registered Users</summary>
<img src="screenshots/live_site/navbar-nonreg.webp" width="80%">
</details>


### A section for the messages
Messages if available are relayed to the users here. This message can be as a result of actions like login, logout, updating a profile, submitting a recipe. They all assure the user of the completion of their actions.

### Footer 
Links to various social media platforms are featured here with a copyright caption.

![Footer Picture](screenshots/live_site/footer.webp)


---

## Admin Section 

The project Mama'sKitchen has an admin section accessible only to its superusers. The admin section is displayed in a list for easy view by the admin, in the search field, recipes can be searched by recipe title, cook time and country. Also, the list can be filtered by date created, post approved and country, all this were included to ease the admin duties. There is also a section where the admin is set to manage the country list. The admin can view the list of countries from here.
Once the section is accessed, superusers may:

+ Create recipes to add to the page.
+ View the list of all submitted recipes.
+ Update and delete any submitted recipes.
+ Approve a recipe post so that it will be displayed on the main application.
+ View the list of all country names.
+ Update and delete countries when needed.
+ View a list of all authenticated users.
+ Delete any user.
+ Update any user information.
+ Change status of users to staff or superusers.


---

## Landing Page
---

This is the template rendered to the users when visiting the deployed site (Mama'sKitchen). The landing page is rendered from templates/index.html using the RecipeView view.
This view inherits from the Django [ListView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/) class. It uses the model Recipe and queries the database for approved posts. It paginates by 6 recipes per page allowing users navigate to other page to view more recipes.
In order to provide additional context-data a function was defined to return the url_name and the country list as part of the rendered template. 

![Landing page screenshot](screenshots/live_site/landing-page.webp)


### Recipes

Each recipe card presents a brief overview of a particular recipe. Allowing the user to view the image, local name, post author, country, likes and dislikes, date posted. A user click on the local name directs the user to a page containing more details (cook-time, instructions, ingredients) about the recipe.

The details page with its view is discussed below.

<details>
<summary>Screenshot of recipe card with image and template image respectively</summary>
    <img src="screenshots/live_site/recipe-card.webp" width="80%">
    <img src="screenshots/live_site/recipe-card2.webp" width="80%">
</details>

### Pagination

The landing page is set to display recipes in batches of 6. Other recipes are paginated. The pagination allows users  to move in a variety of ways that intrest the user. Users can choose to move to the first page to view the first 6 recipes, move to the previous page from where they are currently on, move to the next page from where they are currently on, move to the last page of available recipes. By clicking on the button **First**, **Previous**, **Next**, **Last** respectively.

Users can access any particular pagination page by clicking on the appropriate numbered square Including the pagination will help users to have a smooth scroll through to different pages of the site thereby improving user experience.

Pagination bar:
![Pagination Bar Picture](screenshots/live_site/pagination.webp)


### Recipe by Country

Due to the nature of the project and its targets, I initially considered allowing users to filter the recipes available by country name. Users can access this function by either clicking on their desired country name on each post or by using the country dropdown in the navbar to select their choiced country.

If there are no recipe posted for such country, users are given a feedback informing them of no recipe posted for their country of choice. Users are then encouraged to add recipe for such country.

![Dropdown Picture of African Countries](screenshots/live_site/country-list.webp)


---

## Details Page

To promote the use of the site among users, all users are allowed access to the details page.The details page is used to display all about a single recipe that is clicked. It is rendered using the details template and the **RecipeDetails** view. The details page is styled mostly with bootstrap and some vanilla css. It features the recipe picture, title(recipe localname), number of likes and dislikes, instructions, ingredients, cook time.
The details page restricts some of its features, it displays the edit and delete button for recipe author and prevent non-authors access to it, it also allows authenticated users access to like and dislike function for each recipe.
A signed-in user and author of a recipe can edit or delete his recipe post from here.
The page also contains a placeholder image for posts made without an image this is to allow recipe in which its author might not have the picture as at when making the post.

Additionally, at the end of the recipe description is the back button that directs the user back to the default landing page providing an alternative to the user's browser back button.

<details>
<summary>Screenshot of recipe details page</summary>
<img src="screenshots/live_site/details-page.webp" width="80%">
</details>

---

## Add Recipe Page

The add recipe page is rendered using the addrecipe template and the AddRecipe view. The AddRecipe class inherits from the class CreateView. It allows users to submit new recipe to be posted to the platform. 

The addrecipe page allows a user to write and submit a recipe of choice specifying the country it belongs. Submitting the recipe is done with a form and submitted. The user must enter all of the necessary information about the recipe like the title, ingredients required, instructions,  cook time. The user has to choose from the dropdown provided the country, a placeholder image is used if the user fails to provide a recipe image as I considered some users might not have the recipe picture but have the recipe description.

Recipe posts submitted needs to be approved by an administrator before it can be updated on the page. On successfull submission of recipe, the user is notified of the successful submission of the recipe and an assurance that its awaiting approval from an administrator.

Success message is relayed to the users using the imported class based view [SuccessMessageMixin](https://tech.serhatteker.com/post/2020-11/show-success-message-in-cbv-django/). 

Recipe posts needs to be approved to prevent unwanted posts from the platform.

<details>
<summary>Screenshot of add recipe page</summary>
    <img src="screenshots/live_site/addrecipe-page.webp" width="80%">
    <img src="screenshots/live_site/addrecipe-page2.webp" width="80%">
    <img src="screenshots/live_site/addrecipe-page3.webp" width="80%">
</details>

---

## Update Recipe Post

The update recipe page is rendered using the updaterecipe template and the UpdateRecipe view. 
Only authenticated users have access to the update recipe page, I added a link to direct unauthenticated users to the signup page in case they try to access this page.

To render the page, it inherits from the class based view [UpdateView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/). It uses the model Recipe and the form RecipeForm class. Users get a feedback of successful recipe post edit using the SuccessMessageMixin to generate the message contained in the success_message variable as contained in the class definition.

To update a recipe post, the form field are pre-filled once the user click the specific recipe to update, this is done via the specific primary key of each post. The users can then update the needed field.

Only recipe post authors can update their recipe to prevent abuse of the update function since updating does not require permission from the administrator.

<details>
<summary>Screenshot of update recipe page</summary>
    <img src="screenshots/live_site/update-page.webp" width="80%">
    <img src="screenshots/live_site/update-page2.webp" width="80%">
    <img src="screenshots/live_site/update-page3.webp" width="80%">
</details>


I have included the measure below to prevent unregistered users with links to any of the recipes from updating any recipe.

<details>
<summary>Screenshot page displayed to Non-registered users on attempt to update recipe</summary>
    <img src="screenshots/live_site/update-page-nonuser.webp" width="80%">
</details>

---

## Delete Recipe

The delete recipe page is rendered using the deleterecipe template and the DeleteReview view. The view inherits from the class based view [Deleteview](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/). It uses the model Recipe. Upon successful deletion, it reverts back to the home page.

A simple template page that allows a user to delete a particular recipe. Rather than allowing the recipe posts deleted immediately after the user clicks on the delete, I allowed the user to choose weather to continue with the deletion or stop the process. Once deleted, the user is redirected back to the homepage and a message is relayed confirming successful deletion from the database.

To delete a recipe post, only the author is allowed to access the delete function of a particuler recipe post, non-authors of the posts are informed that they cannot delete any post with a link to go back to the home page. Also unauthorized users are informed that they are not allowed to delete any posts and can signup using the link to register.



**Screenshot of delete page**

<details>
<summary>Screenshot of delete recipe page</summary>
    <img src="screenshots/live_site/author-delete.webp" width="80%">
    <img src="screenshots/live_site/non-user.webp" width="80%">
</details>


---

## Share Post 

While building this project, I thought about adding a feature to allow users share recipe post. All users can share posts from this platform, this is to further promote the awareness for this site and also help to reach more audience with the african recipes.

Using the [social share](https://pypi.org/project/django-social-share/) documentation on django and a bootstrap dropdown, I was able to include a share post feature on twitter, telegram and whatsapp. I would have loved to include facebook but it was said in the documentation that facebook no longer supports this feature.

**Share post feature**

![Share post dropdown picture](screenshots/live_site/share-recipe.webp)

---

## Countries Page
This page presents to users a list of recipes available for their country of choice. Users can choose countries either by using the country dropdown as shown in the **"recipes by countries"** section or by clicking on the country name in each post.

The page is rendered using the countries template and the CountryView view. The view retrieves country object from the country model and gets all recipe that matches the query from the the recipe model. It renders the countries template with the requested recipes.

Each post is quite similar in display to the landing page but it does not have the country names specified on each post anymore as the recipe displayed belong to the same country referred to in the subject header.


**Screenshot of the Country Page**

![Country page screenshot](screenshots/live_site/country-page.webp)


---

## Edit User Page

The page is rendered using the edit_profile template and the EditUserView. Once signed in, users can click on their name on the right corner of the navbar to be taken to the edit_profile page. Users can then update whatever user detail they want to change. 

Once updated, users are redirected back home and a message is popped onto the screen confirming successful update of the user's profile.


<details>
<summary>Edit Profile page screenshot</summary>
    <img src="screenshots/live_site/edit-profile.webp" width="80%">
</details>

---

## Change Password Page
 As part of the user's profile, the website include functionality that allows users to change their password if needed. A click on 'this form' brings up the change password page.
 
  To change password, user is required to provide their old password, the new one and a confirmation of the new one.

**Password change access**
 ![Click](screenshots/live_site/passchange-access.webp)

<details>
<summary>Password Change Page</summary>
    <img src="screenshots/live_site/password-change.webp" width="80%">
</details>

---

## Sign In, Sign Out, Sign Up Pages

These are modified versions of the standard AllAuth templates that can be copied over from the site-packages directory with the cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates command. Its modification include extending mama's kitchen base template and adding some bootstrap classes.

<details>
<summary>Sign In page screenshot</summary>
    <img src="screenshots/live_site/sign-in.webp" width="80%">
</details>

<details>
<summary>Sign Out page screenshot</summary>
    <img src="screenshots/live_site/sign-out.webp" width="80%">
</details>

<details>
<summary>Sign Up page screenshot</summary>
    <img src="screenshots/live_site/sign-up.webp" width="80%">
</details>

---

## Messages

This was included to give the user a form of feedback for their actions. Users get a message when they successfully sign-in, sign-out, add a recipe post, delete a recipe post, change password, update their profile information.

<details>
<summary>Message Sample screenshots</summary>
    <img src="screenshots/live_site/password-changed.webp" width="80%">
    <img src="screenshots/live_site/post-update.webp" width="80%">
    <img src="screenshots/live_site/profile-update.webp" width="80%">
    <img src="screenshots/live_site/signin-feedback.webp" width="80%">
    <img src="screenshots/live_site/signout-feedback.webp" width="80%">
</details>


---

## Error Pages

I have added an error 400 and 500 pages to the website. They provide links back to the home page.

**Error 400**

![Error 400](screenshots/live_site/error-400.webp)

**Error 500**

![Error 500](screenshots/live_site/error-500.webp)


---

# Database Model

![Representation of the user structure and the model used.](static/images/site_description/recipe_db_model.png)

This section shows a representation of user structure and the database used in the buildup of Mama'sKitchen project. Two models were made representing the Recipe and Country.

## Recipe Class

The is used as a template to add in different recipes, users and admin can add post using this model.

|Field | Details|
|---   | --------
|Title | CharField with maximum length set to 150 Each title is set be be unique|
| Author| This takes the creators name, It is a foreign key linked to Users model. Deleting the author will cause all posts in the author's name to be deleted as well (on_delete=models.CASCADE)|
|Instructions| This field takes text(TextField()) describing the cooking process.|
|Ingredients| This field takes text(TextField()) describing the cooking materials.|
|Recipe Image| A cloudinary image field. If users fail to provide an image it is set to the default placeholder.|
|Cook Time| Represents the time required. It is set to PositiveIntegerField()|
|Country| A foreign key which represents recipe country. If not provided, the default is applied.|
|Likes| ManyToManyField, since many users can like many posts.|
|Dislikes|ManyToManyField, since many users can dislike many posts.|
|Date Created | Sets the date the post is made. It is set to auto_now_add=True so that exact time of creating the post can be recorded.|
| Date Updated | Sets the date any update is made on the post.|
|Post Approved |A BooleanField that default to 'False'. Can be changed by admin to make post appear on the site.|

### Recipe Class Methods
Recipe class contains some methods; 

* The first been the Meta class which returns the ordering of the recipes.
* A string method returning the recipe title for easy identification of the recipe.
* The number_of_likes() method returns the likes coount.
* The number_of_dislikes() method returns the dislike count.
* The get_absolute_url() method directs the url back home.
* The save() method overide function to date of post update.


## Country Class
This is majorly added by the superuser used to populate the dropdown choice on the navbar, it is also used as a reference for users to access recipes of different countries.

|Field|Details
|---|---|
|Name|A CharField set to maximum length of 150, each country name is unique.|

Primary key is used in referencing posts and countries throughout the project. It is unique and is added automatically by django to each post created.

Images used are cloudinary images linked to my cloudinary account.

Included with the instruction and ingredients field is the django_summernote which adds rich text editor to the fields.

The likes and dislikes field allow user a form of expression on different recipes thereby communicating their views to others.

### Country Class Methods
Country class contains the following methods;

* A Meta class which returns the ordering by name of the countries.
* A string method which returns the name of the country.
 
---

# Recipe Views
This section explains different views used to render pages to users.

## Landing Page View

RecipeView class renders the index.html page. It inherits from the django class [ListView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/). It defines a set of query to filter objects by their approval status and orders them by descending date created. It paginates post by 6  and adds url data and country list to the returned context allowing me access to the url name and list of countries.

## Details Page View

RecipeDetails is used to display more details on a specific post to the users. Defined using a function based class. It gets the specific object query from the model and returns the content containing the full recipe and the liked and also filters if like or dislike value exists. It renders the page using the 'details.html'.

## Likes and Dislike View

This views handles the like and dislike feature of the app. Very similar but a little different. They both handle post request from the user and toggles the buttons to either add or remove the user. If there was an existing like/dislike on a recipe by a user and he decides to change to the other, the like is automatically removed. 

It uses an HttpResponseRedirect to redirect the user back to the details page.

## Add Recipe View

This view handles adding recipe post to the site. It uses the Recipe model and inherits from the django [CreateView class](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/). It displays a form using the form class RecipeForm for creating a new recipe and allows users to submit a new recipe for approval by the admin. It renders the template 'addrecipe.html' and returns the url back home once successfully submitted.

It contains a method that displays message to user confirming successful submission of recipe to users. Also, it returns the url data as part of the context for access to the url name.

## Update Recipe View

This view handles recipe recipe post update, it inherits from django [class UpdateView](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/) and displays a form using the Recipe model and the RecipeForm to update a selected recipe post. It uses [SuccessMessageMixin](https://stackoverflow.com/questions/29521871/why-success-message-messagemixin-is-called-after-form-valid-shouldnt-it-be) to alert users successful recipe post update.

## Delete Recipe View

This view allows authors of a recipe post to delete the recipe if neccessary. It inherits from django class [DeleteView ](https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/). It renders a deleterecipe form (deleterecipe.html) allowing user to confirm delete action and returnd the user back home.

It uses [SuccessMessageMixin](https://stackoverflow.com/questions/47636968/django-messages-for-a-successfully-delete-add-or-edit-item) overwritten to return a successful deletion message to users.

## Country View

A function based view that accepts user's request and choice. It retrieves the requested object from the country model and renders the countries template with the requested countries.
Due to issues of case and space, I have used Q search for the country's name because to allows for a broader search in country's name in cases of case or space in country name.

The view is set to return a 404 page if the query is not available.

## Edit User View

This view allows users to edit their profile details, it inherits from the django class UpdateView.It uses the EditProfile form to render the edit_profile page. It redirects the users back home.
Once successful, users are informed of the successful edit of their profile using the SuccessMessageMixins.

It has a method that returns the current logged in user's details.

## Change Password View

This view allows users to change password details inheriting from django PasswordChangeView, it uses the ChangePasswordForm to change the user's details.

---

# Recipe Forms
The recipe forms file contains three form classes - RecipeForm, EditProfileForm and ChangePasswordForm. The forms are defined to specifically control which fields to be displayed. Also to apply the Bootstrap form-control class to makes the forms nicer to use. Widgets variable was used to apply the form-control class, widgets was also used to get the django-summernote Rich Text Editor working by way of the SummernoteWidget for some of the fields. 


## RecipeForm
RecipeForm class uses the model Recipe inherits from django forms.ModelForm and states the fields to be displayed. It uses widgets to customise the appearance and behavior of form fields defined.

SummernoteWidget is applied to two of the fields; instruction and ingredients to allow users access to different stylings of fonts.

It has an _init_ method that defines the form layout and styles using FormHelper and Layout, this form will be rendered in the template with the specified fields and styles, making it easier to create consistent and visually appealing form.

## Edit Profile Form
This form uses the model User and inherits from django class [UserChangeForm](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/). It allows users to edit choice fields in the user's detail. Styled with bootstrap for a more appealing view. It defines fields to be displayed to users.

## Change Password Form
This form uses the model User and inherits django's class [PasswordChangeForm](https://docs.djangoproject.com/en/1.8/_modules/django/contrib/auth/forms/). It allows users change their password by entering their old password and confirming a new one. For each field, it uses a Charfield and sets the maximum length of password to 100 including widget to add attributes for styling.

---

# Mama'sKitchen Url

The url file holds the urlpatterns for Mama'skitchen app. The paths renders different pages discussed above. The first been the landing page, recipe details page, add recipe page, update recipe page, delete recipe page, countries page, editprofile, change password. Also the likes and dislike view . 

As previously mentioned, recipes are listed by their primary key, hence for paths that deal with a specific item; <int:pk> is used instead of <slug:slug> as in the walkthrough project.

---

# Mama'sKitchen Admin

The admin file controls the layout of, and actions available in, the Django admin panel. There are two classes - RecipeAdmin and CountryAdmin. RecipeAdmin class extend the SummernoteModelAdmin class in its ingredients and instructions field.

RecipeAdmin class has list_filter, search_fields, list_display, and summernote_fields. 

The list_display control variable within the class allow an administrator to quickly see some important meta-data about a recipe - id, title, post approval status and date of post creation.

The search_field allow access to recipe using the quick search feature within it - post title, cook time, country.

The list_filter allow easy filtering of recipes by date created, post approval state, and country 
   

CountryAdmin class specifies how the country view panel is displayed. It has list_display which allows the administrator to have a view of the country list with its id.

---

# Future Features

This section lists all features I will like implement to improve the project and futher increase my knowledge of the process. Some were not due to time constraints and others to a lack of skill.

Add an homepage banner display for non-authenticated user.

Add comments section to promote communication and interactions on the platform.

Display number of approved comments attached to each review on the index and details pages.

Extend user model to include profile picture and more information about the user.

Allow accessibility to user's profile but not edit if not the real profile user.

Add higher-level AllAuth functionality - social media sign in, password complexity, confirmation emails, etc

Modify UserSignUpForm in user/forms.py to include additional first_name and last_name fields

Allow users access to a list of his unapproved posts.



---

# Bugs

## Requirements file bug

* When trying to deploy the first Mama'skitchen blank site, the deployment failed as heroku could not complete the buildup, but after lots of investigation I noticed that I omitted the 's' after the requirement hence the reason for a failed deployment.

      * Adding 's' to the file name and trying redeploying fixed this.

## Active Link Bug

* When I was trying to feature the active link on the homepage, even after writing the link in the django way, there was no feature of the active link on the live site.

      * Adding **url name** to the context passed fixed this.


## Add Recipe Page Bug

* When adding a new recipe from the user's side, I always try to make some adjustment on the admin section before approving. The homepage display always display html and css code.

      * Gemma of tutor support enlightened me on this and encouraged me to add summernote editor to the user's section.


## Country Page Bug

* While trying to make each country a link to access different recipes, I got error with countries with space and casing. 

      * Importing Q to use for advance search fixed this.

* Border around country page stoped on the first column.

      * Replacing the border with 'hr' below the country header fixed this.


## Tab Duplication Bug

After adding some pages especially the add recipe and delete recipe, I researched into ways to limit only the user of a post to edit or delete it, from the walkthrough video guide, I decided to add **{% if user.is_authenticated %}** and the corresponding else statement statement to control who has access to the post, with this, I was able to restrict it to only registered users. 

I found out that a user that already knows the link of a particular can still perform these actions even when he is not the owner of the post. For a further restriction, I added **{% if user == recipe.author %}**, this is to allow only the post author access to these actions. I added text and links to take users back home on both instance.This was put in place to protect against malicious users.


## First Project Error and Restart

While building my first project, I decided to remove the approved field from the **Country Model**, this was after migrating and using it in my buildup. In order to finally remove its history, I removed the migration file associated with it and this resulted in django requesting for a part of the table as it cannot be found. I read different contributions on **Stackoverflow** but I just did not find a way out. A senior colleague **Adam Boley** helped me with debugging it but he advised I start a new one.

While putting up the new project, I decided to add only the name field to the model Country and to make it only an admin duties since there are specific number of African countries which can be added at once and users can select from the option.
 

## Update Recipe Image Input

* When testing, I realised that the default word next to 'No file chosen' on the image field was overflowing its box.

      * Inspecting with devtool and adding font size 10px to it fix this. I also decided to make the lettering bold for clear visibility.

## Missing Navbar Toggler

* On viewing the site live browser, I realised that the bootstrap toggler was not present. On further look, I discovered that it is still active but just not showing.

     * Since it is navbar there must have been a deletion by mistake. Although frustrating because the search for what is wrong took days, I finally realised that the class responsible for the toggler display has been deleted.

      Adding the missing bootstrap class **navlight** fixed this issue.

## Image Size Bug
* I noted that uploaded images on posts have varying heights.

      * Adding height and margin to the post image solved this


## Flash Messages

* My mentor noted that the initial time of 2000ms delay on the flash message before disapppearance seem too small.

     * Adding 500ms more delay fixed this. 


## Likes and Dislike Message Bug

* I noticed that after setting up the like and dislike feature, a user can add like to a recipe and at the same time add dislike to it.

      * Adding an if statement to check and remove one if the other is already present fixed this.

    
## Country Dropdown List
* I noticed the country list was too long (as I have many afrrican countries to add), which to me reduces good user experience and it will be covering too much of the page content.

     * Adding max-height and overflow property to the dropdown menu style fixed this, so I was able to add in more countries without fear of covering up the landing page.


## Home Page Validation Bug

* While validating the homepage, I got the error of "Multiple use of id values" on the template.

      * The thought of adding a unique number at the end of the id values with the recipe primary keys fixed this. 


## Heroku Deployment Bug

* While deploying with contents as I did not deploy the empty project as advised by a senior colleague, I got this deployment error :

      "KeyError: 'etag' !   Error while running '$ python manage.py collectstatic --noinput'."

   *  As advised by Oisin(one of the tutors), I had to create a new cloudinary account to serve the static files as he said that etag errors are difficult to resolve. After deleting and connecting another cloudinary account, I added another static files with all its content.only to discover that all images were no longer available. This brought about lots of confusion but I decided to try add a new post to see if it will work and it did perfectly. This helped me to know that the images were associated with the former cloudinary account.
          I thought about deleting all the post and adding them again, then I felt there should be a way to synchronize contents in the two accounts. The search for a way to do that began. Fortunately, I found [this material](https://cloudinary.com/documentation/migration) and [this material](https://support.cloudinary.com/hc/en-us/articles/202521122-How-can-I-copy-images-between-accounts) illustrating how to migrate and copy images between accounts respectively but I did not implement the contents of the materials as I was scared of disrupting anything already set. I needed an experienced person to lead me through it. In the end, I decided to manually delete all post and add them again to fill the new database content. After doing all these and still the error persisted this time all static folder content were reflected in the deployed site but no style on the style sheet was applied. The confusion was now real as all efforts and contributions from colleadues and tutors feels abortive.
    Finally, I just decided to move my wireframe folder out of the static folder, commit and push. After few minutes, I observed my email notification from heroku has not come through. I decide to check the build log and suprisingly saw that the deployment was successful.
    This error took a lot of commits and push as I was trying looking around for possible areas of error.I had to downgrade cloudinary as advised by a tutor, modify my cloudinary settings, create a new account, among others but I was glad it was solved finally.

## Summernote Widget Bug and Admin Section Bug

* Just after resolving the bug above, a few hours later when I tried to continue work on the project, I realised the summernote widget on the user side (on the update page, add_recipe page) and the whole admin section have become [this](screenshots/bug_pic/admin_pagebug.webp), [this](screenshots/bug_pic/instruc_pagebug.webp) and [this](screenshots/bug_pic/ingre_pagebug.webp).

      * I thought it could be because I have turned the DEBUG to False or added the X_FRAME_OPTIONS, I decided to comment the X_FRAME_OPTIONS but it did not change. I also changed the DEBUG settings back to True and everything was fixed.

## Admin Search Fields Bug

While testing, I discovered that the admin search field was not working as it should. I got this error.
       
       Related field got invalid lookup: icontains

On searching for the possible solution. I found [this material](https://www.infinetsoft.com/Post/SOLVED-Related-Field-got-invalid-lookup-icontains-error-in-Django/3153#:~:text=This%20error%20is%20happening%20due%20to%20adding%20foreign,and%20grab%20name%20field%20from%20the%20category%20model.) with details that helped me solve it.

     Adding '__name' to the country index fixed this error.


## Link Color Bug
I had used important to feature links hover but I decided to fix it because it was causing difficulty with styling other aspects of the website.

    Using specificity and inheritance to select the different element I wanted helped fix this.


---

# Design Choices

* The design choices made in the project are to project the true African nature.

## Font
* [Great Vibes](https://fonts.google.com/specimen/Great+Vibes?preview.text=oswald&preview.text_type=custom&query=great) font from google fonts to write the site logo. It has a fallback of **Cursive**.

* [Playfair Display](https://fonts.google.com/specimen/Playfair+Display?preview.text=oswald&preview.text_type=custom&query=playfair) was used for links. It has a fall back of **Serif**.

* [Roboto](https://fonts.google.com/specimen/Roboto?preview.text=oswald&preview.text_type=custom&query=roboto) was used for the body of the project as it is clean, bold, and has a nice presentation. It has a fallback of **Sans-serif**.

Combining Roboto with Playfair Display presents a nice contrast which I think helps differentiate different sections of my content and adds visual interest to the site.

## Colour Scheme

In line with the theme of the website, I have chosen to use representative African colors illustrated as follows;

**Body Background Color:** White color representing Purity and Peace a treasured characteristics of africa.

**Homepage Headers, Links Hover, active link background color, dropdown list focus, active page indicators**. All have a shade of red (#840404) symbolizing the african struggles. In order to boldly project the like and dislike, I used the red color shade #E84610 which is brighter than the former.

**Homepage Header and Footer**: A shade of green (#aaf3aa) was used symbolizing growth.

**Post Card** made with a border of a shade of green (#5c875c) to highlight and contain each post.

**Buttons** were made a shade of grey (bootstrap btn-secondary) symbolizing cleansing and healing rituals.

**Header and Footer content**: Made with color black, symbolizing the maturity of the african culture.

Different color combination and their contrast is summarised as follows:

   |Foreground | Background | Contrast Ratio | Comment on Large and Small Text |
   |-----------|------------|----------------|---------|
   | Black     | #aaf3aa    | 16.11           | Super
   | #aaf3aa   |  #840404   |8.05       |  Very Good   |
   |  #840404    |  #ffffff   | 8.05      |  Very Good   |
   | #ffffff    | #840404   |  10.50      | Very Good


## Favicon

I decided to use the same image used as the placeholder image for the favicon as it reflects the african theme of the project. I used [favicon](https://favicon.io/) to generate it using the image I already have.

---

# Accessibility

I have designed the site to be easily accessible with links that connects different pages together in order to enhance effective use of the site and to allow for easy access to information required by its users.

Landing Page

This serve as the main gateway for users to explore and engage with the platform. It contains the following section;

Header Section which consist;

Logo and Site Name : The website's logo and name are prominently displayed to providing instant brand recognition.

Navigation Menu: Navigation menus allow users to explore different sections of the website, including recipes, social media link, registration, sign out link and more.

User Authentication: Options for user login and registration are provided, allowing users to create accounts and log in to their own account.

Country Categories: Different country can be accessed and recipes of each country can be viewed together by clicking on the country dropdown option.

Main Content Section:

Featured Recipes: Eye-catching images and titles of selected recipes are presented for users to view.

Share Button: User can use this button to share recipe of choice on different social media platform like twitter, telegram and whatsapp.

Footer Section:

Social Media Integration: Links to the website's social media profiles for users to follow and engage with the community.

---

# Technology Used

## Languages

The project been a full stack development used the following languages;

* Python - Used to set up the main functionaluty of the website.

* HTML - Used to build up the different template files contained in the website.

* CSS - Used to customize styles for the website.

* Javascript - Used to manipulate the DOM on different pages.

## Python Modules/ Packages Used

Some of the several python packages used to execute the project are illustrated below;

* django _ This is the main framework used to design this application.

* psycopg2 - PostgreSQL database adapter used for puthon programming language.

* dj3-cloudinary- cloudinary-storage - This facilitates integration with cloudinary by implementing Django storage API.

* django-allauth - This is an integrated set of django applications that handles registration, authentication, registration, account management e.t.c

* django-crispy-forms - This provides crispy filter that allows rendering django forms in an 
alegant and DRY form.

* django-social-share - This simplifies the process of adding social media sharing functionality to the websites. Details on its implementation can he read [here](https://pypi.org/project/django-social-share/).

* django-summernote - This helps in the integration of a feature-rich, responsive, and customizable WYSIWYG editor into the website.

* crispy-bootstrap4 - This is the bootstrap template package for django-crispy-forms.

* coverage - This allows the creation of coverage report for automated testing.

---

# Frameworks and Tools

* Django - This was used to set up different user logic and model used.

* Balsamiq - This was used to draw up the wireframes used to build up the project.

* Github - This was used to store written code, it also contained the Agile development plan set up to build the project.

* Gitpod - This was used to write code, correct code, commiting and pushing code up to github.

* Heroku - Used for the live deployment of the site.

* Cloudinary - This is the cloud storage used for website media and other static files.

* Bootstrap - This was used to add styles to the website. It was used for the nav section, cards and different sections of the website.

* Lucid Chart - This was used for creating the website ERD, a demonstration of the database structure.

* Google Fonts - This was used to add fonts to the website.

* Font Awesome - This was used for icon features on the website.

---

# Development and Deployment

## Development

To develop this project;

 * install django using pip3 install 'django<4' gunicorn
 * install database using pip3 install dj_database_url==0.5.0 psycopg2
 * install cloudinary using pip3 install dj3_cloudinary_storage
 * create the requirement file using pip3 freeze --local requirements.txt
 * create the new django project using django-admin startproject africanrecipes
 * create a new app using python3 manage.py startapp recipes
 * ensure the app is added to the list of installed app in the settings file contained in the project created above.

 ## Creating Heroku App

  * Log into Heroku and go to the Dashboard.
  * Click "New" and then select "Create new app".
  * Give your app a name and select the region closest to you.
  * Click "Create app" to confirm.

## Creating a database

   * Log into ElephantSQL.com and access your dashboard.
   * If no account create a new one
   * Click "Create New Instance"
   * Set up a plan
       * Give your plan a Name
       * Select the Tiny Turtel (Free) plan
       * Leave the Tags field blank.
   * Select "Select Region"
   * Select a data center new you.
   * Click "Review".
   * Check your details, confirm it is correct and then click "Create instance".
   * Return to the ElephantSQL dashboard and click on the database instance name for this project.
   * In the URL section, click the copy icon to copy the database URL.
   * In your workspace make sure django and gunicorn are already installed.

## Creating a Cloudinary Account

   * Create a cloudinary account
   * Select the sign up for free account
   * Provide your name, email address and choose a password
   * For your primary interest option, choose Programmable Media
   * If required, edit your assigned cloudname.
   * Select 'Create Account'
   * Verify your email and you will be brought to the dashboard
   * Copy the environment variable

## Adding the env.py file

This file is needed to store environment-specific configuration variables. If you do not have an env.py file in your workspace create one and make sure it is included in the .gitignore file.

At the top of the env.py file add the line: import os.

Below that set environment variable with:

     os.environ["DATABASE_URL"] = "<copied URL from SQL database>"

     os.environ["SECRET_KEY"] = "<create a secret key of your own>"

If using Cloudinary storage also include the following line:

     os.environ["CLOUDINARY_URL"] = "<copied URL from Cloudinary account>" 
     (remove the cloudinary-url = from the beginning of the copied string)

Make sure the environment variables are imported correctly into the settings.py file.

Run python manage.py migrate in the terminal window to migrate the data structure to the database instance.

## Modifying Settings File

To ensure django is aware of your env.py file, add the following lines to the settings file;

    import os
    import dj-database-url
    if os.path.isfile('env.py')
        import env

Remove the secret key provided by django, instead reference the variable in the env.py file as follows;

    SECRET_KEY = os.environ.get('SECRET_KEY')

To attach your database to the file, comment out the DATABASE variable and add the following;

    DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

Save your changes.

To confirm if your changes to the database is correct, run the migration command in your terminal;
    
    python manage.py migrate

Once completed, 
* headover to ElephantSQL dashboard
* select your database instance
* select the 'Browser' tab on the left
* click on 'Table queries' to reveal a dropdown list generated by your migration.
* Add commit and push to github

Also, in the list of the installed app add the following in order;

    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',

In the STATIC_URL section, add the following after it;

    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

Django also needs to know about our template files storage using;
    
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

In the TEMPLATES list section, add in the value 'TEMPLATE_DIR' as a value to 'DIRS'

Add in your heroku app name in the ALLOWED_HOSTS list.


## Setting Environment Variables on Heroku

On the Heroku Dashboard select the app created and then select the "Settings" tab.

Click "Reveal Config Vars"

Add the following config vars:

* DATABASE_URL - copy the database URL from ElephantSQL in here, it should also be in the env.py file.
     SECRET_KEY - copy your secret key in here.

* CLOUDINARY_URL - If using Cloudinary storage you also need to copy your personal CLOUDINARY_URL into these fields.

* PORT with value 8000.

## Requirement and Procfile

Before deployment on Heroku, ensure the requirements.txt file and Procfile exists.

The requirements.txt file is created using the following command in the terminal:

     pip3 freeze --local > requirements.txt

A file with all requirements will be created.
Also create a new file and name it Procfile and insert the following code: 

     web: gunicorn africanrecipes.wsgi

Ensure there are no empty lines after it.

Then make sure to push these files to your repository.

## Connecting to GitHub and Deploy

   * On the Heroku Dashboard select the app created and then select the "Deploy" tab.
   * Select GitHub for the deployment method.
   * Search for the project repository name and click "Connect".
   * You can also select "Enable Automatic Deploys" if desired down the page.
   * Finally, select "Deploy Branch" and watch the app being built.

---

# How to Fork

By forking a repository, you make a copy of a repository without affecting the original repository. You can fork this repository using the following steps.

 * Log in to GitHub and locate the [GitHub repository](https://github.com/belovedpearl/AfricanRecipes-PP4).
* At the top of the Repository above the "Settings" Tab on the menu, 
    * locate the "Fork" Button
    * Click it.
* You will have a copy of the original repository in your GitHub account.
* Doing this will allow you make changes to your copy and keep the original safe.

# How to Clone

* Log into GitHub and locate the [Github repository](https://github.com/belovedpearl/AfricanRecipes-PP4).
* Click the 'Code' dropdown at the right of the 'Open' button.
* Copy the URL for the repository.
* Open Git Bash in your IDE.
* Change the current working directory to your desired location.
* Type git clone in the CLI and then paste the URL you copied. 

      $ git clone https://github.com/

* Press Enter to create your local clone.

NOTE- You will need to install all of the packages listed in the requirements file. Use the following command in the terminal 

     pip install -r requirements.txt 

to install required packages.

---

## Testing

### Automatic Testing

At the start of the project, I decided to write in some test to get a good grasp of the concept and my mentor also advised me to especially for a career changer like me as this will show my capacity in another level, while faced some challenges writing the tests, I was happy that I could write some in the end. I have been able to write 17 tests for this project, using [this](https://docs.djangoproject.com/en/4.2/topics/testing/overview/) material helped.

Automatic test for this project can be found ![here](recipes/). The files are named ![test_forms](recipes/test_forms.py),![test_models](recipes/test_models.py) and ![test_views](recipes/test_views.py).

As advised by my mentor, I used the **db.sqlite** to run the tests.

Test results are shown below;

<details>
<summary>Automatic Test Result</summary>
    <img src="screenshots/test_pic/test-forms.webp" width="80%">
    <img src="screenshots/test_pic/test-models.webp" width="80%">
    <img src="screenshots/test_pic/test-views.webp" width="80%">
</details>

**Coverage Report of test is illustrated below**
![Coverage Report](screenshots/test_pic/coverage-report.webp)


### Manual Testing

All manual tests was done on the deployed site.

#### Admin User Test

Mama'sKitchen has an admin section which is the standard django admin that can be accessed by the superuser. It is built with different functions to improve admin experience.

![Mama'sKitchen Admin](screenshots/test_pic/admin-access.webp)

The admin section can be accessed by adding '/admin' at the end of the home page url as illustrated below.
 
        https://africanrecipes-95e71e30ded1.herokuapp.com/admin/

* The admin user can sign-in to the admin section with the superuser details. For this project, a superuser 'Oluwaseun' has been created, password supplied separately.


<details>
<summary>Admin Sign in</summary>
    <img src="screenshots/test_pic/admin-pass.webp" width="80%">
</details>

     Admin is able to sign-in with the username and password.

* The admin can access the project admin-board.

<details>
<summary>Admin Board</summary>
    <img src="screenshots/test_pic/admin-board.webp" width="80%">
</details>

* The admin can view all recipe posts submitted by users, so that I can view and edit posts if needed

<details>
<summary>Admin Recipe Board</summary>
    <img src="screenshots/test_pic/recipe-board.webp" width="80%">
</details>

     The admin is able to view all recipes submitted by users.

* The admin can filter and sort recipe posts easily, so that I can see all of the posts that needs to be approved.

<details>
<summary>Admin Filter Result</summary>
    <img src="screenshots/test_pic/filter-section.webp" width="80%">
    <img src="screenshots/test_pic/filter-result.webp" width="80%">
    <img src="screenshots/test_pic/filter-result2.webp" width="80%">
</details>

       The admin is able to filter recipes as stated in the list_filter in the admin.py file.

* The admin can approve recipes post so that they can be be visible on the site.
     Admin click on approve post field makes, saving it makes it shows up on the main site.

* The admin can delete any number of selected recipe, so that they no longer take up memory in the database especially the ones that are not on line with the platform values.

<details>
<summary>Admin Delete Action</summary>
    <img src="screenshots/test_pic/admin-delete.webp" width="80%">
    <img src="screenshots/test_pic/admin-deletesuccess.webp" width="80%">
</details>

      Admin delete successful

* The admin can make posts with rich text and images, so that I can improve the quality of posts.
* The admin can add a recipe post, so that I do not have to use the add post page on the front-end

<details>
<summary>Admin Add Recipe Action</summary>
    <img src="screenshots/test_pic/admin-addrecipe.webp" width="80%">
    <img src="screenshots/test_pic/admin-addrecipe2.webp" width="80%">
    <img src="screenshots/test_pic/admin-addrecipe3.webp" width="80%">
</details>

       Admin can successfully add recipe from the admin section.

* The admin can use the search field to search for required recipes, so that I can see all recipes posts that fulfil certain criteria

<details>
<summary>Admin Search Action</summary>
    <img src="screenshots/test_pic/searchfield-admin.webp" width="80%">
    <img src="screenshots/test_pic/searchfield-admin2.webp" width="80%">
    <img src="screenshots/test_pic/searchfield-admin3.webp" width="80%">
</details>

       Admin is able to use the search field successfully as specfied in the search_fields list in the admin.py file

* The admin has access to the country board, he is able  view all countries, add more African countries, update and delete.

<details>
<summary>Admin Country Board</summary>
    <img src="screenshots/test_pic/country-board.webp" width="80%">
    <img src="screenshots/test_pic/country-delete.webp" width="80%">
    <img src="screenshots/test_pic/country-delete2.webp" width="80%">
    <img src="screenshots/test_pic/country-delete3.webp" width="80%">
</details>

#### General User User Story Test

|User Story | Action / Expected result | COMMENT |
|-----------|------------|----------------|
|Immediately determine the purpose of the application on first visit, so that I can quickly decide whether its of interest or not     | The user should see a variety of food displayed giving him an idea of the site's overview    | PASS           | 
|Have a positive user experience irrespective of the means of access, so that I can access the application from enjoy the platform from any device  | Responsiveness on all screens, Pagination for desktop users on home page   |PASS       | 
|View all recipe posts so that I can choose one to read in detail   |Recipes display to users in group of 6, User click on any recipe title to access the recipe detail   | PASS     |
| Sort recipe posts by country name so that I can see only the recipe post of intrested countries    | Click on a country in the country dropdown or click on the country name under each post   |  PASS     |
|If my search by country returned no results, have a message displayed informing me of no posts related to my country search.   |  User sees a message informing him 'no recipe for the selected country'.   |  PASS   |


#### Unregistered user User Story Test

|User Story | Action / Expected result | COMMENT |
|-----------|------------|----------------|
|Sign-up and create an account, so that I can access the detailed functionality of the application     | Interested users should be able to register with a sign up page   | PASS           | 
|Sign-in to that created account, so that I can access the detailed functionality of the application  | After successfully registering, users should be able to access their personal accounts   |PASS       | 

#### Registered user User Story Test
|User Story | Action / Expected result | COMMENT |
|-----------|------------|----------------|
|Sign in to an already existing account, so that I can access the full functionality of the application.     | The user should be able to sign in to his account using the sign in page in order to access the full website functionality    | PASS           | 
|Add a recipe post easily so that I can share food recipe on the website  | Clicking on the add recipe button should bring up the add recipe page for user to add his recipe   |PASS       | 
|Edit recipe posts I created so that I can improve or modify the content  |Clicking on the update icon below his recipe should bring up the recipe in their different field allowing the user to update it.   | PASS     |
| Delete recipe posts I created so that I know that I have the control of the content I created.    | User should be able to delete his own recipe by using the delete icon under the recipe picture.   |  PASS     |
|Change the password for that account, so that it becomes more memorable. |  From the profilr page, user is able to change his password   |  PASS   |
|Sign-out easily, when already signed-in, so that I can be sure that my session was closed securely | User should be able to sign-out of his session to keep his account secured. | PASS |
| Have my sign-in status reflected back to me, so that I can be sure that I have signed-in | User signed in status is reflected at the top right corner of the home page. | PASS |
| Apply rich text formatting to the content of my recipe, so that I can better express myself and provide additional structure to my recipe.  | User should have access to use the summernotewidget on the frontend  | PASS |
| Upload an image to my recipe, so that I can show other users what the recipe looks like. | User shold be able to add recipe image | PASS |
| If there is no recipe when searching by countrry, have that reflected back to me so that I know that there is no recipe for the selected country | User can add recipe without its image, a placeholder image is used to represent recipes without image added by the author | PASS |
| Allow for confirmation of delete recipe befor deletion, so that I cannot accidentally delete any recipe post.  | User should be presented a warning for delete actions and is allwed to use the 'NO' button to stop the process  | PASS |
|  Be alerted when I have posted a recipe, so that I can be assured that I have submitted the recipe. | On successful submission of recipe, user should be shown a message confirming successful submission | PASS |
| Be informed when I have successfully signed in, so that I can be assured that I have submitted the right details.  | Users should be alerted when signed in | PASS |
|  Be informed when I have updated a recipe, so that I can be assured that I have updated the recipe. | User should be alerted with a message on successful update of recipe |  PASS |
| Be informed when I have deleted a recipe, so that I can be assured that I have deleted the recipe. | User should be informed on successful dletion of recipe posts | PASS |
| When viewing a recipe detail, like the page , so that I can express my thoughts of the recipe | User should be able to like a food recipe | PASS |
| When viewing a recipe detail, dislike the page , so that I can express my thoughts of the recipe. | User should be able to like a food recipe | PASS |


### Validator Testing

#### PEP8

I have validated the code (form, views, admin, url and all automatic test files) with [CI Pep8](https://pep8ci.herokuapp.com/), details of the  validation can be found ![here](screenshots/validator_test/pep_linter/).

Recommendations of whitespace error and comments too long were given and was corrected to get the above results.

### Javascript

Javascript was used in the DOM manipulation to fade away messages from screen, written towards the end of the base file. I have passed the code through [JSHINT](https://jshint.com/).

![Javascript Validation](screenshots/validator_test/js_and_css/jshint.webp)

### W3 Validation

All codes written have been passed through the [w3 validation](https://validator.w3.org/) using the direct input method. Results can be viewed ![here](screenshots/validator_test/w3_check/).

Some pages returned with errors and warnings like;

![Details page](screenshots/validator_test/w3_check/details_page.webp)

On assessing and checking the cause of the errors and warnings, I realise they are due to the copied styles from the Summernote used in the frontend. As I could not find a way to fix this, I decided to show it and possibly continue my learing from there.

![country page](screenshots/validator_test/w3_check/post_country_page.webp)


The error was due to the injected template. I inspected the code and also tried using [this tool](https://www.aliciaramirez.com/closing-tags-checker/) to find the unclosed tags but it came back with nothing shown [here](screenshots/validator_test/w3_check/tag_confirmation.webp).

After adjustments were made, the live site was passed again through W3C validation. The results are presented below.

[Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2F)

[Details page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fdetails%2F39)

[Country Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fcountries%2FEthiopia%2F)

[Add recipe page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Faddrecipe%2F)

[Sign out Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2F)

[Edit profile page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fedit_profile%2F)

[Change password Page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fpassword%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

[Update recipe page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fupdaterecipe%2Fedit%2F41)

[Delete Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fdetails%2F41%2Fdelete)

[404 page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2Fgh)

### CSS

No errors were found when the passed through [W3C Validation Service](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fafricanrecipes-95e71e30ded1.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

![CSS Validation](screenshots/validator_test/js_and_css/css-validation.webp)

### WAVE Report

[WAVE]() was used to test the live site and it gave the following [result](https://wave.webaim.org/report#/https://africanrecipes-95e71e30ded1.herokuapp.com/).

<details>
<summary>Wave Report</summary>
    <img src="screenshots/validator_test/js_and_css/wave-report.webp" width="80%">
</details>

---

# Tools


  *  [Balsamiq Wireframes](https://balsamiq.com/)
  *  [Resizing Images](https://www.reduceimages.com/)
  *  [Reducing Images size](https://tinypng.com/)
  *  [Test for Responsiveness](https://ui.dev/amiresponsive)
  *  [HTML validator](https://validator.w3.org/)
  *  [CSS validation](https://jigsaw.w3.org/)
  *  [Contrast checker](https://dequeuniversity.com/)
  *  [Coolors.co](https://coolors.co/)
  *  [Font Awesome](https://fontawesome.com/)
  *  [Fonts](https://fonts.google.com/)
  *  [Font pair](https://fontpair.com/) 
  *  [Squoosh](https://squoosh.app/)
  *  [Unclosed Tag Checker](https://www.aliciaramirez.com/closing-tags-checker/)
  *  [Lucid Chart](https://lucid.app/)


---

# Credits

## Media

Images used to populate different posts are from the following sources.

 * [Beer-braised lamb shanks](https://www.delicious.com.au/recipes/beer-braised-lamb-shanks-mieliepap/b63ba9d0-7a77-4257-8f16-e6ef5d2f71bb)
 * [Efo](https://hintng.com/how-to-prepare-efo-riro/)
 * [Amala](https://molabatkitchen.com/menu/amala/)
 * [Okra](https://blog.allnigerianrecipes.com/okra-soup-overload/)
 * [Matoke](http://www.food-of-africa.com/zimbabwean-food/sadza/)
 
  

## Images

Template image and favicon images added to the project is from [here](africa-facts.org)

## Code

To put up this project, the main inspiration was from the Code Institute's 'I Think Therefore I Blog' Django walkthrough project'. With a desire to express my website differently to further my knowledge of django, I learned from [John Elder](https://www.youtube.com/@Codemycom) in his [series](https://www.youtube.com/watch?v=B40bteAMM_M). This really helped in my understanding of django usage.

Adam Boley for giving his approval to his page pagination code.

Throughout the project, the following were helpful websites often used for troubleshooting:
* [W3 Schools](https://www.w3schools.com/django/index.php)
* [Stack Overflow](https://stackoverflow.com/)
* [Mdn web docs](https://developer.mozilla.org/en-US/)
* [Django documentation](https://docs.djangoproject.com/en/4.2/)

---

# Acknowledgement

My special thank you goes to the following:

My mentor Sandeep Aggarwal for his feedback, advice, guidance, and support on this and the previous projects. And for all of his encouragements when I had some challenges. He was always quick to answer to all my questions.

[Adam Boley](https://github.com/AdamBoley/); for giving me your time, support and advice in setting up the project after the first project crash. I am very grateful to you.

The tutors especially Oisin, Roman for taking your time out to help me debug the issue I had during the deployment of the project.

My husband Adegoke, for his encouragement and support along the way. I do cherish all your effort even when you don't know what your point mean in development (smiles), I can tell you they have always propped me in the right path.

My kids (my boys), for allowing mummy take time out to learn and always assuring me that I can do it.

