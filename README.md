# My School — Django Course Project (Classes 1–4)

A small Django project we build together in class. It has three apps —
**students**, **classes** and **teacher** — and shows real data from the
database on styled pages.

Use this as a clean, working starting point for **Class 5 (Forms)**.

## What's inside (and which class it comes from)

- **Class 1** — project & app setup, `settings.py`, running the server
- **Class 2** — URLs, views, dynamic pages (`<int:id>`), named URLs, `include()`
- **Class 3** — templates, template inheritance (`base.html`), static files & Bootstrap
- **Class 4** — models, migrations, the ORM, and a `ForeignKey` (a student belongs to a class)

## How to run it

From a terminal:

```bash
# 1. Go into the project folder
cd my_school

# 2. Create and activate a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac / Linux:
source venv/bin/activate

# 3. Install the requirements
pip install -r requirements.txt

# 6. Start the server
python manage.py runserver
```

Now open **http://127.0.0.1:8000/** in your browser.

## Pages you can visit

| URL | What it shows |
| --- | --- |
| `/` | Home page |
| `/students/` | List of all students |
| `/students/1/` | One student's details |
| `/classes/` | List of all classes |
| `/classes/1/` | One class + its students |
| `/teachers/` | List of all teachers |
| `/teachers/1/` | One teacher's details |

## (Optional) Admin site

To browse the data in Django's admin:

```bash
python manage.py createsuperuser
```

Then visit **http://127.0.0.1:8000/admin/** and log in.

## Project structure

```
my_school/
├── manage.py
├── seed_data.py          # fills the database with sample data
├── requirements.txt
├── templates/
│   └── base.html         # shared layout (nav + Bootstrap), every page extends this
├── static/
│   └── css/style.css     # our custom styles
├── my_school/            # project settings
│   ├── settings.py
│   └── urls.py
├── students/             # students app (home page + student list/detail)
├── classes/              # classes app (class list/detail)
└── teacher/              # teacher app (teacher list/detail)
```
