# User Stories

## Booking
- As a guest, I want to choose a room type and dates so I can see the price.
  - Acceptance: date inputs required; price shown on room card; modal shows total.
- As a logged-in user, I want to create a reservation so my stay is confirmed.
  - Acceptance: booking form validates dates; reservation saved; success message shown.
- As a logged-in user, I want to edit or delete my reservation so I can manage my plans.
  - Acceptance: only the owner can edit/delete; success message shown.

## Accounts
- As a user, I want to sign up and log in so I can manage my reservations.
  - Acceptance: unique email enforced; login state shown in nav.
- As a user, I want to log out so I can end my session securely.
  - Acceptance: logout link available on every page.

## Comments
- As a logged-in user, I want to leave a comment on the rooms page.
  - Acceptance: comment saved with timestamp and username.

## Admin
- As an admin, I want to manage rooms and reservations in Django admin.
  - Acceptance: Room and Reservation visible and editable in admin.
