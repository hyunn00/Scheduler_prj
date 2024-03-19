from tkinter import *
import tkinter.messagebox
import sys, os

# window 창 가운데 띄우기
def get_screen_size(window) :
    return window.winfo_screenwidth(), window.winfo_screenheight()

def get_window_size(window) :
    return window.winfo_reqwidth(), window.winfo_reqheight()

def center_window(root, width, height) :
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 4)
    root.geometry(size)

def restart_s() :
    frame_sign.destroy()
    loginform()

def restart_f() : 
    frame_find.destroy()
    loginform()


# 회원가입 기능
def register() :
    global user
    id = sid.get()
    pwd = spwd.get()
    repwd = srepwd.get()
    name = sname.get()
    phone = sphone.get()
    

    if id=='' or pwd =='' or repwd=='' or name=='' or phone=='':
        tkinter.messagebox.showerror('Sign up fail', 'fill the empty field.')
    else :
        if pwd == repwd :
            tkinter.messagebox.showinfo('Sign up Success', 'Welcome Scheduler.')
            user['id']=id
            user['pwd']=pwd
            user['name']=name
            user['phone']=phone
            restart_s()
        else :           
            tkinter.messagebox.showerror('Sign up fail', 'Password does not match.')

def signup(event) :
    global sid, spwd,srepwd, sname, sphone, frame_sign
    sid=StringVar()
    spwd=StringVar()
    srepwd = StringVar()
    sname=StringVar()
    sphone=StringVar()

    frame_login.destroy()

    frame_sign = Frame(root, bd=1, relief='solid')
    frame_sign.pack(padx=5, pady=5, fill=BOTH, expand=1)

    Label(frame_sign, text='📝 Sign Up', font=('TkDefaultFont', 30)).pack(pady=30)
    Label(frame_sign, text='ID', font=('TkDefaultFont', 20)).place(x=100, y=150)
    Entry(frame_sign, textvariable=sid, width=60).place(x=400, y=160)
    Label(frame_sign, text='Password', font=('TkDefaultFont', 20)).place(x=100, y=200)
    Entry(frame_sign, textvariable=spwd, show = '*', width=60).place(x=400, y=210)
    Label(frame_sign, text='Password Check', font=('TkDefaultFont', 20)).place(x=100, y=250)
    Entry(frame_sign, textvariable=srepwd, show = '*', width=60).place(x=400, y=260)
    Label(frame_sign, text='Name', font=('TkDefaultFont', 20)).place(x=100, y=300)
    Entry(frame_sign, textvariable=sname, width=60).place(x=400, y=310)
    Label(frame_sign, text='Phone', font=('TkDefaultFont', 20)).place(x=100, y=350)
    Entry(frame_sign, textvariable=sphone, width=60).place(x=400, y=360)
    Button(frame_sign, text='Register', command=register, width = 10, height=2).place(x=550, y=450)
    Button(frame_sign, text='Cancel', command=restart_s, width = 10, height=2).place(x=350, y=450)

# 비밀번호 찾기 기능
def search() :
    global user

    id=fid.get()
    name=fname.get()
    phone=fphone.get()

    if id =='' or name=='' or phone=='' :
        tkinter.messagebox.showerror('Search fail', 'fill the empty field.')
    else :
        if id==user['id'] and name ==user['name'] and phone==user['phone'] :
            tkinter.messagebox.showinfo('Search Complete', 'PW : %s' % user['pwd'])
            restart_f()
        else :
            tkinter.messagebox.showerror('Search fail', 'No matching members.\n Check your entries.')

def findpw(event) :
    global fid, fname, fphone, frame_find
    fid = StringVar()
    fname = StringVar()
    fphone = StringVar()
    
    frame_login.destroy()

    frame_find = Frame(root, bd=1, relief='solid')
    frame_find.pack(padx=5, pady=5, fill=BOTH, expand=1)

    Label(frame_find, text='💡 Find Password', font=('TkDefaultFont', 30)).pack(pady=30)
    Label(frame_find, text='ID', font=('TkDefaultFont', 20)).place(x=100, y=200)
    Entry(frame_find, textvariable=fid, width=60).place(x=400, y=210)
    Label(frame_find, text='Name', font=('TkDefaultFont', 20)).place(x=100, y=250)
    Entry(frame_find, textvariable=fname, width=60).place(x=400, y=260)
    Label(frame_find, text='Phone', font=('TkDefaultFont', 20)).place(x=100, y=300)
    Entry(frame_find, textvariable=fphone, width=60).place(x=400, y=310)
    Button(frame_find, text='Search', command=search, width = 10, height=2).place(x=550, y=450)
    Button(frame_find, text='Cancel', command=restart_f, width = 10, height=2).place(x=350, y=450)

# 로그인 기능
def login() :
    global user
    id = lid.get()
    pwd = lpassword.get()

    if id=='' or pwd =='' :
        tkinter.messagebox.showerror('Login fail', 'fill the empty field.')
    else :
        if id ==user['id'] and pwd==user['pwd'] :
            tkinter.messagebox.showinfo('Login Success', 'Welcome Scheduler.')
        elif user['id']=='' and user['pwd']=='' :
            tkinter.messagebox.showerror('Login fail', 'There are no members.\n Please sign up first.')
        else :           
            tkinter.messagebox.showerror('Login fail', 'Wrong ID or password.')

def loginform() :
    global lid, lpassword, frame_login
    lid = StringVar()
    lpassword = StringVar()

    frame_login = Frame(root, bd=1, relief='solid')
    frame_login.pack(padx=5, pady=5, fill = BOTH, expand = 1)

    Label(frame_login, text='📅 DAILY SCHEDULER', font=('TkDefaultFont', 30)).pack(pady=30)
    Label(frame_login, text = "ID", font=('TkDefaultFont', 20)).place(x=100, y=200)
    Entry(frame_login, textvariable=lid, width=60).place(x=300, y=210)
    Label(frame_login, text='Password', font=('TkDefaultFont', 20)).place(x=100, y=250)
    Entry(frame_login, textvariable=lpassword, show = '*', width=60).place(x=300, y=260)
    Button(frame_login, text='Login', command=login, width = 10, height=2).place(x=450, y=300)
    slabel = Label(frame_login, text='Signup', font=('TkDefaultFont', 15))
    slabel.place(x=350, y=350)
    slabel.bind("<Button-1>", signup)
    sfind = Label(frame_login, text='find PW', font=('TkDefaultFont', 15))
    sfind.place(x=550, y=350)
    sfind.bind("<Button-1>", findpw)

user={'id':'', 'pwd':'', 'name':'', 'phone':''}

# main
root = Tk()
root.title('Welcom Scheduler!')
root.resizable(False, False)
center_window(root, 960, 640)

loginform()

root.mainloop()