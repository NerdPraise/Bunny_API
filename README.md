# Bunny Service architecture
A microservice model of a simple RESTful API for managing todo actions for Bunny Limited

### Requirements :
```
python == 3.9.1
Django >= 3.0.0
```
 
API References
### Usage
1. Clone project
2. Create .env file and add a key value pair with the key DJANGO_SECRET_KEY `DJANGO_SECRET_KEY="soome value"`
3. Run `python -m venv venv` to create a virtual environment
4. Run `pip install -r requirements.txt` to install all the necessary required packages
5. Run `python manage.py runserver` to start server and follow code snippet
6. Using any request simulator of your choice, perform the following actions
```python
base_url = 'http://localhost:8000/v1/'
routes = [
'users/' # Get all users
'user/create/' # Create a user
'user/<int:user_id>' # Retrieve, update or delete users by Id 
'user/profile' # Get current logged in user detail
'task/<int:user_id>/' # Create task, List task by user
'tasks/<int:task_id>' # Retrieve update, delete task 
'auth/login/' # log in using JWT
  ]
```
### Authentication
This project uses JWT for authentication. 
To authenticate a request, the steps listed below
1. Create a user using the routes above. Format should be
```json
{
    "username":"<username>",
    "password":"<password>"
}
```
2. Send a post request to `auth/login/` using the same format as above
3. A POST request to the route would give a response in the format
```json
{
    "access":"<some long list of characters>",
    "refresh":"<some long list of characters>"
}
```
4. Set the access key in your header as `{'Authorization':'Bearer <access>}` for every request



<!-- ##### NB: This project was made with some assumptions in mind  -->
