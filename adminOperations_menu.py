import tkinter
from tkinter import *
import tkinter.messagebox as tkMessageBox
from instructor_operations import instroutors_Manage
from students_Manage import students_Registration
from instructor_Manage import course_Booking


class admin_area_window():
    def __init__(self, window):
        self.admin_window = window
        self.admin_window.title("Admin Area - DanceFeet System")
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
        self.Forms = Frame(self.Left, width=800, height=450)
        self.Forms.pack(side=TOP)
        
        self.txt_title = Label(self.Top, width=900, font=('arial', 24), text="Admin Area - DanceFeet System")
        self.txt_title.pack()
        

        # Menu buttons
        self.StudentManagement_btn =Button(self.Forms, text="Student Management", width=50, height=1, font=('arial', 20), fg='white',background='green',bd=2,command=self.student_area). \
            grid(row=1, column=1, padx=4, pady=5)
        
        self.InstructorManagement_btn = Button(self.Forms, text="Instructor Management", width=50, height=1, fg='white', font=('arial', 20),background='green',bd=2,activeforeground = "green",command=self.instructor_area). \
            grid(row=2, column=1, padx=4, pady=5)
        self.LessonBooking_btn = Button(self.Forms, text="Lesson Booking", width=50, height=1, font=('arial', 20), fg='white', background='green',bd=2,command=self.cource_area). \
            grid(row=3, column=1, padx=4, pady=5)
        self.exit_btn = Button(self.Forms, text="EXIT", width=50, height=1, font=('arial', 20), fg='white', command=self.Exit, background='red',bd=2). \
            grid(row=4, column=1, padx=4, pady=5)

        

    #Exit funtion
    def Exit(self):
        self.result = tkMessageBox.askquestion('DanceFeet System', 'Are you sure you want to exit?', icon="warning")
        if self.result == 'yes':
            self.admin_window.destroy()
            exit()

        
    
    # Instructor operation class loading funtion
    def instructor_area(self):
        self.admin_window.destroy()
        window2=Tk()
        instroutors_Manage(window2)
        window2.mainloop()
        
    # students management operation class loading
    def student_area(self):
        self.admin_window.destroy()
        window3=Tk()
        students_Registration(window3)
        window3.mainloop()

    # student booking operation class loading
    def cource_area(self):
        self.admin_window.destroy()
        window4=Tk()
        course_Booking(window4)
        window4.mainloop()



# window testing installations

# root=Tk()
# gui2=admin_area_window(root)
# root.mainloop()