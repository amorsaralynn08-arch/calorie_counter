# Calorie Counter

A Django web application that helps users track their daily calorie intake by adding, viewing, deleting, and resetting food items.

---

## Project Description

The **Calorie Counter** is a Django-based web application that allows users to:

- Add food items with their calorie values.
- View a list of all food items consumed.
- Delete individual food items.
- Calculate the total calories consumed.
- Reset the daily calorie count.

---

## Features

- Add new food items
- View all food items
- Delete food items
- Calculate total daily calories
- Reset the calorie count
- PostgreSQL database integration
- Django Admin support

---

## Technologies Used

- Python
- Django
- PostgreSQL
- HTML
- Bootstrap 5
- Git
- GitHub
- python-decouple
- psycopg2
- psycopg2-binary

---

# Installation and Setup

## 1. Clone the repository

```bash
git clone https://github.com/amorsaralynn08-arch/calorie_counter.git
```

Navigate into the project folder:

```bash
cd calorie_counter
```

---

## 2. Create a virtual environment

```bash
python -m venv myenv
```

---

## 3. Activate the virtual environment

### Windows (Git Bash)

```bash
source myenv/Scripts/activate
```

### Windows (Command Prompt)

```bash
myenv\Scripts\activate
```

---

## 4. Install the project dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

## Step 1: Install PostgreSQL

Install PostgreSQL and pgAdmin 4 on your computer.

---

## Step 2: Create a PostgreSQL database

Open pgAdmin 4 and create a new database.

Example:

```
Calories
```

Assign the database owner to your PostgreSQL user.

---

## Step 3: Create a `.env` file

Create a `.env` file in the project's root directory.

Add the following variables:

```env
DATABASE_NAME=Calories
DATABASE_USER=your_postgres_username
DATABASE_PASSWORD=your_postgres_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Replace the values with your PostgreSQL credentials.

---

## Step 4: Apply migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## Step 5: Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator account.

---

## Step 6: Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

To access the Django administration panel:

```
http://127.0.0.1:8000/admin/
```

---

# Project Structure

```
calorie_counter/
│
├── calorieApp/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│
├── calorieProject/
│   ├── settings.py
│   ├── urls.py
│
├── myenv/
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

# Environment Variables

| Variable | Description |
|----------|-------------|
| DATABASE_NAME | PostgreSQL database name |
| DATABASE_USER | PostgreSQL username |
| DATABASE_PASSWORD | PostgreSQL password |
| DATABASE_HOST | Database host |
| DATABASE_PORT | PostgreSQL port |

---

# Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

# Contributing

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/feature-name
```

3. Commit your changes.

```bash
git commit -m "Describe your changes"
```

4. Push the branch.

```bash
git push origin feature/feature-name
```

5. Open a Pull Request.

---

# Author

Amor

GitHub: https://github.com/amorsaralynn08-arch

---

# License

This project is for educational purposes.
