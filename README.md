1) How do I implemented the checklist above step-by-step?

Create a new Django project.
> First of all, I made a new folder in my laptop called live-to-kick (which will be my Django project name). Then, I changed the directory in command prompt to the file I created and use the command "python -m venv env" and then "env\Scripts\activate" to activate the virtual environment. After that, I opened my VSCode, opened the folder live-to-kick there, then I create a new requirements.txt file and add the needed dependencies and install it using the command "pip install -r requirements.txt" so that we can use those dependencies. After that, I just create a django project name live_to_kick by using "django-admin startproject live_to_kick ." command. Then, I make a .env file and ensure that "PRODUCTION=False" is there. Afterwards, create a .env.prod file with the database credentials from my gmail, then replace tutorial with tugas_individu. Then I modify the settings.py file to use the enviroment variable and also add localhost to ALLOWED_HOST and PRODUCTION configuration. After that I only need to try running the server to make sure everything went alright, by doing "python manage.py migrate" then "python manage.py runserver" then opening the link "http://localhost:8000" to see if it works or not.

> After that, I connect my project to github by running the command "git branch -M main" then using the HTTPS URL of the respitory I made in github website, I typed the command "git remote add origin https://github.com/EvelynOct/live-to-kick.git" on command prompt. 

Create an application named main within the project.
> To do this, I ran the command "python manage.py startapp main" on command prompt, then I register the "main" application on the settings.py of the "live_to_kick" project by adding it to INSTALLED_APPS.

Configure routing in the project to run the main application.
> This is similar to my answer in creating the routing using urls.py. To do this, first I made a urls.py file in the main directory, this will contain the routing configurations. Then we import the path function and the show_main function from main.views so it will be called when it matchs with a URL. 


Create a model in the main application named Product with the mandatory attributes.
> For this, I open the models.py file in the main application directory, then add a class Product(models.Model). Afterwards, I add the mandatory attributes alongside the needed type. Then, to apply the changes made in models.py, we need to run the model migrations using the command "python manage.py makemigrations" and then "python manage.py migrate".

Create a function in views.py to be returned to an HTML template that displays the application name, your name, and your class.
> I just edit my views.py that has the data (my app name, my name, and my class), then I return render with the main.html. Then on the main application there's a folder called templates where I will make a file called main.html. It will contains the app title, name, and my class.


Create routing in urls.py of the main application to map the function created in views.py.
> To do this, first I made a urls.py file in the main directory, this will contain the routing configurations. Then we import the path function and the show_main function from main.views so it will be called when it matchs with a URL. We also import the include function from django.urls to import URL route patterns from other application to the urls.py file. 

Deploy the application to PWS so that it can be accessed by your peers via the Internet.
> To do this, I just log in to the PWS website, then log in using my SSO information. After that, I made a new project called livetokick and copy the credential. Then, I edit the enviroment in the website according to the contents of the .env.prod file. Then in the settings.py I add the PWS deployment URL,then do the usual git add, commit, push. Then build the website using the credentials from earlier. 

Create a README.md file
> I just make a new file called README.md in my live-to-kick root folder, then I do "git add README.md" command at command prompt, followed by "git commit -m "Answers" as commit. Then I do "git push origin master" and "git push pws master" everytime I edit something in the files I'm using.

2) Create a diagram showing the client request to the Django-based web application and its response, and explain the relationship between urls.py, views.py, models.py, and the HTML file in the diagram.

This is the diagram (source from the MTV PPT of PDB):

Link to gdrive (in case it doesn't show properly): https://drive.google.com/file/d/1G-kt6VAG6eZvukHYEFUtWymNYRYqi8xY/view?usp=sharing 
> HTTP request --> URLS (urls.py) -- (then it forwards the request to the mentioned view)
>                                                    |
>                                                    |
>                                                    ↓
> Model (models.py) <--- Read/Write data --->  View (views.py) --> HTTP response (html)
>                                                    ↑
>                                                    |
>                                                    |
>                                            Template (filename.html)

Explanation: 

urls.py acts like a traffic controller, so the user accesses the URL they want on their browser, then the Django will map the request to a View via the urls.py to the correct functions or classes in views.py. Then, the view retrieves and process the data from the Model or data structure in models.py. Lastly there is the HTML template (such as filename.html) that is the presentation layer, where user get contexts of the view, and it can use Django template to insert the data to html. 

3) Explain the role of settings.py in a Django project!

settings.py is like the control center for the Django project. It contains all the configurations for the Django project. For example, we can modify the settings.py to use environment var, or to edit the ALLOWED_HOST for development purposes.

4) How does database migration work in Django?

We use 2 commands to run the database migration on Django. The first command to run is "python manage.py makemigrations", this will create migration files that contains model changes that hasn't been applied to the database. Afterwards, we need to apply the migrations to the database by running "python manage.py migrate" which applies the model changes listed in the migration files to the database. So, if we change a model, we need to repeat the 2 migration command.

5) In your opinion, among all existing frameworks, why is the Django framework chosen as the starting point for learning software development?

In my opinion, I think the MTV structure from Django is good to learn in software development. Because I think it has a clear separation, which is the Model-Template-View. So the data and the presentation is separated. Other than the MTV structure, I also this that the Django commands are not that complicated, like by using startapp we could start an app already.

6) Do you have any feedback for the teaching assistant for Tutorial 1 that you previously completed?

I think the tutorial 1 is clear. However I did encounter some problem because my phyton file wasn't auto save. So when I forgot to save the file before running the command in command prompt, the command and the next commands that I used becomes an error. 


--------------------------------------------------
Assignment 3:
1. Why do we need data delivery in implementing a platform?
> In my opinion, it is important because all platforms needs data to function. Having the right data delivery is important because we need the right data to move between the users and services at the right time. For example, we can use the data delivery to have real time interaction with the user. We can also use our platform to interact with another platform by using API.

2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
> I believe that JSON is better than XML for me because it's easier to read compared to XML. I think JSON is more popular than XML because it works well with JavaScript and since a lot of platform use JavaScript now, JSON is more prefered. 

3. What is the purpose of the is_valid() method in Django forms, and why do we need it?
> I believe that is_valid() is used to check if the form has been submitted with the data, then each field is also checked so that it matches the requirement (for example it must have the right data type). Then, if everything works fine, Django creates a place for clean data in form.cleaned_data. If it fails, it will store error message in form.errors.

4. Why do we need a csrf_token when making forms in Django? What can happen if we don't include a csrf_token in a Django form? How can this be exploited by an attacker?
> csrf_token is needed so that it ensures the form submission is really from our website and not a malicious or dangerous third party website. If we dont use a csrf_token, our site will be vulnerable to CSRF attacks. This can be exploited by an attacker by tricking the users to do something they doesnt intend, like changing the user's password.

5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).

a. Add 4 new views functions to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.
> First of all, I do this by adding HttpResponse and Serializer to views.py. Then, I made the 4 views function show_xml, show_json, show_xml_by_id, and show_json_by_id by using HttpResponse to return a response. Then, I add those functions in urls.py by using from main-views import (the functions) and add it into the path url.

b. Create URL routings for each of the views added in point 1.
> I do this by opening urls.py, then using from main-views import (the functions) and add it into the path url. The form of path url should be something like path('json/', show_json, name='show_json').

c. Create a webpage to display the model object data with an "Add" button that redirects to the form page, and a "Detail" button on each model object data that displays the object's detail page.
> To do this, I made a main.html file at the main/templates, then I made a new button called Add Product where it is linked to the create_product.html so that it will redirect to the form page. Then I made a if else function. If there is no product list (its empty), then it will return a message. If there is a product, then it will show the products alongside it properties. I also add a "Detail" button where the user will get redirected to the product_detail.html page .

d. Create a form page to add model objects to the previous app.
> Im using the create_product.html file for this, in the file I use the models from assignment 1, then I also link it to base.html. Then, I linked it to urls.py so that it can be imported to the path url.

e. Create a webpage that displays the details of each model object data.
> Im using the product_detail.html page for this, in the file I use the models I created from assignment 1 before, such as name, description, etc. Then link it with the main.html page. Then, I linked it to urls.py so that it can be imported to the path url.

6.  Do you have any feedback for the teaching assistants for Tutorial 2?
> I think the many typos made it harder/longer for the debugging kak. But other than that, I think it's good. The TAs is very helpful to help fix the bugs and teach us how to read the bugs :D

7. Access the four URLs in point 2 using Postman, take screenshots of the URL access results in Postman, and add them to your README.md
> https://drive.google.com/drive/folders/1xcZHH48Btw6ELFNUVkmNJ6viT7iGQvF0?usp=sharing 

--------------------------------------------------
Assignment 4 : Implementing Authentication, Session, and Cookies in Django

1. What is Django's AuthenticationForm? Explain its advantages and disadvantages.
> Django's AuthenticationForm handle user login functionality. It is located in django.contrib.auth.forms and we can use it for authenticating users. The uses for it are to validates username/email and password combinations, checks if the user exists and credentials are correct, and it also handles authentication logic automatically.

> Some of the advantages: 
> It's secure and reliable, includes CSRF protection, easy to implement since we don't need to write custom validation logic, standard form rendering in termplates, etc.

> Some of the disadvantages:
> It has basic features only, like there is no custom user field support like phone number, fixed field structure (username/password only), no multi-factor authentication support, etc.

2. What is the difference between authentication and authorization? How does Django implement the two concepts?
> Authentication is is the process of verifying who you are to login, meanwhile authorization is the process of verifying that you have access to something. For example authentication is logging into your email account with credentials. Meanwhile authorization example is that admin can delete posts while regular users can only edit their own post. Authentication happens only once (at login) and maintains state, while authorization happens multiple times (everytime a protected resource is accessed) and it checks current permissions. 

> In Django, it implements authentication using a layered system, it has User Model (user credentials and profile data in the database), Authentication Backends (it handle the actual credential verification process like password hashing, database lookups), Sessions Framework (it maintains user login state across HTTP requests using session cookies), Middleware (it automatically attaches the current user to every request), and also it has Built-in Views/Forms that has login/logout functionality we can use right away.

> Meanwhile for authorization, Django does it through a permission-based system, it has Permission Model (stores individual permissions), Groups System (it allows grouping permissions together for easier management), User-Permission Relationships (links users to permissions), Decorators/Mixins (it provide easy ways to check permissions before executing view logic), and lastly Template Tags (which enable permission checking within templates).

3. What are the benefits and drawbacks of using sessions and cookies in storing the state of a web application?
> Sessions's benefits: Sensitive data stays on the server, only session ID is sent to client so it's more secure. It can store large amounts of data without size limitations. It has built-in timeout mechanisms for better security.
> Session's drawbacks: Consumes server memory/storage, so it's more expensive in resources. If session store fails, all user states are lost. It also has load balancing complexity (since it will use shared storage across servers).
> Cookies' benefits: No server storage. Can survive server restarts and browser sessions. Faster access since data is local
> Cookies' drawbacks: Maximum 4KB per cookie, 20-50 cookies per domain (size is limited). Security risk is higher. Sent with every HTTP request, increasing payload.

4. In web development, is the usage of cookies secure by default, or is there any potential risk that we should be aware of? How does Django handle this problem?
> No, cookies are not secure by default since it can have cybersecurity attacks such as XSS, hijacking, cookie tampering, etc. Django tries to handle this problem though, one of them is by using CSRF protection. It includes CSRF tokens in forms by default, then it validates tokens on POST requests. It also uses double-submit cookie pattern. The web creator can edit the security settings to increase or decrease the security used for the website.

5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).
a. Implementing register, login, and logout functions that allow user to access the application based on their login/logout status.
> To do this, I just open views.py and import the modules that I need, then I put the functions that I need for register, login, and logout in views.py. I made a new html file in the templates for the website, connect the routing to urls,py and path url. This is also the same for login and logout, since I also made a html then do the routing to urls.py and path url.

b. Create two (2) user accounts each having three (3) dummy datas of the models that was previously made for each account in local.
> For this, I simply open the website then create 2 user accounts with the name and password that I wanted, then I made 3 dummy datas which are the products in the website for each account (so the total is 6 products). I got the information for the products through google pictures.

c. Connect the Product model with the User model.
> To do this, I open the models.py then import User from django.contrib.auth.models. Then I add the user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) in my Product class which connects one product to the user. Then I do makemigration and migrate. Then I open views.py and modify the functions that I used (create_product and show_main) to add the user field there. 

d. Show the logged in user's detailed information such as username, as well as implement cookies such as last_login on the application's home page.
> To do this, I added the last_login to if form.is_valid and using the import datetime to get the current date and time when I logged in. Then I use cookies in request to get the last_login key. Also, I edited the logout_user to delete the last_login cookie after logging out, so that it will be updated. Then I edit the html file so that it shows the information in the website.

--------------------------------------------------
Assignment 5 : Web Design using HTML, CSS and CSS Framework

1. CSS Selector Priority: If multiple CSS selectors target an HTML element, explain the priority order for CSS selector selection

It is based off the priorities (highest order wins):
    1. Origin & Importance (Author > User > User agent)
    2. Selector Specificity (Inline styles (anything inside a style tag) > ID selectors > Classes selector > Element selector)
    3. Order of Appearance
    4. Initial & Inherited Properties

2. Responsive Design:

a. Why is responsive design important in web application development?
Responsive design ensures that a website or web application adapts to different screen sizes and devices, it improves user experience, makes the app usable across devices, cost efficient.

b. Provide examples of applications that have and haven't implemented responsive design
Have implemented: applications like twitter or instagram can be used on mobile website and pc/laptop website
Haven't implemented: old websites like old university websites that hasnt implemented it

c. Explain the reasons behind your examples
Twitter or instagram focuses on modern web practices and mobile-first design because they need to keep users engaged, so user response is very needed. Meanwhile for old websites that barely need any user responses like old university websites doesn't really need user responses, so a lot of them doesn't update their website to include one.

3. Box Model: Explain the differences between margin, border, and padding, and how to implement them

Margin: The space outside the border of an element, this doesn't have a background color, and it's used to create spacing between elements.

Border: The line between margin and padding around the element, it outlines the element and can have style, color, and thickness. It's used to highlight or visually separate elements.

Padding: The space between the content and the border. It pushes the content inward, increasing space inside the element. Can have background colors. It's used to add spacing around text/images inside a box.

4. Layout Systems: Explain the concepts of flexbox and grid layout along with their uses

Flexbox: one dimensional, great for smaller UI elements (like either a single row or column). Works from a flex container (display: flex) that controls flex items inside it. One of the uses is for navigation bars.
Grid: two dimensional, perfect for full layouts with both rows and columns. Works with a grid container (display: grid) and grid items placed in defined cells. Few of the uses is for full page layouts, photo galleries, etc.

5. Implementation Steps: Explain how you implemented the above checklist step-by-step (not just following the tutorial)

a. Implement functions to delete and edit products
I use tailwind for the customizations. First of all, add tailwind in base.html so that it will connect to the django. Then in the views.py I added edit_product function so we can edit the products. I also added a delete product function there. Then I made a new html file edit_product.html so the user can edit the product at that page. Also editing the main.html so that it uses the delete button so user can delete. Then I made the routing to urls.py and urlpatterns so that the page is connected to the html and the functions that we created.

e. Navigation Bar (this first before the others)
I made a new html file called navbar.html then I linked it to the main.html. Then I added global.css so I can style it with tailwind (after changing settings.py to static). Then I added custom styling then I style my navigation bar.

b. Page Customization
I styled the login page, register page, add product page, edit product page, and product detail page by changing the each respective html that the page uses to use form-style, colors, center allignment, etc.

c. Product List Page
I styled the product list page so that when there is no product, it will show a text that says that there is no product there. We do this by modifying the main.html, and also added the card_products to the main.html so that the users will see each products using the product cards (so that it'll look more neat)

d. Product Cards
I styled the product cards by making a new card_product.html then I edited the main.html to include the card_product.html. Then on the html I edited it from the one in the tutorial so that the views count and creation date appears on the top, and removed one of the margin so that it looks more clean. Also I replaced the color to appear darker. It's also connected with the edit button and delete button by referencing the url html from edit and delete to the card_product.html.

-------------------------------------------------------------------------------------------------
Assignment 6:

1. What is the difference between synchronous and asynchronous request?
A synchronous request is blocking. When your browser sends a synchronous request, it freezes and waits for the server's response before you can do anything else. It's like being on a phone call where you can't do anything else until the call is over. An asynchronous request is non-blocking. Your browser sends the request in the background and continues to work. You can keep interacting with the page while waiting for the server's response. It's like sending a text message; you can go about your day and will be notified when a reply comes in.


2. How does AJAX work in Django (request–response flow)?
AJAX (Asynchronous JavaScript and XML) allows a web page to communicate with a server without reloading the entire page. Basically:
Trigger: An event on the webpage (like a button click) triggers a JavaScript function.
Request: The JavaScript function creates and sends an asynchronous HTTP request (using fetch() or XMLHttpRequest) to a specific URL in your Django project.
Django View: A dedicated Django view function handles this incoming request. It processes the data, interacts with the database, and prepares a response.
Response: Instead of rendering a full HTML template, the view typically returns data in a lightweight format like JSON using Django's JsonResponse.
Update: The JavaScript on the client-side receives the JSON data and uses it to dynamically update a specific part of the page's HTML (the DOM) without a full page refresh.

3. What are the advantages of using AJAX compared to regular rendering in Django?
Improved User Experience: The page doesn't go blank and reload for every small interaction, making the website feel faster, smoother, and more like a desktop application.
Reduced Server Load: Only small amounts of data (like JSON) are transferred instead of entire HTML pages, which reduces the processing load on the server.
More Responsiveness: Users get instant feedback for their actions (seeing a "like" count increase immediately) because the updates happen in the background.

4. How do you ensure security when using AJAX for Login and Register features in Django?
Some of them are:
CSRF Protection: Django's built-in Cross-Site Request Forgery protection works with AJAX. You must include the CSRF token in the headers of your AJAX request.
Using HTTPS: Always serve your login and registration pages over HTTPS (SSL/TLS) to encrypt the username and password data being sent between the client and server.

5. How does AJAX affect user experience (UX) on websites?
AJAX enhances user experience by making websites feel more dynamic, responsive, and interactive. It eliminates the "stop-and-wait" experience of full page reloads. Actions like submitting comments, voting on a post, or adding an item to a cart happen instantly without interrupting the user's flow. It also has real time update.

