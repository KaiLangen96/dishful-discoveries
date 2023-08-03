# Dishful Discoveries

Dishful Discoveries is an online recipe-sharing app, that is designed to get new inspirations from cooks all over the world. The app is targeted toward users to share their recipes and build a growing community together.

The site acts as a recipe repository whereby users can store their recipes, browse other users' recipes and add them to their favorites.

The live link can be found here - [Dishful Discoveries](https://dishful-discoveries-773712c83723.herokuapp.com/)

![Responsiveness of the website](https://cdn.discordapp.com/attachments/1049024982694498367/1136613112619999343/image.png)

- [Dishful Discoveries](#dishful-discoveries)
  * [User Experience (UX)](#user-experience--ux-)
    + [User Stories](#user-stories)
      - [EPIC | User Profile](#epic---user-profile)
      - [EPIC | User Navigation](#epic---user-navigation)
      - [EPIC | Recipe Management](#epic---recipe-management)
      - [EPIC | Recipe Interaction](#epic---recipe-interaction)
      - [EPIC | Site Administration](#epic---site-administration)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
    + [HTML Validation](#html-validation)
    + [CSS Validation](#css-validation)
    + [JavaScript Validation](#javascript-validation)
    + [Python Linter Validaion](#python-linter-validaion)
    + [Lighthouse](#lighthouse)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages](#custom-error-pages)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [User Account Pages](#user-account-pages)
    + [Browse Recipes](#browse-recipes)
    + [Recipe Detail Page](#recipe-detail-page)
    + [Add Recipe Form](#add-recipe-form)
    + [Update Recipe Form](#update-recipe-form)
    + [Delete Recipe](#delete-recipe)
    + [My Recipes Page](#my-recipes-page)
    + [My Likes Page](#my-likes-page)
    + [Error Pages](#error-pages)
  * [Deployment - Heroku](#deployment---heroku)
    + [Create the Heroku App](#create-the-heroku-app)
    + [Attach the Postgres database](#attach-the-postgres-database)
    + [Prepare the environment and settings.py file](#prepare-the-environment-and-settingspy-file)
    + [Create files/directories](#create-files-directories)
    + [Update Heroku Config Vars](#update-heroku-config-vars)
    + [Deploy](#deploy)
  * [Forking this repository](#forking-this-repository)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
    + [Code](#code)
    + [Media](#media)
    + [Content](#content)
  * [Special Thanks](#special-thanks)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Experience (UX)

A Site-Visitor to Dishful Discoveries would be someone who takes pleasure in savoring delicious meals and exploring new recipes. They are eager to expand and enrich their collection of recipes or simply share them with others.

### User Stories

#### EPIC | User Profile

- As a Site User, I can register myself to this website, so that I can create/update/delete my own recipes and comments.
- As a Site User, I can see my current login status, so that I know if I am logged in or logged out.
- As a Site User, I can log in and out of my account, so that post, comment and like recipes.

#### EPIC | User Navigation

- As a Site User, I can navigate myself throughout the website in an intuitive way, so that I can go back and forth between pages without an issue.
- As a Site User, I can open a recipe with a click, so that I can see the full details, ingredients required, comments and like the recipe.
- As a Site User, I can scroll through a paginated list of recipes, so that I can get a quick overview of many recipes.

#### EPIC | Recipe Management

- As a Site User, I can upload my own recipes through an easy form, so that I can share them with other users.
- As a Site User, I can view my own recipes, so that I can review and manage the recipes I have created.
- As a Site User, I can view all recipes I liked on one page, so that I can sort out my favorite recipes from the big list of all recipes.
- As a Site User, I can edit and delete my own recipes, so that I can keep my recipes up to date or remove them.

#### EPIC | Recipe Interaction

- As a Site User, I can comment on recipes, so that I can give my own feedback or start a conversation.
- As a Site User, I can edit and delete my comments, so that adjust my comments if I made a mistake.
- As a Site User, I can "Like" a recipe, so that I can sort out recipes I like from others.

#### EPIC | Site Administration

- As a Site Administrator, I can create, read, update and delete categories, recipes and comments so that I can manage the website.

### Design

#### Colour Scheme

![Colour Palette](https://cdn.discordapp.com/attachments/1049024982694498367/1136615923697057874/image.png)

Throughout the development process, the color scheme underwent several revisions. Ultimately, I opted to adopt a neutral color palette to ensure that the website's purpose remained front and center, without unnecessary distractions. Given that the primary focus of the website is to experiment with and exchange recipes, a white background complemented by subtle light-colored accents felt most appropriate.

For these accents, I selected a golden border, imparting an element of elegance and significance to the showcased recipes. This deliberate choice of colors and highlights aligns with the site's core objectives, contributing to a harmonious and engaging user experience.

#### Imagery

The web app features two fixed images. The [first image](https://res.cloudinary.com/dxjwzyf7j/image/upload/v1690982163/hero-image.jpg) serves as the hero image on the home page, displaying a table filled with delicious dishes. The [second image](https://res.cloudinary.com/dxjwzyf7j/image/upload/v1690982163/placeholder.jpg) acts as a placeholder for recipes without their own designated images, depicting a table with different dishes. All other images are intended to be uploaded by users, showcasing their unique culinary creations.

#### Fonts

The Montserrat font is the main font used for the body of the website with the Playfair Display font used for the main headings on the home page. These fonts were imported via Google Fonts. Sans Serif is the backup font, in case for any reason the main font isn't being imported into the site correctly.

#### Wireframes

<details>
<summary>Home Page</summary>

![Home Page](https://cdn.discordapp.com/attachments/1049024982694498367/1136654948118057051/image.png)
</details>

<details>
<summary>Browse Recipes</summary>

![Browse Recipes](https://cdn.discordapp.com/attachments/1049024982694498367/1136657983405826159/image.png)
</details>

<details>
<summary>Add Recipe</summary>

![Add Recipe](https://cdn.discordapp.com/attachments/1049024982694498367/1136658037499773118/image.png)
</details>

<details>
<summary>My Recipes</summary>

![My Recipes](https://cdn.discordapp.com/attachments/1049024982694498367/1136658094626185226/image.png)
</details>

<details>
<summary>My Likes</summary>

![My Likes](https://cdn.discordapp.com/attachments/1049024982694498367/1136658142961336410/image.png)
</details>

## Agile Methodology

For managing the development process with an agile approach, GitHub Projects was utilized. Here you can find the [link](https://github.com/users/KaiLangen96/projects/5) to the project board for reference.

The five Epics mentioned earlier were recorded as Milestones in the GitHub project. To manage each User Story effectively, a corresponding GitHub Issue was created and linked to an appropriate milestone. Each User Story has well-defined acceptance criteria, providing clarity on its completion. Furthermore, these acceptance criteria are broken down into tasks, streamlining the execution of each User Story.

## Data Model

Throughout this project, I applied Object-Oriented Programming principles, in conjunction with Django's Class-Based Generic Views.

For user authentication, I integrated Django AllAuth, which facilitates the authentication system.

The central focus of the website revolves around recipes. To create a recipe, two fundamental components are essential. Firstly, every recipe requires an author, with the user creating the recipe assuming this role. Secondly, a category is needed for the recipe. While users can select the category, the modification of categories is limited to the website administrators.

The Comment model permits users to leave comments on individual recipes. The Recipe and Profile serve as foreign keys in the Comment model. This setup ensures that a comment is linked to a single recipe and created by a specific user. The Likes model follows a similar structure.

The diagram provided below offers a comprehensive illustration of the database schema.

![Database Schema](https://cdn.discordapp.com/attachments/1049024982694498367/1136622718066892830/image.png)

## Testing

### HTML Validation

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/).

<details>
<summary>Home Page</summary>

![Home Page](https://cdn.discordapp.com/attachments/1049024982694498367/1136295141678780416/image.png)
</details>

<details>
<summary>Browse Recipes</summary>

![Browse Recipes](https://cdn.discordapp.com/attachments/1049024982694498367/1136295297350381689/image.png)
</details>

<details>
<summary>Add Recipe</summary>

![Add Recipe](https://cdn.discordapp.com/attachments/1049024982694498367/1136295875237380146/image.png)
</details>

<details>
<summary>My Recipes</summary>

![My Recipes](https://cdn.discordapp.com/attachments/1049024982694498367/1136296147787456512/image.png)
</details>

<details>
<summary>My Likes</summary>

![My Likes](https://cdn.discordapp.com/attachments/1049024982694498367/1136296425299378238/image.png)
</details>

<details>
<summary>Logout</summary>

![Logout](https://cdn.discordapp.com/attachments/1049024982694498367/1136296521231511614/image.png)
</details>

<details>
<summary>Sign Up</summary>

![Sign Up](https://cdn.discordapp.com/attachments/1049024982694498367/1136296672499085435/image.png)
</details>

<details>
<summary>Login</summary>

![Login](https://cdn.discordapp.com/attachments/1049024982694498367/1136296772122202122/image.png)
</details>

<details>
<summary>Recipe Details (Waffles)</summary>

![Recipe Details (Waffles)](https://cdn.discordapp.com/attachments/1049024982694498367/1136297119125344336/image.png)
</details>

<details>
<summary>Recipe Update (Another test / deleted)</summary>

![Recipe Update (Another test / deleted)](https://cdn.discordapp.com/attachments/1049024982694498367/1136297542045413527/image.png)
</details>

<details>
<summary>Recipe Delete (Another test / deleted)</summary>

![Recipe Delete (Another test / deleted)](https://cdn.discordapp.com/attachments/1049024982694498367/1136297707326152794/image.png)
</details>

<details>
<summary>Comment Update (Comment 4 / Waffle Recipe)</summary>

![Comment Update (Comment 4 / Waffle Recipe)](https://cdn.discordapp.com/attachments/1049024982694498367/1136297821537042462/image.png)
</details>

<details>
<summary>Comment Delete (Comment 4 / Waffle Recipe)</summary>

![Comment Delete (Comment 4 / Waffle Recipe)](https://cdn.discordapp.com/attachments/1049024982694498367/1136297933852131410/image.png)
</details>

### CSS Validation

No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

<details>
<summary>Result</summary>

![CSS validation results](https://cdn.discordapp.com/attachments/1049024982694498367/1136299407197872265/image.png)
</details>

### JavaScript Validation

No errors were found when passing the javascript snippet through [Jshint](https://jshint.com/).

<details>
<summary>Result</summary>

![JavaScript validation results](https://cdn.discordapp.com/attachments/1049024982694498367/1136300306079174807/image.png)
</details>

### Python Linter Validaion

All Python files I worked with were run through the [CI Python Linter](https://pep8ci.herokuapp.com/).

<details>
<summary>admin.py</summary>

![Result](https://cdn.discordapp.com/attachments/1049024982694498367/1136300547784314960/image.png)
</details>

<details>
<summary>froms.py</summary>

![Result](https://cdn.discordapp.com/attachments/1049024982694498367/1136300716458266644/image.png)
</details>

<details>
<summary>models.py</summary>

![Result](https://cdn.discordapp.com/attachments/1049024982694498367/1136300802936414328/image.png)
</details>

<details>
<summary>cookbook/urls.py</summary>

![Result](https://cdn.discordapp.com/attachments/1049024982694498367/1136300886419841125/image.png)
</details>

<details>
<summary>views.py</summary>

![Result](https://cdn.discordapp.com/attachments/1049024982694498367/1136300972805722194/image.png)
</details>

<details>
<summary>settings.py</summary>

![CSS validation results](https://cdn.discordapp.com/attachments/1049024982694498367/1136301338431586395/image.png)

The lines exceeding the maximal length have been solved by adding the # noqa tag.
</details>

<details>
<summary>dishful_discoveries/urls.py</summary>

![CSS validation results](https://cdn.discordapp.com/attachments/1049024982694498367/1136301405427216474/image.png)
</details>

### Lighthouse

[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was run on all pages to check Performance, Accessibility, Best Practices, and SEO scores.

<details>
<summary>Home Page</summary>

![Home Page](https://cdn.discordapp.com/attachments/1049024982694498367/1136304681988141187/image.png)
</details>

<details>
<summary>Browse Recipes</summary>

![Browse Recipes](https://cdn.discordapp.com/attachments/1049024982694498367/1136305574984822884/image.png)

The drop in the performance is explained by the images and styles loading from an external source, [Cloudinary](https://cloudinary.com/).
</details>

<details>
<summary>Add Recipe</summary>

![Add Recipe](https://cdn.discordapp.com/attachments/1049024982694498367/1136306365871165531/image.png)

The drop of the [accessibility](<https://cdn.discordapp.com/attachments/1049024982694498367/1136306366114439329/image.png>) is explained by missing titles. The [titles](https://cdn.discordapp.com/attachments/1049024982694498367/1136306366361911477/image.png) are not actually missing. The problem is caused by the use of the Summernote extension.
</details>

<details>
<summary>My Recipes</summary>

![My Recipes](https://cdn.discordapp.com/attachments/1049024982694498367/1136306701142868068/image.png)
</details>

<details>
<summary>My Likes</summary>

![My Likes](https://cdn.discordapp.com/attachments/1049024982694498367/1136307024154599574/image.png)
</details>

<details>
<summary>Logout</summary>

![Logout](https://cdn.discordapp.com/attachments/1049024982694498367/1136307550237757512/image.png)
</details>

<details>
<summary>Sign Up</summary>

![Sign Up](https://cdn.discordapp.com/attachments/1049024982694498367/1136307861048266823/image.png)
</details>

<details>
<summary>Login</summary>

![Login](https://cdn.discordapp.com/attachments/1049024982694498367/1136308128963633222/image.png)
</details>

<details>
<summary>Recipe Details (Waffles)</summary>

![Recipe Details (Waffles)](https://cdn.discordapp.com/attachments/1049024982694498367/1136308912241520720/image.png)

The drop in the performance is explained by the images and styles loading from an external source, [Cloudinary](https://cloudinary.com/).
</details>

<details>
<summary>Recipe Update (Another test / deleted)</summary>

![Recipe Update (Another test / deleted)](https://cdn.discordapp.com/attachments/1049024982694498367/1136312079062667335/image.png)

The drop of the [accessibility](<https://cdn.discordapp.com/attachments/1049024982694498367/1136306366114439329/image.png>) is explained by missing titles. The [titles](https://cdn.discordapp.com/attachments/1049024982694498367/1136306366361911477/image.png) are not actually missing. The problem is caused by the use of the Summernote extension.
</details>

<details>
<summary>Recipe Delete (Another test / deleted)</summary>

![Recipe Delete (Another test / deleted)](https://cdn.discordapp.com/attachments/1049024982694498367/1136312608845221938/image.png)
</details>

<details>
<summary>Comment Update (Comment 4 / Waffle Recipe)</summary>

![Comment Update (Comment 4 / Waffle Recipe)](https://cdn.discordapp.com/attachments/1049024982694498367/1136312961183518761/image.png)
</details>

<details>
<summary>Comment Delete (Comment 4 / Waffle Recipe)</summary>

![Comment Delete (Comment 4 / Waffle Recipe)](https://cdn.discordapp.com/attachments/1049024982694498367/1136313251106390036/image.png)
</details>

## Security Features and Defensive Design

### User Authentication

- Django's LoginRequiredMixin is employed to ensure that any attempts to access secure pages by non-authenticated users are redirected to the login page.
- Django's UserPassesTestMixin is utilized to restrict access based on specific permissions, such as allowing users to edit or delete only their own recipes and comments. If the user does not pass the test, they will be presented with an HTTP 403 Forbidden error.

### Form Validation

When incorrect or empty data is entered into a form, submitting the form will not be possible, and a warning message will be displayed to the user, indicating which field raised the error. This ensures that users are informed about the issues in their input and prompts them to correct the errors before submitting the form.

### Database Security

The database URL and secret key are stored in the env.py file to prevent any unauthorized connections to the database. This setup was implemented prior to the initial push to GitHub, ensuring sensitive information remains secure.

Furthermore, Cross-Site Request Forgery (CSRF) tokens have been incorporated into all forms across the site. This additional security measure helps protect against CSRF attacks, enhancing the overall security of the application.

### Custom error pages

Custom Error Pages have been implemented to offer users more information about the encountered errors and to guide them back to the site with the help of navigational buttons.

400 Bad Request: Dishful Discoveries is unable to process this request.
403 Forbidden: It appears that you are attempting to access restricted content. Please log out and sign in with the appropriate account.
404 Not Found: The page you are searching for does not exist.
500 Internal Server Error: Dishful Discoveries is presently unable to handle this request.

## Features

### Header

![header logged out](https://cdn.discordapp.com/attachments/1049024982694498367/1136649495204081694/image.png)

**Logo**

- A personalized logo was crafted by my partner [Hanna Kronberg](https://www.linkedin.com/in/hanna-kronberg-534a2b199/). Together we took an icon from Google Search and added the website's name to it.
- This logo is situated in the top left corner of the navigation bar, providing a distinct brand identity for the site. Moreover, the logo is linked to the home page, enabling seamless navigation for the users back to the main page with just a click.

**Navigation Bar**

- The website features a consistent navigation bar at the top of every page, containing links to various other pages.
- In particular, the "My Account" link appears as a drop-down menu. For non-logged-in users, this drop-down menu includes options for "Sign Up" and "Log In."
- Once a user successfully logs in, the "My Account" drop-down menu dynamically changes to show the user's name along with a profile icon, offering personalized access to their account details.

![header logged in](https://cdn.discordapp.com/attachments/1049024982694498367/1136649952420970577/image.png)

- Once a user has logged in, the options to "Sign Up" or "Log In" in the navigation bar will dynamically change to "Log Out" for easy account management.
- Upon successful login, additional options such as "Add Recipe", "My Recipes," and "My Bookmarks" become accessible, providing enhanced functionality and personalized features to the user.
- The navigation bar is fully responsive and adapts to different screen sizes. When the screen size is reduced, it collapses into a hamburger menu, ensuring optimal user experience on smaller devices.
- Additionally, hovering over the links in the navigation bar triggers a visual effect where the font lightens, providing feedback to users as they interact with the links.

### Footer

![footer](https://cdn.discordapp.com/attachments/1049024982694498367/1136650143089832016/image.png)

- The footer section of the website contains convenient links to social media platforms such as Facebook, Instagram, Twitter, and YouTube.
- When users click on these links in the footer, they will open in separate browser tabs. This approach ensures that users can access the social media pages without being redirected away from the main site, maintaining a seamless browsing experience.

### Home Page

**Hero Section**

![hero-section logged out](https://cdn.discordapp.com/attachments/1049024982694498367/1136673405492539434/image.png)

- The homepage prominently features a call-to-action (CTA) section that invites users to engage with the site.
- The compelling message, "Embrace the adventure of trying out different dishes every day!" is accompanied by an enticing image of delectable dishes on a table.
- Within this CTA, a prominent "Sign Up" button is provided, allowing users to easily navigate to the sign-up page and embark on their culinary journey. This strategically placed CTA encourages user interaction and enrollment, contributing to an engaging and immersive user experience.

![hero-sectoin logged in](https://cdn.discordapp.com/attachments/1049024982694498367/1136673867847454831/image.png)

- If a user is already logged in, the displayed message transforms into a warm "Welcome back to Dishful Discoveries!", setting the tone for their continued exploration.
- Furthermore, logged-in users are prompted to contribute to the culinary community by creating their own recipes. To facilitate this, the "Sign Up" button is replaced with a purposeful "Create" button. Clicking on this button seamlessly redirects the user to the 'Add recipe' page, encouraging them to share their unique culinary creations and enhance the website's content.
- This tailored messaging and intuitive navigation cater to both new and returning users, fostering an environment of continuous discovery and participation.

**Three-Reasons Section**

![features](https://cdn.discordapp.com/attachments/1049024982694498367/1136675169872642068/image.png)

- The "Three-Reasons" section succinctly outlines the site's offerings, encapsulating its fundamental features through a trio of uncomplicated steps.
- These steps are elegantly depicted using Font Awesome icons, providing a visually engaging representation of the process.
- This approach effectively communicates the essence of the site and its core functionalities in a clear and concise manner.

### User Account Pages

**Sign Up**

![sign Up](https://cdn.discordapp.com/attachments/1049024982694498367/1136675837039628348/image.png)

**Log In**

![login](https://cdn.discordapp.com/attachments/1049024982694498367/1136675931730231336/image.png)

**Log Out**

![logout](https://cdn.discordapp.com/attachments/1049024982694498367/1136675759763751024/image.png)

- The implementation of Django AllAuth facilitated the establishment of essential user functionalities such as Sign Up, Log In, and Log Out.

**Messages**

![messages](https://cdn.discordapp.com/attachments/1049024982694498367/1136676330457546856/image.png)

- To enhance user experience, success messages are incorporated to provide immediate feedback when users successfully log in or log out. These messages play a pivotal role in informing users about the status of their actions and contribute to seamless interaction with the website.
- The messages close themselves after a short delay of three seconds.

### Browse Recipes

![browse recipes page](https://cdn.discordapp.com/attachments/1049024982694498367/1136677267481821295/image.png)

- On this page, an assortment of recipes is presented, arranged in descending order based on their date of creation.
- To facilitate optimal presentation, the recipe cards are organized into pagination groups, with a new batch of cards emerging after every 8 recipes.
- Each individual recipe card thoughtfully exhibits the recipe's image, title, and estimated cook time, providing a concise glimpse into its key attributes.
- Furthermore, users can seamlessly delve into the comprehensive details of any recipe by simply clicking anywhere within the corresponding recipe card.
- This intuitive design ensures direct navigation to the dedicated detailed page, where users can explore the recipe's ingredients, instructions, and other information.

### Recipe Detail Page

**Recipe Header Section**

![recipe header](https://cdn.discordapp.com/attachments/1049024982694498367/1136679296618999951/image.png)

The uppermost section of the recipe page features a distinctive recipe header, showcasing the recipe's image, title, author, preparation time, and cooking time.

**Recipe Action Buttons**

If the user is logged in, the following button will be displayed:

![logged in](https://cdn.discordapp.com/attachments/1049024982694498367/1136680377650532372/image.png)

- By clicking the outlined heart icon, the user can indicate their appreciation for the recipe, marking it as 'liked'. This action transforms the heart icon into a filled version and adds the recipe to the user's 'my likes' page for future reference.
- Clicking the button again will reverse the process, removing the recipe from the user's saved collection and changing the heart icon back to its initial outline state.

For logged-in users who are also the authors of the recipe, the following buttons will be available:

![logged in owner](https://cdn.discordapp.com/attachments/1049024982694498367/1136680130677309523/image.png)

- The "Update Recipe" Button: Clicking this button triggers the opening of an update recipe form. The form is prepopulated with the existing recipe details, providing an efficient way to make modifications.
- The "Delete Recipe" Button: When this button is clicked, it prompts the opening of a confirmation page for recipe deletion. This additional step helps prevent accidental deletion by requiring user confirmation before proceeding.

**Recipe Details Section**

![recipe details](https://cdn.discordapp.com/attachments/1049024982694498367/1136681730598768761/image.png)

- The primary content of the page is centered around the recipe itself and encompasses the recipe description, list of ingredients, and step-by-step method for preparation.

**Comments Section**

![comments](https://cdn.discordapp.com/attachments/1049024982694498367/1136682559577804890/image.png)

- The comments section presents a compilation of user-contributed comments specific to the given recipe.
- To interact with the comments section, users must be logged in. Once logged in, users have the ability to leave comments on the recipe.
- Comments authored by the currently logged-in user offer additional options.
- Comments can be modified or removed using the buttons conveniently situated within the comment header.

![header](https://cdn.discordapp.com/attachments/1049024982694498367/1136683645852192880/image.png)

![header](https://cdn.discordapp.com/attachments/1049024982694498367/1136683697949646948/image.png)

- Upon updating or deleting a comment, the user is promptly presented with a success message, confirming the successful execution of the respective action.
- This immediate feedback ensures that users are aware of the outcome of their interactions with the comments section.

![message](https://cdn.discordapp.com/attachments/1049024982694498367/1136683745781481615/image.png)

- If a user tries to edit or delete a comment (by changing the url) without being signed in they are redirected to the log in page.
- If a user tries to edit/delete another user's comment (by changing the url) they receive a custom 403 error.

![403 Forbidden](https://cdn.discordapp.com/attachments/1049024982694498367/1136687662607118436/image.png)

### Add Recipe Form

![add recipe page](https://cdn.discordapp.com/attachments/1049024982694498367/1136689270610993212/image.png)

- When a user is logged in, they can initiate the process of adding a recipe by selecting the appropriate link in the navigation bar.
- Within the form, the 'Ingredients' and 'Method' fields are equipped with a user-friendly WYSIWYG editor named Summernote. This editor empowers users to format their content with ease by incorporating elements like bullet points and headings.
- Users also have the option to upload a photo alongside their recipe. Should they opt not to, a default image is displayed as the recipe's visual representation.
- In cases where essential fields like 'Title', 'Category', 'Description', 'Ingredients', or 'Method' are left incomplete, the form will not proceed and will instead present an error message specifying the missing fields.
- For users attempting to add a recipe without being logged in, they will be automatically redirected to the login page, preventing unauthorized access.
- Following the successful addition of a recipe, users are promptly presented with a success message confirming the completion of the process.

### Update Recipe Form

![recipe update page](https://cdn.discordapp.com/attachments/1049024982694498367/1136690504214511626/image.png)

- When a logged-in user is the author of a recipe, they are given the option to edit the recipe by clicking the designated edit button on the recipe detail page.
- Upon initiating the editing process, the form opens, and all fields are prepopulated with the original content, streamlining the editing experience.
- For users who attempt to update a recipe without being logged in, they will be automatically redirected to the login page, ensuring secure access.
- In situations where a user tries to modify another user's recipe by manipulating the URL, they will be presented with a custom 403 error, safeguarding the integrity of the content.
- Following the successful completion of a recipe update, users are promptly presented with a success message, confirming the successful execution of the update action.

### Delete Recipe

 ![recipe delete page](https://cdn.discordapp.com/attachments/1049024982694498367/1136691077529743470/image.png)

- When a logged-in user is the author of a recipe, they have the option to delete the recipe by clicking the dedicated delete button on the recipe detail page.
- Upon clicking the delete button, the user is prompted with a confirmation dialog, presenting the choice to proceed with deleting the recipe or to cancel the action.
- After successfully confirming the deletion, users are informed of the success with a prompt message indicating that the recipe has been successfully deleted. This feedback ensures users are aware of the outcome of their action and maintains transparency in the process.

### My Recipes Page

![my recipes page](https://cdn.discordapp.com/attachments/1049024982694498367/1136691568816963584/image.png)

- This page presents a comprehensive list of recipes exclusively authored by the logged-in user.
- To optimize the presentation, the recipe cards are divided into pagination groups, with each set containing up to 8 recipes.
- Each recipe card provides essential information including the recipe's image, title, and cook time.
- By clicking anywhere within the recipe card, users are seamlessly directed to the dedicated detailed page for that specific recipe, ensuring swift access to the comprehensive information.
- To ensure the integrity of access, users attempting to reach this page without being logged in will be automatically redirected to the login page, safeguarding the privacy of recipe creators.

### My Likes Page

![my likes page](https://cdn.discordapp.com/attachments/1049024982694498367/1136692313322696774/image.png)

- This page showcases an assortment of recipes that the currently logged-in user has liked.
- Users can seamlessly navigate to the detailed page of any desired recipe by clicking anywhere within its respective recipe card.
- To maintain the integrity of access, users attempting to reach this page without being logged in will be promptly redirected to the login page, ensuring the security of user data and preferences.

### Error Pages

Tailored error pages have been developed to offer users detailed insights into encountered errors and to provide guidance for returning to the main site.

These error pages are designed to enhance the user experience by delivering relevant information and navigation options in case unexpected issues arise during their interaction with the website.

![header](https://cdn.discordapp.com/attachments/1049024982694498367/1136692821080936479/image.png)

- 400 Bad Request - Dishful Discoveries is unable to handle this request.
- 403 Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Not Found - The page you're looking for doesn't exist.
- 500 Internal Server Error - Dishful Discoveries is currently unable to handle this request.

## Deployment - Heroku

The subsequent actions were carried out to facilitate the deployment of this page to Heroku from its corresponding GitHub repository:

### Create the Heroku App

- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labeled "New" in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next, select your region.
- Click on the Create App button.

### Attach the Postgres database

- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file

- In your workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py.
- Add the Cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url, and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR.
- Add Heroku to the ALLOWED_HOSTS list.

### Create files/directories

- Create requirements.txt file.
- Create three directories in the main directory; media, storage, and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi.

### Update Heroku Config Vars

Add the following Config Vars in Heroku:

- SECRET_KEY = yoursecretkey
- CLOUDINARY_URL = yourcloudinaryurl
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy

- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository.
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.

## Forking this repository

- Locate the repository at this link [Dishful Discoveries](https://github.com/KaiLangen96/dishful-discoveries).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available.
- A copy of the repository is now created.

## Cloning this repository

To clone this repository follow the below steps:

1. Locate the repository at this link [Dishful Discoveries](https://github.com/KaiLangen96/dishful-discoveries).
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the preferred cloning option, and then copy the link provided.
3. Open **Terminal**.
4. In the Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier.
6. Type **'Enter'** to create the local clone.

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used

- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud-based platform to deploy the site on.
- [AmIResponsive?](https://ui.dev/amiresponsive) - Used to verify the responsiveness of my website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and using lighthouse.
- [Font Awesome](https://fontawesome.com/) - Used for icons in the three-reasons section.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [CI Python Linter](https://pep8ci.herokuapp.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create color palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Grammerly](https://app.grammarly.com/) - used to proofread the README.md
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling

## Credits

### Code

- I created my recipe website partially with the help of [AliOKeeffe's PP4_My_Meal_Planner](https://github.com/AliOKeeffe/PP4_My_Meal_Planner).

### Media

- The static images used as hero-image and placeholder-image were found on Google. Every image used by Hinion to create a recipe for my website was taken by [Hanna Kronberg](https://www.linkedin.com/in/hanna-kronberg-534a2b199/).

### Content

- The recipes posted on my website were found throughout the web. I have no copyright for any of them.

## Special Thanks

[Code Institude](https://codeinstitute.net/), for teaching me the languages needed to create this page.

[w3schools](https://www.w3schools.com/), for so many helpful pages and tools to support learning the languages.

[Django](https://docs.djangoproject.com/en/4.0/) and [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) docs, for a lot of helpful information.

[Stack Overflow](https://stackoverflow.com/), for a lot of help, especially regarding bug fixes.

[Antonio Rodríguez](https://www.linkedin.com/in/antonio-rodr%C3%ADguez-bb9b99b7/), as my mentor. Once again, he helped me a lot with getting started with the recipe website and creating the ERD.
