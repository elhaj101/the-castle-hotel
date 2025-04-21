-- Connect to the castle_hotel database
     \c castle_hotel;

     -- Enable btree_gist extension for exclusion constraint
     CREATE EXTENSION IF NOT EXISTS btree_gist;

     -- Create Users table
     CREATE TABLE IF NOT EXISTS users (
         user_id SERIAL PRIMARY KEY,
         name VARCHAR(100) NOT NULL,
         email VARCHAR(255) UNIQUE NOT NULL,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );

     -- Create Rooms table
     CREATE TABLE IF NOT EXISTS rooms (
         room_id SERIAL PRIMARY KEY,
         room_number VARCHAR(50) NOT NULL,
         type VARCHAR(50) NOT NULL,
         price_per_night DECIMAL(10, 2),
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );

     -- Create Room Reservations table
     CREATE TABLE IF NOT EXISTS room_reservations (
         reservation_id SERIAL PRIMARY KEY,
         user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
         room_id INTEGER NOT NULL REFERENCES rooms(room_id) ON DELETE CASCADE,
         start_date DATE NOT NULL,
         end_date DATE NOT NULL,
         status VARCHAR(20) DEFAULT 'confirmed',
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         CHECK (end_date > start_date)
     );

     -- Create Treatments table
     CREATE TABLE IF NOT EXISTS treatments (
         treatment_id SERIAL PRIMARY KEY,
         name VARCHAR(100) NOT NULL,
         duration INTEGER NOT NULL,
         price DECIMAL(10, 2),
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );

     -- Create Appointments table
     CREATE TABLE IF NOT EXISTS appointments (
         appointment_id SERIAL PRIMARY KEY,
         user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
         treatment_id INTEGER NOT NULL REFERENCES treatments(treatment_id) ON DELETE CASCADE,
         appointment_date DATE NOT NULL,
         appointment_time TIME NOT NULL,
         status VARCHAR(20) DEFAULT 'scheduled',
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );

     -- Create Tables table
     CREATE TABLE IF NOT EXISTS tables (
         table_id SERIAL PRIMARY KEY,
         table_number VARCHAR(50) NOT NULL,
         capacity INTEGER NOT NULL,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );

     -- Create Restaurant Reservations table
     CREATE TABLE IF NOT EXISTS restaurant_reservations (
         reservation_id SERIAL PRIMARY KEY,
         user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
         table_id INTEGER NOT NULL REFERENCES tables(table_id) ON DELETE CASCADE,
         reservation_date DATE NOT NULL,
         reservation_time TIME NOT NULL,
         status VARCHAR(20) DEFAULT 'confirmed',
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );

     -- Add exclusion constraint for non-overlapping restaurant reservations (2-hour duration)
     ALTER TABLE restaurant_reservations
     ADD CONSTRAINT no_overlapping_reservations
     EXCLUDE USING gist (
         table_id WITH =,
         tsrange(
             (reservation_date + reservation_time)::timestamp,
             (reservation_date + reservation_time + INTERVAL '2 hours')::timestamp
         ) WITH &&
     );

     -- Add indexes for performance
     CREATE INDEX IF NOT EXISTS idx_room_reservations_user_id ON room_reservations(user_id);
     CREATE INDEX IF NOT EXISTS idx_room_reservations_room_id ON room_reservations(room_id);
     CREATE INDEX IF NOT EXISTS idx_appointments_user_id ON appointments(user_id);
     CREATE INDEX IF NOT EXISTS idx_appointments_treatment_id ON appointments(treatment_id);
     CREATE INDEX IF NOT EXISTS idx_restaurant_reservations_user_id ON restaurant_reservations(user_id);
     CREATE INDEX IF NOT EXISTS idx_restaurant_reservations_table_id ON restaurant_reservations(table_id);