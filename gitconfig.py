from dotenv import load_dotenv
from os import environ,path,system
if path.exists("config.env"):
    load_dotenv("config.env")

GIT_EMAIL = environ.get("GIT_EMAIL", "nezuko@demon.org")
GIT_USERNAME = environ.get("GIT_USERNAME", 'nezuko')

system("git config --global user.email " + GIT_EMAIL)
system("git config --global user.name " + GIT_USERNAME)
