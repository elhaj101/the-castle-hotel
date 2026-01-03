# Dev Workflow (Local First)

This workflow keeps development local and ensures every page, function, and
feature is verified end-to-end before production work begins.

## Start of Session
- Pull latest changes and confirm working tree status.
- Run migrations if needed.
- Start the dev server and keep the browser open.

## Page Inventory Pass
Open and render each template to confirm routes and context:
- `content/home.html`
- `rooms/room_list.html`
- `rooms/interactive/details.html`
- `rooms/reservations.html`
- `rooms/reservation_edit.html`
- `rooms/reservation_confirm_delete.html`
- `templates/base.html`
- `templates/registration/login.html`
- `templates/registration/signup.html`

## Core Booking Flow
- Home CTA -> Rooms list -> Room details -> Booking modal -> Reservation create.
- Verify date validation and total price calculation.
- Confirm success messages and redirects.

## Reservation Management
- Reservations list shows only the current user.
- Edit flow updates data and shows success feedback.
- Delete flow confirms and removes the reservation.
- Ownership checks prevent access to other users' reservations.

## Accounts and Auth
- Signup, login, logout all work.
- Navigation reflects login state.
- Profile delete removes user data with confirmation.

## Comments
- Add comment and confirm timestamp/username.
- Delete only own comments.
- Confirm feedback messages for create/delete.

## UI and Accessibility
- Test mobile layout (no horizontal scroll).
- Check form labels, focus states, and errors.
- Verify CTA visibility and clarity.

## Testing and Docs
- Run Python tests and record results in README.
- Complete manual JS/UI checklist and record in README.

## Cleanup and Git
- Remove local artifacts if present (`.pyc`, `.DS_Store`, `db.sqlite3`).
- Update `.gitignore` as needed.
- Commit with clear, scoped messages.
