# 💼 cv-maker

## Requirements

- Python: [Downloads](https://www.python.org/downloads/) |
  [Install Guide for MacOS](https://stackoverflow.com/a/71657414/2030184)

## How to run

1. _clone the project and change the directory_
   ```
   git clone https://github.com/ioprodz/cv-maker
   cd cv-maker
   ```
2. _create virtual environment for the project_
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. _Install the required libraries_
   ```
   pip install -r requirements.txt
   ```
4. _MIGRATE & RUN_

   ```
   python manage.py migrate
   python manage.py runserver
   ```

5. Create a super user
   ```
   python manage.py createsuperuser
   ```
