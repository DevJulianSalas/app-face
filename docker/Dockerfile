
# Docker file to install flask and gunicorn
FROM python:2.7
RUN echo "Creating image"
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y \
   gcc \
   python-dev python-distribute \
   python-pip \
   python-dev \
   python-distribute python-pip
RUN groupadd -r develop && useradd -r -g develop develop
COPY cmd.sh /opt
RUN mkdir /opt/appWeb/
COPY requirements.txt /opt
RUN pip install -r /opt/requirements.txt
WORKDIR /opt/appWeb/
RUN pwd
COPY  /scripts /opt/appWeb/
USER develop
CMD ["/opt/cmd.sh"]
