# Gwent

This project is a Gwent game developped in Python for the back-end and VueJS for the front-end.

## How to use

To launch this project, you can either launch the back-end and the front-end or just the back-end, as we have a live version of the front-end running polling your localhost server.

#### Back-end

To launch the backend, we need first to create a virtualenv and install the requirements once :

```
$ cd back/
$ virtualenv --python=python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Then to launch it everytime :

```
$ cd back/
$ source venv/bin/activate
(venv) $ python run.py
```

#### Front-end

The front-end is developped in VueJS and needs Node to run. If you don't want to launch the local front-end, you can access a deployed one at [https://gwent-pooa.netlify.com/](https://gwent-pooa.netlify.com/).

To launch the front, we need first to install the requirements once :

```
$ cd front/
$ npm install
```

Then to launch it everytime :

```
$ cd front/
$ npm run serve
```

#### Pycharm configuration

In this project, Pycharm is already configured with the right run configurations : the backend and
the frontend ones.

