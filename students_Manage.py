import tkinter
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import instructor_operations
import instructor_Manage


class students_Registration(object):
    def __init__(self, window):
        self.root = window
        self.root.title("Student Management - DanceFeet System")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.width = 1200
        self.height = 900
        x = (self.screen_width / 2) - (self.width / 2)
        y = (self.screen_height / 2) - (self.height / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))


        # VARIABLES

        self.ID = tkinter.StringVar()
        self.FIRSTNAME = tkinter.StringVar()
        self.SURNAME = tkinter.StringVar()
        self.EMAIL = tkinter.StringVar()
        self.GENDER = tkinter.StringVar()
        self.DOB = tkinter.StringVar()
        self.TP = tkinter.StringVar()
        self.STYLE = tkinter.StringVar()
        self.HRATE = tkinter.StringVar()
        self.INSTRUCTOR = tkinter.StringVar()
        self.INSTRUCTOR_COMBO = tkinter.StringVar()
        self.AVAILABILITY = tkinter.StringVar()
        self.ADDRESS = tkinter.StringVar()

       # FRAME
        self.Top = Frame(self.root, width=900, height=50, bd=8, relief="raise")
        self.Top.pack(side=TOP)
        self.Left = Frame(self.root, width=300, height=600, bd=8, relief="raise")
        self.Left.pack(side=LEFT)
        self.Right = Frame(self.root, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=RIGHT)
        self.Forms = Frame(self.Left, width=300, height=450)
        self.Forms.pack(side=TOP)
        self.Buttons = Frame(self.Left, width=300, height=100, bd=8, relief="raise")
        self.Buttons.pack(side=BOTTOM)

        self.StudentManagement_btn =Button(self.Top, text="Student Management", width=30, height=1, font=('arial', 12), fg='white',background='green',bd=2,command=self.student_area). \
            grid(row=0, column=1, padx=4, pady=5)
        
        self.InstructorManagement_btn = Button(self.Top, text="Instructor Management", width=30, height=1, fg='white', font=('arial', 12),background='green',bd=2,activeforeground = "Deepskyblue2",activebackground = "blue",command=self.instructor_area,relief="groove"). \
            grid(row=0, column=2, padx=4, pady=5)
        self.LessonBooking_btn = Button(self.Top, text="Lesson Booking", width=30, height=1, font=('arial', 12), fg='white', background='green',bd=2,command=self.cource_area). \
            grid(row=0, column=3, padx=4, pady=5)
        self.exit_btn = Button(self.Top, text="EXIT", width=30, height=1, font=('arial', 12), fg='white', command=self.Exit, background='green',bd=2). \
            grid(row=0, column=4, padx=4, pady=5)

        self.txt_title = Label(self.Top,width=40,font=('arial', 10),text="Student Management - DanceFeet System",borderwidth=0,relief="groove",fg='#01579b')
        self.txt_title. grid(row=2, column=1, padx=4, pady=5)

        # LABEL WIDGET

        self.txt_firstname = Label(self.Forms, text="First Name:", font=('arial', 16), bd=15)
        self.txt_firstname.grid(row=0, sticky="e")
        self.txt_lastName = Label(self.Forms, text="Surname:", font=('arial', 16), bd=15)
        self.txt_lastName.grid(row=1, sticky="e")
        self.txt_Email = Label(self.Forms, text="Email:", font=('arial', 16), bd=15)
        self.txt_Email.grid(row=2, sticky="e")
        self.txt_gender = Label(self.Forms, text="Gender:", font=('arial', 16), bd=15)
        self.txt_gender.grid(row=3, sticky="e")
        self.txt_DOB = Label(self.Forms, text="Date of Birth:", font=('arial', 16), bd=15)
        self.txt_DOB.grid(row=4, sticky="e")
        self.txt_TpNo = Label(self.Forms, text="Telephone Number:", font=('arial', 16), bd=15)
        self.txt_TpNo.grid(row=5, sticky="e")
        self.txt_address = Label(self.Forms, text="Address:", font=('arial', 16), bd=15)
        self.txt_address.grid(row=6, sticky="e")
        self.txt_Style = Label(self.Forms, text="Style:", font=('arial', 16), bd=15)
        self.txt_Style.grid(row=7, sticky="e")
        self.txt_hourRate = Label(self.Forms, text="Rate can pay for hour:", font=('arial', 16), bd=15)
        self.txt_hourRate.grid(row=8, sticky="e")
        self.txt_availablity = Label(self.Forms, text="Date Available:", font=('arial', 16), bd=15)
        self.txt_availablity.grid(row=9, sticky="e")
        self.txt_Instructor = Label(self.Forms, text="Instructor:", font=('arial', 16), bd=15)
        self.txt_Instructor.grid(row=10, sticky="e")


        self.txt_result = Label(self.Buttons)
        self.txt_result.pack(side=TOP)

        # ENTRY WIDGET
        self.entry_id = Entry(self.Forms, textvariable=self.ID, width=30)
        self.entry_id.grid(row=0, column=1)
        self.entry_id.config(state=DISABLED)

        self.entry_firstname = Entry(self.Forms, textvariable=self.FIRSTNAME, width=30)
        self.entry_firstname.grid(row=0, column=1)

        self.password = Entry(self.Forms, textvariable=self.SURNAME, width=30)
        self.password.grid(row=1, column=1)

        self.name = Entry(self.Forms, textvariable=self.EMAIL, width=30)
        self.name.grid(row=2, column=1)


        self.gender = ttk.Combobox(self.Forms, textvariable=self.GENDER, width=30)
        self.gender.grid(row=3, column=1)
        self.gender['values'] = ('male', 'female')

        self.styles = Entry(self.Forms, textvariable=self.DOB, width=30)
        self.styles.grid(row=4, column=1)

        self.tp = Entry(self.Forms, textvariable=self.TP, width=30)
        self.tp.grid(row=5, column=1)

        self.address = Entry(self.Forms, textvariable=self.ADDRESS, width=30)
        self.address.grid(row=6, column=1)

        self.hrate = Entry(self.Forms, textvariable=self.STYLE, width=30)
        self.hrate.grid(row=7, column=1)

        self.hrate = Entry(self.Forms, textvariable=self.HRATE, width=30)
        self.hrate.grid(row=8, column=1)

        self.entry_availability = Entry(self.Forms, textvariable=self.AVAILABILITY, width=30)
        self.entry_availability.grid(row=9, column=1)

        self.instructor_combo = ttk.Combobox(self.Forms, textvariable=self.INSTRUCTOR, width=28)
        self.instructor_combo.grid(row=10, column=1)

        # BUTTONS WIDGET
        self.btn_create = Button(self.Buttons, width=10, text="Create", command=self.Create)
        self.btn_create.pack(side=LEFT)
        self.btn_read = Button(self.Buttons, width=10, text="Read", command=self.Read)
        self.btn_read.pack(side=LEFT)
        self.btn_update = Button(self.Buttons, width=10, text="Update", command=self.Update)
        self.btn_update.pack(side=LEFT)
        self.btn_delete = Button(self.Buttons, width=10, text="Delete", command=self.Delete)
        self.btn_delete.pack(side=LEFT)


        # LIST WIDGET
        self.scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.Right, columns=("id", "firstname", "surname", "email", "gender", "dob", "TP", "style", "hrate", "instructor","availability", "address"), selectmode="extended", height=500, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('id', text="id", anchor=W)
        self.tree.heading('firstname', text="firstname", anchor=W)
        self.tree.heading('surname', text="surname", anchor=W)
        self.tree.heading('email', text="email", anchor=W)
        self.tree.heading('gender', text="gender", anchor=W)
        self.tree.heading('dob', text="DOB", anchor=W)
        self.tree.heading('TP', text="telephone_num", anchor=W)
        self.tree.heading('style', text="styles", anchor=W)
        self.tree.heading('hrate', text="m.h.rate", anchor=W)
        self.tree.heading('instructor', text="instructor", anchor=W)
        self.tree.heading('availability', text="availability", anchor=W)
        self.tree.heading('address', text="address", anchor=W)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=30)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=80)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)
        self.tree.column('#5', stretch=NO, minwidth=0, width=60)
        self.tree.column('#6', stretch=NO, minwidth=0, width=60)
        self.tree.column('#7', stretch=NO, minwidth=0, width=60)
        self.tree.column('#8', stretch=NO, minwidth=0, width=80)
        self.tree.column('#9', stretch=NO, minwidth=0, width=60)
        self.tree.column('#10', stretch=NO, minwidth=0, width=80)
        self.tree.column('#11', stretch=NO, minwidth=0, width=40)
        self.tree.column('#12', stretch=NO, minwidth=0, width=80)
        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.OnSelected)
        #  ==================================METHODS============================================
    def Database(self):
        global conn, cursor
        self.conn = sqlite3.connect('dancefeet_database.db')
        self.cursor = self.conn.cursor()

    def Create(self):
        if self.FIRSTNAME.get() == "" or self.SURNAME.get() == "" or self.EMAIL.get() == "" or self.GENDER.get() == "" or self.DOB.get() == "" or self.TP.get() == "" or self.ADDRESS.get() == "":
            self.txt_result.config(text="Please complete the required field!", fg="red")
        else:
            self.Database()
            self.firstname_entry = self.FIRSTNAME.get()
            self.surname_entry = self.SURNAME.get()
            self.email_entry = self.EMAIL.get()
            self.gender_entry = self.GENDER.get()
            self.dob_entry = self.DOB.get()
            self.tp_entry = self.TP.get()
            self.style_entry = self.STYLE.get()
            self.hrate_entry = self.HRATE.get()
            self.instructor_entry = self.INSTRUCTOR.get()
            self.availability_enetry = self.AVAILABILITY.get()
            self.address_entry = self.ADDRESS.get()
            self.insert_statement = f"INSERT INTO students (firstname,surname,email,gender,dob,tp,style,hrate,instructor,availability,address) VALUES ('{self.firstname_entry}','{self.surname_entry}','{self.email_entry}','{self.gender_entry}','{self.dob_entry}','{self.tp_entry}','{self.style_entry}','{self.hrate_entry}','{self.instructor_entry}','{self.availability_enetry}','{self.address_entry}')"

            self.cursor.execute(self.insert_statement)


            self.tree.delete(*self.tree.get_children())
            self.cursor.execute("SELECT * FROM `students` ORDER BY `ID` ASC")
            self.fetch = self.cursor.fetchall()
            print(self.fetch)
            for self.data in self.fetch:
                self.tree.insert('', 'end', values=(
                self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8], self.data[9], self.data[10], self.data[11]))
            self.conn.commit()
            self.ID.set("")
            self.FIRSTNAME.set("")
            self.SURNAME.set("")
            self.EMAIL.set("")
            self.GENDER.set("")
            self.DOB.set("")
            self.TP.set("")
            self.STYLE.set("")
            self.AVAILABILITY.set("")
            self.INSTRUCTOR.set("")
            self.ADDRESS.set("")
            self.cursor.close()
            self.conn.close()
            self.txt_result.config(text="Created a data!", fg="green")

    def Read(self):
        self.tree.delete(*self.tree.get_children())
        self.Database()
        self.cursor.execute("SELECT * FROM `students` ORDER BY `ID` ASC")
        self.fetch = self.cursor.fetchall()
        print(self.fetch)
        for self.data in self.fetch:
            self.tree.insert('', 'end', values=(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8], self.data[9], self.data[10], self.data[11]))
            # self.cursor.close()
            self.conn.close()
            self.txt_result.config(text="Successfully read the data from database", fg="black")

    def Update(self):
        self.Database()
        self.id_entry = self.ID.get()
        self.firstname_entry = self.FIRSTNAME.get()
        self.surname_entry = self.SURNAME.get()
        self.email_entry = self.EMAIL.get()
        self.gender_entry = self.GENDER.get()
        self.dob_entry = self.DOB.get()
        self.tp_entry = self.TP.get()
        self.style_entry = self.STYLE.get()
        self.hrate_entry = self.HRATE.get()
        self.instructor_entry = self.INSTRUCTOR.get()
        self.availability_entry = self.AVAILABILITY.get()
        self.address_entry = self.ADDRESS.get()
        print(self.id_entry)
        if self.GENDER.get() == "":
            self.txt_result.config(text="Please select a gender", fg="red")
        else:
            self.tree.delete(*self.tree.get_children())
            self.cursor.execute(f"UPDATE `students` SET `firstname` = '{self.firstname_entry}', `gender` = '{self.gender_entry}', `surname` = '{self.surname_entry}',  `email` = '{self.email_entry}',  `dob` = '{self.dob_entry}', `tp` = '{self.tp_entry}', `style` = '{self.style_entry}', `hrate` = '{self.hrate_entry}', `instructor` = '{self.instructor_entry}', `availability` = '{self.availability_entry}', `address` = '{self.address_entry}' WHERE `ID` = '{self.id_entry}'")
            self.conn.commit()
            self.cursor.execute("SELECT * FROM `students` ORDER BY `ID` ASC")
            self.fetch = self.cursor.fetchall()
            for self.data in self.fetch:
                self.tree.insert('', 'end', values=(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8], self.data[9], self.data[10], self.data[11]))
            self.cursor.close()
            self.conn.close()
            self.ID.set("")
            self.FIRSTNAME.set("")
            self.SURNAME.set("")
            self.EMAIL.set("")
            self.GENDER.set("")
            self.DOB.set("")
            self.TP.set("")
            self.STYLE.set("")
            self.INSTRUCTOR.set("")
            self.ADDRESS.set("")
            self.btn_create.config(state=NORMAL)
            self.btn_read.config(state=NORMAL)
            self.btn_read.config(state=DISABLED)
            self.btn_delete.config(state=NORMAL)
            self.txt_result.config(text="Successfully updated the data", fg="black")

    def OnSelected(self, event):
        global id;
        self.curItem = self.tree.focus()
        self.contents = (self.tree.item(self.curItem))
        self.selecteditem = self.contents['values']
        id = self.selecteditem[0]
        self.FIRSTNAME.set("")
        self.SURNAME.set("")
        self.EMAIL.set("")
        self.GENDER.set("")
        self.DOB.set("")
        self.TP.set("")
        self.ADDRESS.set("")
        self.STYLE.set("")
        self.AVAILABILITY.set("")
        self.INSTRUCTOR.set("")
        self.ID.set(id)
        self.FIRSTNAME.set(self.selecteditem[1])
        self.SURNAME.set(self.selecteditem[2])
        self.EMAIL.set(self.selecteditem[3])
        self.GENDER.set(self.selecteditem[4])
        self.DOB.set(self.selecteditem[5])
        self.TP.set(self.selecteditem[6])
        self.STYLE.set(self.selecteditem[7])
        self.HRATE.set(self.selecteditem[8])
        self.AVAILABILITY.set(self.selecteditem[10])
        self.instructor_combo['values'] = self.combo_values_input(self.selecteditem[8],self.selecteditem[7],self.selecteditem[10])
        self.INSTRUCTOR.set(self.selecteditem[9])
        self.ADDRESS.set(self.selecteditem[11])
        self.btn_create.config(state=DISABLED)
        self.btn_read.config(state=DISABLED)
        self.btn_update.config(state=NORMAL)
        self.btn_delete.config(state=DISABLED)

    def Delete(self):
        if not self.tree.selection():
            self.txt_result.config(text="Please select an item first", fg="red")
        else:
            self.result = tkMessageBox.askquestion('Course Management - DanceFeet System',
                                                'Are you sure you want to delete this record?', icon="warning")
            if self.result == 'yes':
                self.curItem = self.tree.focus()
                self.contents = (self.tree.item(self.curItem))
                self.selecteditem = self.contents['values']
                self.tree.delete(self.curItem)
                self.Database()
                self.cursor.execute(f"DELETE FROM `students` WHERE `ID` = '{self.selecteditem[0]}'")
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
                self.txt_result.config(text="Successfully deleted the data", fg="black")

    def combo_values_input(self, student_rate,student_style,student_availability):
        self.conn = sqlite3.connect('dancefeet_database.db')
        self.cur = self.conn.cursor()
        print(student_availability)
        print(student_rate)
        print(student_style)
        self.query = self.cur.execute(f'SELECT name FROM instructors WHERE hrate <= {student_rate} AND styles LIKE "%{student_style}%" AND availability LIKE "%{student_availability}%"')

        self.data = []
        for self.row in self.cur.fetchall():
            self.data.append(self.row[0])
        return self.datas

        self.cur.close()
        self.conn.close()


    def instructor_area(self):
        self.root.destroy()
        window2=Tk()
        instructor_operations.instroutors_Manage(window2)
        window2.mainloop()

        
    def student_area(self):
        self.root.destroy()
        window3=Tk()
        students_Registration(window3)
        window3.mainloop()

    def cource_area(self):
        self.root.destroy()
        window4=Tk()
        instructor_Manage.course_Booking(window4)
        window4.mainloop()   

    def Exit(self):
        self.result = tkMessageBox.askquestion('DanceFeet System', 'Are you sure you want to exit?', icon="warning")
        if self.result == 'yes':
            self.root.destroy()
            exit()


    # INITIALIZATION
    # root.mainloop()
# root = Tk()
# gui = students_Registration(root)
# root.mainloop()
