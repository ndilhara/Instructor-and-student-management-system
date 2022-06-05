import tkinter
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import studentsBook_instructor



class instructor_area_window():
    def __init__(self, window):
        self.admin_window = window
        self.admin_window.title("Instructor Area - DanceFeet System")
        self.screen_width = self.admin_window.winfo_screenwidth()
        self.screen_height = self.admin_window.winfo_screenheight()
        self.width = 900
        self.height = 350
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.admin_window.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.admin_window.resizable(0, 0)

        # FRAME
        self.Top = Frame(self.admin_window, width=900, height=50, bd=8, relief="raise")
        self.Top.pack(side=TOP)
        self.Left = Frame(self.admin_window, width=300, height=500, bd=8, relief="raise")
        self.Left.pack(side=LEFT)
        self.Right = Frame(self.admin_window, width=600, height=500, bd=8, relief="raise")
        self.Right.pack(side=RIGHT)
        self.Forms = Frame(self.Left, width=300, height=450)
        self.Forms.pack(side=TOP)


        # LABEL WIDGET
        self.txt_title = Label(self.Top, width=900, font=('arial', 24), text="Instructor Area - DanceFeet System")
        self.txt_title.pack()

        self.LessonBooking_btn = Button(self.Forms, text="Lesson Booking", width=50, height=1, font=('arial', 20),
                                        fg='white', background='green', bd=2, command=self.cource_area). \
            grid(row=3, column=1, padx=4, pady=5)
        self.exit_btn = Button(self.Forms, text="EXIT", width=50, height=1, font=('arial', 20), fg='white',
                               command=self.Exit, background='red', bd=2). \
            grid(row=4, column=1, padx=4, pady=5)




    def Exit(self):
        self.result = tkMessageBox.askquestion('DanceFeet System', 'Are you sure you want to exit?', icon="warning")
        if self.result == 'yes':
            self.admin_window.destroy()
            exit()

    # course booking class loading funtion
    def cource_area(self):
        self.admin_window.destroy()
        window4 = Tk()
        studentsBook_instructor.student_Booking(window4)
        window4.mainloop()


# root=Tk()
# gui2=instructor_area_window(root)
# root.mainloop()