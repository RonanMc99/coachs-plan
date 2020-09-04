# "The Coach's Plan" - an app for fitness and nutrition coaches

![PCbuzz-screenshot1](/)

## Live Demo
[See the live demo here](/)

## Introduction

This is a digital fitness and nutrition plan app for the web.

I have been a fitness coach for years and have a strong interest in nutrition, and wanted to explore creating a web app that would allow myself, or any other fitness or nutrition coach, to sell their products and servcies on the web.

The idea is that a coach can upload a series of instructions and guides for the user.  A new user can then browse for a fitness plan or diet plan that they like, and purchase it for instant access.

The app is based on Python with Django v 3.1.1, and uses a database to persist the data.   In the development phase, this is SQLite3 and for production deployment, PostgreSQL is a better choice.  To read more about my process for developing the app, see the design section below.

This is a simple, M.V.P version of the app as proof-of-concept, and its primary aim is to achieve these goals using Django. 

### Technologies

Backend: Python, Django, SQLite3, Stripe API, PostgreSQL. 

Frontend: HTML / CSS / JS / Bootstrap 4

Deployment: Docker / Heroku

## Prerequisites

* Python 3.8.2.
* Django==3.1.1
* PostgreSQL or SQLite3.  Either a local installation or a cloud-based instance is suitable
* Additional package requirements are provided in the requirements.txt file.  See below for installation
* The application uses the Stripe API to make payments.  You must [request your own API key here](https://www.stripe.com) 

## Installation

1. Clone the repositary to your installation location
2. Create a docker-compose.yml file, using the command "touch docker-compose.yml" and add the following:
'''
version: '3.8'

services:
    web:
        build: .
        command: python /code/manage.py runserver 0.0.0.0:8000
        environment: 
        - DEBUG=1
        - SECRET_KEY=
        - STRIPE_TEST_PUBLISHABLE_KEY=
        - STRIPE_TEST_SECRET_KEY=env('STRIPE_TEST_SECRET_KEY')=
        volumes:
        - .:/code
        ports:
        - 8000:8000
        depends_on:
        - db
    db:
        image: postgres:11
        volumes:
        - postgres_data:/var/lib/postgresql/data/
        environment:
        - "POSTGRES_HOST_AUTH_METHOD=trust"

volumes:
        postgres_data:
''' 
3. Build the initial image using the command docker-compose up --build
4. Wait for the build to complete and use the command "docker-compose logs" to view the logs

## UX

### User

As a 'coach' user I would like...

- to be able to upload my fitness and nutrition plans to the site
- to allow users to purchase and gain access to these plans without my intervention
- to upload text and image content which is beneficial to my customer
- to add examples of completed plans and worksheets

As an 'athlete' user I would like...

- to browse a selection of fitness and nutrition plans from multiple coaches
- to purchase any plans that appeal to me and gain access to them whenever I like
- a secure login where my password and personal details are protected
- secure payments with a well-trusted payment provider
- an application that can run on any device
- the application to be easy to navigate with clear menus and navigation

### Design

The goal of this project was to create a web app that uses Django and a database on the backend to manage and persist the data. The site is neat, clean and responsive and suitable for all devices.  Visually, this is a simple e-commerce design, and as a proof-of-concept project, this version uses basic Bootstrap classes to style the various elements. Django Crispy forms has been added to improve the look and usability of the forms.

Database relationships between the various tables are shown [here]()

The site is made up of multiple Django apps, named Pages, Plans and Cart.

## Pages
The pages app contains any static pages required on the site, such as 'home', 'contact' and 'profile'.  These are a mix of function and Class-based views.

## Plans
The pages app oulines the main structure in terms of models.  
- Coach represents the plan's author.  
- Plan is the plan itself, and includes such fields as description and image, but the extensible nature of Django means that additional fields can easily be added e.g. for unlimited scalability of text sections, activities or downloadable documents
- Sections are the high-level plan breakdown and could represent, for example, a set of activites to complete in one week
- Activites are the information and tasks that the coach can set e.g. complete a food diary or a sleep journal
- Examples are provided to allow the coach to upload a pre-completed worksheet as an example to the user
- Users Plans is a model which represents the user's purchased library of plans

## Cart
The cart app contains the main shopping logic including the shopping cart and checkout
- Order represents the user's order, including a reference field,  and all items in the order 
- Cart Item is a plan which has been added to the cart but not yet checked out
- Completed Order includes the order relationship and some metadata

## Features
The site has a breadcrumb trail which advances and retreats through Plans - Sections - Activites - Examples.  There is also a main navigation including shop, and cart links.  The site has been secured using Django-Allauth and use of permissions / the login required decorator as well as some logic within the templates.

Stripe integration has been added using Stripe elements and some javascript to integrate a secure payment form within the checkout page.

### Features to implement
This app was built as a proof-of-concept to define the logic and verify the idea would work.  There are several improvements I would like to make and these will be in version 2, including:

- A better UI and copy for the front page
- Production-ready email integration for signups and order receipts. I will probably use Sendgrid for this.  Async taks will be handled with Celery
- Better user profile view

## Testing

Testing is handled by a small number of unit tests using SimpleTestCase and TestCase.  Most tests for the main logic was performed by manual QA and recorded in a spreadsheet.
Execute tests by:
'''
docker-compose exec web python manage.py test
 
'''

### Google Lighthouse

I used google lighthouse in to perform some basic tests and look for performance issues.


## Credits

In preparation for this project, I studied the work of:

Vincent, William S.. Django for Professionals: Production websites with Python & Django (p. 67). Still River Press. Kindle Edition. 
Django 3 By Example - Third Edition, Mele, S

and massive thanks to my Youtube superstars, from whom I learn so much every day!  

Denis Ivy
Corey Schafer
Max Goodridge
Just Django
Pretty Printed

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to provide tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)