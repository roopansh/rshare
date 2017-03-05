# installing django
sudo apt-get update
sudo apt install python3 python3-setuptools
pip3 install django

# installing the reuired libraries
pip3 install passlib
pip3 install django-simple-captcha

# setting up the server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

echo -e "Use \e[7mpython3 manage.py runserver <host>:<port>\e[0m to run the server"