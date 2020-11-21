# "The Coach's Plan" - an app for fitness and nutrition coaches

![Coachs Plan](https://user-images.githubusercontent.com/51950969/99876319-fbff7b00-2bed-11eb-8ba3-9e9f85dc9cc7.png)

![Home 2](https://user-images.githubusercontent.com/51950969/99876441-a9728e80-2bee-11eb-9ad4-1f48c1df6f5c.png)

## Live Demo
I have created a demo site that includes some dummy plans.
[See the live demo here](https://the-coachs-plan.herokuapp.com/).  

***No actual purchases can be made using this site.***

To access the demo, you can use the credentials below, or register for your own.

```
demouser@thisisnotreal.com
notaverygoodsecret
```

## Introduction

This is a digital fitness and nutrition plan app for the web - it allows sports coaches, personal trainers and nutritionists to deliver a training or nutrition plan, accept orders, take payment, and provide access to the product.

I am a fitness and nutrition coach and this app was build with my own needs in mind.  I help athletes reach their sporting and body composition goals, and generally speaking, coaching individuals in this way means providing them with a plan they can follow which contains instructions, guidance and any other information they may need.

There are various online coaching platforms available, such as Teachable, Fitr, or Kajabi, but I had always found them to be somewhat inflexible for my needs, and also quite costly.  So - I decided to build my own!

The simple aim for this app was to allow a coach to upload a series of instructions and guides for the user.  A user can then browse for a fitness plan or diet plan that they like, and purchase it for instant access.

The plans may consist of written and video material, as well as images and descriptions for thier plan.  The highly extensible nature of Django means that it's very easy to add additional content types as my needs develop - For any new type of content, I can simply make changes to the relevant model, make some additions to the view if needed, and update the template.  This is the power of Django for e-commerce.

There is also a very simple blog function which the coach can use to share information and reach new clients.

The app is based on Python with Django v 3.1.1, with a relational database to persist the data.  In the development phase, I used SQLite3, but for the main deployment, I switched to using a PostgreSQL relational database is a better choice for performance. 

To read more about my process for developing this app, see the sections below.

### Technologies

Backend: Python, Django, SQLite3, Stripe API, PostgreSQL. 

Frontend: HTML / CSS / Jquery / Bootstrap 4

Deployment: Docker / Heroku

## Prerequisites

* Python 3.8.2.
* Django 3.1.1
* PostgreSQL or SQLite3.  Either a local installation or a cloud-based instance is suitable
* Additional package requirements are provided in the pipenv and pipenv.lock files.  See below for installation instructions
* The application uses the Stripe API to make payments.  If cloning this project, you must [request your own API key at Stripe.com](https://www.stripe.com).  For additional requirements see the installation and deployment sections.

## Installation

1. Clone the repositary to your installation location
2. Create a docker-compose.yml file, using the template (docker-compose.yml.template).  This may be customised as needed to suit your local environment.
3. Within the databases section of settings file, comment the appropriate block to select postgres.  ![Databases Screenshot](https://user-images.githubusercontent.com/51950969/99876241-67951880-2bed-11eb-9266-304fef8b82d1.png "Databases Screenshot")
4. With Docker desktop running, build the initial image using the command docker-compose up --build
5. Wait for the build to complete and use the command "docker-compose logs" to view the logs
6. Run the command ` docker-compose -f docker-compose.local.yml up ` to run the containers.  This will also execute the docker_start_up.sh file which makes migrations and sets up the project.  You may then access your project at 0.0.0.0:8000.

## UX
As mentioned in the Introduction, the site was based on my own personal need as a fitness coach.  I wanted to investigate how to deliver some content using Django.

This content needed to be structured, as by it's nature, a fitness-training or nutritional protocol will be progessive, and vary with time.  This is how pysiological adaptations occur and the plans needed to reflect that.

Plans however, also needed to be flexible and adaptable, to accomodate both fixed-length and individualised plans, "one-off's" or anything a coach could conceive.

I elected to use a simple heirarchy of Plans, which consist of 'Sections'.  Sections include activites, which may then have linked resources.  See the 'Plans' section below for a further description.

Using this heirarchy, it is possible to create a range of plan types - from a 28 week marathon training plan, to a week-long workshop.  Downloadable programs, sample weekly schedules, nutirition tracking worksheets or a bespoke plan for an individual athlete.  It is also suitable for grouping together content for selling online, such as a disparate set of exercise plans or recipes.

The type of content within each section would vary between plans, and may have to be modified to accomodate new plan structures, but this is made very simple through the use of extensible Django models and the extremely powerful built-in ORM.

To begin to think about the content, and the overall user experience, I constructed some simple user stories to inform my decisions:

### User Stories

As an administrative user I would like...

- to be able to upload my fitness and nutrition plans to the site
- to allow users to purchase and gain access to these plans without my intervention
- to upload text and image content which is beneficial to my customer
- to add examples of completed plans and worksheets
- Publish my blog posts to encourage and inform users, and also begin to build a relationship with prospective clients.  They can "see what I'm about" and perhaps choose to purchase one of my plans
- Provide a way to register for a new account
- Provide a way to contact me via the site

As an 'athlete' user I would like...

- to browse a selection of fitness and nutrition plans from multiple coaches on any device
- to purchase any plans that appeal to me and gain access to them whenever I like
- a secure login where my password and personal details are protected
- secure payments with a well-trusted payment provider
- an application that can run on any device
- the application to be easy to navigate with clear menus and navigation

### Design

The primary goal of this project was about testing the viability of delivering fitness content using Django, and so the visual design is basic, but functional for this purpose.

Visually, this is a simple e-commerce design, using Bootstrap classes and some simple CSS to style the various elements. Django Crispy forms has been added to improve the look and usability of the forms.  

The visual design has a simple 'no-frills' look and feel, as the main focus for this project was the e-commerce functionality.  The site is very simple, clean and responsive and is suitable for display on all devices.  Future development will include a front-end redesign.

![Wireframe for Home and Shop](https://user-images.githubusercontent.com/51950969/99879769-cc10a180-2c06-11eb-9429-1314674ebb66.png)

### Database

The database schema is shown below ![schema](https://user-images.githubusercontent.com/51950969/99878569-425cd600-2bfe-11eb-8727-7a8138778147.png)

The site is made up of multiple Django apps, named Blog, Pages, Plans and Cart.

## Blog
The blog app contains a series of posts which are linked to the coach table.  Users can click on the coach's name to filter by that coach.

![Blog image](https://user-images.githubusercontent.com/51950969/99879819-332e5600-2c07-11eb-9dfe-98a142be7674.png)

## Pages
The pages app contains any static pages required on the site, such as 'home', 'contact' and 'profile'.  These are a mix of function and Class-based views.

## Plans
![Plan Image](https://user-images.githubusercontent.com/51950969/99880353-c61cbf80-2c0a-11eb-94f0-d7d05706e52b.png)

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
The site has a breadcrumb trail which advances and retreats through Plans - Sections - Activites - Examples.  

There is also a main navigation including shop, and cart links.  The site has been secured using Django-Allauth and use of permissions / the login required decorator as well as some logic within the templates.

![Sign Up](https://user-images.githubusercontent.com/51950969/99879864-80122c80-2c07-11eb-9187-cf071db54411.png)

![Unauthorised](https://user-images.githubusercontent.com/51950969/99879877-90c2a280-2c07-11eb-8fe8-36a26e4cfaec.png)

Stripe integration has been added using Stripe elements and some Javascript to integrate a secure payment form within the checkout page.

## Payments
This project uses Stripe to take payments for plans.  The user can add a plan to their cart, and when they select checkout, will be offered a payment form.

![Stripe](https://user-images.githubusercontent.com/51950969/99879899-af289e00-2c07-11eb-9a3c-6058e4cca106.png)

This form uses some Javascript to accept a credit card number, date and CCV.  If you wish to accept payments from Stripe, you must sign up for an account at Stripe.com and complete the necessary requirements in order to get an API key.

For the live demo, this payment form is linked to a sandboxed payment system, meaning, if you enter card details using the demo app, **you will not be charged**

Dummy payments can be made in order to explore the demo's functionality.  [See the Stripe documentation for more information](https://stripe.com/docs/api).

## Security
There are a number of security features included in the app.

User registration and authentication is one of the most important elements of a website security, especially when payments are involved.  For this, I have decided to make use of the library, [Django-AllAuth](https://django-allauth.readthedocs.io/en/latest/)

This is actually a set of applications related to authentication, account management and social account integration.  It was added as an additional package and included into 'Authentication_backends' within the main settings file.  Templates and messaging was customised to accomodate this package.

### Other security configurations
- Environ was used to handle environment variables and ensure that secrets were kept out of the repositary
- The Django deployment checklist was run to check for issues
- DEBUG is set to false by default and within the hosting environment to ensure no sensitive data may leak during unhandled exceptions
- ALLOWED_HOSTS was set in Production so that only specified hosts are valid. This is a measure to prevent host header attacks
- Steps have been taken to prevent cross-site scripting, including additional configurations within settings.py
- Cross Site Forgery Requests are prevented with CSRF middleware
- SSL enforcement and HTTP Strict Transport Security (HSTS) settings have been enabled
- Secure cookies have been enabled
- The default administration path has been modified

Django and packages were fully up to date i.e. the latest stable build, at project inception.

## Deployment
Deployment for the demo site uses Heroku, which is a platform as a service (PAAS) that enables developers to easily deploy applications on the cloud.  The app was developed using Docker on the desktop, and this offers some advantages.  Development work on the local machine can more closely mimic that in a 'live' environment, which Ill call Production.

This approach greatly simplifies the Heroku deployment, as the Docker containers can be hosted there directly (lift-and-shift), although some additional packages are required for a more production-ready deployment, and these are detailed below.  

Heroku offer two container deployment options - using the container registry to deploy pre-built images, or you can specify the environment configuration with a YAML file.  This project will utilise the latter approach as it offers more customisation, such as including scripts to execute additional commands.  Heroku provide [complete setup instructions for Docker deployments here](https://devcenter.heroku.com/categories/deploying-with-docker).

- Dependancies listed in the pipfile are included within the Docker container (they are installed using pipenv with a Dockerfile command)
- Gunicorn 20.0.4 will replace the local web server in Production
- The Dockerfile and docker-compose files are located at the project root
- PYTHONDONTWRITEBYTECODE & PYTHONUNBUFFERED are set in the Dockerfile to prevent Python from writing pyc files to the disc volume, and from buffering stout and stderr.  [See here for more information](https://docs.python.org/3/using/cmdline.html).
- A dockerignore file exists to exclude unneeded files when generating a Docker build
- The Heroku.yml manifest contains the instructions for building the environment, and is made up of four sections:
    - Setup: This adds a Postgres instance to Heroku add-on.  This is a requirement for the build.
    - Build: Specifes the Dockerfile
    - Release: Specifies the image and entrypoint script
    - Run: Specifes the wsgi module to be associated with Gunicorn
- An entrypoint named docker_start_up_prod.sh exists at the project root.  This command executes the Django migrate command to populate the database, and collects static files

### Heroku Setup
- A new Heroku app was created with the Heroku dashboard with the title 'the-coachs-plan'
- Environment variables (known as Config Vars) MUST be set, and configured to include all of the project secrets.  The project requires the following variables to be set:

- AWS_STORAGE_BUCKET_NAME
- AWS_SECRET_ACCESS_KEY
- AWS_S3_REGION_NAME
- AWS_ACCESS_KEY_ID
- DATABASE_URL **Note** This is added automatically with the Heroku Postgres add-on
- DEBUG (set to 0 for False)
- ENVIRONMENT (set to prod)
- SECRET_KEY
- SENDGRID_API_KEY
- STRIPE_TEST_PUBLISHABLE_KEY
- STRIPE_TEST_SECRET_KEY

### Media File Storage
- Media files are handled using Amazon AWS, specifically, an S3 storage bucket.  Whitenoise was utilised during development, but [this is not suitable for Production](http://whitenoise.evans.io/en/stable/django.html#serving-media-files).
    - The django-storages library provides easy integration with AWS for storing user-media content
    - Follow the [instructions given](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) to configure Amazon S3 with django-storages.  Note that this requires an Amazon AWS account and has an associated cost.  Another good article on [setting up S3 with Django can be found here](https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html).
    - The package 's3boto3Storage' is required for interacting with S3

### Future Development
There are several improvements I would like to make in version 2, including:

- A better UI and updated sales copy for the front page
- Updates to the email sending functionality.  I am currently using Sendgrid for this, however, there have been one or two bugs, and I would like to iron those out.  Email autoresponder technology would be a great addition from a marketing point of view and any associated async taks will be handled with Celery
- Improve the user's profile / library views and make it easier to reset passwords
- A customised administraton area making it easier to add plans, with their related sections, activities and example files
- I will work on exception handling and more automated tests
- Performance issues related to location of static assets

## Testing

I began the testing using some simple unittests using SimpleTestCase and TestCasel; however, due to the complexity of working with a third-party payment processor, testing for the main shopping logic was performed by manual QA and recorded in a spreadsheet.

To execute tests:

'''
docker-compose exec web python manage.py test
 
'''

## Test Results
The results of the manual testing are shown in [this document](https://docs.google.com/spreadsheets/d/1N19byJ9rkPg5WHwHa128r-hQgwOpUP3e19HZ-KL9xuk/edit?usp=sharing.

### Google Lighthouse

I used google lighthouse in to perform some tests against the demo site and look for performance issues.  This has indicated some performance issues which are mainly related to slow loading of CDN-based files.  This is one area where I will look for improvements when creating version 2 of this app.

## Credits

In preparation for this project, I studied the following:

"Django 3 By Example - Third Edition, Mele, S"

Acknowledgements 
I must acknowledge the developers who I learned so much from during this project.

- The approach to working with Stripe, and also security and best-practice configuration was learned from: "Vincent, William S.. Django for Professionals: Production websites with Python & Django. Still River Press. Kindle Edition."

- The method of handling orders & cart items and getting the order total came from Matt Freire @ [JustDjango](https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ).

Massive thanks to the YouTube Superstars:
- [Denis Ivy](https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg)
- [Corey Schafer](https://www.youtube.com/user/schafer5)
- [Max Goodridge](https://www.youtube.com/user/Max204204204)
- [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)

## Known Issues
- There is one bug that I am aware of within the demo, which is related to SendGrid and not the project code itself.  This is related to a domain verification issue, and at the time of writing, I am working to resolve this with my nameserver provider.  The bug causes periodic failure of the 'admistrative-email send' feature during user signup, and an 'SMTPDataError at /accounts/signup/' message is displayed.  The user signup process itself is not affected, and the user may log on  by navigating back to home and clicking 'Log In'.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to provide tests as appropriate.

## License
This project is licensed under the standard MIT terms:
[MIT](https://choosealicense.com/licenses/mit/)