import os
import subprocess

UPSTREAM_REPO = os.environ.get('UPSTREAM_REPO', "https://github.com/rozari0/NezukoBot.git")
try:
    if len(UPSTREAM_REPO) == 0:
       raise TypeError
except TypeError:
    UPSTREAM_REPO = None

if UPSTREAM_REPO is not None:
    if os.path.exists('.git'):
        subprocess.run(["rm", "-rf", ".git"])

    subprocess.run([f"git init -q \
                      && git config --global user.email nezuko@demonslayer.corp \
                      && git config --global user.name nezuko \
                      && git add . \
                      && git commit -sm update -q \
                      && git remote add origin {UPSTREAM_REPO} \
                      && git fetch origin -q \
                      && git reset --hard origin/master -q"], shell=True)

