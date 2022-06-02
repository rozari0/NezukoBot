FROM rozari0/python:latest

# Install dependencies
RUN pacman -S --noconfirm git wget libxml2 libxslt zip

# Downloading mongodb tools
RUN wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu2004-x86_64-100.5.2.tgz && tar -xf mongodb*.tgz && \ 
  mv mongodb-database-tools-ubuntu2004-x86_64-100.5.2/bin/* /bin/ && \
  rm -rf mongodb-database-tools-ubuntu2004-x86_64-100.5.2*

# Changing working directory and it's permission
WORKDIR /app
RUN chmod 777 /app

# Install python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Copy files to the working directory
COPY . .

# Run the application
CMD ["python3","-m","nezuko"]
