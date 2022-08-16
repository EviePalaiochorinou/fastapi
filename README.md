# FastAPI Blogging

A simple Blogging API where users can create articles and post comments.  

This project is made with:  
- Python3
- FastAPI
- SQLAlchemy
- SQLite

This project features:
- Authentication & Authorization (OAuth2)
- BCrypt for password hashing
- Deployment on Heroku
- Testing with Pytest

### View The Project
```sh
https://fastapi-blogging.herokuapp.com/docs 
```
Authenticate with the top right button.  
username: cat  
password: cat  

## Running The Project Locally

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/EviePalaiochorinou/fastapi 
   ```
2. Activate your virtual environment

3. Install the requirements
   ```sh
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```  
   
4. Generate a JWT secret key using following command:
   ```shell script
   openssl rand -hex 32
   ```
   Set the SECRET_KEY variable to your new key it in the ./auth/oauth2.py or add in a new **.env** file from root of this directory.
  
### Usage

- Start the server
  ```sh
  uvicorn main:app --reload
  ```
- View your Swagger UI
  ```sh
  http://127.0.0.1:8000/docs
  ``` 

### Testing

You can run your tests using:
```shell script
pytest -s -v
```

## Future Work

- Complete all CRUD operations for all models
- New display model for the current_user

