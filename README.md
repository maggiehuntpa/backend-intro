# backend-intro

Hello!

Welcome to the exercises for our Back-End Programming Crash-Course.

You will find here two folders, one for each exercise:

1. Flask App
2. API Call

## To do:
- Sign up to (or log in to) [Github] (https://github.com/)
- Ensure you have [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) set up
- Clone this repository - git clone git@github.com:maggiehuntpa/backend-intro.git
- Create your own branch - [instructions here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)
- Have a play around!

## Task Instructions:

### 1. Flask App
Flask is a framework for developing web applications using a Python backend, linking your Python code with your front-end files. Read about it [here](https://flask.palletsprojects.com/en/2.3.x/).

Install it on your computer using pip (unless using [Cloudshell](https://cloud.google.com/shell) )

Import it into your code like so:
`from flask import Flask, request, render_template`

Your directories should be structured as follows:
- app.py
- static/
    - css/
    - images/
    - js/
- templates/
    - Index.html

Ensure :
- Your html includes a form `<form>` using `method=”POST”` - you can borrow elements from [Bootstrap](https://getbootstrap.com/docs/4.0/components/forms/)
- Each element (e.g. `‘num1’`) has a name as well as an id (e.g. name=”num1”)
- The `‘results’` box uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/api/#basics) notation - double curly brackets `{{ }}` 

### 2. API Call

Convert the amount from one currency to another!

Every API call must include a ‘request body’ (the information sent when the API is contacted, so it knows what to return) and a ‘response body’ (the information received in response to the request).

Write some python code which converts some currency using [this API](https://rapidapi.com/natkapral/api/currency-converter5/)

Have a play with extracting what you get as a response and returning it as a result!

You will need to sign up for the API first, and add this to the top of your code:
```
import requests
import json
```
