FROM python:3.9

# Check Versions
#RUN apt-get -y update

# Set a working directory inside the container 
WORKDIR /app

# Check Python and Pip version
RUN python3 --version
RUN pip3 --version

# Copy requirements.txt
COPY requirements.txt .

# Copy 
COPY ./src /app

# Install Python Packagee Dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]