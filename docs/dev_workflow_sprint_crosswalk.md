# Sprint Plan to Dev Workflow Crosswalk

This crosswalk maps every item in `docs/sprint_plan.md` to its matching step in
`docs/dev_workflow.md`.

## Global Checklist (Pages, Flows, Features)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Home page with clear CTA to booking (content/home.html) | Global Checklist (Pages, Flows, Features) -> Home page with clear CTA to booking (content/home.html) |
| Rooms list with pricing cards and booking entry (rooms/room_list.html) | Global Checklist (Pages, Flows, Features) -> Rooms list with pricing cards and booking entry (rooms/room_list.html) |
| Room details + booking modal (rooms/interactive/details.html) | Global Checklist (Pages, Flows, Features) -> Room details + booking modal (rooms/interactive/details.html) |
| Reservation create form (rooms/reservation form) | Global Checklist (Pages, Flows, Features) -> Reservation create form (rooms/reservation form) |
| Reservations list page (rooms/reservations.html) | Global Checklist (Pages, Flows, Features) -> Reservations list page (rooms/reservations.html) |
| Reservation edit page (rooms/reservation_edit.html) | Global Checklist (Pages, Flows, Features) -> Reservation edit page (rooms/reservation_edit.html) |
| Reservation delete confirmation (rooms/reservation_confirm_delete.html) | Global Checklist (Pages, Flows, Features) -> Reservation delete confirmation (rooms/reservation_confirm_delete.html) |
| Login, Signup, Logout (templates/registration/*) | Global Checklist (Pages, Flows, Features) -> Login, Signup, Logout (templates/registration/*) |
| Profile delete and delete comments (accounts/views + template) | Global Checklist (Pages, Flows, Features) -> Profile delete and delete comments (accounts/views + template) |
| Comment create/delete (comments/views + templates) | Global Checklist (Pages, Flows, Features) -> Comment create/delete (comments/views + templates) |
| Admin panel coverage (Room, Reservation, Comment, User, Guest if present) | Global Checklist (Pages, Flows, Features) -> Admin panel coverage (Room, Reservation, Comment, User, Guest if present) |
| Navigation reflects auth state (templates/base.html) | Global Checklist (Pages, Flows, Features) -> Navigation reflects auth state (templates/base.html) |
| Pricing calculation and date validation (rooms/views + rooms/forms) | Global Checklist (Pages, Flows, Features) -> Pricing calculation and date validation (rooms/views + rooms/forms) |
| User feedback messages for all create/edit/delete actions | Global Checklist (Pages, Flows, Features) -> User feedback messages for all create/edit/delete actions |
| Responsive layout and accessibility checks | Global Checklist (Pages, Flows, Features) -> Responsive layout and accessibility checks |
| Test coverage (Python + manual JS/UI) | Global Checklist (Pages, Flows, Features) -> Test coverage (Python + manual JS/UI) |

## Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Map every README requirement to LO1-LO7 in a tracking checklist. | Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7) -> Map every README requirement to LO1-LO7 in a tracking checklist. |
| Confirm user stories in docs/user_stories.md match implemented features. | Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7) -> Confirm user stories in docs/user_stories.md match implemented features. |
| Document UX rationale and wireframes usage in README. | Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7) -> Document UX rationale and wireframes usage in README. |
| Validate naming conventions and file structure (no spaces, lowercase). | Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7) -> Validate naming conventions and file structure (no spaces, lowercase). |
| Review page inventory and ensure templates exist for all flows. | Sprint 1 - Requirements Mapping and UX Foundations (LO1, LO5, LO7) -> Review page inventory and ensure templates exist for all flows. |

## Sprint 2 - Data Model and Core Booking (LO2, LO7)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Validate Room, Reservation, Comment models and relationships. | Sprint 2 - Data Model and Core Booking (LO2, LO7) -> Validate Room, Reservation, Comment models and relationships. |
| Confirm fields and constraints (dates, availability, total price). | Sprint 2 - Data Model and Core Booking (LO2, LO7) -> Confirm fields and constraints (dates, availability, total price). |
| Implement/verify reservation creation flow end-to-end. | Sprint 2 - Data Model and Core Booking (LO2, LO7) -> Implement/verify reservation creation flow end-to-end. |
| Ensure schema summary in README matches actual models. | Sprint 2 - Data Model and Core Booking (LO2, LO7) -> Ensure schema summary in README matches actual models. |
| Confirm migrations reflect current model state. | Sprint 2 - Data Model and Core Booking (LO2, LO7) -> Confirm migrations reflect current model state. |

## Sprint 3 - Reservation Management and Business Logic (LO2, LO3)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Reservation list view (owner only). | Sprint 3 - Reservation Management and Business Logic (LO2, LO3) -> Reservation list view (owner only). |
| Reservation edit view with validation and feedback. | Sprint 3 - Reservation Management and Business Logic (LO2, LO3) -> Reservation edit view with validation and feedback. |
| Reservation delete confirmation and delete action. | Sprint 3 - Reservation Management and Business Logic (LO2, LO3) -> Reservation delete confirmation and delete action. |
| Enforce auth/ownership checks on all reservation actions. | Sprint 3 - Reservation Management and Business Logic (LO2, LO3) -> Enforce auth/ownership checks on all reservation actions. |
| Ensure login state is visible in UI and restricted pages are protected. | Sprint 3 - Reservation Management and Business Logic (LO2, LO3) -> Ensure login state is visible in UI and restricted pages are protected. |

## Sprint 4 - Comments and Profile Management (LO2, LO3)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Comment create and delete with user ownership checks. | Sprint 4 - Comments and Profile Management (LO2, LO3) -> Comment create and delete with user ownership checks. |
| Profile delete flow and cascade delete of user comments (if required). | Sprint 4 - Comments and Profile Management (LO2, LO3) -> Profile delete flow and cascade delete of user comments (if required). |
| Confirm feedback messages for all comment/profile actions. | Sprint 4 - Comments and Profile Management (LO2, LO3) -> Confirm feedback messages for all comment/profile actions. |

## Sprint 5 - Frontend Polish and Accessibility (LO1)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Navigation highlights Rooms, Contact, Account, Reservations. | Sprint 5 - Frontend Polish and Accessibility (LO1) -> Navigation highlights Rooms, Contact, Account, Reservations. |
| Responsive layout verified on mobile and desktop. | Sprint 5 - Frontend Polish and Accessibility (LO1) -> Responsive layout verified on mobile and desktop. |
| Accessibility pass (labels, headings, contrast, focus states). | Sprint 5 - Frontend Polish and Accessibility (LO1) -> Accessibility pass (labels, headings, contrast, focus states). |
| Ensure CTA and booking flow are clear and consistent. | Sprint 5 - Frontend Polish and Accessibility (LO1) -> Ensure CTA and booking flow are clear and consistent. |

## Sprint 6 - Testing and Documentation (LO4, LO5)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Python tests: reservations create/edit/delete, auth checks, comments CRUD. | Sprint 6 - Testing and Documentation (LO4, LO5) -> Python tests: reservations create/edit/delete, auth checks, comments CRUD. |
| Manual JS/UI tests: modal open, price updates, date handling. | Sprint 6 - Testing and Documentation (LO4, LO5) -> Manual JS/UI tests: modal open, price updates, date handling. |
| Document all tests in README with steps and expected results. | Sprint 6 - Testing and Documentation (LO4, LO5) -> Document all tests in README with steps and expected results. |
| Confirm Git commit history uses descriptive messages. | Sprint 6 - Testing and Documentation (LO4, LO5) -> Confirm Git commit history uses descriptive messages. |

## Sprint 7 - Deployment and Final QA (LO6)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| Verify SECRET_KEY, DEBUG, DATABASE_URL handling. | Sprint 7 - Deployment and Final QA (LO6) -> Verify SECRET_KEY, DEBUG, DATABASE_URL handling. |
| Ensure Procfile, requirements.txt, and static config are correct. | Sprint 7 - Deployment and Final QA (LO6) -> Ensure Procfile, requirements.txt, and static config are correct. |
| Run migrations and collectstatic in production flow. | Sprint 7 - Deployment and Final QA (LO6) -> Run migrations and collectstatic in production flow. |
| Check for broken links, commented-out code, and missing templates. | Sprint 7 - Deployment and Final QA (LO6) -> Check for broken links, commented-out code, and missing templates. |

## Done Criteria (All LO1-LO7)
| Sprint Plan Item | Dev Workflow Step |
| --- | --- |
| All pages and features above are implemented and tested. | Done Criteria (All LO1-LO7) -> All pages and features above are implemented and tested. |
| README is complete: setup, deployment, testing, data model, UX. | Done Criteria (All LO1-LO7) -> README is complete: setup, deployment, testing, data model, UX. |
| Deployed app matches local behavior with DEBUG off. | Done Criteria (All LO1-LO7) -> Deployed app matches local behavior with DEBUG off. |
