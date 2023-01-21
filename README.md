# How to Use

## Install Python and check the version using
```bash
  >python --version
```

## Clone This Repo

```bash
  git clone https://github.com/harjasdt/cloudinayTutorial.git
```
A cloudinayTutorial Directory will be created(NOTE: Their is a missing r in this repo name)

## Install requirements.txt
Navigate to cloudinayTutorial and install all dependencies by
```bash
  pip install -r requirements.txt
```

## Changing Settings.py 
Create your Cloudinary Account and add the following Authentication keys to settings.py(located at cloudinayTutorial/cloudinaryTutorial Directory)

```bash
cloudinary.config( 
  cloud_name = "YOUR_CLOUD_NAME", 
  api_key = "YOUR_API_KEY", 
  api_secret = "YOUR_API_SECRET" 
)
```

## Running locally
Navigate to cloudinayTutorial

```bash
  python managye.py runserver
```

Go to http://127.0.0.1:8000/ to enjoy your own google cloud locallly


# Host on AWS
First of all go to https://portal.aws.amazon.com/billing/signup#/start/email and Create your AWS Account(will ask for credit card and charge only Rs.2)

## New EC2 Instance
1.Now navigate to EC2 Dashboard and click on Create Instance(Top Right)
2.Select the latest Ubuntu Virtual Machine which is eligible for Free Tier
3.Generate a new Key-Pair Token 

## Connect to your EC2 Instance
It will take some time to get the instance running at first, there are 2 ways of connecting to your instance.
1.Connecting using Browser>
Select the instance and click on connect

2.Connecting using GitBash and Key-Pair Token
Open GitBash, navigate to the location of you r saved token and enter>
```bash
  ssh -i <YOUR .pem Token> ubuntu@<YOUR PUBLIC IP>
```
## VM Setup
Directory setup and cloning code:-

```bash
  mkdir project
  cd project
  git clone https://github.com/harjasdt/cloudinayTutorial.git
```

A project directory will be created having cloudinayTutorial Directory inside it(NOTE: Their is a missing r in this repo name)

## Changing Settings.py 
Create your Cloudinary Account and add the following Authentication keys to settings.py(located at project/cloudinayTutorial/cloudinaryTutorial Directory)

```bash
  sudo nano  project/cloudinayTutorial/cloudinaryTutorial/settings.py
```

```bash
cloudinary.config( 
  cloud_name = "YOUR_CLOUD_NAME", 
  api_key = "YOUR_API_KEY", 
  api_secret = "YOUR_API_SECRET" 
)
```

## Install Install... 
```bash
  sudo apt update
  sudo apt install python3-pip python3-dev nginx curl
  sudo -H pip3 install --upgrade pip
  sudo -H pip3 install virtualenv
```

## Creating Virtual Environment
Navigate to project directory and run

```bash
  virtualenv myprojectenv
  source myprojectenv/bin/activate
  pip install gunicorn 
  pip install -r requirements.txt
```

## Giving Permissions
To avoide future errors due to lack of permissions run 

```bash
  sudo ufw allow 8000
  sudo chmod 777 /home/ubuntu/project/cloudinayTutorial -R
```

## Gunicorn Configs
```bash
  gunicorn --bind 0.0.0.0:8000 cloudinaryTutorial.wsgi
```
Now you can deactivate your venv

## Creating systemd Socket and Service Files for Gunicorn

```bash
  sudo nano /etc/systemd/system/gunicorn.socket
```
Populate this with>
```bash
  [Unit]
  Description=gunicorn socket

  [Socket]
  ListenStream=/run/gunicorn.sock

  [Install]
  WantedBy=sockets.target
```


```bash
  sudo nano /etc/systemd/system/gunicorn.service
```
Populate this with>
```bash
  [Unit]
  Description=gunicorn daemon
  Requires=gunicorn.socket
  After=network.target

  [Service]
  User=ubuntu 
  Group=www-data
  WorkingDirectory=/home/ubuntu/cloudinayTutorial <MIND THE R>
  ExecStart=/home/samubuntu/project/myprojectenv/bin/gunicorn \
            --access-logfile - \
            --workers 3 \
            --bind unix:/run/gunicorn.sock \
            cloudinaryTutorial.wsgi:application

  [Install]
  WantedBy=multi-user.target
```

```bash
  sudo systemctl start gunicorn.socket
  sudo systemctl enable gunicorn.socket
  sudo systemctl daemon-reload
  sudo systemctl restart gunicorn
```

## Configure Nginx to Proxy Pass to Gunicorn

```bash
  sudo nano /etc/nginx/sites-available/myproject
```

Populae this with>

```bash
  server {
    listen 80;
    server_name <server_domain_or_IP>;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
```bash
  sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
  sudo systemctl restart nginx
  sudo ufw delete allow 8000
  sudo ufw allow 'Nginx Full'
```

This completes ouw AWS Hosting. Your can refer https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04 for any errors.






