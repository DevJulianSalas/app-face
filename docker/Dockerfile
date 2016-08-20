
# Docker file to install flask and gunicorn
FROM python:3.4
RUN echo "Creating image"
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y \
   gcc \
   python-dev python-distribute \
   python-pip \
   python-dev \
   python-distribute python-pip
RUN groupadd -r develop && useradd -r -g develop develop
COPY script_aut/cmd.sh /opt
RUN mkdir /opt/appWeb/
WORKDIR /opt/appWeb/
COPY  appWeb /opt/appWeb/
COPY requirements.txt /opt
RUN pip install -r /opt/requirements.txt
USER develop
RUN echo "$ls"
EXPOSE 5000 5001
CMD ["python", "run.py"]
