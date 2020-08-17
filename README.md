# Casting Agency Specifications
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

# Models: (models.py)
Movies with attributes title and release date
Actors with attributes name, age and gender

# Endpoints: (app.py)
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/

# Roles: (auth.py)
Casting Assistant
Can view actors and movies

Casting Director
All permissions a Casting Assistant has and…
Add or delete an actor from the database
Modify actors or movies

Executive Producer
All permissions a Casting Director has and…
Add or delete a movie from the database

# Tests:
One test for success behavior of each endpoint
One test for error behavior of each endpoint
At least two tests of RBAC for each role



## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

# URL where the application is hosted

https://udacity-fsdn-capstone-project.herokuapp.com/


### Setup Auth0 here is the access tokens 

# Casting Assistant
access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxZDY1YjY2NTQyYzQwMDNkYzk1ZTJjIiwiYXVkIjoiQ2FzdGluZyIsImlhdCI6MTU5NzY5NTAwMCwiZXhwIjoxNTk3NzgxNDAwLCJhenAiOiJqMWFEMFNmdDU5SnNpUG5YS2ZSRXoxWjM3akFEcER4TiIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.FzbV89ksVV9BAaPDput897wqipuEoAbWMsCNdnJcJ88lC1g5zXjZSDCoJugVizGqNUWEJdYae3WGGDShBUYUClOWDkKiWCvTNcOvYE6B741n5PGrUi9THoEwNzBEkct1cKLyknqoCTleCayz_LlyHswpih67PdJ7a7ZUjCW3gG5kPHLaF3Y7YsANspUB_ovE_0bldiIMReqirjGpVT-tnn-7CRmePZlDy6APHm22MZmfw1mZ0U7fQifSNZHhLObBGdy3wKFqETVDWFsSkOJsotU33_66Uj84tDgWXtM8XZWN7Lt-PAxVZ34bb1lCXnr-4M9Q1p-FxPijO7B-OYdldQ


# Casting Director
access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDQwNTQwODM1MTIyNjQ3MzE2OTMiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTc2OTU2NzUsImV4cCI6MTU5Nzc4MjA3NSwiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.kiwLb71_KMIXTs1SVXfEmlrVa2piHsvrQZDhsAfWgCI9uuL-GK4kaa5HMUrG_5iXkXXVFjSTyYC8ynXhYjV4cB_fXPhuY-PxG7PEOVjkgjpXX0kovzRbwjjrIOQom3sVPuXY1ML-vjHE37QhkXtfBRZDXz_gAcJRH8rSZmNRMTd_Ty2hNLpVFYOBMO2payW3iqohrjawAv7xhfXDIQlr9ZcKW0L-5tURWFrWpB8lgQqNkHAo_0ZfXWaFDx13-OQBwoJ0shgdqgJLBOLULgSWkuGr1bcIIMwRO-h8kTqn5h9zwIrD6LnAUjS-w05b0qLkq7cIVOKgHPAGOnivHWA27g


# Executive Producer


access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhVM3Z3XzBuUGFQY214bmZXdllTUCJ9.eyJpc3MiOiJodHRwczovL2FscGhhLXdhbC5ldS5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTI1NDk4MjM1Mzg0ODM1MjI4MDQiLCJhdWQiOlsiQ2FzdGluZyIsImh0dHBzOi8vYWxwaGEtd2FsLmV1LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTc2OTUwMzUsImV4cCI6MTU5Nzc4MTQzNSwiYXpwIjoiajFhRDBTZnQ1OUpzaVBuWEtmUkV6MVozN2pBRHBEeE4iLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.kQicstC2d89cCxbZ9_nsAcBkLBDTG4QMCjtNojVP_U0exyfr_FmCsh8s8bcV97YlrMdVx_5EGFnCvzHOEBjVtZsIoVMFGDQa1RiAfIf9NksA1-MuqcMbP-yS4jlH4SGf_HtdAcfo_8WP50g4VljQt-TeWT7HjE92y9qr9MzxKgCMnEisHBPqJnm0SHpEXhx7xMCLSLbrl0qxMYaeo0s_Zzw7OvmIXdp_BscD8PXDi_hkGFJ2satH6MStibSE7-cQsIAkZXgZOBBn697Kg0QwqPLgaIThGoQa7bPJjRu6Q1qmlLe8scizL9hjrIwb9bBJLM_bIsf_yuSxXK1fH2IvoQ




# Tests

1. Test the endpoints with [Postman](https://getpostman.com). 
    - Import the postman collection `test_app.json`
    - Run the collection.


### Implement The Server

