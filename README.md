# backend-intro

Hello!

Welcome to the exercises for our Back-End Programming Crash-Course. These are the two Python exercises to accompany [these slides](https://docs.google.com/presentation/d/1_rxOPxl4PAXPJmTotoqev6pISNESj8-l60yvAa2kCkE/edit?usp=sharing).

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
`pip install Flask`

Import it into your code like so:
`from flask import Flask, request, render_template`

Your directories should be structured as follows:
- app.py
- static/
    - css/  _this folder is for stylesheets (optional)_
    - images/  _this folder is for images (optional)_
    - js/  _this folder is for javascript scripts (optional)_
- templates/
    - index.html

Ensure :
- Your html includes a form `<form>` using `method=”POST”` - you can borrow elements from [Bootstrap](https://getbootstrap.com/docs/4.0/components/forms/)
- Each element (e.g. `‘num1’`) has a name as well as an id (e.g. name=”num1”)
- The `‘results’` box uses [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/api/#basics) notation - double curly brackets `{{ }}` 

Running your Flask App:
- Run your Flask app from the terminal by going into the directory and running the following command:
    `python app.py`
- Click the hyperlink!
- Use `ctrl+c` to end the app running.

Next, have a play around with different mathematical operations. Explore what you you do with strings vs integers. How many fields can you add to the form?

### 2. API Call

Convert the amount from one currency to another!

Every API call must include a ‘request body’ (the information sent when the API is contacted, so it knows what to return) and a ‘response body’ (the information received in response to the request).

Write some python code which converts some currency!

Steps:
- Install the 'requests' library `pip3 install requests`
- Sign up to use [RapidApi] (https://rapidapi.com/)
- Read the documentation for using [this API](https://rapidapi.com/natkapral/api/currency-converter5/)
- Ensure you note your API key = and remember, DO NOT share it online anywhere, or commit it to github! You can find it ocne you have signed up, [here](https://rapidapi.com/natkapral/api/currency-converter5/playground/).
- Look at the code snippet in this repository, or browse the different [code snippets](https://rapidapi.com/natkapral/api/currency-converter5/playground/apiendpoint_b0d109c2-e479-4f70-be68-ab4dbe08cfcf) for other back-end languages (e.g. Java)
- You will need to add this to the top of your Python code:
    ```
    import requests
    import json
    ```
- Have a play with extracting what you get as a response and returning it as a result!

Tasks:
- Make it run!
- Practice changing the `input()` message using [string formatting](https://www.w3schools.com/python/ref_string_format.asp).
- See if you can use `input()` to request the kinds of currency the user is onverting.
- Have a play with adding other calculations and messages.
- HAve a go at formatting the result - e.g. so you don't get the entire JSON, just the number and currency, or a sentence containing the message!


Running your Python programme:
- Run it from the terminal by going into the directory and running the following command:
    `python apicall.py`
- Use `ctrl+c` to end it running.
