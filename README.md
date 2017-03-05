# R-Share
#####This is a Django based file uploader with following features :
  
##Version 1 :-

  - Share via link

  - Share to public repository

  - Sharing with existing user

  - File expiry

  - Option to set password on file

  - Download file from link / public repository
  
##Version 2 :-

  - Completely new look

  - Password is hashed and saved for the new upload files

  - Captcha validation while uploading the files


### Setting up

1. Your machine needs to have django installed. (taken care by install.sh)

2. Clone the repository, unzip and go to the main directory of the repo .

        wget https://github.com/roopansh/rshare/archive/master.zip
        unzip master.zip
        cd rshare-master

3. Run the 'install.sh' 
        
        bash install.sh
        
   Fill all the settings required.

4. In the ``rshare/settings.py`` file, edit the ``ALLOWED_HOSTS`` to the host address you want to host from.
    
**NOTE : Currently every host is allowed**

5. Create the server
        
        python manage.py runserver 0.0.0.0:8000

6. Everything is done. Visit the following link in your browser 
        
        localhost:8000/share
        
**NOTE : Replace localhost with the host address of the pc hosting the site.**

## About the project author
#### Roopansh Bansal
B.Tech undergraduate (Computer Science & Engineering)  
IIT Guwahati  
India  

roopansh.bansal@gmail.com  
www.linkedin.com/in/roopansh-bansal


# ScreenShots

##Version 2 :-

![Home Page](/screenshots/v2/home.png "Main Page")

![Public Repo](/screenshots/v2/public.png "Password")

![Sign In](/screenshots/v2/signin.png "Download")


##Version 1 :-

![Home Page](/screenshots/v1/Home.png "Main Page")

![Upload](/screenshots/v1/Upload.png "Upload")

![Password Protected](/screenshots/v1/Password.png "Password")

![Download](/screenshots/v1/Download.png "Download")
