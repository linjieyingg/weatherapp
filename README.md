# Rain Rain Go Away 
Collaborators: Jieying Lin, Hui Wen Weng, Xinyi Ruan

Group Name: The Cruisers

Summary: This site shows the daily and hourly weather forecast for today and the next 2 days (due to API free subscription restrictions) for the location that is searched in the home page. 

API: WeatherAPI.com - https://rapidapi.com/weatherapi/api/weatherapi-com

Launch Codes:
- create virtual env in root folder --> activate virtual env
- build the packages: pip install --upgrade pip-tools pip setuptools wheel pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in
- install the packages: pip-sync requirements_env/main.txt requirements_env/dev.txt
- in the project directory, go to final/secrets_template.json -> copy the code and create file secrets.json and paste the code there and enter in your database information.
- create node env in root folder --> activate
- run (in project_folder/vue-project):
    - npm install
    - npm run dev
- run (in project_folder/final and in another termainal tab):
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
- go onto the server and search for a location
