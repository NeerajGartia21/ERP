## Quick Setup

1. Clone the Template

```bash
$ git clone https://github.com/NeerajGartia21/ERP.git
```

2. Create a `virtual environment` and install the requirements

```bash
$ pip install -r requirements.txt
```

3. Setup your [environment](#environment)

4. Run the project

  - Using `main.py`

  ```bash
  // using main.py

  $ cd src/app

  $ python main.py

  ```

  - Using `uvicorn` command

  ```bash
  $ uvicorn --app-dir="./src/app" --reload main:app
  ```

## Project Structure

```
.
├── LICENSE
├── README.md
├── requirements.txt
├── requirements_dev.txt
├── src
│   └── app
│       ├── __init__.py
│       ├── database
│       │   ├── __init__.py
│       │   ├── db.py
│       │   ├── models.py
│       │   ├── queries.py
│       │   └── schemas.py
│       ├── exceptions
│       │   ├── __init__.py
│       │   └── user.py
│       ├── helpers
│       │   └── auth.py
│       ├── main.py
│       ├── middleware
│       │   ├── __init__.py
│       │   └── auth.py
│       └── routers
│           ├── __init__.py
│           └── auth.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_auth.py
```

### Routes

You can add new routes for resources inside the `routers` directory using FastAPI's `APIRouter`. Out of the box, the routes for user creation and authentication have been provided with `JWT` support.

### Database

The `database` directory holds all database, models and schema related files. You can set your `DATABASE_URL` in the environment and the `SQLAlchemy` engine in `database/db.py` will create the required sessions and connections.

All your database models go inside the `database/models.py` file. These are standard `SQLAlchemy` models.

`Pydantic` schemas for data validation reside in the `database/schemas.py` file. There can be 2 schemas defined for each resource, `ResourceBase` which validates the request body and `ResourceSchema` which resembles the database resource item.

### Middleware

All the app-wide applicable middleware can be added to `main.py` directly. Middleware applicable to specific routes can be placed inside the `middleware` directory.

The `is_autheticated` middleware checks for valid `JWT` tokens and can be added to routes as a dependency.

The `CORS` middleware is added app-wide and list of origins can be changed inside `main.py`.

### Exceptions

You can put your custom exceptions inside `exceptions` directory.

### Testing

Testing is done using `pytest` and `fastapi.test_client`. You can add your tests inside the `tests` directory. You add your custom `pytest fixtures` inside `conftest.py` file. Currently, tests are run against the production database but they will shifted to a test database soon.

You can run the tests from inside the project folder

```bash
$ pytest
```

### Environment

You need to set the following environment variables

```
SECRET_KEY                    // JWT secret
ALGORITHM                     // Algorithm for encoding JWT
ACCESS_TOKEN_EXPIRE_MINUTES   // JWT token expiration in minutes
DATABASE_URL                  // Database URL
```

You can generate a secure `SECRET_KEY` using -

```bash
$ openssl rand -hex 32
```

See this for a list of [supported encoding algorithms](https://python-jose.readthedocs.io/en/latest/jws/index.html#supported-algorithms).

### Helpers

You can add your helper functions to `helpers` directory.
