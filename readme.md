# storyhouse

## Technical Requirements
- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtual environment](https://docs.python.org/3/library/venv.html)


## Getting Started Instructions
 Make sure that your project contains media folder with following paths:
 
- /images


## Installation
Write these commands in terminal

1. create virtual environment

For Windows run:
```sh
py -m pip install --upgrade pip

py -m pip --version

py -m pip install --user virtualenv

py -m venv illustration_env

.\storyHouse_env\Scripts\activate
```


For Unix/macOS run:
```sh
python3 -m pip install --user --upgrade pip

python3 -m pip --version

python3 -m pip install --user virtualenv

python3 -m venv illustration_env

source illustration_env/bin/activate
```

2. Change Directory:
```sh
cd ./illustration/ebookcreatorai/
```

3. Create .env file in root directorary
```
add all the variables with theit key values present in .env.local file
```
4. Install requirements:
```sh
pip install -r requirement.txt
```
5. Run Migrate command:
```sh
python manage.py migrate
```
6. Now you are ready to go:
```sh
python manage.py runserver
```
