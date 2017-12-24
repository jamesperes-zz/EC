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

## Authors

* **James Peres** - *Initial work* - [jamesperes](https://github.com/jamesperes)
* **Samuel Sampaio** - *Initial work* - [samukasmk](https://github.com/samukasmk)
* **Werberth Vinícius** - *Initial work* - [werberth](https://github.com/werberth)

See also the list of [contributors](https://github.com/jamesperes/EC/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
