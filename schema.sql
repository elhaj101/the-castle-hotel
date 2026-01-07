-- Create and use the castle_hotel database
CREATE DATABASE IF NOT EXISTS castle_hotel;
USE castle_hotel;

-- Create Users table
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create Rooms table
CREATE TABLE IF NOT EXISTS rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(50) NOT NULL,
    type VARCHAR(50) NOT NULL,
    price_per_night DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create Room Reservations table
CREATE TABLE IF NOT EXISTS room_reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    room_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'confirmed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chk_room_reservations_dates CHECK (end_date > start_date),
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create Treatments table
CREATE TABLE IF NOT EXISTS treatments (
    treatment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    duration INT NOT NULL,
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create Appointments table
CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    treatment_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'scheduled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (treatment_id) REFERENCES treatments(treatment_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Create Tables table
CREATE TABLE IF NOT EXISTS tables (
    table_id INT AUTO_INCREMENT PRIMARY KEY,
    table_number VARCHAR(50) NOT NULL,
    capacity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- Create Restaurant Reservations table
CREATE TABLE IF NOT EXISTS restaurant_reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    table_id INT NOT NULL,
    reservation_date DATE NOT NULL,
    reservation_time TIME NOT NULL,
    status VARCHAR(20) DEFAULT 'confirmed',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (table_id) REFERENCES tables(table_id) ON DELETE CASCADE
) ENGINE=InnoDB;

-- Overlap enforcement for restaurant reservations should be handled in application logic.

-- Add indexes for performance
CREATE INDEX idx_room_reservations_user_id ON room_reservations(user_id);
CREATE INDEX idx_room_reservations_room_id ON room_reservations(room_id);
CREATE INDEX idx_appointments_user_id ON appointments(user_id);
CREATE INDEX idx_appointments_treatment_id ON appointments(treatment_id);
CREATE INDEX idx_restaurant_reservations_user_id ON restaurant_reservations(user_id);
CREATE INDEX idx_restaurant_reservations_table_id ON restaurant_reservations(table_id);
