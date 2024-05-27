# Build Server Instructions
## Migrate the models to the database using the following commands:
- ``` python manage.py makemigrations ```
- ``` python manage.py migrate ```

## Create the super user using the following command: 
- ``` python manage.py createsuperuser ```

## Run the build server using the following command:
- ``` python manage.py runserver ```

## Open the following link and log in with the credentials created:
- http://127.0.0.1:8000/admin
