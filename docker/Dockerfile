
# Docker file to install flask and gunicorn
# Anotation,  run as root if you don't have your user normal in the file sudoers,
#otherwise run docker as normal user.
FROM python:2.7
RUN echo "Creating image"
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y \
   gcc \
   python-dev python-distribute \
   python-pip \
   python-dev \
   python-distribute python-pip
# Add new user by security, the container don't execute as root and add group to
#execute anywhere commands as sudo.

RUN groupadd -r develop && useradd -p develop -r -g develop develop
RUN adduser develop sudo
RUN echo ' %sudo   ALL=(ALL:ALL) ALL' >> /etc/sudoers

# Give permissions of users by folders
RUN chmod 700 /opt/
RUN chown -R develop /opt/


#Create workdirectory and copy pip requirements.txt
RUN mkdir /opt/appWeb/
COPY requirements.txt /opt
RUN pip install -r /opt/requirements.txt
WORKDIR /opt/appWeb/
COPY  /scripts /opt/appWeb/

#Copy files .bash to execute and give permissions
COPY cmd.sh /opt
RUN chmod +x /opt/cmd.sh

#Execute file .bash to automation install packages

CMD ["/opt/cmd.sh"]
