FROM williambutcherbot/python:latest

WORKDIR /wbb
RUN chmod 777 /wbb

# Installing Requirements
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copying All Source
COPY . .

# If u don't want to use /update feature, comment the following and edit
RUN python3 gitconfig.py

# Starting Bot
CMD ["python3", "-m", "wbb"]
