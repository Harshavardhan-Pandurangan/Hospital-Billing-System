DROP DATABASE HospitalBilling;

CREATE DATABASE HospitalBilling;
USE HospitalBilling;

CREATE TABLE Users (
    usrname VARCHAR(255) NOT NULL UNIQUE,
    passwrd VARCHAR(255) NOT NULL,
    id INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);

CREATE Table Patients (
    patient_id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    dob VARCHAR(20) NOT NULL,
    doe DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    PRIMARY KEY (patient_id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE Table Bills (
    bill_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    patient_id INT NOT NULL,
    amount FLOAT NOT NULL DEFAULT 0,
    problem VARCHAR(300) NOT NULL,
    doa DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dod DATETIME DEFAULT NULL,
    PRIMARY KEY (bill_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE Table Payments (
    payment_id INT NOT NULL AUTO_INCREMENT,
    bill_id INT NOT NULL,
    amount FLOAT NOT NULL DEFAULT 0,
    dop DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (bill_id) REFERENCES Bills(bill_id)
);

INSERT INTO Users (usrname, passwrd) VALUES ('admin', 'admin');
INSERT INTO Users (usrname, passwrd) VALUES ('user', 'user');
