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