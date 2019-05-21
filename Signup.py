from tkinter import*
import os
creds='tempfile.temp'
def Signup():
    global pword
    global name
    global roots
    roots =Tk()
    roots.title('signup')
    instruction =Label(roots,text='please enter new cedentials\n')
    instruction.grid(row=0,column=0,sticky=E)

    name = Label(roots,text ='New Username:')
    pword =Label(roots,text='New Password:')
    name.grid(row=1,column=0,sticky=W)
    pword.grid(row=2,column=0,sticky=W)
    
    name = Entry(roots)
    pword = Entry(roots,show='*')
    name.grid(row=1,column=1)
    pword.grid(row=2,column=1)

    signupButton = Button(roots,text ='Signup',command =FSSignup)
    signupButton.grid(columnspan=2,sticky=W)
    roots.mainloop()

def FSSignup():
    with open(creds,'W') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()

    roots.destroy()
    Login()

def Login():
    global nameEL
    global pwordEL
    rootA =Tk()
    rootA.title('Login')
    instruction =Label(rootA,text='please login\n')
    instruction.grid(sticky=E)

    nameEL = Label(rootA,text='Username:')
    pwordEL =Label(rootA,text='Password:')
    nameEL.grid(row=1,sticky=W)
    pwordEL.grid(row=1,sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA,show='*')
    nameEL.grid(row=1,column=1)
    pwordEL.grid(row=2,column=1)

    LoginButton = button(rootA,text ='Login',command =CheckLogin)
    LoginButton.grid(columnSpan=2,sticky=W)
    
    reuser =Buttton(rootA,tex='Delete user',command=CheckLogin)
    reuser.grid(columnspan=2,sticky=W)
    rootA.mainloop()

def CheckLogin():
    with open(creds)as f:
        data =f.readLines()
        uname =data[0].rstrip()
        pword = data[1].rstrip()

        if Name.get() ==uname and pword ==pword:

            r =Tk()
            r.title(':D')
            r.geometry('150*50')
            rlbl =Label(r,text ='\n[+]Logged in')
            rlbl.pack()
            r.mainloop()
        else:
            r =Tk()
            r.title(':D')
            r.geometry('150*50')
            rlbl =Label(r,text ='\n[+] invalid Login')
            rlbl.pack()
            r.mainloop()

def Deluser():
    os.remove(creds)
    rootA.destroy()
    signup()

    if os.path.isfile(creds):
        Login()
    else:
        signup()
if __name__ == '__main__':
    Signup()
                
            
