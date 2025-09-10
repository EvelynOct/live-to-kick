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
