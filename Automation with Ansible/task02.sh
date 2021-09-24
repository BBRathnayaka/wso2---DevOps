# seperate header elements are added for webservers as webserver1 & webserver2
ansible webserver1 -m shell -a "sudo hostnamectl set-hostname lt-2021-070-webserver1"
ansible webserver2 -m shell -a "sudo hostnamectl set-hostname lt-2021-070-webserver2"
