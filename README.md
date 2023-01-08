# bubu-itter
bubu-itter is a social media platform built using Django.

## installation
To install bubu-itter, follow these steps:

1.Create a virtual environment for your project using virtualenv or conda. This will allow you to isolate the dependencies of your project from other packages on your system.

### using venv
python3 -m venv env

source env/bin/activate

### using poetry
poetry create bubu-itter

poetry shell



2.Install Django and Pillow using pip. Pillow is a library for handling images and is required for image uploads in bubu-itter.

pip install django
pip install pillow


3.Clone the bubu-itter repository from GitHub.

git clone https://github.com/JonassousaDev/Bubu-itter

4.Navigate to the bubu-itter directory and run the migrations to set up the database.

cd bubu-itter
python manage.py migrate

5.Create a superuser to access the Django admin site.

python manage.py createsuperuser

6.Run the development server to start the application.

python manage.py runserver

7.Open your browser and visit http://127.0.0.1:8000/ to view the bubu-itter app.
