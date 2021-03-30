from tkinter import * 
import tkinter.messagebox
from tkinter import ttk
import random 
import time
import datetime
import pymysql

def main() : 
    root = Tk ()
    app = Window1(root)
    root.mainloop()

class Window1 : 
    def __init__ (self ,  master) : 
        self.master = master 
        self.master.title("Employee Management System")
        self.master.geometry('600x300+0+0')
        self.master.config(bg='sky blue')
        self.frame = Frame(self.master , bg='steel blue')
        self.frame.pack()

        self.labelTitle = Label(self.frame ,bg='sky blue', text = "EMPLOYEE TASK MANAGER", font=('arial' , 15 , 'bold'),bd=20)
        self.labelTitle.grid(row=0 ,column = 0 ,columnspan = 2 , pady =4 )

        
# ===================================================  Frame  ===================================================================
        self.LoginFrame1 = LabelFrame(self.frame ,bg='steel blue ', width=600 ,height=200 ,bd=5, relief='flat')
        self.LoginFrame1.grid(row=1 ,column = 0 ,padx=10)


if __name__ == '__main__' :
    main() 