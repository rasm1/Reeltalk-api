# Reeltalk Backend API

**Advanced Front-End Portfolio Project(PP5) - Code Institute**

The *Reeltalk API* is the backend for the reeltalk-frontend application, built using Django Rest Framework. It serves as the foundation for a social network [Reeltalk-frontend ](https://reeltalk-9iif.onrender.com/) focused on sharing opinions on movies<br>

*Reeltalk API* is designed for users who want to share their opinion on their favorite movies. Posts can be created to show and promote their favorite movies so that other users can engage with them. The post functionality includes: a title, a movie title, content, an image of your favorite movie, moviepostives & negatives as well as a spoiler warning.<br>

Additionally, users have the ability to follow others, allowing them to stay updated on Reeltalk.
<br>
The API is organized into several key apps:<br>

_posts_: Manages the creation and details of posts<br>
_profiles_: Handles user profiles and related information.<br>
_comments_: Enables users to comment on Reeltalk.<br>
_likes_: Allows users to like a Post they are interested in.<br>
_followers_: Facilitates the following and tracking of other users' activities.<br>
<br>
This API is designed to be consumed by a React frontend, providing a seamless experience for users looking to connect and engage in activities together.
<br>
The deployed API can be found here: [Reeltalk API](https://reeltalk-api.onrender.com/)<br>
The deployed React project can be found [here](https://reeltalk-9iif.onrender.com/) <br>
The link for the GitHub repository to the associated front end can be found [here](https://github.com/rasm1/Reeltalk)

## Table of Contents

- [User Experience](#user-experience)
- [Structure](#structure)
- [Database](#database)
  - [Models](#models)
- [API Endpoints](#api-endpoints)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Tools](#tools)
  - [Frameworks](#frameworks)
  - [Libraries and modules](#libraries-and-modules)
- [Testing](#testing)
  - [Python Validator Testing](#python-validator-testing)
  - [Manual testing](#manual-testing)
  - [Browser Compatibility](#browser-compatibility)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Local deployment](#local-deployment)
  - [Forking this GitHub repository](#forking-this-github-repository)
  - [Clone this repository](#clone-this-repository)
  - [Cloudinary](#cloudinary)
  - [Create PostgreSQL using Code Institute Database Maker](#create-postgresql-using-code-institute-database-maker)
- [Credits](#credits)
  - [Code](#code)
  - [ReadMe](#readme)
  - [Acknowledgments](#acknowledgments)


## User Experience

I used an Agile methodology approach to plan this project. This was implemented through the GitHub Project board with epics, user stories and acceptance criteria .
Each user story was classified with a label according to MoSCoW prioritization.<br>


### User stories

The Kanban board for reeltalk user stories can be seen [here](https://github.com/users/rasm1/projects/4).<br>


## Structure

The database schema was crafted during the planning phase of the project.

## Database<br>
I used a PostgreSQL provided by Code Institute as relational database.<br>


- **Relationships:**<br>
  - A User has one Profile.
  - A Profile belongs to one User.
  - A Post is created by one User.
  - A User can create many posts.
  - A User can like many Posts.
  - A User can create many comments for a Post. 
  - A Comments belongs to one User and one Post
  - A User can follow another User.

### Models

*Profile* <br>
- The Profile model represents a user's profile in the application, automatically created when a new user is registered. It includes various fields to store personal information such as the user's name, profile image, date of creation The model also tracks when the profile was created and last updated. The associated *ProfileSerializer* is responsible for serializing the profile data, adding additional computed fields like whether the requesting user owns the profile (is_owner), and validating the profile image size and dimensions. The serializer also integrates follower-related information, such as follower counts and the ID of the current user's following relationship with the profile owner, to support social features in the application.<br>
<br>

*Posts* <br>
- The Posts model represents an event posted by a user within the application. Each posts includes details like the event name, image, the date and time it is scheduled to occur, the location, and a description and automatically tracks when the event was created and last updated. The associated *PostsSerializer* handles serialization of this data, adding additional fields to represent the ownership status, profile information of the post creator, likes and counts of likes and comments.<br>

*Likes*<br>
- The likes model represents a user liking a specific Posts for showing his interest. Each like links a user to a Posts, recording when the likes was created. The model enforces that a user can only likes a Post once, ensuring no duplicates. The associated *likesSerializer* is responsible for handling the serialization of likes data, including the user and event details. It also includes validation logic to raise an error if a user attempts to likes the same event more than once. This structure supports a clean and efficient way to manage user likes within the application.<br>

*Comment*<br>
- The Comment model is designed to manage user-generated comments on specific Posts. Each comment is associated with a user (owner) and a Posts, capturing the content of the comment along with timestamps for when it was created and last updated. The model ensures that comments are displayed in reverse chronological order by default, showing the most recent ones first.
The associated *CommentSerializer* handles the serialization of comment data, including details about the user who made the comment, their profile picture, and the timestamps formatted in a human-readable manner. The CommentDetailSerializer extends this by providing additional details, such as the ID of the associated Posts event. This setup enables efficient management and display of comments within the application, fostering interaction and discussion around Posts.<br>

*Follower*<br>
- The Follower model manages the relationships where users follow other users within the application. It establishes a connection between the owner (the user who is following) and the followed (the user being followed), allowing for tracking of these interactions. Each follow relationship is time-stamped, showing when it was created, and the model enforces uniqueness to prevent duplicate follow relationships. The data is ordered by the most recent followings by default.
The *FollowerSerializer* is responsible for converting these follow relationships into a serialized format for API responses. It includes fields for the usernames of both the follower and the followed, and it prevents users from following themselves or following the same user multiple times. This ensures the integrity of the following system within the application, supporting functionalities like displaying followers, following counts, and managing user connections.

*Home*<br>
A welcome message is displayed when you first enter the API site.<br>
![Screenshot of welcome message](/README-Assets/welcome-message.png)<br>

## API Endpoints

The endpoints provided by the API are:<br>

| Endpoint                                     | HTTP Method | CRUD Operation |
| -------------------------------------------- | ----------- | -------------- |
| /dj-rest-auth/registration/                  | POST        | N/A            |
| /dj-rest-auth/login/                         | POST        | N/A            |
| /dj-rest-auth/logout/                        | POST        | N/A            |
| /profiles/                                   | GET         | Read           |
| /profiles/\\<int:pk\\>/                      | GET         | Read           |
|                                              | PUT         | Update         |
| /posts/                                      | GET         | Read           |
|                                              | POST        | Create         |
| /posts/\\<int:pk\\>/                         | GET         | Read           |
|                                              | PUT         | Update         |
|                                              | DELETE      | Delete         |
| /comments/                                   | GET         | Read           |
|                                              | POST        | Create         |
| /comments/\\<int:pk\\>                       | GET         | Read           |
|                                              | PUT         | Update         |
|                                              | DELETE      | Delete         |
| likes                                        | GET         | Read           |
|                                              | POST        | Create         |
| /likes/\\<int:pk\\>/                         | GET         | Read           |
|                                              | DELETE      | Delete         |

## Bugs

### post image URL prefixed bug
<br>
Images posted by users would be prefixed with the deployed heroku URL instead of the required cloudinary URL
<br>


### 500 error in post model
<br>
Due to the conversion of imagefield to cloudinaryfield the /posts/ endpoint threw a 500 error.
<br>

### Post image shows broken image
<br>
Imagefield was required so when an invalid (or no) image was uploaded
it displayed a broken image
<br>

### profile edit page did not display profile image
<br>
Due to a mismatch of image names between the front and backend the avar 
image did not display in profile edit page.
<br>

### profile edit page did not update the avatar image
<br>
When updating the profile iamge in edit profile page, when clicking save the avatar image did not update due to a naming mismatch between front and backend.
<br>



## Technologies Used

### Languages:
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Tools:
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) have been used for Agile sprint planning and task tracking.
- [Heroku](https://www.heroku.com) was used to deploy the application.
- [VSCode](https://code.visualstudio.com) was used as IDE. 
- [Code Insitute Database Maker](https://dbs.ci-dbs.net/) PostgreSQL database hosting for this project
- [remove.bg](https://www.remove.bg/upload) was used to remove the background from displayed images.
- [Cloudinary](https://cloudinary.com/) was used to store the item images.
- [Favicon.io](https://favicon.io/favicon-generator/) was used to create the favicon.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools?hl=de) were used to check the application for responsiveness and errors.

### Frameworks:  
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))

### Libraries and modules:
- [os](https://docs.python.org/3/library/os.html) provides functions to interact with the operating system. 
- [sys](https://docs.python.org/3/library/sys.html) was used to get system-specific functions.
- [datetime](https://docs.python.org/3/library/time.html) supplies classes for manipulating dates and times.
- [Gunicorn](https://gunicorn.org/) provides a way to serve Python web applications.
- [Pycopg 2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for Python.
- [dj_database_url](https://pypi.org/project/dj-database-url/) enables the ability to represent their database settings via a string.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/): was used to connect Cloudinary as Django file storage
- [django-cors-headers](https://pypi.org/project/django-cors-headers/): Handle Cross-Origin Resource Sharing in Django
- [django-filter](https://pypi.org/project/django-filter/): Provides filtering with URL parameters for querysets
- [dj-rest-auth](https://dj-rest-auth.readthedocs.io/en/latest/): to handle user registration, login, and logout
- [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html): JSON Web Token authentication for Django REST Framework.
- [oauthlib](https://oauthlib.readthedocs.io/en/latest/): A generic, spec-compliant, thorough implementation of the OAuth request-signing logic.
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/): JSON Web Token implementation in Python.
- [python3-openid](https://pypi.org/project/python3-openid/): A library for implementing OpenID in Python.
- [requests-oauthlib](https://pypi.org/project/requests-oauthlib/): OAuth library that implements the client side of the OAuth protocol.
- [dj-database-url](https://pypi.org/project/dj-database-url/): A simple utility to allow using Database URLs in Django.
- [whitenoise](https://whitenoise.readthedocs.io/en/latest/): A Django middleware to serve static files 
- [pillow](https://pypi.org/project/pillow/): A Python Imaging Library (PIL) fork, adding image processing capabilities to your Python applications.

## Testing

The app was tested regularly and deployed to Heroku to make sure both local and remote worked the same.

### Python Validator Testing

- All created python files were checked with the [Code Insitute validator - CI Python Linter](https://pep8ci.herokuapp.com/#). <br>

### Manual Testing

- *URL Path Verification*: Confirmed that all URL endpoints were correctly set up and functioning as expected, with no errors encountered during navigation.<br>
- *CRUD Operations Validation*: Conducted thorough testing of the create, read, update, and/or delete operations across various entities, including: posts, comments, shares, profiles, reports, followers, and likes.
  - Successfully created new entries and ensured the corresponding URLs were working properly.
  - Verified the update functionality, ensuring data could be correctly modified (with the exception of followers and likes).
  - Performed delete operations to confirm that posts and comments could be removed as intended.

These manual tests were conducted to ensure that the API operates smoothly and behaves as intended.

### Automated Testing
To cover all the user story scenarios, the following automated tests have been written into the Groovemates API. <br>

**Posts**<br>

PostListViewTest<br>
- test_can_list_posts:<br>
Confirms that logged-in users can retrieve a list of all posts. The server should return a 200 OK status.<br>

- test_logged_in_user_can_create_post:<br>
Ensures that a logged-in user can create a new post. Verifies that the post count increases, and the server returns a 201 CREATED status.<br>

- test_logged_out_user_cant_create_post:<br>
Ensures that logged-out users cannot create a post. The server should return a 403 FORBIDDEN status.<br>

PostDetailViewTest<br>
- test_can_retrieve_post_with_id:<br>
Ensures that a logged-in user can retrieve a post's details by its ID. The server returns a 200 OK status and the correct post data.<br>

- test_cant_retrieve_post_using_invalid_id:<br>
Validates that trying to retrieve a non-existent post (invalid ID) results in a 404 NOT FOUND status.<br>

- test_user_can_update_post:<br>
Verifies that a logged-in user can update their own post. Confirms the post's data is updated, and the server returns a 200 OK status.<br>

- test_user_cant_update_other_users_post:<br>
Ensures that users cannot update posts they do not own. Returns a 403 FORBIDDEN status.<br>

- test_user_can_delete_own_post:<br>
Confirms that users can delete their own posts. The post is removed, and the server returns a 204 NO CONTENT status.<br>

- test_user_cant_delete_other_users_post:<br>
Validates that users cannot delete posts owned by others. The server should return a 403 FORBIDDEN status.<br>


### Browser Compatibility
  The tests were conducted using the following browser:

- Google Chrome Version 127.0.6533.120 

## Deployment

### Heroku
This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:

1. Create a list of requirements in the requirements.txt file by using the command _pip3 freeze > requirements.txt_
2. Log in (or sign up) to Heroku
3. Click on the _New_ button and select _Create new app_
4. Give it a unique name and choose the region _Europe_
5. Click the *Settings* tab, go to the _Config Vars_ section and click on the _Reveal Config Vars_ button
6. Add all variables from *env.py* to _ConfigVars_ of Heroku
![Screenshot of config vars](documentation/readme/heroku_details.png)<br>
7. Click the _Add_ button
8. Click the *Deploy* tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button
9. Search for the repository name on github Reeltalk_api and click the _Connect_ button
10. Add in the setting.py the Heroku app URL into ALLOWED HOSTS<br>
11. Gather all static files of the project by using the command _python3 manage.py collectstatic_ in the terminal
12. Make sure that DEBUG=FALSE in settings.py
13. Create a _Procfile_ in the root directory and add *web: gunicorn fv_api.wsgi*
13. In Heroku enable the automatic deploy or manually deploy the code from the main branch

 click on the _Open app_ button in the top right corner or, if you enabled automatic deploy (step 13), log in to GitHub, navigate to the repository for this project by selecting [Reeltalk-api](https://github.com/rasm1/Reeltalk-api), click on the _Deployments_ heading and choose in the _Environments_ section GrooveMates_backend. On top of the latest deployment is the link to the [live site ](https://reeltalk-api-a79479495f97.herokuapp.com/).<br>

### Local deployment

1. Generate an env.py file in the root directory of the project
2. Configure the environment variables within this file.
3. Create a virtual environment, if neccessary
4. Install all required dependencies using _pip install_ command (into the .venv)
5. Add dependencies to the requirements.txt file using _pip3 freeze > requirements.txt_ command

### Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by select [rasm1 Reeltalk-api](https://github.com/rasm1/Reeltalk-api)
3. Click at the top of the repository on the **Fork** button on the right side

### Clone this repository
1. Log in to GitHub.
2. Navigate to the repository for this project by select [rasm1 Reeltalk-api](https://github.com/rasm1/Reeltalk-api)
3. In the top-right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

### Cloudinary
1. Navigate to [Cloudinary](https://cloudinary.com/)
2. Sign up or log in to account
3. Go to the dashboard
4. Click on _Go to API Keys_ button
5. Generate a new API Key
6. Provide the API environment variable in format: *CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dwqek0e9x* in _env.py_ and _Config Vars_
7. Update settings.py

### Create PostgreSQL using Code Institute Database Maker
1. As Student of the Code Institute, navigate to the [CI Database Maker](https://dbs.ci-dbs.net/)
2. Input your email address
3. Paste the provided URL in as your DATABASE_URL value

## Credits

### Code
- The initial setup and overall architecture of this project were guided by the Code Institute's Django Rest Framework walkthrough project. The core elements of the Profile, Post, Follower, likes and Comment models, along with their respective serializers, filtering capabilities, and tests, were derived from the walkthrough project and subsequently tailored to meet the unique requirements of this project.
- Token authentication code was inspired by [Liene Breide]https://github.com/lienebriede/habit-react/


- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [Stack Overflow](https://stackoverflow.com/)
  - [reddit](https://www.reddit.com/)
  - Documentation for [Django](https://www.djangoproject.com/), [Django Rest Framework]((https://www.django-rest-framework.org/)), [Cloudinary](https://cloudinary.com/documentation)
  - Slack Community
  - For troubleshooting, [Google](www.google.com), and [ChatGPT](https://chatgpt.com/) were used, too. Especially since the walkthrough project is completely outdated and many of the components no longer work as they should.

  ### ReadMe

- a big thank you to [Pramila shanmugam](https://github.com/Pramilashanmugam/GrooveMates_backend), her README server as an inspiration and as an example.

### Acknowledgements

- I would like to thank my wonderful mentor Mitko Bacharov for his numerous tips and great assistance during the creation of this project.  
- I would like to give a shoutout to the tutor team who helped me multiple times when I was stuck and struggling to achieve the results I was aiming for. Your support and guidance have been amazing. Thank you!

**This is for educational use.**