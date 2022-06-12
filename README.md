# Repository Description

Project To collect NEPSE DATA and to run analysis on it in order to get stock predictions. This projected was 
created in order to complete the CSIT course in DWIT as it contains the code submitted for completion of Project 2 
Semester 6 to DWIT institute of Technology.

**In order to set the project up, clone it and then follow the provided Command Sequence:**

```
> cd <CLONE_DIR>
> python -m venv env
> pip install -r require.txt

To run the Django Project you have two steps ...
-- For Windows --
> env\Scripts\activate 
-- For Linux Based Systems --
> source env\Scripts\activate

-- Setting up Django Files --
> cd neppredictor
> python manage.py makemigrations
> python manage.py migrate
> python manage.py runserver
```

This is **not** for production and hence doesn't violate any IT policies that have been created for the integrity of 
the Cyber World. **Scraping of NEPSE in production enviroment is not allowed or encouraged.**  

## Divided into two Segments
### 1. A scrapy project
The **Scrapy** package has been used to create spiders which crawl through the NEPSE site for data collection. There 
may be multiple scrapers in the above project on the basis of details required as per need.
### 2. A Django project
It provides an interface for the demonstration of data that has been collected and provides a user with login and 
follow facilities that has been created using the django **(Specifically django 4.0.X)** module. 

