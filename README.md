# ediary-hacks

This script file is a set of utility functions that can be used in conjunction with a particular type of [Digital School Diary](https://github.com/devmanorg/e-diary/) to access / modify / delete certain database entries. 

Despite word *hacks* being... uh... mentioned here and there, it does not encourage any illegal activity, and provided toolset should be used only for administrative or educational purposes.

General use cases are covered under **BASIC USAGE** section.

## Setup guidelines

As mentioned above, this toolset was created for a specific type of digital diary, that is built using Django web framework. So in order to use this script, you'll need to have access to a deployed instance of this project, or you may run it localy for testing. The E-Diary project can be found [here](https://github.com/devmanorg/e-diary/). Follow the provided guidelines to start it up on your local machine.

In order to manipulate database entries, you obviously need a database. Unfortunately, you must acquire a valid testing database elsewhere.

Once you have your Django application set up, put the `hacks.py` in the root of the project folder next to `manage.py`. No additional dependencies are required. 

## Basic usage

Easiest way to use this toolset is by running it from Django shell terminal. Learn more about it [here](https://docs.djangoproject.com/en/2.2/ref/django-admin/#shell). You can start it using this command:

```
> py manage.py shell
```

Once new terminal session is initialized, you may enter Python code interactively. You can import functions from `hacks.py` by following line of code:
```Python
>>> from hacks import *
>>>
```

This gives you access to following functions:

### `fix_marks(kid_name)` 
look up the schoolkid by his name in the database, and change all of his marks below 4 to either 4 or 5 for all past lessons.

`kid_name` - is a string parameter, that must represent a name (or part of the name specific enough to find unique identity). If no kid with the given name is found, or if there is more than one entry for specified part of the name - error will be raised and no data will be changed.


### `remove_chastisements(kid_name)`
look up the schoolkid by his name in the database, and remove all associated chastisement entries.


`kid_name` - is a string parameter, that must represent a name (or part of the name specific enough to find unique identity). If no kid with the given name is found, or if there is more than one entry for specified part of the name - error will be raised and no data will be changed.


### `create_commendation(kid_name, subject_title)`
look up the schoolkid by his name in the database, and last lesson he had for provided subject title. Create a new entry in commendation table, that will be associated with the kid, and refer to the last lesson data.

`kid_name` - is a string parameter, that must represent a name (or part of the name specific enough to find unique identity). If no kid with the given name is found, or if there is more than one entry for specified part of the name - error will be raised and no data will be changed.

`subject_title` is a string parameter, that must represent a title of the subject to look up. The exact title of the subject must be provided, otherwise an error will be raised, and no data will be changed.


### Example
Here is how these functions can be used for a kid named `Мешроп Маштоц`, who wants a commendation for his `Математика` lessons.
```Python
>>> from hacks import *
>>> fix_marks('Мешроп Маштоц')
>>> remove_chastisements('Мешроп Маштоц')
>>> create_commendation('Мешроп Маштоц', 'Математика')
```

## Goals

This script was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.