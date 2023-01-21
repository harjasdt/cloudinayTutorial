# Step 1: Setting up the Development Environment

## Checking if Python is installed
```bash
  >python --version
```

```bash
  >pip --version
```
## Installing Virtual Environment
```bash
  >pip install virtualenv
```

```bash
  >virtualenv --version
```

## Creating a New Directory
```bash
  >mkdir cloud
```

Navigate inside the cloud Directory
```bash
  >cd cloud
```
## Creating a Virtual Environment
```bash
  >virtualenv env
```
You should see a self generated folder named "env" inside cloud
## Activating our Virtual Environment
```bash
  >env\Scripts\activate
```
Now you should see name of your virtual environment at the starting of each line
```bash
  (env) PS D:\ATOMPROJECTS\cloud> 
```

To exit your virtual environment just use the deactivate command and environment name will disappear
```bash
  >deactivate
```

## Finally Installing Django

```bash
  >pip install django
```

To Create a new project use the following command inside the cloud directory
```bash
  >django startproject cloudinaryTutorial
```
Now you should see a new directory named cloudinaryTutorial(project name) inside cloud directory.


```bash
  >cd cloudinaryTutorial
```

Create a new app after entering your project directory named cloudy

```bash
  >python manage.py startapp cloudy
```

# Step 2: Configuring our cloudinaryTutorial project

## Settings.py 
1. Navigate to settings.py which is located at cloud>cloudinaryTutorial>cloudinaryTutorial>settings.py

```bash
  python manage.py startapp cloudy
```
 
At the time of writing, it is Python 3.9.7. You might have a different version from mine, and that’s fine. As long as you see the Python version logged, Python is installed on your system.

Now that you’ve confirmed Python is installed on your system, you will upgrade pip.
## Step 3  - Creating a Project Directory
