create schema if not exists raw_data;

CREATE TABLE IF NOT EXISTS flight_data (
    id SERIAL PRIMARY KEY,
    icao24 VARCHAR(20),
    callsign VARCHAR(20),
    longitude DECIMAL(9,6),
    latitude DECIMAL(9,6),
    velocity FLOAT,
    captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);