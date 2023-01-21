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

Go to http://127.0.0.1:8000/ to enjoy your own google cloud
