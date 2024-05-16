pip install --upgrade pip-tools pip setuptools wheel
pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in

# production
pip-sync requirements_env/main.txt

# development
pip-sync requirements_env/main.txt requirements_env/dev.txt