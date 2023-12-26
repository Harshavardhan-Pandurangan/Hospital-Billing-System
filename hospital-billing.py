'''
Hospital billing system using MySQL Connector and Database

- Harshamithran P
- Shreyas B

4 databases used for users, patients, bills and payments details
UI built using Tkinter
'''

# Importing all the modules required
import mysql.connector
from tkinter import *
from tkinter import messagebox
from datetime import datetime
import time


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
    print("Logout function called")

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
    dob = patient_details_create_dob_entry.get('1.0', END)

    name = name[:-1]
    address = address[:-1]
    phone = phone[:-1]
    gender = gender[:-1]
    dob = dob[:-1]

    mycursor = mydb.cursor()
    mycursor.execute('''INSERT INTO Patients(name, address, phone, gender, dob, user_id)
        VALUES(%s, %s, %s, %s, %s, %s);''', (name, address, phone, gender, dob, user_id))
    result = mycursor.fetchall()
    mydb.commit()

    PatientDetailsCreateWindow.withdraw()
    MainMenuWindow.deiconify()

    messagebox.showinfo("Success", "Patient Details Created Successfully")

    patient_details_create_name_entry.delete('1.0', END)
    patient_details_create_address_entry.delete('1.0', END)
    patient_details_create_phone_entry.delete('1.0', END)
    patient_details_create_gender_entry.delete('1.0', END)
    patient_details_create_dob_entry.delete('1.0', END)

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
        patient_details_update_dob_entry.insert(END, result[0][5])

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
    dob = patient_details_update_dob_entry.get('1.0', END)

    name = name[:-1]
    address = address[:-1]
    phone = phone[:-1]
    gender = gender[:-1]
    dob = dob[:-1]

    mycursor = mydb.cursor()
    sql = "UPDATE Patients SET name = %s, address = %s, phone = %s, gender = %s, dob = %s, user_id = %s WHERE patient_id = %s;"
    val = (name, address, phone, gender, dob, user_id, patient_id)
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
        patient_details_view_name_entry.config(state=NORMAL)
        patient_details_view_address_entry.config(state=NORMAL)
        patient_details_view_phone_entry.config(state=NORMAL)
        patient_details_view_gender_entry.config(state=NORMAL)
        patient_details_view_dob_entry.config(state=NORMAL)

        patient_details_view_name_entry.delete('1.0', END)
        patient_details_view_address_entry.delete('1.0', END)
        patient_details_view_phone_entry.delete('1.0', END)
        patient_details_view_gender_entry.delete('1.0', END)
        patient_details_view_dob_entry.delete('1.0', END)

        patient_details_view_name_entry.insert(END, result[0][1])
        patient_details_view_address_entry.insert(END, result[0][2])
        patient_details_view_phone_entry.insert(END, result[0][3])
        patient_details_view_gender_entry.insert(END, result[0][4])
        patient_details_view_dob_entry.insert(END, result[0][5])

        patient_details_view_name_entry.config(state=DISABLED)
        patient_details_view_address_entry.config(state=DISABLED)
        patient_details_view_phone_entry.config(state=DISABLED)
        patient_details_view_gender_entry.config(state=DISABLED)
        patient_details_view_dob_entry.config(state=DISABLED)

# 7 - retrieve all patients function
def retreive_all_patients():
    print("Retreive All Patients function called")

    global mydb
    global user_id

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Patients WHERE user_id = %s;", (user_id, ))

    result = mycursor.fetchall()

    for i in range(len(result)):
        result[i] = list(result[i])
        result[i][1] = result[i][1][:24]
        patient_details_all_entries_listbox.insert(END, f"{result[i][0]:<4} {result[i][1]:<25} {result[i][3]:<11}")

# 8 - bills details view function
def bills_details_view():
    print("Bills Details View function called")

    global mydb
    global user_id

    patient_id_entry = bills_details_view_id_entry.get('1.0', END)

    patient_id_entry = patient_id_entry[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Patients WHERE patient_id = %s;", (patient_id_entry, ))

    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Patient ID")
    else:
        global patient_id
        patient_id = result[0][0]

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Bills WHERE patient_id = %s ORDER BY doa DESC;", (patient_id, ))

        result = mycursor.fetchall()

        bills_details_view_listbox.delete(0, END)

        if len(result) == 0:
            messagebox.showerror("Error", "No Bills Found")
        else:
            for i in range(len(result)):
                result[i] = list(result[i])
                result[i][4] = result[i][4][:20]
                bills_details_view_listbox.insert(END, f"{result[i][0]:<4} {result[i][4]:<21} {result[i][3]:<11}")

            bills_details_view_listbox.bind("<Double-1>", bill_payment_details_view)

# 9 - bills details create function
def bills_details_create():
    print("Bills Details Create function called")

    global mydb
    global user_id
    global patient_id

    problem = bills_details_create_problem_entry.get('1.0', END)

    problem = problem[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE patient_id = %s AND dod IS NULL;", (patient_id, ))

    result = mycursor.fetchall()

    if len(result) == 0:
        mycursor = mydb.cursor()
        mycursor.execute('''INSERT INTO Bills(user_id, patient_id, problem)
            VALUES(%s, %s, %s);''', (user_id, patient_id, problem))
        result = mycursor.fetchall()
        mydb.commit()

        BillsDetailsCreateWindow.withdraw()
        BillsDetailsViewWindow.deiconify()

        messagebox.showinfo("Success", "Bill Created Successfully")

        bills_details_create_problem_entry.delete('1.0', END)
    else:
        messagebox.showerror("Error", "Patient already has an active bill")

# 10 - bill payment details view function
def bill_payment_details_view(event):
    print("Bill Payment Details View function called")

    global mydb
    global user_id
    global patient_id
    global bill_id

    BillsDetailsViewWindow.withdraw()
    BillsDetailsUpdateWindow.deiconify()

    selection = bills_details_view_listbox.curselection()
    value = bills_details_view_listbox.get(selection[0])

    bill_id_clicked = int(value.split(" ")[0])
    bill_id = bill_id_clicked

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE bill_id = %s;", (bill_id_clicked, ))

    result = mycursor.fetchall()

    bills_details_update_problem_entry.config(state=NORMAL)
    bills_details_update_amount_entry.config(state=NORMAL)
    bills_details_update_doa_entry.config(state=NORMAL)

    bills_details_update_problem_entry.delete('1.0', END)
    bills_details_update_amount_entry.delete('1.0', END)
    bills_details_update_doa_entry.delete('1.0', END)
    bills_details_update_payments_listbox.delete(0, END)
    bills_details_update_payments_listbox.unbind("<Double-1>")
    bills_details_update_add_new_payment_amount_entry.delete('1.0', END)

    bills_details_update_problem_entry.insert(END, result[0][4])
    bills_details_update_amount_entry.insert(END, result[0][3])
    bills_details_update_doa_entry.insert(END, result[0][5])

    if result[0][6] != None:
        bills_details_update_problem_entry.config(state=DISABLED)
        bills_details_update_add_new_payment_amount_entry.config(state=DISABLED)
        bills_details_update_button.config(state=DISABLED)
        bills_details_update_add_new_payment_button.config(state=DISABLED)
        bills_details_update_complete_bill_button.config(state=DISABLED)
    else:
        bills_details_update_problem_entry.config(state=NORMAL)
        bills_details_update_add_new_payment_amount_entry.config(state=NORMAL)
        bills_details_update_button.config(state=NORMAL)
        bills_details_update_add_new_payment_button.config(state=NORMAL)
        bills_details_update_complete_bill_button.config(state=NORMAL)

    bills_details_update_amount_entry.config(state=DISABLED)
    bills_details_update_doa_entry.config(state=DISABLED)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY dop DESC;", (bill_id_clicked, ))

    result = mycursor.fetchall()

    for i in range(len(result)):
        result[i] = list(result[i])
        result[i][3] = str(result[i][3])[:20]
        bills_details_update_payments_listbox.insert(END, f"{result[i][0]:<4} {result[i][3]:<21} {result[i][2]:<11}")

# 11 - bill_details_update_add_new_payment function
def bill_details_update_add_new_payment():
    print("Bill Details Update Add New Payment function called")

    global mydb
    global user_id
    global patient_id
    global bill_id

    amount = bills_details_update_add_new_payment_amount_entry.get('1.0', END)

    amount = amount[:-1]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Bills WHERE bill_id = %s;", (bill_id, ))

    result = mycursor.fetchall()

    if len(result) == 0:
        messagebox.showerror("Error", "Invalid Bill ID")
    else:
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO Payments(bill_id, amount) VALUES(%s, %s);", (bill_id, amount))
        result = mycursor.fetchall()
        mydb.commit()

        messagebox.showinfo("Success", "Payment Added Successfully")

        bills_details_update_add_new_payment_amount_entry.delete('1.0', END)

        bills_details_update_payments_listbox.delete(0, END)

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s ORDER BY dop DESC;", (bill_id, ))

        result = mycursor.fetchall()

        for i in range(len(result)):
            result[i] = list(result[i])
            result[i][3] = str(result[i][3])[:20]
            bills_details_update_payments_listbox.insert(END, f"{result[i][0]:<4} {result[i][3]:<21} {result[i][2]:<11}")

# 12 - update bill details function
def bill_details_update():
    print("Update Bill Details function called")

    global mydb
    global user_id
    global patient_id
    global bill_id

    problem = bills_details_update_problem_entry.get('1.0', END)

    problem = problem[:-1]

    mycursor = mydb.cursor()
    sql = "UPDATE Bills SET problem = %s WHERE bill_id = %s;"
    val = (problem, bill_id)
    mycursor.execute(sql, val)
    mydb.commit()

    messagebox.showinfo("Success", "Bill details updated successfully!")

# 13 - complete bill function
def complete_bill():
    print("Complete Bill function called")

    global mydb
    global user_id
    global patient_id
    global bill_id

    # set the total amount and the date of discharge
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Payments WHERE bill_id = %s;", (bill_id, ))

    result = mycursor.fetchall()

    total_amount = 0
    for i in range(len(result)):
        total_amount += result[i][2]

    mycursor = mydb.cursor()
    mycursor.execute("UPDATE Bills SET amount = %s, dod = %s WHERE bill_id = %s;", (total_amount, datetime.now(), bill_id))
    mydb.commit()

    messagebox.showinfo("Success", "Bill Completed Successfully")

    BillsDetailsUpdateWindow.withdraw()
    BillsDetailsViewWindow.deiconify()


# Additional functions for the UI

def main_to_add_new_patient():
    print("Main to Add New Patient function called")

    MainMenuWindow.withdraw()
    PatientDetailsCreateWindow.deiconify()

    patient_details_create_name_entry.delete('1.0', END)
    patient_details_create_address_entry.delete('1.0', END)
    patient_details_create_phone_entry.delete('1.0', END)
    patient_details_create_gender_entry.delete('1.0', END)
    patient_details_create_dob_entry.delete('1.0', END)

def main_to_update_patient_details():
    print("Main to Update Patient Details function called")

    MainMenuWindow.withdraw()
    PatientDetailsUpdateWindow.deiconify()

    patient_details_update_id_entry.delete('1.0', END)
    patient_details_update_name_entry.delete('1.0', END)
    patient_details_update_address_entry.delete('1.0', END)
    patient_details_update_phone_entry.delete('1.0', END)
    patient_details_update_gender_entry.delete('1.0', END)
    patient_details_update_dob_entry.delete('1.0', END)

def main_to_view_patient_details():
    print("Main to View Patient Details function called")

    MainMenuWindow.withdraw()
    PatientDetailsViewWindow.deiconify()

    patient_details_view_id_entry.delete('1.0', END)
    patient_details_view_name_entry.delete('1.0', END)
    patient_details_view_address_entry.delete('1.0', END)
    patient_details_view_phone_entry.delete('1.0', END)
    patient_details_view_gender_entry.delete('1.0', END)
    patient_details_view_dob_entry.delete('1.0', END)

def main_to_view_all_patient_details():
    print("Main to View All Patient Details function called")

    MainMenuWindow.withdraw()
    PatientsDetailsAllEntriesWindow.deiconify()

    patient_details_all_entries_listbox.delete(0, END)

    retreive_all_patients()

def main_to_view_bills_details():
    print("Main to View Bills Details function called")

    MainMenuWindow.withdraw()
    BillsDetailsViewWindow.deiconify()

    bills_details_view_id_entry.delete('1.0', END)
    bills_details_view_listbox.delete(0, END)

def bills_details_view_to_bills_details_create():
    print("Bills Details View to Bills Details Create function called")

    BillsDetailsViewWindow.withdraw()
    BillsDetailsCreateWindow.deiconify()

    bills_details_create_problem_entry.delete('1.0', END)


def exit():
    print("Exit function called")

    LoginWindow.destroy()
    MainMenuWindow.destroy()
    PatientDetailsCreateWindow.destroy()
    PatientDetailsUpdateWindow.destroy()
    PatientDetailsViewWindow.destroy()
    PatientsDetailsAllEntriesWindow.destroy()
    BillsDetailsViewWindow.destroy()
    BillsDetailsCreateWindow.destroy()
    BillsDetailsUpdateWindow.destroy()


# Creating all the windows required

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

# 6 - Patients Details All Entries Window
PatientsDetailsAllEntriesWindow = Tk()
PatientsDetailsAllEntriesWindow.title("Patients Details All Entries")
PatientsDetailsAllEntriesWindow.geometry(f"500x500+{x_position}+{y_position}")
PatientsDetailsAllEntriesWindow.resizable(0, 0)
PatientsDetailsAllEntriesWindow.configure(bg="white")
PatientsDetailsAllEntriesWindow.withdraw()
PatientsDetailsAllEntriesWindow.protocol("WM_DELETE_WINDOW", exit)

# 7 - Bills Details View Window
BillsDetailsViewWindow = Tk()
BillsDetailsViewWindow.title("Bills Details View")
BillsDetailsViewWindow.geometry(f"500x500+{x_position}+{y_position}")
BillsDetailsViewWindow.resizable(0, 0)
BillsDetailsViewWindow.configure(bg="white")
BillsDetailsViewWindow.withdraw()
BillsDetailsViewWindow.protocol("WM_DELETE_WINDOW", exit)

# 8 - Bills Details Create Window
BillsDetailsCreateWindow = Tk()
BillsDetailsCreateWindow.title("Bills Details Create")
BillsDetailsCreateWindow.geometry(f"500x500+{x_position}+{y_position}")
BillsDetailsCreateWindow.resizable(0, 0)
BillsDetailsCreateWindow.configure(bg="white")
BillsDetailsCreateWindow.withdraw()
BillsDetailsCreateWindow.protocol("WM_DELETE_WINDOW", exit)

# 9 - Bills Details Update Window
BillsDetailsUpdateWindow = Tk()
BillsDetailsUpdateWindow.title("Bills Details Update")
BillsDetailsUpdateWindow.geometry(f"500x500+{x_position}+{y_position}")
BillsDetailsUpdateWindow.resizable(0, 0)
BillsDetailsUpdateWindow.configure(bg="white")
BillsDetailsUpdateWindow.withdraw()
BillsDetailsUpdateWindow.protocol("WM_DELETE_WINDOW", exit)


# Adding all elements to all the windows

# 1 - Login Window
login_label = Label(LoginWindow, text="Login", font=("Arial", 20), bg="white")
login_label.place(x=220, y=50)

login_usrname_label = Label(LoginWindow, text="Username", font=("Arial", 20), bg="white")
login_usrname_label.place(x=50, y=150)

login_usrname_entry = Text(LoginWindow, height=1, width=20, font=("Arial", 20))
login_usrname_entry.place(x=200, y=150)

login_passwrd_label = Label(LoginWindow, text="Password", font=("Arial", 20), bg="white")
login_passwrd_label.place(x=50, y=230)

login_passwrd_entry = Text(LoginWindow, height=1, width=20, font=("Arial", 20))
login_passwrd_entry.place(x=200, y=230)

login_button = Button(LoginWindow, text="Login", font=("Arial", 20), bg="white", command=lambda: login())
login_button.place(x=213, y=330)

login_exit_button = Button(LoginWindow, text="Exit", font=("Arial", 20), bg="white", command=lambda: exit())
login_exit_button.place(x=220, y=390)


# 2 - Main Menu Window
main_menu_label = Label(MainMenuWindow, text="Main Menu", font=("Arial", 20), bg="white")
main_menu_label.place(x=200, y=50)

main_menu_patient_details_create_button = Button(MainMenuWindow, text="Add New Patient", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: main_to_add_new_patient())
main_menu_patient_details_create_button.place(x=110, y=100)

main_menu_patient_details_update_button = Button(MainMenuWindow, text="Update Patient Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: main_to_update_patient_details())
main_menu_patient_details_update_button.place(x=110, y=150)

main_menu_patient_details_view_button = Button(MainMenuWindow, text="View Patient Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: main_to_view_patient_details())
main_menu_patient_details_view_button.place(x=110, y=200)

main_menu_patient_details_all_entries_button = Button(MainMenuWindow, text="View All Patient Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: main_to_view_all_patient_details())
main_menu_patient_details_all_entries_button.place(x=110, y=250)

main_menu_bills_details_view_button = Button(MainMenuWindow, text="View Bills Details", font=("Arial", 20), bg="white", height=1, width=20, command=lambda: main_to_view_bills_details())
main_menu_bills_details_view_button.place(x=110, y=300)

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

patient_details_create_dob_label = Label(PatientDetailsCreateWindow, text="DOB", font=("Arial", 20), bg="white")
patient_details_create_dob_label.place(x=50, y=300)

patient_details_create_dob_entry = Text(PatientDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
patient_details_create_dob_entry.place(x=200, y=300)

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

patient_details_update_dob_label = Label(PatientDetailsUpdateWindow, text="DOB", font=("Arial", 20), bg="white")
patient_details_update_dob_label.place(x=50, y=400)

patient_details_update_dob_entry = Text(PatientDetailsUpdateWindow, font=("Arial", 20), height=1, width=20)
patient_details_update_dob_entry.place(x=200, y=400)

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

patient_details_view_name_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20, state=DISABLED)
patient_details_view_name_entry.place(x=200, y=200)

patient_details_view_address_label = Label(PatientDetailsViewWindow, text="Address", font=("Arial", 20), bg="white")
patient_details_view_address_label.place(x=50, y=250)

patient_details_view_address_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20, state=DISABLED)
patient_details_view_address_entry.place(x=200, y=250)

patient_details_view_phone_label = Label(PatientDetailsViewWindow, text="Phone", font=("Arial", 20), bg="white")
patient_details_view_phone_label.place(x=50, y=300)

patient_details_view_phone_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20, state=DISABLED)
patient_details_view_phone_entry.place(x=200, y=300)

patient_details_view_gender_label = Label(PatientDetailsViewWindow, text="Gender", font=("Arial", 20), bg="white")
patient_details_view_gender_label.place(x=50, y=350)

patient_details_view_gender_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20, state=DISABLED)
patient_details_view_gender_entry.place(x=200, y=350)

patient_details_view_dob_label = Label(PatientDetailsViewWindow, text="DOB", font=("Arial", 20), bg="white")
patient_details_view_dob_label.place(x=50, y=400)

patient_details_view_dob_entry = Text(PatientDetailsViewWindow, font=("Arial", 20), height=1, width=20, state=DISABLED)
patient_details_view_dob_entry.place(x=200, y=400)

patient_details_view_exit_button = Button(PatientDetailsViewWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [PatientDetailsViewWindow.withdraw(), MainMenuWindow.deiconify()])
patient_details_view_exit_button.place(x=210, y=450)


# 6 - Patient Details All Entries Window
patient_details_all_entries_label = Label(PatientsDetailsAllEntriesWindow, text="All Patient Details", font=("Arial", 20), bg="white")
patient_details_all_entries_label.place(x=166, y=50)

patient_details_all_entries_canvas = Canvas(PatientsDetailsAllEntriesWindow, width=50, height=21, bg="white")
patient_details_all_entries_canvas.place(x=50, y=100)

patient_details_all_entries_scrollbar = Scrollbar(PatientsDetailsAllEntriesWindow, orient="vertical", command=patient_details_all_entries_canvas.yview)
patient_details_all_entries_scrollbar.place(x=450, y=100)

patient_details_all_entries_listbox = Listbox(PatientsDetailsAllEntriesWindow, yscrollcommand=patient_details_all_entries_scrollbar.set, font=("Courier", 14), width=50, height=21)
patient_details_all_entries_listbox.place(x=50, y=100)

patient_details_all_entries_canvas.configure(yscrollcommand=patient_details_all_entries_scrollbar.set, scrollregion=patient_details_all_entries_canvas.bbox("all"))

patient_details_all_entries_exit_button = Button(PatientsDetailsAllEntriesWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [PatientsDetailsAllEntriesWindow.withdraw(), MainMenuWindow.deiconify()])
patient_details_all_entries_exit_button.place(x=210, y=450)


# 7 - Bills Details View Window
bills_details_view_label = Label(BillsDetailsViewWindow, text="View Bills Details", font=("Arial", 20), bg="white")
bills_details_view_label.place(x=156, y=50)

bills_details_view_id_label = Label(BillsDetailsViewWindow, text="Patient ID", font=("Arial", 20), bg="white")
bills_details_view_id_label.place(x=50, y=100)

bills_details_view_id_entry = Text(BillsDetailsViewWindow, font=("Arial", 20), height=1, width=20)
bills_details_view_id_entry.place(x=200, y=100)

bills_details_view_button = Button(BillsDetailsViewWindow, text="View", font=("Arial", 20), bg="white", command=lambda: bills_details_view())
bills_details_view_button.place(x=200, y=150)

bills_details_view_canvas = Canvas(BillsDetailsViewWindow, width=50, height=15, bg="white")
bills_details_view_canvas.place(x=50, y=200)

bills_details_view_scrollbar = Scrollbar(BillsDetailsViewWindow, orient="vertical", command=bills_details_view_canvas.yview)
bills_details_view_scrollbar.place(x=450, y=200)

bills_details_view_listbox = Listbox(BillsDetailsViewWindow, yscrollcommand=bills_details_view_scrollbar.set, font=("Courier", 14), width=50, height=15)
bills_details_view_listbox.place(x=50, y=200)

bills_details_view_canvas.configure(yscrollcommand=bills_details_view_scrollbar.set, scrollregion=bills_details_view_canvas.bbox("all"))

bills_details_view_add_new_bill_button = Button(BillsDetailsViewWindow, text="Add New Bill", font=("Arial", 20), bg="white", command=lambda: bills_details_view_to_bills_details_create())
bills_details_view_add_new_bill_button.place(x=50, y=450)

bills_details_view_exit_button = Button(BillsDetailsViewWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [BillsDetailsViewWindow.withdraw(), MainMenuWindow.deiconify()])
bills_details_view_exit_button.place(x=350, y=450)


# 8 - Bills Details Create Window
bills_details_create_label = Label(BillsDetailsCreateWindow, text="Create New Bill", font=("Arial", 20), bg="white")
bills_details_create_label.place(x=156, y=50)

bills_details_create_problem_label = Label(BillsDetailsCreateWindow, text="Problem", font=("Arial", 20), bg="white")
bills_details_create_problem_label.place(x=50, y=185)

bills_details_create_problem_entry = Text(BillsDetailsCreateWindow, font=("Arial", 20), height=1, width=20)
bills_details_create_problem_entry.place(x=200, y=185)

bills_details_create_button = Button(BillsDetailsCreateWindow, text="Create", font=("Arial", 20), bg="white", command=lambda: bills_details_create())
bills_details_create_button.place(x=200, y=320)

bill_details_create_exit_button = Button(BillsDetailsCreateWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [BillsDetailsCreateWindow.withdraw(), BillsDetailsViewWindow.deiconify()])
bill_details_create_exit_button.place(x=210, y=400)


# 9 - Bills Details Update Window
bills_details_update_label = Label(BillsDetailsUpdateWindow, text="Update Bill Details", font=("Arial", 20), bg="white")
bills_details_update_label.place(x=165, y=20)

bills_details_update_problem_label = Label(BillsDetailsUpdateWindow, text="Problem", font=("Arial", 13), bg="white")
bills_details_update_problem_label.place(x=50, y=70)

bills_details_update_problem_entry = Text(BillsDetailsUpdateWindow, font=("Arial", 13), height=1, width=20)
bills_details_update_problem_entry.place(x=200, y=70)

bills_details_update_doa_label = Label(BillsDetailsUpdateWindow, text="DOA", font=("Arial", 13), bg="white")
bills_details_update_doa_label.place(x=50, y=105)

bills_details_update_doa_entry = Text(BillsDetailsUpdateWindow, font=("Arial", 13), height=1, width=20)
bills_details_update_doa_entry.place(x=200, y=105)

bills_details_update_amount_label = Label(BillsDetailsUpdateWindow, text="Total Amount", font=("Arial", 13), bg="white")
bills_details_update_amount_label.place(x=50, y=140)

bills_details_update_amount_entry = Text(BillsDetailsUpdateWindow, font=("Arial", 13), height=1, width=20)
bills_details_update_amount_entry.place(x=200, y=140)

bills_details_update_payments_canvas = Canvas(BillsDetailsUpdateWindow, width=50, height=12, bg="white")
bills_details_update_payments_canvas.place(x=50, y=175)

bills_details_update_payments_scrollbar = Scrollbar(BillsDetailsUpdateWindow, orient="vertical", command=bills_details_update_payments_canvas.yview)
bills_details_update_payments_scrollbar.place(x=450, y=175)

bills_details_update_payments_listbox = Listbox(BillsDetailsUpdateWindow, yscrollcommand=bills_details_update_payments_scrollbar.set, font=("Courier", 13), width=50, height=12)
bills_details_update_payments_listbox.place(x=50, y=175)

bills_details_update_payments_canvas.configure(yscrollcommand=bills_details_update_payments_scrollbar.set, scrollregion=bills_details_update_payments_canvas.bbox("all"))

bills_details_update_add_new_payment_label = Label(BillsDetailsUpdateWindow, text="Add New Payment", font=("Arial", 17), bg="white")
bills_details_update_add_new_payment_label.place(x=50, y=350)

bills_details_update_add_new_payment_amount_label = Label(BillsDetailsUpdateWindow, text="Amount", font=("Arial", 13), bg="white")
bills_details_update_add_new_payment_amount_label.place(x=50, y=400)

bills_details_update_add_new_payment_amount_entry = Text(BillsDetailsUpdateWindow, font=("Arial", 13), height=1, width=20)
bills_details_update_add_new_payment_amount_entry.place(x=170, y=400)

bill_details_update_add_new_payment_button = Button(BillsDetailsUpdateWindow, text="Add", font=("Arial", 13), bg="white", command=lambda: bill_details_update_add_new_payment())
bill_details_update_add_new_payment_button.place(x=400, y=400)

bills_details_update_update_button = Button(BillsDetailsUpdateWindow, text="Update", font=("Arial", 20), bg="white", command=lambda: bill_details_update())
bills_details_update_update_button.place(x=20, y=450)

bills_details_update_complete_payment_button = Button(BillsDetailsUpdateWindow, text="Complete Payment", font=("Arial", 20), bg="white", command=lambda: complete_bill())
bills_details_update_complete_payment_button.place(x=155, y=450)

bills_details_update_exit_button = Button(BillsDetailsUpdateWindow, text="Back", font=("Arial", 20), bg="white", command=lambda: [BillsDetailsUpdateWindow.withdraw(), BillsDetailsViewWindow.deiconify()])
bills_details_update_exit_button.place(x=395, y=450)


# Mainloops for all the windows

LoginWindow.mainloop()
MainMenuWindow.mainloop()
PatientDetailsCreateWindow.mainloop()
PatientDetailsUpdateWindow.mainloop()
PatientDetailsViewWindow.mainloop()
PatientsDetailsAllEntriesWindow.mainloop()
BillsDetailsViewWindow.mainloop()
BillsDetailsCreateWindow.mainloop()
BillsDetailsUpdateWindow.mainloop()


# End of the program
# Thank you
