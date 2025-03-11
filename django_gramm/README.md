# Django Gramm - Login via Third-Party Services

## Overview

This Django application demonstrates user authentication via third-party services. It includes standard login, registration, profile management, and integration of OAuth authentication providers.

## Features

- User Registration and Authentication
- OAuth Login Integration (e.g., Google, GitHub, Facebook)
- User Profile Management
- Posting system

## Structure

```
.
├── django_gramm/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── posts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/posts/
│       ├── post_new.html
│       └── posts_list.html
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   └── templates/users/
│       ├── login.html
│       ├── register.html
│       ├── profile.html
│       └── configurate_page.html
├── templates/
│   ├── home.html
│   └── layout.html
├── manage.py
├── requirements.txt
├── .gitignore
└── .dockerignore
```

## Setup

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to project directory:

```bash
cd django_gramm
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Database Setup

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

Start Django server:

```bash
python manage.py runserver
```

Open http\://localhost:8000 in your browser.

## Contributing

Contributions are welcome. Please submit a pull request or create an issue if you have suggestions or find bugs.

## License

This project is licensed under the MIT License.


