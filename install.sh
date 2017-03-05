# installing django
sudo apt-get update
sudo apt-get install python3 python3-setuptools
sudo apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev python3-dev
sudo pip3 install django

# installing the reuired libraries
sudo pip3 install --upgrade passlib django-simple-captcha django-crispy-forms

# setting up the server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser

echo -e "Use \e[7mpython3 manage.py runserver <host>:<port>\e[0m to run the server"