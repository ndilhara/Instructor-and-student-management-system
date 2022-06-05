from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import tkinter
from tkinter import *
import sqlite3
import tkinter.messagebox as tkMessageBox
import adminOperations_menu
import instructor_Menu



class login_Window:
    def __init__(self,root):
      
        self.root=root
        self.root.title("DanceFeet System Login ")
        self.root.geometry("550x500")
      
        # Background Image
        self.bg=ImageTk.PhotoImage(file="BG.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        

        # login
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=140,y=100,height=340,width=300)

        title=Label(Frame_login,text="DanceFeet System Login",font=("Arial Black",15,"bold"),fg="green",bg="white").place(x=20,y=30)
        
        
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=140)
        self.USERNAME=Entry(Frame_login,font=("times new roman",15),bg="white")
        self.USERNAME.place(x=90,y=170,width=180,height=35)

        lbl_user=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="black",bg="white").place(x=90,y=210)
        self.PASSWORD=Entry(Frame_login,font=("times new roman",15),bg="white",show='*')
        self.PASSWORD.place(x=90,y=240,width=180,height=35)

        
        Login_btn=Button(self.root,command=self.submit0, text="Login",cursor="hand2", bg="green", fg="white", font=("times new roman",20)).place(x=200,y=420,width=180,height=40)
    

  
        # Database connect

        try:
            self.sqlconnection = sqlite3.connect('dancefeet_database.db')
            self.cursor = self.sqlconnection.cursor()
            print("Database created and Successfully Connected to SQLite")

            self.sqlite_select_Query = "select sqlite_version();"
            self.cursor.execute(self.sqlite_select_Query)
            self.record = self.cursor.fetchall()
            print("SQLite Database Version is: ", self.record)
            #cursor.close()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)


        # FUNCTIONS

    # Submit funtion
    def submit0(self):
        print("Submit")

        self.user = self.USERNAME.get()
        self.passw = self.PASSWORD.get()

        
        self.privilege_admin = "Admin"
        self.privilege_instructor = "instructor"


        while 1:
            self.check_statement = f"SELECT privilege from users WHERE username='{self.user}' AND Password = '{self.passw}';"
            self.cursor.execute(self.check_statement)
            self.privilege = self.cursor.fetchone()
            if (not self.privilege):
                print("Login failed")
                messagebox.showwarning("LOGIN FAILED","        Incorrect Credential        ")

            else:
                if self.privilege[0] == self.privilege_admin:
                    print("admin")
                    self.admin_area()

                elif self.privilege[0] == self.privilege_instructor:

                    self.instructor_area()

                else:
                    print("Incorrect Login")

                    messagebox.showwarning("LOGIN FAILED","        Incorrect Credential        ")
            break
    # Administrator operation menu loading function
    def admin_area(self):
        self.root.destroy()
        window2 = Tk()
        adminOperations_menu.admin_area_window(window2)
        window2.mainloop()


    # Instructor operation menu loading function

    def instructor_area(self):
        self.root.destroy()
        window3 = Tk()
        instructor_Menu.instructor_area_window(window3)
        window3.mainloop()

    # Exit funtion
    def Exit(self):
        self.result = tkMessageBox.askquestion('DanceFeet System', 'Are you sure you want to exit?', icon="warning")
        if self.result == 'yes':
            self.root.destroy()
            exit()


   
    



 # INITIALIZATION
if __name__ == '__main__':

    root=Tk()
    login_Window(root)
    root.mainloop()






          

 
