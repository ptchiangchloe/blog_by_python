# Blog By Python & Django

This is a simple blogging app built by python and django.

## Getting Started

1. Set up your local git environment.
2. Download the repository into your local machine.

```
git clone https://github.com/ptchiangchloe/blog_by_python.git
```

### Prerequisites

Use python 2 instead of python 3 in this project. Mac has built-in python2

Windows users can see this page
https://www.python.org/download/releases/2.7/

### Installing

 step1:

 For Mac users
 ```
 sudo pip install pip
 ```
 For windows users
 ```
 pip install pip
 ```

 step2:

 Create a virtual environment inside of your project folder.

 ```
 pip install virtualenv
 ```
 If you have installed virtual environment, make sure your environment is up to date.
 ```
 pip install virtualenv --upgrade
 mkdir my_project
 cd my_project
 virtualenv .
 ```

Activate your virtual environment

For Mac users:

```
source bin/activate
```

For windows users:

```
.\Scripts\activate
```

Once you get into the virtual environment, you can check the packages you have.

```
pip freeze
```

- Install [Django 1.9 version](https://www.djangoproject.com/download/)

```
pip install django==1.9
pip install pillow
```

 There are just slight difference between 1.8 and 1.9. Because 1.8 is a long term support version.

 For more information, please check https://www.djangoproject.com/download/

 # Create a super user

 - In you virtual environment, you should create a super user under the src directory.

 ```
  python manage.py createsuperuser
```

- Start the server
```
  python manage.py runserver
```

<!-- ```
Give the example
```

And repeat

```
until finished
``` -->

<!-- ## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
``` -->

<!-- ### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc -->
