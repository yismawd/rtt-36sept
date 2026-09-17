#how to protect your passwords
Create a .env file and put your passwords in it as a variables
Add .env file to your .gitignore so that it doesnt get pushed to github
Enable env variables by installing library to env
pip install python-dotenv
In files that need private passwords/api keys
from dotenv import load_env
import os
load_env()
password = os.getenv(password)
