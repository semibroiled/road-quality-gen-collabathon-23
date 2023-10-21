FROM --platform=linux/x86_64 python:3.9
# Check Versions
RUN apt-get -y update
RUN python3 --version
RUN pip3 --version

###install all the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY ./src .