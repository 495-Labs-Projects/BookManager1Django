# Book Manager

This is just a recreation of the Ruby on Rails version of the Book Manager lab part 1 in Django. 

For more information of how you should set up Django, look at the [DjangoNotes](https://github.com/495-Labs-Projects/DjangoNotes)

#### Install requirements

First make sure you have Python >= 3.4 and then you need to install all the project requirements:

```
$ pip install -r requirements
```

More info on installing requirements [here](https://github.com/495-Labs-Projects/DjangoNotes/blob/master/PythonRequirements.md)

#### Running the application

To run the application run the following command at the root of the project:

```
$ manage.py runserver
```

If any migration errors come up, run the following before starting up the server:

```
$ manage.py migrate
```

More info on running Django apps go [here](https://github.com/495-Labs-Projects/DjangoNotes/blob/master/DjangoApps.md)

#### Running tests

To run all of the tests make sure you have a webdriver installed in order for Selenium functional tests to run. Go [here](https://github.com/495-Labs-Projects/DjangoNotes/blob/master/TestingDjangoApps.md) for instructions on how to do so.

If you just want to run all tests:

```
$ manage.py test
```

If you just want to run the unit tests:

```
$ manage.py test books.tests.test_models
$ manage.py test books.tests.test_views
```

If you want to run the functional tests:

```
$ manage.py test books.tests.test_functional
```
