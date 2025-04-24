# The Castle Hotel

A hotel website with booking features.



## Wireframes

<img src="screenshots/screenshot1.png" alt="Wireframe 1" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />

<img src="screenshots/Screenshot 2025-04-24 at 03.52.25.png" alt="Wireframe 2" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />



## User Features

As a user, I want to:
- Book rooms.
- Sign up and sign in to my account.
- post and delete comments 
- delete my profile
- be directed to the next steps on the landing page by clicking a button that takes me to booking
choose a room type and choose dates to know its price
- book a room and fill in my information for booking 


# The Castle Hotel

A modern hotel booking web application built with Django, PostgreSQL, Tailwind CSS, Bootstrap, and JavaScript.

---

## Overview

**The Castle Hotel** is a full-featured hotel website that allows users to:
- Browse and book rooms
- Register and manage their accounts
- Post and delete comments
- Delete their own profile and all their comments
- View dynamic room pricing based on selected dates
- Enjoy a responsive, visually appealing interface

The project is designed for easy deployment on Heroku, using the Heroku Postgres add-on for production data storage.

---
## Screenshots

### Home Page
<img src="screenshots/home.png" alt="Home Page" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />

### Room Booking Page
<img src="screenshots/rooms.png" alt="Room Booking Page" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />

### Admin Panel Overview
<img src="screenshots/admindjango.png" alt="Django Admin Panel" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />

### User Profile Management
<img src="screenshots/panelmanage.png" alt="User Profile Management" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />

### Comments Section
<img src="screenshots/comments.png" alt="Comments Section" style="max-width:700px; width:100%; border:1px solid #ccc; margin-bottom:16px;" />
## Features

### User Features
- **Sign Up / Sign In:** Secure authentication system for user accounts.
- **Room Booking:** Choose room type, select dates, and book available rooms.
- **Comment System:** Post and delete comments on rooms/pages.
- **Profile Management:** Delete all comments or delete your account from the frontend.
- **Responsive UI:** Works on desktop and mobile devices.

### Admin Features (Django Admin Panel)
- **Rooms & Reservations Overview:** See the number of rooms, types, and real room numbers.
- **Room Management:** Add, edit, or delete rooms and their details (type, price, availability).
- **Reservation Management:** View all reservations and guest information submitted via booking forms.
- **User Management:** Create, edit, or delete users.
- **Guest Management:** Add or remove guests.
- **Full Data Overview:** Access and edit all room, reservation, and guest data directly from the admin panel.

---

## Tech Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL (Heroku Postgres add-on in production), SQLite for local/dev, schema in `schema.sql`
- **Frontend:** Tailwind CSS, Bootstrap 5, custom CSS (`static/css/style.css`)
- **JavaScript:** For modals, booking UI, and interactive features (`static/js/script.js`)
- **Deployment:** Heroku (with `Procfile` and `requirements.txt`)
- **Other:** Whitenoise for static file serving, Django templates

---

## Project Structure

```
the-castle-hotel/
│
├── accounts/         # User authentication and profile management
├── comments/         # Comment system
├── content/          # Static pages (home, contact, etc.)
├── rooms/            # Room models, booking, and reservation logic
├── static/           # Static files (CSS, JS, images)
├── templates/        # HTML templates (base, login, room list, etc.)
├── data.json         # Sample data for initial load/backup
├── schema.sql        # SQL schema for PostgreSQL
├── manage.py         # Django management script
├── requirements.txt  # Python dependencies
├── Procfile          # Heroku deployment config
├── README.md         # This file
└── ...               # Other standard Django files
```

---

## Setup & Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/the-castle-hotel.git
    cd the-castle-hotel
    ```

2. **Create and Activate a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**
    - `SECRET_KEY`
    - `DEBUG`
    - `DATABASE_URL` (for production/Postgres)

5. **Run Migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Load Sample Data (Optional)**
    ```bash
    python manage.py loaddata data.json
    ```

7. **Create a Superuser**
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the Development Server**
    ```bash
    python manage.py runserver
    ```
    Visit [http://localhost:8000](http://localhost:8000) in your browser.

---

## Deployment (Heroku)

1. **Push your code to Heroku:**
    - Make sure you have a `Procfile` with:  
      ```
      web: gunicorn the_castle_hotel.wsgi
      ```
    - Make sure `requirements.txt` is up to date.

2. **Provision the Heroku Postgres Add-on:**
    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

3. **Set environment variables on Heroku:**
    - `SECRET_KEY`
    - `DEBUG` (set to `False` in production)

4. **Deploy:**
    ```bash
    git push heroku main
    ```

5. **Run migrations and collect static files:**
    ```bash
    heroku run python manage.py migrate
    heroku run python manage.py collectstatic --noinput
    ```

6. **(Optional) Load initial data:**
    ```bash
    heroku run python manage.py loaddata data.json
    ```

---

## Frontend

- **Tailwind CSS** and **Bootstrap 5** are both used for rapid, responsive UI development.
- Custom styles are in `static/css/style.css`.
- **JavaScript** (`static/js/script.js`) powers modals, booking forms, and UI interactivity.

---
## Debugging Checklist

| Area             | Check                                                                 |
|------------------|-----------------------------------------------------------------------|
| Environment      | All environment variables (SECRET_KEY, DB, etc.) are set              |
| Database         | Database is configured and migrations are applied                     |
| Static Files     | Static files are collected and served correctly                       |
| URLs             | All routes are included and correct                                   |
| Templates        | All required context variables are passed to templates                |
| User Auth        | Login, logout, signup, and user management forms work                 |
| Comments         | Users can add and delete comments                                     |
| Room Booking     | Users can view, select, and book rooms                               |
| Admin Panel      | Django admin is accessible and shows rooms, reservations, users, etc. |
| Deployment       | All deployment files are present and correct for Heroku               |
| Data Import      | Initial data is loaded if needed                                      |
| Removed Features | No leftover references to Wellness/Restaurant apps                    |
| Error Logs       | No errors on startup or during requests                               |
| Dependencies     | All required packages are installed                                   |
| Migrations       | All migrations are applied                                            |
| Backup           | Database and data backups exist                                       |
| Heroku Add-ons   | Heroku Postgres add-on is attached and configured                     |
| Session/Cookies  | Sessions and cookies work for login/logout                            |
| CSRF Protection  | All forms are protected with `{% csrf_token %}`                       |
| README           | README is up to date and clear                                        |





## Services & Technologies Table

| Area             | Service / Technology Used                          |
|------------------|---------------------------------------------------|
| Environment      | Heroku (deployment), local dev environment        |
| Database         | Heroku Postgres (production), SQLite3 (fallback)  |
| Static Files     | Whitenoise, Django staticfiles, Heroku CDN        |
| URLs             | Django URL dispatcher                             |
| Templates        | Django Templates                                  |
| User Auth        | Django Authentication system                      |
| Comments         | Custom Django app (comments)                      |
| Room Booking     | Custom Django app (rooms), Django ORM             |
| Admin Panel      | Django Admin                                      |
| Deployment       | Heroku, Procfile, Gunicorn                        |
| Data Import      | Django loaddata, data.json                        |
| Removed Features | N/A (Wellness/Restaurant apps removed)            |
| Error Logs       | Heroku logs, Django runserver output              |
| Dependencies     | requirements.txt, pip                             |
| Migrations       | Django migrations                                 |
| Backup           | data.json, db.sqlite3                             |
| Heroku Add-ons   | Heroku Postgres                                   |
| Session/Cookies  | Django sessions, browser cookies                  |
| CSRF Protection  | Django CSRF middleware                            |
| README           | Markdown, GitHub                                  |
| Frontend (CSS)   | Tailwind CSS, Bootstrap 5, custom CSS             |
| Frontend (JS)    | Custom JavaScript (`static/js/script.js`)         |

| CSS Validation    | [W3C CSS Validator](screenshots/cssvalid.png)            |


## Development Notes

- Originally, the project included wellness and restaurant apps, but these were removed for focus and simplicity.
- The database was migrated from Railway to Heroku Postgres due to compatibility and reliability.
- All forms are protected with CSRF tokens.
- The project is structured for easy extension and maintenance.

---

## License

This project is for educational/demo purposes.  
Contact the author for commercial use or contributions.

All images were taken from Pexels ( No license needed )
---

## Author

Ali Elhaj  
[alielhajj@outlook.de](mailto : alielhajj@outlook.de )

---

**Enjoy using The Castle Hotel!**  
For questions or issues, please open an issue or contact the author.