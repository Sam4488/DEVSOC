import pickle
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os


def empty(x, y, z, fg, bg):
    lbl = Label(z, text=" ", fg=fg, bg=bg)
    lbl.grid(row=x, column=y)


def signup():
    top = Toplevel()
    top.title('Sign Yourself Up')
    top.geometry('1600x800')
    top.configure(bg='black')

    def output(D):
        C1 = open("signups.dat", "ab+")
        C2 = open("Backup.dat", "ab+")
        for x in D:
            try:
                D[x] = D[x].get()
            except AttributeError:
                pass
        f = 'Data entry of ' + D['FName'] + ' ' + D['LName'] + ' was successful.'
        messagebox.showinfo('Confirmation', f)
        pickle.dump(D, C1)
        pickle.dump(D, C2)
        C1.close()
        C2.close()
        top.destroy()

    lbl = Label(top,
                text='                                                                                                                                                                 ',
                bg='black', fg='black')
    lbl.grid(row=0, column=0)
    for i in range(15):
        lbl2 = Label(top,
                     text='                                                                                                                                                                 ',
                     bg='black', fg='white')
        lbl2.grid(row=i, column=1)
    fr = LabelFrame(top, text='Fill in Your Details', bg='black', fg='white', highlightthickness=10,
                    highlightcolor='#EDB84D')
    fr.grid(row=8, column=1)
    # Labels--------------------------------------------------------------------------------------------------
    L_text = ["First Name : ", "Last Name : ", "Vehicle Name : ", "Email ID : ", "Password :"]
    L_row = [1, 2, 3, 4, 5]
    for j in L_text:
        Label(fr, text=j, font="Helvetica 12 bold", bg='black', fg='#EDB84D').grid(row=L_row[L_text.index(j)], column=1,
                                                                                   sticky=W)
    # Entry Box Variables----------------------------------------------------------------------------------------------
    VarFName = StringVar()
    VarLName = StringVar()
    VarVehicle = StringVar()
    VarEMail = StringVar()
    VarPSWRD = StringVar()
    # Entry Boxes------------------------------------------------------------------------------------------------------
    FNameEntry = Entry(fr, borderwidth=3, textvariable=VarFName)
    FNameEntry.grid(row=1, column=2, sticky=W, padx=10, pady=10, ipadx=100)

    VarLNameEntry = Entry(fr, borderwidth=3, textvariable=VarLName)
    VarLNameEntry.grid(row=2, column=2, sticky=W, padx=10, pady=10, ipadx=100)

    Vehicle = Entry(fr, borderwidth=3, textvariable=VarVehicle)
    Vehicle.grid(row=3, column=2, sticky=W, padx=10, pady=10, ipadx=100)

    Mail = Entry(fr, borderwidth=3, textvariable=VarEMail)

    Mail.grid(row=4, column=2, sticky=W, padx=10, pady=10, ipadx=100)

    Pswrd = Entry(fr, borderwidth=3, textvariable=VarPSWRD)
    Pswrd.grid(row=5, column=2, sticky=W, padx=10, pady=10, ipadx=100)

    D = {}
    D["FName"] = VarFName
    D["LName"] = VarLName
    D["Vehicle"] = VarVehicle
    D["EMail"] = VarEMail
    D["Password"] = VarPSWRD
    D["Booked Seat"] = ""
    # Buttons-------------------------------------------------------------------------------------------------
    submit = Button(fr, text='SUBMIT', borderwidth=3, command=lambda: output(D), bg='black', fg='#EDB84D',
                    font="Times 12 italic bold", relief='groove', bd=7, activebackground='#EDB84D').grid(row=6,
                                                                                                         column=2,
                                                                                                         ipadx=100,
                                                                                                         sticky=W)
    done = Button(fr, text='EXIT', borderwidth=3, command=lambda: top.destroy(), bg='black', fg='#EDB84D',
                  font="Times 12 italic bold", relief='groove', bd=7, activebackground='#EDB84D').grid(row=8, column=2,
                                                                                                       ipadx=110,
                                                                                                       sticky=W)


def book(z):
    booking = Tk()
    booking.geometry('800x800')
    booking.configure(bg="black")
    def colour(a):
        
        if(button_row1[All_slots.index(a.get())]["bg"]=="green"):
            button_row1[All_slots.index(a.get())]["bg"]="red"
        for i in All_slots:
            if(a.get()!=i):
                button_row1[All_slots.index(i)]["bg"]="green"
    
    for i in range(20):
        lbl2 = Label(booking,
                     text='                                                                                                                                                                 ',
                     bg='black', fg='white')
        lbl2.grid(row=0, column=i)
    
    frame = LabelFrame(booking, text='Following is the Status of the Slots',bg='black')
    frame.grid(row=0, column=0)
    button_row1 = []
    All_slots = []
    for i in range(6):
        button_row1.append(Button(frame, text='A' + str(i + 1), bg='green', fg='black'))
        button_row1[i].grid(row=0, column=i)
        All_slots.append('A' + str(i + 1))
    button_row1.append(Button(frame, text='B7', bg='green', fg='black'))
    button_row1[6].grid(row=1, column=5)
    All_slots.append('B7')
    for i in range(7, 13):
        button_row1.append(Button(frame, text='C' + str(i + 1), bg='green', fg='black'))
        button_row1[i].grid(row=2, column=i - 7)
        All_slots.append('C' + str(i + 1))
    button_row1.append(Button(frame, text='D14', bg='green', fg='black'))
    button_row1[13].grid(row=3, column=5)
    All_slots.append('D14')
    for i in range(14, 20):
        button_row1.append(Button(frame, text='E' + str(i + 1), bg='green', fg='black'))
        button_row1[i].grid(row=4, column=i - 14)
        All_slots.append('E' + str(i + 1))
    
    frame2 = LabelFrame(booking, text='Fill whatever You want to do :)',bg='black')
    frame2.grid(row=1, column=0)
    C1 = open("signups.dat", "ab+")
    data = datas()
    Available = []
    Booked = []

    try:
        while True:
            x = pickle.load(C1)
            Booked.append(x['FName'][1])

    except EOFError:
        C1.close()
    for i in All_slots:
        if i not in Booked:
            Available.append(i)
    C1 = open("signups.dat", "rb+")
    try:
        while True:
            x = pickle.load(C1)
            for i in All_slots:
                if(i==x['Booked Seat']):
                    button_row1[All_slots.index(x['Booked Seat'])]["bg"]="red"

    except EOFError:
        C1.close()
    
    Label(frame2, text="Book a Slot ? Available Seats ->",bg='black',fg='#EDB84D').grid(row=0,column=0)
    avs = StringVar()
    def confirm_seat(a):
        C1 = open("signups.dat", "rb+")
        already_booked=[]
        try:
            while True:
                i=pickle.load(C1)
                if(i['Booked Seat']!=''):
                    already_booked.append(i['Booked Seat'])
        except EOFError:
            C1.close()
        
        C1 = open("signups.dat", "rb+")
   
#---------------------------------------------------------------------------------------------------------------------------
        temp=open("Clone.dat","wb+")
        try:
            while True:
                i=pickle.load(C1)
                if(i['FName']==z):
                    if(a.get() in already_booked):
                        messagebox.showerror('Confirmation status','Slot number '+a.get()+' is already Booked !')
                    else:
                        i['Booked Seat']=a.get()
                        messagebox.showinfo('Confirmation status','Your Slot number '+a.get()+' is confirmed')
                pickle.dump(i,temp)
        except EOFError:
            booking.destroy()
        C1.close()
        temp.close()
        os.remove('signups.dat')
        os.rename('Clone.dat','signups.dat')
        
#---------------------------------------------------------------------------------------------------------------------------
    o = OptionMenu(frame2, avs, *Available)
    o.grid(row=0,column=1)
    b = Button(frame2, text="Check Seat Location", command=lambda: colour(avs),bg='black',fg='#EDB84D').grid(row=1,column=0,sticky=W,padx=10)
    b2 = Button(frame2, text="Confirm Seat", command=lambda: confirm_seat(avs),bg='black',fg='#EDB84D').grid(row=2,column=0,sticky=W,padx=10)
    



def datas():
    data_dict = {}
    f = open('signups.dat', 'rb+')
    try:
        while True:
            x = pickle.load(f)
            L=[x["Password"],x["Booked Seat"]]
            data_dict[x['FName']] = L
    except EOFError:
        f.close()
    return data_dict


def password():
    def submit():
        C1 = open("signups.dat", "ab+")
        data = datas()
        count = 0
        for i in data:
            count += 1
            if (PASSWORD.get() == data[i][0] and NAME.get() == i):
                passwin.destroy()
                book(i)
                break
            else:
                if (count == len(data)):
                    messagebox.showerror('ERROR !', 'The Password you entered is incorrect')

    passwin = Toplevel()
    passwin.geometry('1600x800')
    passwin.configure(bg='black')
    passwin.title('PASSWORD')

    lbl = Label(passwin,
                text='                                                                                                                                                                 ',
                bg='black', fg='black')
    lbl.grid(row=0, column=0)
    for i in range(8):
        lbl2 = Label(passwin,
                     text='                                                                                                                                                                 ',
                     bg='black', fg='white')
        lbl2.grid(row=i, column=1)
    fr = LabelFrame(passwin, text='LOG IN !', bg='black', fg='white', highlightthickness=10, highlightcolor='#EDB84D')
    fr.grid(row=8, column=1)

    PASSWORD = StringVar()
    NAME = StringVar()
    name_lbl = Label(fr, text='Enter your Name : ', bg='black', fg='#EDB84D', font='28').grid(row=0, column=0)
    lbl = Label(fr, bg='black', fg='#EDB84D', font='28').grid(row=1, column=0)
    pass_lbl = Label(fr, text='Enter the Password : ', bg='black', fg='#EDB84D', font='28').grid(row=2, column=0)
    lbl = Label(fr, bg='black', fg='#EDB84D', font='28').grid(row=3, column=0)
    name_entry = Entry(fr, textvariable=NAME, borderwidth=3).grid(row=0, column=1, padx=50)
    password_entry = Entry(fr, textvariable=PASSWORD, borderwidth=3, show='*').grid(row=2, column=1, padx=50)
    pass_submit = Button(fr, text='Continue', font='28', command=submit, bg='black', fg='#EDB84D', padx=30,
                         relief='groove', bd=7, activebackground='#EDB84D').grid(row=4, column=1, sticky=W)


root = Tk()
root.title("PMS")
root.configure(bg='black')

frame = LabelFrame(root, padx=100, pady=20, fg="white", bg="black", highlightbackground="black")
frame.grid(row=0, column=0)

frame2 = LabelFrame(root, padx=100, pady=20, fg="white", bg="black", highlightbackground="black", highlightthickness=10,
                    highlightcolor='#EDB84D')
frame2.grid(row=1, column=0)

Label(frame, text='Parking Management System', font="Verdana 40 italic bold", bg='black', fg='#EDB84D').grid(row=0,
                                                                                                             column=0)

button1 = Button(frame2, text="Sign Up", command=signup, padx=10, pady=5, bg='black', fg='#EDB84D', font='28',
                 relief='groove', bd=7, activebackground='#EDB84D')
button1.grid(row=0, column=0)
empty(1, 0, frame2, 'black', 'black')
button2 = Button(frame2, text="Log in", padx=10, pady=5, bg='black', fg='#EDB84D', command=password, font='28',
                 relief='groove', bd=7, activebackground='#EDB84D')
button2.grid(row=2, column=0)

root.mainloop()
