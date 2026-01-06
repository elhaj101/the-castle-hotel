# Report 1: Project Alignment Assessment

## Executive Summary
This report outlines discrepancies between the current project implementation and the requirements defined in `docs/user_stories.md` and `README.md` (Pass, Merit, Distinction criteria). Several critical issues were identified ranging from core business logic flaws to security vulnerabilities.

## 1. Functional Logic & Data Model (LO2, LO7)
### Critical Flaw: Room Availability Logic
- **Issue**: The current booking implementation permanently disables a room after a single reservation. In `rooms/views.py`, the code sets `room.is_available = False` upon a successful booking.
- **Impact**: Once a room is booked for *any* dates, it becomes unavailable for *all* future dates. This fundamentally violates the requirement for a hotel booking system where rooms should be available date-wise.
- **Alignment Failure**: Fails "Implement a data model... to meet given needs in a particular real-world domain" (LO2) and "Design a custom data model that fits the purpose" (LO7).

### Data Types
- **Issue**: `Reservation.children` is a `CharField` rather than an `IntegerField`.
- **Issue**: `Reservation.extras` is a plain `CharField`, which may be difficult to manage or query compared to a ManyToMany relationship or JSONField.

## 2. Security & Configuration (LO6)
### Hardcoded Secrets
- **Issue**: `SECRET_KEY` is hardcoded in `settings.py`.
- **Alignment Failure**: Explicitly violates Pass/Merit criteria: "passwords and secret keys... are never committed to the repository".

### Debug Mode
- **Issue**: `DEBUG = True` is hardcoded in `settings.py`.
- **Alignment Failure**: Violates "ensure... DEBUG mode is turned off" for deployment.

### Database Configuration
- **Issue**: `settings.py` only configures SQLite (`django.db.backends.sqlite3`). There is no configuration for PostgreSQL, despite the README stating: "The database was migrated from Railway to Heroku Postgres".
- **Alignment Failure**: Discrepancy between documentation and code; limits deployment readiness.

## 3. Testing (LO4)
### Missing Test Coverage
- **Issue**: `comments/tests.py` is empty. The Comments feature is a core requirement ("Post and delete comments"), yet it lacks automated verification.
- **Alignment Failure**: Fails "Create manual and/or automated tests... within the entire web application".

## 4. Documentation & Best Practices (LO1, LO5)
- **Code Comments**: Some complex logic (e.g., date overlap checks, which are actually missing in the model) lacks explanatory comments.
- **README Alignment**: The README mentions "Heroku Postgres add-on" but the code does not support it out-of-the-box without manual `settings.py` changes.

## Recommendations
1.  **Refactor Booking Logic**: Remove `is_available` from the `Room` model or decoupling it from reservations. Implement date-range overlap checks in `Reservation.clean()` or the view to determine availability.
2.  **Secure Settings**: Use `os.environ.get()` for `SECRET_KEY`, `DEBUG`, and `DATABASE_URL` (using `dj_database_url` or similar).
3.  **Implement Tests**: Add unit tests for the Comments app.
4.  **Fix Data Model**: Change `children` to `IntegerField` for better validation.
