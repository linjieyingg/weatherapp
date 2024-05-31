# Rain Rain Go Away 

## Project Description

This site shows the daily and hourly weather forecast for today and the next 2 days (due to API free subscription restrictions) for the location that is searched in the home page. 

## The Cruisers
#### Jieying Lin
- Email: jlin41@stuy.edu
- GitHub Username: linjieyingg

#### Hui Wen Weng
- Email: hweng40@stuy.edu
- GitHub Username: HuiWenWeng

#### Xinyi Ruan
- Email: xruan40@stuy.edu
- GitHub Username: xruan40

## API used in this project
WeatherAPI.com: https://rapidapi.com/weatherapi/api/weatherapi-com

## Project Launch Code
In order to access this project, following these directions:

#### Clone the project
1. Open up the project on GitHub 
2. Under <> Code then SSH, copy the URL
3. In your terminal, enter `git clone [copied_url]`
4. Open up the project in your preferred IDE

#### Set Up Python Environment
1. Make sure you're inside the project folder
2. `pyenv local 3.11.5`
3. `python -m venv env_3.11.5`
4. `source env_3.11.5/bin/activate`

#### Set Up Environment Packages
The modules you need are nodeenv, django, django-extensions, django_vite, pgadmin4, jupyter, jupyterlab, pandas, numpy, matplotlib
1. You can choose to use `pip install [module name]` to install your modules individually
2. OR type django and django_vite in a file called `main.in` and the rest of the modules in a file called `dev.in` in a requirements_env/ folder and use the following code
   ```
   pip install --upgrade pip-tools pip setuptools wheel
   pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
   pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in  
   pip-sync requirements_env/main.txt requirements_env/dev.txt
   ```

#### Set Up Node Environment
1. You should have nodeenv already installed if you followed the launch code in order
2. Install node.js version 20.11.1: `nodeenv --node=20.11.1 --prebuilt env_node_20.11.1`
3. Deactivate your python environment: `deactivate`
4. Activate your node environment: `source env_node_20.11.1/bin/activate`

#### Set Up Node Environment
1. On the same level as your python environment

#### Connecting to Local Database
1. Locate the file called `secrets_template.json` in the `project_folder/final/` directory
2. Make a copy of the file and name it to `secrets.json`
3. Replace the data with information about your own database
   
   ```
   {
    "environment": "development",
    "movie_theater_url": "http://localhost:8000",
    "database_name": "[db_name]",
    "database_user": "[db_username]",
    "database_pwd": "[db_pwd]",
    "database_host": "localhost",
    "database_port": "5432"
    "vite_dev_server_port": "5173"
   }
   ```

#### Running the Project
1. Move into the directory on the same level as the file `manage.py`
2. Make sure you migrate your changes before running anything with the command `python manage.py makemigrations` then `python manage.py migrate`
3. Run the command `python manage.py runserver`
4. In another terminal window, make sure your node environment is activate and then run `npm install` and `npm run dev` to run the Vue.js side of the project
5. Open `http://127.0.0.1:8000/` in your browser
6. Read the instructions on the homepage to get started
