# Django Ninja Unfold Template

A Django template pre-configured with Django Ninja, Ninja JWT, and Django Unfold for rapid API development with JWT authentication and a modern admin interface.

## Features

-   **Django Integration:** Pre-configured with essential Django settings and utilities.
-   **Django Ninja:** Ready for building APIs with Django Ninja.
-   **Ninja JWT Authentication:** Implements JWT authentication using Ninja JWT.
-   **Django Unfold:** Includes Django Unfold for a visually appealing and functional admin panel.

## Requirements

-   Python 3.12 or higher
-   Django 5.1 or higher
-   Django Ninja
-   Django Ninja JWT
-   django-unfold
-   Tailwind CSS

## Project Structure

```
project/
├── core/                   # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── users/                  # Authentication and users
│   └── ...
├── common/                 # Shared logic and resources
│   └── ...
├── logs/                   # Application logs
├── .env.example
├── .gitignore
├── manage.py
├── pyproject.toml
├── poetry.lock
├── README.md
└── requirements.txt
```

## Setup Instructions

### Using Poetry

1. **Install Poetry**: If you haven't already, install Poetry by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

2. **Clone the Repository**:

    ```bash
    git clone https://github.com/hrmasss/django-ninja-unfold.git project-name
    cd project-name
    ```

3. **Install Dependencies**:

    ```bash
    poetry install
    ```

4. **Activate the Virtual Environment**:

    ```bash
    poetry shell
    ```

5. **Configure Environment Variables**: Copy `.env.example` to `.env`:

    ```bash
    cp .env.example .env
    ```

    Then, populate the `.env` file with the necessary environment variables (e.g., database URL, secret keys, API keys).

6. **Run Migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Create a Superuser**:

    ```bash
    python manage.py createsuperuser
    ```

8. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

### Using Python venv

1.  **Clone the Repository**:

    ```bash
    git clone https://github.com/hrmasss/django-ninja-unfold.git project-name
    cd project-name
    ```

2.  **Create a Virtual Environment**:

    ```bash
    python -m venv .venv
    ```

3.  **Activate the Virtual Environment**:

    -   On Windows:

        ```bash
        .venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```bash
        source .venv/bin/activate
        ```

4.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables**: Copy `.env.example` to `.env`:

    ```bash
    cp .env.example .env
    ```

    Then, populate the `.env` file with the necessary environment variables (e.g., database URL, secret keys, API keys).

6.  **Run Migrations**:

    ```bash
    python manage.py migrate
    ```

7.  **Create a Superuser**:

    ```bash
    python manage.py createsuperuser
    ```

8.  **Start the Development Server**:

    ```bash
    python manage.py runserver
    ```
