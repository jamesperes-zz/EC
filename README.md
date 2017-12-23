[![Build Status](https://travis-ci.org/jamesperes/EC.svg?branch=master)](https://travis-ci.org/jamesperes/EC)

# EC
Project OpenSource for manage students in English College.

The project is based on the rules of language schools in Ireland and used to show student information during the course. e.g

   - Grades
   - Attendance
   - Nexts events in school
   - Receive documents and Links from teachers


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

See also the list of [contributors](https://github.com/jamesperes/EC/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details