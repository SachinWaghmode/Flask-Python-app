FROM python:2.7.13
MAINTAINER Your Name "sachinwaghmode57@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -r pygit.txt  
ENTRYPOINT ["python","app.py"]
CMD [$1]
