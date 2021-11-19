FROM williambutcherbot/python:latest

WORKDIR /wbb
RUN chmod 777 /wbb

# Installing Requirements
RUN pip3 install -U pip
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# If u don't want to use /update feature, comment the following and edit
COPY gitconfig.py .
RUN python3 gitconfig.py

# Copying All Source
COPY . .

# Starting Bot
CMD ["python3", "-m", "wbb"]
