# The Castle Hotel

A hotel website with booking features.

## User Features

As a user, I want to:
- Book rooms.
- Book a restaurant reservation.
- Book a wellness session.
- Sign up and sign in to my account.
- Receive email confirmation of booking.

## Owner Features

As an owner, I want the user to:
- Sign up/in with email and password.
- Have social media links available in the footer.
- Post and delete comments on the restaurant reservation page or the wellness session page.

## Data Model Overview

| **Entity**       | **Fields**                                                                                      | **Relationships**                                                                                              | **Constraints**                                                                 | **Notes**                                                                                           |
|-------------------|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **User**         | - `first_name`: CharField (max_length=50)<br>- `last_name`: CharField (max_length=50)<br>- `email`: EmailField (unique)<br>- `phone_number`: CharField (max_length=15, optional) | - **One-to-Many with Reservation**: A single user can create multiple reservations for different rooms and dates. | - `email` must be unique.<br>- `phone_number` can be nullable for guest users. | - Represents guests or registered users.<br>- Uses Django’s built-in `User` model for authentication.<br>- Scalable for adding profiles (e.g., address, preferences). |
| **Room**         | - `room_number`: CharField (max_length=10, unique)<br>- `room_type`: CharField (max_length=1, choices: [('S', 'Single'), ('D', 'Double'), ('F', 'Family')])<br>- `price`: DecimalField (max_digits=10, decimal_places=2) | - **One-to-Many with Reservation**: A room can be booked in multiple reservations over time (typically one active reservation per date range). | - `room_number` is unique.<br>- `price` must be positive.<br>- `room_type` restricted to 'S', 'D', or 'F'. | - Represents individual hotel rooms.<br>- `room_type` choices ensure consistency (Single, Double, Family).<br>- Easily extendable for amenities (e.g., Wi-Fi, view). |
| **Reservation**  | - `user`: ForeignKey (to User, on_delete=CASCADE)<br>- `room`: ForeignKey (to Room, on_delete=CASCADE)<br>- `check_in_date`: DateField<br>- `check_out_date`: DateField | - **Many-to-One with User**: Each reservation is tied to exactly one user.<br>- **Many-to-One with Room**: Each reservation is tied to exactly one room. | - `check_in_date` < `check_out_date`.<br>- Foreign keys enforce referential integrity.<br>- CASCADE deletion ensures no orphaned records. | - Core entity for booking management.<br>- Ensures data integrity by linking users and rooms.<br>- Can be extended for status (e.g., confirmed, canceled). |

### Additional Details

- **Primary Keys**: Each model (`User`, `Room`, `Reservation`) automatically includes an `id` field as the primary key (auto-incrementing integer) unless overridden.
- **Foreign Key Behavior**: 
    - `on_delete=models.CASCADE` ensures that if a `User` or `Room` is deleted, associated `Reservation` records are also removed, maintaining data consistency.
- **Scalability**:
    - **User**: Can add fields like `address`, `loyalty_points`, or `preferences` for personalized services.
    - **Room**: Can include attributes like `capacity`, `amenities`, or `availability_status`.
    - **Reservation**: Can support fields like `total_cost`, `status`, or `special_requests`.
- **Data Integrity**:
    - Unique constraints on `email` (User) and `room_number` (Room) prevent duplicates.
    - Date validation in `Reservation` ensures logical booking periods (`check_in_date` < `check_out_date`).
- **User-Centric Design**: The structure prioritizes the user as the central entity, streamlining reservation management and enhancing user experience.
- **Room Type Choices**:
    - `S` (Single): Ideal for solo travelers.
    - `D` (Double): Suitable for couples or pairs.
    - `F` (Family): Designed for larger groups or families.
- **String Representation**:
    - `Room`: Returns formatted string like "Single 101" or "Family 305".
    - `Reservation`: Returns descriptive string like "Reservation for username in Single 101".

### Why This Design Shines

- **Clarity**: Clearly defines entities, fields, and relationships for easy understanding.
- **Flexibility**: Supports future enhancements without breaking existing functionality.
- **Robustness**: Enforces constraints to prevent invalid data (e.g., overlapping bookings, invalid room types).
- **User-Friendly**: Aligns with real-world hotel operations, focusing on user interactions and room availability.
