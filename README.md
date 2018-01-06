[![Build Status](https://travis-ci.org/jamesperes/EC.svg?branch=master)](https://travis-ci.org/jamesperes/EC)

# EC
Project OpenSource for manage students in English College.

The project is based on the rules of language schools in Ireland and used to show student information during the course.

**For students:**
- See test rates
- Follow school attendances
- Receive documents, videos and Links from teachers
- Follow nexts events in school

**For teachers:**
- To plan classes lessons, with videos, links and documents
- To manage the performed tests, giving notes to each student
- To manage the students attendances
- Notify student by emails
- Disclose supplementary events for school

**For Coordinators:**
- To manage student, teachers and users
- To create class rooms, assigning students, teachers

## Entities:

- Student
- Teacher
- Coordinators
- Class Rooms:
  - Number
  - Level
  - Morning / afternoon
  - Many Students
  - Many Teachers
- Classes
  - Class Room
  - Date
  - Lessons
  - Videos
  - Documents
  - Students attendances < Class Room
- Tests
  - Class room
  - Date
  - Type
  - Grade test for each students < Class room
  - Students attendance on the test < Class Room

## Running local server

### Requeriments

   - Python 3
   - Django 2

### Install VirtualEnv

```sh
$ virtualenv --python=python3 venv
$ source venv/bin/Activate
```

### For install Requeriments

```sh
$ pip install -r req_dev.txt
$ python manage.py migrate
$ python manage.py test
```


### For run Server
```sh
$ python manage.py runserver
```

### Access to django-admin

login: admin@admin.com

password: admin123


### Warm up development's environment by docker compose
```sh
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```
*P.s: S.O other than debian look at [here](https://docs.docker.com/compose/install/)*

```sh
cd provision/compose
sudo docker-compose build --no-cache
sudo docker-compose up -d
```

### Warm up development's environment by docker
```sh
sudo apt-get remove docker docker-engine docker.io
sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable"
sudo apt-get update && sudo apt-get install docker-ce
```
*P.s: S.O other than debian look at [here](https://docs.docker.com/engine/installation/)*
```sh
cd provision/docker
sudo docker build -t ec_app -f Dockerfile
sudo docker run -p 8080:8080 -it ec_app
```

## To debug and logs
```sh
sudo docker exec -it <container's id> /bin/bash
sudo docker logs -f --tail=100 <container's id>
```



## Authors

* **James Peres** - *Initial work* - [jamesperes](https://github.com/jamesperes)
* **Samuel Sampaio** - *Initial work* - [samukasmk](https://github.com/samukasmk)
* **Werberth Vinícius** - *Initial work* - [werberth](https://github.com/werberth)

See also the list of [contributors](https://github.com/jamesperes/EC/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
