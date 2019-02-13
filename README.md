# be-coding-challenge

### Expectations

- We do not expect you to completely finish the challenge. We ask that candidates spend 4 hours or more working through the challenge. With that we understand that everyones schedule and availability is different so we ask that you provide a reasonable estimate of your time commitment so we can take it into account when evaluating your submission.
- We expect you to leverage creative license where it makes sense. If you'd like to change the project structure, pull in libraries, or make assumptions about the requirements we openly encourage you to do so. All that we ask is that you are prepared to talk about your choices in future interviews.

### Challenge

For this challenge you will be implementing a family tree API.

The API should be capable of keeping track of people and the connections between them.

While you have full control to model the entities as you see fit you should keep the following guidelines in mind.

Details about a person and their relationships should be editable. At a minimum you should use the following traits to describe a person:

- First name
- Last name
- Phone number
- Email address (unique)
- Address
- Birth date

When thinking about relations between people the API should be able to provide the following information

- For a given person list all of their siblings
- For a given person list all of their parents
- For a given person list all their children
- For a given person list all of their grandparents
- For a given person list all of their cousins

### Getting started

##### Running the service in a virtual environment

If you are using python 3.7 you will need to run
```bash
pipenv run pip install pip==18.0
```

To install dependencies you will need to run
```bash
pipenv install
```

Once dependencies are installed you can run the service with
```bash
pipenv run python manage.py
```
or
```bash
pipenv shell
python server.py
```
