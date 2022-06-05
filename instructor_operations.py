import tkinter
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import students_Manage
import instructor_Manage


class instroutors_Manage(object):

    def __init__(self,window):


        self.root = window
        self.root.title("Instructor Management - DanceFeet System")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.width = 1200
        self.height = 800
        x = (self.screen_width / 2) - (self.width / 2)
        y = (self.screen_height / 2) - (self.height / 2)
        self.root.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        # self.root.resizable(0, 0)
        
    # VARIABLES
        self.USERNAME = tkinter.StringVar()
        self.PASSWORD = tkinter.StringVar()
        self.NAME = tkinter.StringVar()
        self.GENDER = tkinter.StringVar()
        self.STYLES = tkinter.StringVar()
        self.TP = tkinter.StringVar()
        self.HRATE = tkinter.StringVar()
        self.AVAILABILITY = tkinter.StringVar()
        self.gender = tkinter.StringVar()


        #FRAME
        self.Top = Frame(self.root, width=900, height=50, bd=8, relief="raise")
        self.Top.pack(side=TOP)
        self.Left = Frame(self.root, width=300, height=500, bd=8, relief="raise")
        self.Left.pack(side=LEFT)
        self.Right = Frame(self.root, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=RIGHT)
        self.Forms = Frame(self.Left, width=300, height=700)
        self.Forms.pack(side=TOP)
        self.Buttons = Frame(self.Left, width=300, height=100, bd=8, relief="raise")
        self.Buttons.pack(side=BOTTOM)
        self.RadioGroup = Frame(self.Forms)
        self.Male = Radiobutton(self.RadioGroup, text="Male", variable=self.gender, value="Male", font=('arial', 16)).pack(side=LEFT)
        self.Female = Radiobutton(self.RadioGroup, text="Female", variable=self.gender, value="Female", font=('arial', 16)).pack(side=LEFT)
            


        self.StudentManagement_btn =Button(self.Top, text="Student Management", width=30, height=1, font=('arial', 12), fg='white',background='green',bd=2,command=self.student_area). \
            grid(row=0, column=1, padx=4, pady=5)
        
        self.InstructorManagement_btn = Button(self.Top, text="Instructor Management", width=30, height=1, fg='white', font=('arial', 12),background='green',bd=2,activeforeground = "green",activebackground = "pink",command=self.instructor_area,relief="groove"). \
            grid(row=0, column=2, padx=4, pady=5)
        self.LessonBooking_btn = Button(self.Top, text="Lesson Booking", width=30, height=1, font=('arial', 12), fg='white', background='green',bd=2,command=self.cource_area). \
            grid(row=0, column=3, padx=4, pady=5)
        self.exit_btn = Button(self.Top, text="EXIT", width=30, height=1, font=('arial', 12), fg='white', command=self.Exit, background='green',bd=2). \
            grid(row=0, column=4, padx=4, pady=5)

        self.txt_title = Label(self.Top,width=40,font=('arial', 10),text="Instructor Management - DanceFeet System",borderwidth=0,relief="groove",fg='green')
        self.txt_title. grid(row=2, column=1, padx=4, pady=5)


            # LABEL WIDGET

        self.txt_firstname = Label(self.Forms, text="username:", font=('arial', 16), bd=25)
        self.txt_firstname.grid(row=0,sticky="e")
        self.txt_password = Label(self.Forms, text="password:", font=('arial', 16), bd=25)
        self.txt_password.grid(row=1, sticky="e")
        self.txt_lastname = Label(self.Forms, text="Name:", font=('arial', 16), bd=25)
        self.txt_lastname.grid(row=2, sticky="e")
        self.txt_gender = Label(self.Forms, text="Gender:", font=('arial', 16), bd=25)
        self.txt_gender.grid(row=3, sticky="e")
        self.txt_styles = Label(self.Forms, text="styles:", font=('arial', 16), bd=25)
        self.txt_styles.grid(row=4, sticky="e")
        self.txt_TpNo = Label(self.Forms, text="Telephone Number:", font=('arial', 16), bd=25)
        self.txt_TpNo .grid(row=5, sticky="e")
        self.txt_hourRate = Label(self.Forms, text="Hour Rate:", font=('arial', 16), bd=25)
        self.txt_hourRate.grid(row=6, sticky="e")
        self.txt_availability = Label(self.Forms, text="Availability (Ex:Mon,Tue..):", font=('arial', 16), bd=25)
        self.txt_availability.grid(row=7, sticky="e")

        self.txt_result = Label(self.Buttons)
        self.txt_result.pack(side=TOP)
        



        
        # ENTRY WIDGET
        self.entry_username = Entry(self.Forms, textvariable=self.USERNAME, width=30)
        self.entry_username.grid(row=0, column=1)

        self.password = Entry(self.Forms, textvariable=self.PASSWORD, show='*', width=30)
        self.password.grid(row=1, column=1)

        self.name = Entry(self.Forms, textvariable=self.NAME, width=30)
        self.name.grid(row=2, column=1)


        self.gender = ttk.Combobox(self.Forms, textvariable=self.GENDER, width=28)
        self.gender.grid(row=3, column=1)
        self.gender['values'] = ('male', 'female')


        self.styles = Entry(self.Forms, textvariable=self.STYLES, width=30)
        self.styles.grid(row=4, column=1)

        self.tp = Entry(self.Forms, textvariable=self.TP, width=30)
        self.tp.grid(row=5, column=1)

        self.hrate = Entry(self.Forms, textvariable=self.HRATE, width=30)
        self.hrate.grid(row=6, column=1)

        self.availability = Entry(self.Forms, textvariable=self.AVAILABILITY, width=30)
        self.availability.grid(row=7, column=1)

        # BUTTONS WIDGET
        self.btn_create = Button(self.Buttons, width=10, text="Create", command=self.Create)
        self.btn_create.pack(side=LEFT)
        self.btn_read = Button(self.Buttons, width=10, text="Read", command=self.Read)
        self.btn_read.pack(side=LEFT)
        self.btn_update = Button(self.Buttons, width=10, text="Update", command=self.Update, state=DISABLED)
        self.btn_update.pack(side=LEFT)
        self.btn_delete = Button(self.Buttons, width=10, text="Delete", command=self.Delete)
        self.btn_delete.pack(side=LEFT)

        # LIST WIDGET
        self.scrollbary = Scrollbar(self.Right, orient=VERTICAL)
        self.scrollbarx = Scrollbar(self.Right, orient=HORIZONTAL)
        self.tree = ttk.Treeview(self.Right, columns=("username", "name", "gender", "styles", "tp", "hrate", "availability", "password"), selectmode="extended", height=500, yscrollcommand=self.scrollbary.set, xscrollcommand=self.scrollbarx.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)
        self.scrollbarx.config(command=self.tree.xview)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('username', text="Username", anchor=W)
        self.tree.heading('name', text="Name", anchor=W)
        self.tree.heading('gender', text="gender", anchor=W)
        self.tree.heading('styles', text="styles", anchor=W)
        self.tree.heading('tp', text="telephone_number", anchor=W)
        self.tree.heading('hrate', text="hour_rate", anchor=W)
        self.tree.heading('availability', text="Availability", anchor=W)
        self.tree.heading('password', text="Password", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree.column('#2', stretch=NO, minwidth=0, width=80)
        self.tree.column('#3', stretch=NO, minwidth=0, width=120)
        self.tree.column('#4', stretch=NO, minwidth=0, width=80)
        self.tree.column('#5', stretch=NO, minwidth=0, width=150)
        self.tree.column('#6', stretch=NO, minwidth=0, width=120)
        self.tree.column('#7', stretch=NO, minwidth=0, width=120)
        self.tree.column('#8', stretch=NO, minwidth=0, width=120)
        self.tree.pack()
        self.tree.bind('<Double-Button-1>', self.OnSelected)



    # METHODS

    #Database connecting funtion
    def Database(self):
        global conn, cursor
        self.conn = sqlite3.connect('dancefeet_database.db')
        self.cursor = self.conn.cursor()

    # Record creating funtion
    def Create(self):
        if self.USERNAME.get() == "" or self.PASSWORD.get() == "" or self.NAME.get() == "" or self.gender.get() == "" or self.STYLES.get() == "" or self.TP.get() == "" or self.HRATE.get() == "" or self.AVAILABILITY.get() == "":
            self.txt_result.config(text="Please complete the required field!", fg="red")
        else:
            self.Database()
            self.username_entry = self.USERNAME.get()
            self.password_entry = self.PASSWORD.get()
            self.name_entry = self.NAME.get()
            self.gender_entry = self.GENDER.get()
            self.style_entry = self.STYLES.get()
            self.tp_entry = self.TP.get()
            self.hrate_entry = self.HRATE.get()
            self.availability_entry = self.AVAILABILITY.get()

            self.insert_statement = f"INSERT INTO instructors(username,name,gender,styles,tp,hrate,availability,password) VALUES ('{self.username_entry}','{self.name_entry}','{self.gender_entry}','{self.style_entry}','{self.tp_entry}','{self.hrate_entry}','{self.availability_entry}','{self.password_entry}')"
            self.insert_statement_login = f"INSERT INTO users(username,password,privilege) VALUES ('{self.username_entry}','{self.password_entry}','instructor')"
            self.cursor.execute(self.insert_statement)
            self.cursor.execute(self.insert_statement_login)


            self.tree.delete(*self.tree.get_children())
            self.cursor.execute("SELECT * FROM `instructors` ORDER BY `username` ASC")
            self.fetch = self.cursor.fetchall()
            print(self.fetch)

            self.conn.commit()
            self.USERNAME.set("")
            self.NAME.set("")
            self.GENDER.set("")
            self.STYLES.set("")
            self.TP.set("")
            self.HRATE.set("")
            self.AVAILABILITY.set("")
            self.PASSWORD.set("")
            self.cursor.close()
            self.conn.close()
            self.txt_result.config(text="Created a data!", fg="green")


    #Record reading file
    def Read(self):
        self.tree.delete(*self.tree.get_children())
        self.Database()
        self.cursor.execute("SELECT * FROM `instructors` ORDER BY `username` ASC")
        self.fetch = self.cursor.fetchall()
        for self.data in self.fetch:
            self.tree.insert('', 'end', values=(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7]))
            # self.cursor.close()
            self.conn.close()
            self.txt_result.config(text="Successfully read the data from database", fg="black")


    #Record updating funtion
    def Update(self):
        self.Database()
        self.username_entry = self.USERNAME.get()
        self.password_entry = self.PASSWORD.get()
        self.name_entry = self.NAME.get()
        self.gender_entry = self.GENDER.get()
        self.style_entry = self.STYLES.get()
        self.tp_entry = self.TP.get()
        self.hrate_entry = self.HRATE.get()
        self.availability_entry = self.AVAILABILITY.get()
        if self.gender.get() == "":
            self.txt_result.config(text="Please select a gender", fg="red")
        else:
            self.tree.delete(*self.tree.get_children())
            #insert_statement = f"UPDATE instructors(username,name,gender,styles,tp,hrate,availability,password) VALUES ('{self.username_entry}','{self.name_entry}','{self.gender_entry}','{self.style_entry}','{self.tp_entry}','{self.hrate_entry}','{self.availability_entry}','{self.password_entry}')"

            self.cursor.execute(f"UPDATE `instructors` SET `name` = '{self.name_entry}', `gender` = '{self.gender_entry}', `styles` = '{self.style_entry}',  `tp` = '{self.tp_entry}',  `hrate` = '{self.hrate_entry}', `availability` = '{self.availability_entry}',`password` = '{self.password_entry}' WHERE `username` = '{self.username_entry}'")
            self.cursor.execute(f"UPDATE `users` SET `password` = '{self.password_entry}' WHERE `username` = '{self.username_entry}'")
            self.conn.commit()
            self.cursor.execute("SELECT * FROM `instructors` ORDER BY `username` ASC")
            fetch = self.cursor.fetchall()
            for self.data in self.fetch:
                self.tree.insert('', 'end', values=(self.data[0], self.data[1], self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7]))
            self.cursor.close()
            self.conn.close()
            self.USERNAME.set("")
            self.NAME.set("")
            self.PASSWORD.set("")
            self.gender.set("")
            self.STYLES.set("")
            self.TP.set("")
            self.HRATE.set("")
            self.AVAILABILITY.set("")
            self.btn_create.config(state=NORMAL)
            self.btn_read.config(state=NORMAL)
            self.btn_update.config(state=DISABLED)
            self.btn_delete.config(state=NORMAL)
            self.txt_result.config(text="Successfully updated the data", fg="black")


    def OnSelected(self,event):
        global username;
        self.curItem = self.tree.focus()
        self.contents = (self.tree.item(self.curItem))
        self.selecteditem = self.contents['values']
        print(self.selecteditem)
        username = self.selecteditem[0]
        self.USERNAME.set("")
        self.GENDER.set("")
        self.PASSWORD.set("")
        self.STYLES.set("")
        self.TP.set("")
        self.HRATE.set("")
        self.AVAILABILITY.set("")

        self.USERNAME.set(username)
        #PASSWORD.set(selecteditem[7])
        self.NAME.set(self.selecteditem[1])
        self.GENDER.set(self.selecteditem[2])
        self.PASSWORD.set(self.selecteditem[7])
        self.STYLES.set(self.selecteditem[3])
        self.TP.set(self.selecteditem[4])
        self.HRATE.set(self.selecteditem[5])
        self.AVAILABILITY.set(self.selecteditem[6])
        self.btn_create.config(state=DISABLED)
        self.btn_read.config(state=DISABLED)
        self.btn_update.config(state=NORMAL)
        self.btn_delete.config(state=DISABLED)

    #Record delete funtion
    def Delete(self):
        if not self.tree.selection():
            self.txt_result.config(text="Please select an item first", fg="red")
        else:
            self.result = tkMessageBox.askquestion('Instructor Management - DanceFeet System',
                                              'Are you sure you want to delete this record?', icon="warning")
            if self.result == 'yes':
                self.curItem = self.tree.focus()
                self.contents = (self.tree.item(self.curItem))
                self.selecteditem = self.contents['values']
                self.tree.delete(self.curItem)
                self.Database()
                self.cursor.execute(f"DELETE FROM `instructors` WHERE `username` = '{self.selecteditem[0]}'")
                self.cursor.execute(f"DELETE FROM `users` WHERE `username` = '{self.selecteditem[0]}'")
                self.conn.commit()
                self.cursor.close()
                self.conn.close()
                self.txt_result.config(text="Successfully deleted the data", fg="black")


    def instructor_area(self):
        
        
        self.root.destroy()
        window2=Tk()
        instroutors_Manage(window2)
        window2.mainloop()   

    def student_area(self):
        
        
        self.root.destroy()
        window3=Tk()
        students_Manage.students_Registration(window3)
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






    # ==================================INITIALIZATION=====================================
# root=Tk()
# gui2=instroutors(root)
# root.mainloop()