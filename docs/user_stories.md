# User Stories

## Booking
- As a guest, I want to choose a room type and dates so I can see the price.
  - Acceptance: date inputs required; price shown on room card; modal shows total; invalid date range blocked.
  - Pages/URLs: `rooms/` (rooms/room_list.html), `rooms/details/` (rooms/interactive/details.html)
- As a logged-in user, I want to create a reservation so my stay is confirmed.
  - Acceptance: booking form validates dates; reservation saved; success message shown; booking ties to logged-in user.
  - Pages/URLs: `rooms/details/` (rooms/interactive/details.html) -> `rooms/reservations/`
- As a logged-in user, I want to edit or delete my reservation so I can manage my plans.
  - Acceptance: only the owner can edit/delete; success message shown; list reflects updates and deletions.
  - Pages/URLs: `rooms/reservations/` (rooms/reservations.html), `rooms/reservations/<id>/edit/` (rooms/reservation_edit.html), `rooms/reservations/<id>/delete/` (rooms/reservation_confirm_delete.html)
- As a user, I want to view my reservations list so I can see all my bookings in one place.
  - Acceptance: list only shows current user's reservations; empty state shown if none.
  - Pages/URLs: `rooms/reservations/` (rooms/reservations.html)
- As a user, I want a clear booking call-to-action on the home page to reach the room list quickly.
  - Acceptance: primary CTA on home routes to rooms page; CTA is visible on desktop and mobile.
  - Pages/URLs: `/` (content/home.html) -> `rooms/` (rooms/room_list.html)

## Accounts
- As a user, I want to sign up and log in so I can manage my reservations.
  - Acceptance: unique email enforced; login state shown in nav; errors displayed on invalid login.
  - Pages/URLs: `accounts/signup/` (templates/registration/signup.html), `accounts/login/` (templates/registration/login.html)
- As a user, I want to log out so I can end my session securely.
  - Acceptance: logout link available on every page; user is redirected to home.
  - Pages/URLs: `accounts/logout/` (templates/base.html)
- As a user, I want to delete my profile so I can remove my account.
  - Acceptance: delete action removes user and redirects to home; confirmation step required.
  - Pages/URLs: `accounts/manage/` (account management template)

## Comments
- As a logged-in user, I want to leave a comment on the rooms page.
  - Acceptance: comment saved with timestamp and username; form requires login.
  - Pages/URLs: `rooms/comment/add/<page>/` (rooms/room_list.html or rooms/interactive/details.html)
- As a logged-in user, I want to delete my own comments so I can manage my posts.
  - Acceptance: only comment owner can delete; success message shown.
  - Pages/URLs: `rooms/` (comment list action in templates where displayed)

## Admin
- As an admin, I want to manage rooms and reservations in Django admin.
  - Acceptance: Room and Reservation visible and editable in admin; list display and search help management.
  - Pages/URLs: `admin/` (Django admin)
- As an admin, I want to manage users and comments from the admin panel.
  - Acceptance: User and Comment visible and editable in admin.
  - Pages/URLs: `admin/` (Django admin)

## UI, Accessibility, and Navigation
- As a user, I want the navigation to reflect my login state so I know my access level.
  - Acceptance: shows Login/Signup when logged out; shows Reservations/Logout when logged in.
  - Pages/URLs: `templates/base.html` (global nav)
- As a user, I want the site to be responsive so I can book on mobile.
  - Acceptance: pages render without horizontal scroll on common mobile sizes.
  - Pages/URLs: all templates; focus on `content/home.html`, `rooms/room_list.html`, `rooms/interactive/details.html`
- As a user, I want accessible forms so I can complete bookings easily.
  - Acceptance: labels tied to inputs; error messages are visible; focus states are visible.
  - Pages/URLs: reservation form, auth forms, comment form

## Templates and Pages Coverage
- Home page (content/home.html) supports CTA to booking and highlights rooms.
- Rooms list (rooms/room_list.html) shows room cards with prices and booking entry.
- Room details (rooms/interactive/details.html) shows room info and booking modal.
- Reservations list (rooms/reservations.html) shows user bookings with edit/delete actions.
- Reservation edit (rooms/reservation_edit.html) allows updates with validation.
- Reservation delete (rooms/reservation_confirm_delete.html) confirms deletion.
- Base layout (templates/base.html) provides nav, footer, and messages.
- Auth templates (templates/registration/*) support login and signup.

## LO Mapping Checklist
- LO1: UX-focused pages, responsive layout, wireframes documented, user stories tracked.
- LO2: CRUD for reservations and comments with validated forms.
- LO3: Role-based auth for reservations/comments; restricted access enforced.
- LO4: Python tests for key flows; manual JS/UI checks documented.
- LO5: Git/GitHub usage with clear commit history and no secrets.
- LO6: Heroku deployment documented with DEBUG off and env vars set.
- LO7: Custom data model aligned with project domain and README ER summary.
