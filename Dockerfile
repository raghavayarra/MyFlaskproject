#initialize a base image
FROM  python:3.9-alpine
#define the working directory
WORKDIR ./Flaskproject
#adding docker file
COPY . /Flaskproject
#run pip to install the requirements
RUN pip install -r requirements.txt
#define the command to start the computer
CMD ["python", "main.py"]
