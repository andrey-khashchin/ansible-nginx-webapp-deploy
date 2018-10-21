# Ansible Nginx Webapp Deploy

Ansible playbook with 2 included roles. The main goal is to get Nginx server to be deployed as a reverse proxy in front of Python web 
application for showing system information. SSL communication is implemented based on self-signed certificate, all traffic forwarded
from http to https). Web application is using UWSGI application server container with configured service management (supervisord)

### Dependencies

Ubuntu Linux box should be provisioned and Ansible is already installed

### Deployment

- Clone this repository to your home directory:

```
$ https://github.com/andrey-khashchin/ansible-nginx-webapp-deploy.git
```

- Change directory to cloned repository:

```
$ cd ansible-nginx-webapp-deploy
```

- Run playbook with following parameters:

```
$ ansible-playbook -i hosts ansible-nginx-webapp-deploy.yml --tags all
```
