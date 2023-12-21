'''
Hospital billing system using MySQL Connector and Database

- Harshamithran P
- Shreyas B

3 databases used for users, patients details and billing details
UI built using Tkinter
'''

# Importing all the modules required
import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time

'''
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
    patient_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    gender VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    problem VARCHAR(300) NOT NULL,
    doe DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    PRIMARY KEY (patient_id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE Table Bills (
    bill_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    patient_id INT NOT NULL,
    amount INT NOT NULL DEFAULT 0,
    doa DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    dod DATETIME DEFAULT NULL,
    PRIMARY KEY (bill_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

CREATE Table Payments (
    payment_id INT NOT NULL AUTO_INCREMENT,
    bill_id INT NOT NULL,
    amount INT NOT NULL,
    dop DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (bill_id) REFERENCES Bills(bill_id)
);

INSERT INTO Users (usrname, passwrd) VALUES ('admin', 'admin');
INSERT INTO Users (usrname, passwrd) VALUES ('user', 'user');
'''


# Making the connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsha1234",
    database="HospitalBilling"
)


# defining functions for all the functionalities

# 1 - login function
def login():
    global mydb
    global usrname
    global passwrd

    usrname = login_usrname_entry.get()
    passwrd = login_passwrd_entry.get()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Users WHERE usrname = %s AND passwrd = %s", (usrname, passwrd))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Username or Password")
    else:
        messagebox.showinfo("Success", "Login Successful")

        login_usrname_entry.delete(0, END)
        login_passwrd_entry.delete(0, END)

        global user_id
        user_id = result[0][2]

        LoginWindow.withdraw()
        MainMenuWindow.deiconify()


# Creating all the windows required

def exit():
    LoginWindow.destroy()
    MainMenuWindow.destroy()
    PatientDetailsCreateWindow.destroy()
    PatientDetailsUpdateWindow.destroy()
    PatientDetailsViewWindow.destroy()
    BillingDetailsAddWindow.destroy()
    BillingDetailsUpdateWindow.destroy()
    BillingDetailsViewWindow.destroy()


root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width / 2) - (500 / 2))
y_position = int((screen_height / 2) - (500 / 2))
root.destroy()

# 1 - Login Window
LoginWindow = Tk()
LoginWindow.title("Login")
LoginWindow.geometry(f"500x500+{x_position}+{y_position}")
LoginWindow.resizable(0, 0)
LoginWindow.configure(bg="white")
LoginWindow.protocol("WM_DELETE_WINDOW", exit)

# 2 - Main Menu Window
MainMenuWindow = Tk()
MainMenuWindow.title("Main Menu")
MainMenuWindow.geometry(f"500x500+{x_position}+{y_position}")
MainMenuWindow.resizable(0, 0)
MainMenuWindow.configure(bg="white")
MainMenuWindow.withdraw()
MainMenuWindow.protocol("WM_DELETE_WINDOW", exit)

# 3 - Patient Details Create Window
PatientDetailsCreateWindow = Tk()
PatientDetailsCreateWindow.title("Patient Details Create")
PatientDetailsCreateWindow.geometry(f"500x500+{x_position}+{y_position}")
PatientDetailsCreateWindow.resizable(0, 0)
PatientDetailsCreateWindow.configure(bg="white")
PatientDetailsCreateWindow.withdraw()
PatientDetailsCreateWindow.protocol("WM_DELETE_WINDOW", exit)

# 4 - Patient Details Update Window
PatientDetailsUpdateWindow = Tk()
PatientDetailsUpdateWindow.title("Patient Details Update")
PatientDetailsUpdateWindow.geometry(f"500x500+{x_position}+{y_position}")
PatientDetailsUpdateWindow.resizable(0, 0)
PatientDetailsUpdateWindow.configure(bg="white")
PatientDetailsUpdateWindow.withdraw()
PatientDetailsUpdateWindow.protocol("WM_DELETE_WINDOW", exit)

# 5 - Patient Details View Window
PatientDetailsViewWindow = Tk()
PatientDetailsViewWindow.title("Patient Details View")
PatientDetailsViewWindow.geometry(f"500x500+{x_position}+{y_position}")
PatientDetailsViewWindow.resizable(0, 0)
PatientDetailsViewWindow.configure(bg="white")
PatientDetailsViewWindow.withdraw()
PatientDetailsViewWindow.protocol("WM_DELETE_WINDOW", exit)

# 6 - Billing Details Add Window
BillingDetailsAddWindow = Tk()
BillingDetailsAddWindow.title("Billing Details Add")
BillingDetailsAddWindow.geometry(f"500x500+{x_position}+{y_position}")
BillingDetailsAddWindow.resizable(0, 0)
BillingDetailsAddWindow.configure(bg="white")
BillingDetailsAddWindow.withdraw()
BillingDetailsAddWindow.protocol("WM_DELETE_WINDOW", exit)

# 7 - Billing Details Update Window
BillingDetailsUpdateWindow = Tk()
BillingDetailsUpdateWindow.title("Billing Details Update")
BillingDetailsUpdateWindow.geometry(f"500x500+{x_position}+{y_position}")
BillingDetailsUpdateWindow.resizable(0, 0)
BillingDetailsUpdateWindow.configure(bg="white")
BillingDetailsUpdateWindow.withdraw()
BillingDetailsUpdateWindow.protocol("WM_DELETE_WINDOW", exit)

# 8 - Billing Details View Window
BillingDetailsViewWindow = Tk()
BillingDetailsViewWindow.title("Billing Details View")
BillingDetailsViewWindow.geometry(f"500x500+{x_position}+{y_position}")
BillingDetailsViewWindow.resizable(0, 0)
BillingDetailsViewWindow.configure(bg="white")
BillingDetailsViewWindow.withdraw()
BillingDetailsViewWindow.protocol("WM_DELETE_WINDOW", exit)


# Adding all elements to all the windows

# 1 - Login Window

# 2 - Main Menu Window

# 3 - Patient Details Create Window

# 4 - Patient Details Update Window

# 5 - Patient Details View Window

# 6 - Billing Details Add Window

# 7 - Billing Details View Window

# 8 - Billing Details Update Window


# Mainloops for all the windows

LoginWindow.mainloop()
MainMenuWindow.mainloop()
PatientDetailsCreateWindow.mainloop()
PatientDetailsUpdateWindow.mainloop()
PatientDetailsViewWindow.mainloop()
BillingDetailsAddWindow.mainloop()
BillingDetailsViewWindow.mainloop()
BillingDetailsUpdateWindow.mainloop()


# End of the program
# Thank you
