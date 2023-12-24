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

global user_id
user_id = 0

global patient_id
patient_id = 0

global bill_id
bill_id = 0


# defining functions for all the functionalities

# 1 - login function
def login():
    print("Login function called")

    global mydb

    usrname = login_usrname_entry.get('1.0', END)
    passwrd = login_passwrd_entry.get('1.0', END)

    usrname = usrname[:-1]
    passwrd = passwrd[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Users WHERE usrname = %s AND passwrd = %s;", (usrname, passwrd))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Username or Password")
    else:
        messagebox.showinfo("Success", "Login Successful")

        login_usrname_entry.delete('1.0', END)
        login_passwrd_entry.delete('1.0', END)

        global user_id
        user_id = result[0][2]

        LoginWindow.withdraw()
        MainMenuWindow.deiconify()

# 2 - logout function
def logout():
    MainMenuWindow.withdraw()
    LoginWindow.deiconify()

    global user_id
    user_id = 0

# 3 - patient details create function
def patient_details_create():
    print("Patient Details Create function called")

    global mydb
    global user_id

    name = patient_details_create_name_entry.get('1.0', END)
    address = patient_details_create_address_entry.get('1.0', END)
    phone = patient_details_create_phone_entry.get('1.0', END)
    gender = patient_details_create_gender_entry.get('1.0', END)
    age = patient_details_create_age_entry.get('1.0', END)

    name = name[:-1]
    address = address[:-1]
    phone = phone[:-1]
    gender = gender[:-1]
    age = age[:-1]

    mycursor = mydb.cursor()
    mycursor.execute('''INSERT INTO Patients(name, address, phone, gender, age, user_id)
        VALUES(%s, %s, %s, %s, %s, %s);''', (name, address, phone, gender, age, user_id))
    result = mycursor.fetchall()
    mydb.commit()

    PatientDetailsCreateWindow.withdraw()
    MainMenuWindow.deiconify()

    messagebox.showinfo("Success", "Patient Details Created Successfully")

    patient_details_create_name_entry.delete('1.0', END)
    patient_details_create_address_entry.delete('1.0', END)
    patient_details_create_phone_entry.delete('1.0', END)
    patient_details_create_gender_entry.delete('1.0', END)
    patient_details_create_age_entry.delete('1.0', END)

# 4 - patient details retreive function
def patient_details_retreive():
    print("Patient Details Retreive function called")

    global mydb
    global user_id

    patient_id_entry = patient_details_update_id_entry.get('1.0', END)

    patient_id_entry = patient_id_entry[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Patients WHERE patient_id = %s;", (patient_id_entry, ))

    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Patient ID")
    else:
        global patient_id
        patient_id = result[0][0]

        patient_details_update_name_entry.insert(END, result[0][1])
        patient_details_update_address_entry.insert(END, result[0][2])
        patient_details_update_phone_entry.insert(END, result[0][3])
        patient_details_update_gender_entry.insert(END, result[0][4])
        patient_details_update_age_entry.insert(END, result[0][5])

# 5 - patient details update function
def patient_details_update():
    print("Patient Details Update function called")

    global mydb
    global user_id
    global patient_id

    name = patient_details_update_name_entry.get('1.0', END)
    address = patient_details_update_address_entry.get('1.0', END)
    phone = patient_details_update_phone_entry.get('1.0', END)
    gender = patient_details_update_gender_entry.get('1.0', END)
    age = patient_details_update_age_entry.get('1.0', END)

    name = name[:-1]
    address = address[:-1]
    phone = phone[:-1]
    gender = gender[:-1]
    age = age[:-1]

    mycursor = mydb.cursor()
    sql = "UPDATE Patients SET name = %s, address = %s, phone = %s, gender = %s, age = %s, user_id = %s WHERE patient_id = %s;"
    val = (name, address, phone, gender, age, user_id, patient_id)
    mycursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("Success", "Patient details updated successfully!")

# 6 - patient details view function
def patient_details_view():
    print("Patient Details View function called")

    global mydb
    global user_id

    patient_id_entry = patient_details_view_id_entry.get('1.0', END)

    patient_id_entry = patient_id_entry[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Patients WHERE patient_id = %s;", (patient_id_entry, ))

    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Patient ID")
    else:
        patient_details_view_name_entry.insert(END, result[0][1])
        patient_details_view_address_entry.insert(END, result[0][2])
        patient_details_view_phone_entry.insert(END, result[0][3])
        patient_details_view_gender_entry.insert(END, result[0][4])
        patient_details_view_age_entry.insert(END, result[0][5])

        patient_details_view_name_entry.config(state=DISABLED)
        patient_details_view_address_entry.config(state=DISABLED)
        patient_details_view_phone_entry.config(state=DISABLED)
        patient_details_view_gender_entry.config(state=DISABLED)
        patient_details_view_age_entry.config(state=DISABLED)

# 7 - billing details add function
def billing_details_add():
    print("Billing Details Add function called")

    global mydb
    global user_id

    patient_id = billing_details_add_patient_id_entry.get('1.0', END)
    problem = billing_details_add_problem_entry.get('1.0', END)

    patient_id = patient_id[:-1]
    problem = problem[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Patients WHERE patient_id = %s;", (patient_id, ))
    result = mycursor.fetchall()

    print(result)

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Patient ID")
    else:
        # check if there is a existing bill for the patient where dod is null, which means the patient has to complete the previous payment
        mycursor.execute("SELECT * FROM Bills WHERE patient_id = %s AND dod IS NULL;", (patient_id, ))
        result = mycursor.fetchall()

        if len(result) == 0:
            mycursor.execute('''INSERT INTO Bills(user_id, patient_id, problem)
                VALUES(%s, %s, %s);''', (user_id, patient_id, problem))
            mydb.commit()

            messagebox.showinfo("Success", "Bill added successfully!")
        else:
            messagebox.showerror("Error", "Patient has to complete the payment for the previous bill")

    billing_details_add_patient_id_entry.delete('1.0', END)
    billing_details_add_problem_entry.delete('1.0', END)

# 8 - billing details retreive function
def billing_details_retreive():
    # the most recent bill will be used to update. updating basically means to add or delete payments from the payment table
    global mydb
    global user_id

    patient_id = billing_details_update_patient_id_entry.get('1.0', END)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE patient_id = %s ORDER BY bill_id DESC", (patient_id))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Patient ID")
    else:
        global bill_id
        bill_id = result[0][0]

        billing_details_update_problem_entry.insert(0, result[0][4])

        mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY payment_id", (bill_id))
        result = mycursor.fetchall()

        for i in range(len(result)):
            billing_details_update_payments_listbox.insert(i, result[i][2])

        billing_details_update_payments_listbox.insert(END, "Total: " + str(result[0][2]))

        billing_details_update_payments_entry.delete('1.0', END)

# 9 - billing details add payment function
def billing_details_add_payment():
    global mydb
    global user_id
    global bill_id

    amount = billing_details_update_payments_entry.get('1.0', END)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE bill_id = %s", (bill_id))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Bill ID")
    else:
        mycursor.execute('''INSERT INTO Payments(bill_id, amount)
            VALUES(%s, %s)''', (bill_id, amount))
        mydb.commit()

        messagebox.showinfo("Success", "Payment added successfully!")

        billing_details_update_payments_listbox.delete('1.0', END)

        mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY payment_id", (bill_id))
        result = mycursor.fetchall()

        for i in range(len(result)):
            billing_details_update_payments_listbox.insert(i, result[i][2])

        billing_details_update_payments_listbox.insert(END, "Total: " + str(result[0][2]))

        billing_details_update_payments_entry.delete('1.0', END)

# 10 - billing details delete payment function
def billing_details_delete_payment():
    global mydb
    global user_id
    global bill_id

    amount = billing_details_update_payments_entry.get('1.0', END)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE bill_id = %s", (bill_id))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Bill ID")
    else:
        mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY payment_id", (bill_id))
        result = mycursor.fetchall()

        if len(result) == 0:
            messagebox.showerror("Error", "No payments to delete")
        else:
            mycursor.execute("DELETE FROM Payments WHERE payment_id = %s", (result[0][0]))
            mydb.commit()

            messagebox.showinfo("Success", "Payment deleted successfully!")

            billing_details_update_payments_listbox.delete('1.0', END)

            mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY payment_id", (bill_id))
            result = mycursor.fetchall()

            for i in range(len(result)):
                billing_details_update_payments_listbox.insert(i, result[i][2])

            billing_details_update_payments_listbox.insert(END, "Total: " + str(result[0][2]))

            billing_details_update_payments_entry.delete('1.0', END)

# 11 - billing details update function
def billing_details_update():
    global mydb
    global user_id
    global bill_id

    problem = billing_details_update_problem_entry.get('1.0', END)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE bill_id = %s", (bill_id))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Bill ID")
    else:
        mycursor.execute("UPDATE Bills SET problem = %s WHERE bill_id = %s", (problem, bill_id))
        mydb.commit()

        messagebox.showinfo("Success", "Bill updated successfully!")

        billing_details_update_problem_entry.delete('1.0', END)

# 12 - billing details retreive function
def billing_details_view():
    global mydb
    global user_id

    patient_id = billing_details_view_patient_id_entry.get('1.0', END)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE patient_id = %s ORDER BY bill_id DESC", (patient_id))
    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Patient ID")
    else:
        global bill_id
        bill_id = result[0][0]

        billing_details_view_problem_entry.insert(0, result[0][4])

        mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY payment_id", (bill_id))
        result = mycursor.fetchall()

        for i in range(len(result)):
            billing_details_view_payments_listbox.insert(i, result[i][2])

        billing_details_view_payments_listbox.insert(END, "Total: " + str(result[0][2]))

        billing_details_view_payments_entry.delete('1.0', END)


# Creating all the windows required

def exit():
    print("Exit function called")

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

# 6 - Billing Details Update Window
BillingDetailsUpdateWindow = Tk()
BillingDetailsUpdateWindow.title("Billing Details Update")
BillingDetailsUpdateWindow.geometry(f"500x500+{x_position}+{y_position}")
BillingDetailsUpdateWindow.resizable(0, 0)
BillingDetailsUpdateWindow.configure(bg="white")
BillingDetailsUpdateWindow.withdraw()
BillingDetailsUpdateWindow.protocol("WM_DELETE_WINDOW", exit)

# 7 - Billing Details View Window
BillingDetailsViewWindow = Tk()
BillingDetailsViewWindow.title("Billing Details View")
BillingDetailsViewWindow.geometry(f"500x500+{x_position}+{y_position}")
BillingDetailsViewWindow.resizable(0, 0)
BillingDetailsViewWindow.configure(bg="white")
BillingDetailsViewWindow.withdraw()
BillingDetailsViewWindow.protocol("WM_DELETE_WINDOW", exit)


# Adding all elements to all the windows

# 1 - Login Window
login_usrname_label = Label(LoginWindow, text="Username", font=("Arial", 20), bg="white")
login_usrname_label.place(x=50, y=100)

login_usrname_entry = Text(LoginWindow, height=1, width=20, font=("Arial", 20))
login_usrname_entry.place(x=200, y=100)

login_passwrd_label = Label(LoginWindow, text="Password", font=("Arial", 20), bg="white")
login_passwrd_label.place(x=50, y=200)

login_passwrd_entry = Text(LoginWindow, height=1, width=20, font=("Arial", 20))
login_passwrd_entry.place(x=200, y=200)

login_button = Button(LoginWindow, text="Login", font=("Arial", 20), bg="white", command=lambda: login())
login_button.place(x=200, y=320)

login_exit_button = Button(LoginWindow, text="Exit", font=("Arial", 20), bg="white", command=lambda: exit())
login_exit_button.place(x=205, y=380)


# 2 - Main Menu Window
main_menu_label = Label(MainMenuWindow, text="Main Menu", font=("Arial", 20), bg="white")
main_menu_label.place(x=200, y=50)

main_menu_patient_details_create_button = Button(MainMenuWindow, text="Add New Patient", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: [MainMenuWindow.withdraw(), PatientDetailsCreateWindow.deiconify()])
main_menu_patient_details_create_button.place(x=110, y=100)

main_menu_patient_details_update_button = Button(MainMenuWindow, text="Update Patient Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: [MainMenuWindow.withdraw(), PatientDetailsUpdateWindow.deiconify()])
main_menu_patient_details_update_button.place(x=110, y=150)

main_menu_patient_details_view_button = Button(MainMenuWindow, text="View Patient Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: [MainMenuWindow.withdraw(), PatientDetailsViewWindow.deiconify()])
main_menu_patient_details_view_button.place(x=110, y=200)

main_menu_billing_details_add_button = Button(MainMenuWindow, text="Create New Bill", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: [MainMenuWindow.withdraw(), BillingDetailsAddWindow.deiconify()])
main_menu_billing_details_add_button.place(x=110, y=250)

main_menu_billing_details_update_button = Button(MainMenuWindow, text="Update Bill Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: [MainMenuWindow.withdraw(), BillingDetailsUpdateWindow.deiconify()])
main_menu_billing_details_update_button.place(x=110, y=300)

main_menu_billing_details_view_button = Button(MainMenuWindow, text="View Bill Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: [MainMenuWindow.withdraw(), BillingDetailsViewWindow.deiconify()])
main_menu_billing_details_view_button.place(x=110, y=350)

main_menu_logout_button = Button(MainMenuWindow, text="Logout", font=("Arial", 20), bg="white", command=lambda: logout())
main_menu_logout_button.place(x=200, y=420)


# 3 - Patient Details Create Window
patient_details_create_label = Label(PatientDetailsCreateWindow, text="Add New Patient", font=("Arial", 20), bg="white")
patient_details_create_label.place(x=172, y=50)

patient_details_create_name_label = Label(PatientDetailsCreateWindow, text="Name", font=("Arial", 20), bg="white")
patient_details_create_name_label.place(x=50, y=100)

patient_details_create_name_entry = Text(PatientDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
patient_details_create_name_entry.place(x=200, y=100)

patient_details_create_address_label = Label(PatientDetailsCreateWindow, text="Address", font=("Arial", 20), bg="white")
patient_details_create_address_label.place(x=50, y=150)

patient_details_create_address_entry = Text(PatientDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
patient_details_create_address_entry.place(x=200, y=150)

patient_details_create_phone_label = Label(PatientDetailsCreateWindow, text="Phone", font=("Arial", 20), bg="white")
patient_details_create_phone_label.place(x=50, y=200)

patient_details_create_phone_entry = Text(PatientDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
patient_details_create_phone_entry.place(x=200, y=200)

patient_details_create_gender_label = Label(PatientDetailsCreateWindow, text="Gender", font=("Arial", 20), bg="white")
patient_details_create_gender_label.place(x=50, y=250)

patient_details_create_gender_entry = Text(PatientDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
patient_details_create_gender_entry.place(x=200, y=250)

patient_details_create_age_label = Label(PatientDetailsCreateWindow, text="Age", font=("Arial", 20), bg="white")
patient_details_create_age_label.place(x=50, y=300)

patient_details_create_age_entry = Text(PatientDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
patient_details_create_age_entry.place(x=200, y=300)

patient_details_create_button = Button(PatientDetailsCreateWindow, text="Create", font=("Arial", 20), bg="white", command=lambda: patient_details_create())
patient_details_create_button.place(x=200, y=400)

patient_details_create_exit_button = Button(PatientDetailsCreateWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [PatientDetailsCreateWindow.withdraw(), MainMenuWindow.deiconify()])
patient_details_create_exit_button.place(x=210, y=450)


# 4 - Patient Details Update Window
patient_details_update_label = Label(PatientDetailsUpdateWindow, text="Update Patient Details", font=("Arial", 20), bg="white")
patient_details_update_label.place(x=152, y=50)

patient_details_update_id_label = Label(PatientDetailsUpdateWindow, text="ID", font=("Arial", 20), bg="white")
patient_details_update_id_label.place(x=50, y=100)

patient_details_update_id_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_id_entry.place(x=200, y=100)

patient_details_retreive_button = Button(PatientDetailsUpdateWindow, text="Retreive", font=("Arial", 20), bg="white", command=lambda: patient_details_retreive())
patient_details_retreive_button.place(x=200, y=150)

patient_details_update_name_label = Label(PatientDetailsUpdateWindow, text="Name", font=("Arial", 20), bg="white")
patient_details_update_name_label.place(x=50, y=200)

patient_details_update_name_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_name_entry.place(x=200, y=200)

patient_details_update_address_label = Label(PatientDetailsUpdateWindow, text="Address", font=("Arial", 20), bg="white")
patient_details_update_address_label.place(x=50, y=250)

patient_details_update_address_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_address_entry.place(x=200, y=250)

patient_details_update_phone_label = Label(PatientDetailsUpdateWindow, text="Phone", font=("Arial", 20), bg="white")
patient_details_update_phone_label.place(x=50, y=300)

patient_details_update_phone_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_phone_entry.place(x=200, y=300)

patient_details_update_gender_label = Label(PatientDetailsUpdateWindow, text="Gender", font=("Arial", 20), bg="white")
patient_details_update_gender_label.place(x=50, y=350)

patient_details_update_gender_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_gender_entry.place(x=200, y=350)

patient_details_update_age_label = Label(PatientDetailsUpdateWindow, text="Age", font=("Arial", 20), bg="white")
patient_details_update_age_label.place(x=50, y=400)

patient_details_update_age_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_age_entry.place(x=200, y=400)

patient_details_update_button = Button(PatientDetailsUpdateWindow, text="Update", font=("Arial", 20), bg="white", command=lambda: patient_details_update())
patient_details_update_button.place(x=120, y=450)

patient_details_update_exit_button = Button(PatientDetailsUpdateWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [PatientDetailsUpdateWindow.withdraw(), MainMenuWindow.deiconify()])
patient_details_update_exit_button.place(x=270, y=450)


# 5 - Patient Details View Window
patient_details_view_label = Label(PatientDetailsViewWindow, text="View Patient Details", font=("Arial", 20), bg="white")
patient_details_view_label.place(x=156, y=50)

patient_details_view_id_label = Label(PatientDetailsViewWindow, text="ID", font=("Arial", 20), bg="white")
patient_details_view_id_label.place(x=50, y=100)

patient_details_view_id_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20)
patient_details_view_id_entry.place(x=200, y=100)

patient_details_view_button = Button(PatientDetailsViewWindow, text="View", font=("Arial", 20), bg="white", command=lambda: patient_details_view())
patient_details_view_button.place(x=200, y=150)

patient_details_view_name_label = Label(PatientDetailsViewWindow, text="Name", font=("Arial", 20), bg="white")
patient_details_view_name_label.place(x=50, y=200)

patient_details_view_name_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20)
patient_details_view_name_entry.place(x=200, y=200)

patient_details_view_address_label = Label(PatientDetailsViewWindow, text="Address", font=("Arial", 20), bg="white")
patient_details_view_address_label.place(x=50, y=250)

patient_details_view_address_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20)
patient_details_view_address_entry.place(x=200, y=250)

patient_details_view_phone_label = Label(PatientDetailsViewWindow, text="Phone", font=("Arial", 20), bg="white")
patient_details_view_phone_label.place(x=50, y=300)

patient_details_view_phone_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20)
patient_details_view_phone_entry.place(x=200, y=300)

patient_details_view_gender_label = Label(PatientDetailsViewWindow, text="Gender", font=("Arial", 20), bg="white")
patient_details_view_gender_label.place(x=50, y=350)

patient_details_view_gender_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20)
patient_details_view_gender_entry.place(x=200, y=350)

patient_details_view_age_label = Label(PatientDetailsViewWindow, text="Age", font=("Arial", 20), bg="white")
patient_details_view_age_label.place(x=50, y=400)

patient_details_view_age_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20)
patient_details_view_age_entry.place(x=200, y=400)

patient_details_view_exit_button = Button(PatientDetailsViewWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [PatientDetailsViewWindow.withdraw(), MainMenuWindow.deiconify()])
patient_details_view_exit_button.place(x=210, y=450)


# 6 - Billing Details View Window
billing_details_view_label = Label(BillingDetailsViewWindow, text="View Bill Details", font=("Arial", 20), bg="white")
billing_details_view_label.place(x=177, y=50)

billing_details_view_patient_id_label = Label(BillingDetailsViewWindow, text="Patient ID", font=("Arial", 20), bg="white")
billing_details_view_patient_id_label.place(x=50, y=120)


# 7 - Billing Details Update Window



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
