# Todo List
ToDo List App is a kind of app that generally used to maintain our day-to-day tasks or list everything that we have to do, with the most important tasks at the top of the list, and the least important tasks at the bottom. It is helpful in planning our daily schedules.

*Frontend:* HTML, CSS, JavaScript, Jquery <br>
*Backend:* Django  
*Database:* SQLite3 

# Setup
* Download and Install Python 3.9
* Download and Install Git
* Fork the Repository
* Clone the Repository to your local machine, `$ git clone https://github.com/<your-github-username>/todo-list.git`
* Change the directory to Jagrati, `$ cd todo-list`
* Install virtualenv `$ pip install virtualenv`
* Create a virtual environment `$ virtualenv env`  
* Activate the environment: `env\Scripts\activate`
* Install the requirements: `$ pip install -r requirements.txt`
* Make migrations `$ python manage.py makemigrations`
* Migrate the changes to the database `$ python manage.py migrate`
* Create admin Using `$ python manage.py createsuperuser`
* Run the server `$ python manage.py runserver`
* Go to `127.0.0.1:8000`
