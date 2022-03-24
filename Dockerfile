#python 3.8 is the base image for the build
FROM python:3.8-slim

#sets the working directory for instructions that follow
WORKDIR /factorial-digits

#install numpy library for the python script
RUN pip install numpy

#copy files and adds them to the file system of the image in the path
COPY factorial-digits.py .

#used to set executables that will always run when the container is initiated
ENTRYPOINT ["python" , "factorial-digits.py"]

#if no entry is made, set the executable to 10 (default value)
CMD [ "10" ]