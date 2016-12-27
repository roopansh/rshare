# R-Share
#####This is a Django based file uploader with following features :
  
  - Share via link

  - Share to public repository

  - Sharing with existing user

  - File expiry

  - Option to set password on file

  - Download file from link / public repository
  
### Setting up

1. Your machine needs to have django installed

2. Clone the repository, unzip and go to the main directory of the repo .

        wget https://github.com/roopansh/rshare/archive/master.zip
        unzip master.zip
        cd rshare-master

3. Create a super user to manage the server 
        
        python manage.py createsuperuser
        
   Fill all the settings required.

4. In the ``rshare/settings.py`` file, edit the ``ALLOWED_HOSTS`` to the host address you want to host from.
    
**NOTE : Currently every host is allowed**

5. Create the server
        
        python manage.py runserver 0.0.0.0:8000

6. Everything is done.



## About the project author
#### Roopansh Bansal
B.Tech undergraduate (Computer Science & Engineering)  
IIT Guwahati  
India  

roopansh.bansal@gmail.com  
www.linkedin.com/in/roopansh
