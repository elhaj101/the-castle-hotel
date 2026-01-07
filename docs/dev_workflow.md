# Dev Workflow (Local First)

This workflow keeps development local and ensures every page, function, and
feature is verified end-to-end before production work begins.

## Start of Session
- Pull latest changes and confirm working tree status.
- Run migrations if needed.
- Start the dev server and keep the browser open.

## Global Checklist (Pages, Flows, Features)
- Home page with clear CTA to booking (content/home.html)
- Rooms list with pricing cards and booking entry (rooms/room_list.html)
- Room details + booking modal (rooms/interactive/details.html)
- Reservation create form (rooms/reservation form)
- Reservations list page (rooms/reservations.html)
- Reservation edit page (rooms/reservation_edit.html)
- Reservation delete confirmation (rooms/reservation_confirm_delete.html)
- Login, Signup, Logout (templates/registration/*)
- Profile delete and delete comments (accounts/views + template)
- Comment create/delete (comments/views + templates)
- Admin panel coverage (Room, Reservation, Comment, User, Guest if present)
- Navigation reflects auth state (templates/base.html)
- Pricing calculation and date validation (rooms/views + rooms/forms)
- User feedback messages for all create/edit/delete actions
- Responsive layout and accessibility checks
- Test coverage (Python + manual JS/UI)

## Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7)
- Map every README requirement to LO1-LO7 in a tracking checklist.
- Confirm user stories in docs/user_stories.md match implemented features.
- Document UX rationale and wireframes usage in README.
- Validate naming conventions and file structure (no spaces, lowercase).
- Review page inventory and ensure templates exist for all flows.

## Sprint 2 - Data Model and Core Booking (LO2, LO7)
- Validate Room, Reservation, Comment models and relationships.
- Confirm fields and constraints (dates, availability, total price).
- Implement/verify reservation creation flow end-to-end.
- Ensure schema summary in README matches actual models.
- Confirm migrations reflect current model state.

## Sprint 3 - Reservation Management and Business Logic (LO2, LO3)
- Reservation list view (owner only).
- Reservation edit view with validation and feedback.
- Reservation delete confirmation and delete action.
- Enforce auth/ownership checks on all reservation actions.
- Ensure login state is visible in UI and restricted pages are protected.

## Sprint 4 - Comments and Profile Management (LO2, LO3)
- Comment create and delete with user ownership checks.
- Profile delete flow and cascade delete of user comments (if required).
- Confirm feedback messages for all comment/profile actions.

## Sprint 5 - Frontend Polish and Accessibility (LO1)
- Navigation highlights Rooms, Contact, Account, Reservations.
- Responsive layout verified on mobile and desktop.
- Accessibility pass (labels, headings, contrast, focus states).
- Ensure CTA and booking flow are clear and consistent.

## Sprint 6 - Testing and Documentation (LO4, LO5)
- Python tests: reservations create/edit/delete, auth checks, comments CRUD.
- Manual JS/UI tests: modal open, price updates, date handling.
- Document all tests in README with steps and expected results.
- Confirm Git commit history uses descriptive messages.

## Sprint 7 - Deployment and Final QA (LO6)
- Verify SECRET_KEY, DEBUG, MYSQL_* handling.
- Ensure Procfile, requirements.txt, and static config are correct.
- Run migrations and collectstatic in production flow.
- Check for broken links, commented-out code, and missing templates.

## Done Criteria (All LO1-LO7)
- All pages and features above are implemented and tested.
- README is complete: setup, deployment, testing, data model, UX.
- Deployed app matches local behavior with DEBUG off.

## Execution Details (Local Verification)
- Page inventory pass: open each template route and confirm context renders.
- Core booking flow: home CTA -> rooms list -> room details -> booking modal -> reservation create.
- Reservation management: list owner-only, edit saves, delete removes, ownership checks hold.
- Accounts and auth: signup/login/logout work; profile delete confirms and removes user data.
- Comments: add/delete work with ownership enforcement and feedback messages.
- UI/accessibility: mobile layout has no horizontal scroll; labels/focus/errors are visible.
- Testing/docs: run Python tests and record results in README; complete manual JS/UI checklist and record in README.
- Cleanup and git: remove local artifacts (.pyc, .DS_Store, db.sqlite3), update .gitignore if needed, commit with clear scoped messages.
