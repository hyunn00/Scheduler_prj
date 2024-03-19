from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import tkinter.messagebox

def get_screen_size(window) :
    return window.winfo_screenwidth(), window.winfo_screenheight()

def get_window_size(window) :
    return window.winfo_reqwidth(), window.winfo_reqheight()

def center_window(root, width, height) :
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 4)
    root.geometry(size)

def calendar() :

    root.title('Schedule_calendar')

    schet = StringVar()
    sche={}
    def cancle_regi() :
        t.delete(0,END)
        t.config(state='readonly')
        d.config(state=NORMAL)
        d.delete(0,END)
        d.config(state='readonly')
        c.delete(0.0,END)
        c.config(state=DISABLED)
        reb1.destroy()
        reb2.destroy()
    
    def cancle_modi() :
        t.delete(0,END)
        t.config(state='readonly')
        d.config(state=NORMAL)
        d.delete(0,END)
        d.config(state='readonly')
        c.delete(0.0,END)
        c.config(state=DISABLED)
        reb1.destroy()
        reb2.destroy()

    def fetch_date():
        date.config(text = cal.get_date())
        
        if sche['date'] == cal.get_date() :
            list.insert(END, sche['title'])
        else :
            list.delete(0, END)

    def sche_regi_save() :
        sche['title']=t.get()
        sche['date']=cal.get_date()
        sche['content']=c.get(0.0, END)
        list.insert(END, sche['title'])
        t.delete(0,END)
        t.config(state='readonly')
        d.config(state=NORMAL)
        d.delete(0,END)
        d.config(state='readonly')
        c.delete(0.0,END)
        c.config(state=DISABLED)
        reb1.destroy()
        reb2.destroy()
        
    def sche_regi() :
        global reb1, reb2
        t.config(state=NORMAL, textvariable=schet)
        d.config(state=NORMAL)
        d.insert(0, cal.get_date())
        d.config(state='readonly')
        c.config(state=NORMAL)
        reb1 = Button(frame_right, text='Register', command=sche_regi_save)
        reb1.pack(padx=10, pady=5, side=LEFT)
        reb2 = Button(frame_right, text='Cancle', command=cancle_regi)
        reb2.pack(padx=10, pady=5, side=LEFT)

    def sche_modi_save() :
        sche['title']=t.get()
        sche['date']=cal.get_date()
        sche['content']=c.get(0.0, END)
        list.delete(END)
        list.insert(END, sche['title'])
        t.delete(0,END)
        t.config(state='readonly')
        d.config(state=NORMAL)
        d.delete(0,END)
        d.config(state='readonly')
        c.delete(0.0,END)
        c.config(state=DISABLED)
        mob1.destroy()
        mob2.destroy()

    def sche_modi() :
        global mob1, mob2
        if list.curselection=='' :
            print(list.curselection=='')
            tkinter.messagebox.showerror('modification err', 'Not choice schedule')
        else :
            t.config(state=NORMAL)
            t.insert(0, sche['title'])
            d.config(state=NORMAL)
            d.insert(0, sche['date'])
            c.config(state=NORMAL)
            c.insert(0.0, sche['content'])
            mob1 = Button(frame_right, text='Modification', command=sche_modi_save)
            mob1.pack(padx=10, pady=5, side=LEFT)
            mob2 = Button(frame_right, text='Cancle', command=cancle_modi)
            mob2.pack(padx=10, pady=5, side=LEFT)

    def sche_dele() :
        sche['content'] = ''
        sche['date'] = ''
        sche['title'] = ''
        list.delete(END)

    frame_cal = Frame(root)
    frame_cal.pack(fill=BOTH, expand=1)

    frame_left = Frame(frame_cal, bd=1, relief='solid')
    frame_left.pack(padx=5, pady=5, fill=BOTH, expand=1, side=LEFT)

    cal = Calendar(frame_left,selectmode = "day",year=2022,month=11,date=1)
    cal.pack(pady=5)

    Button(frame_left, text='Select Date', command=fetch_date).pack(pady=5)
    date = Label(frame_left, text='')
    date.pack(pady=5)

    list=Listbox(frame_left, height=20)
    list.pack(pady=5, padx=10, fill=BOTH)
    Button(frame_left, text="Schedule Register", command=sche_regi).pack(pady=5, padx=5, side=LEFT)
    Button(frame_left, text="Schedule Modification", command=sche_modi).pack(pady=5, padx=5, side=LEFT)
    Button(frame_left, text="Schedule Delete", command=sche_dele).pack(pady=5, padx=5, side=LEFT)

    frame_right = Frame(frame_cal, bd=1, relief='solid')
    frame_right.pack(padx=5, pady=5, fill=BOTH, expand=1, side=LEFT)

    Label(frame_right, text='Title', font=('TkDefaultFont', 20)).pack(pady=5, padx=5,anchor=NW)
    t = Entry(frame_right, width=60, state='readonly')
    t.pack(pady=5, padx=5,anchor=NW)
    Label(frame_right, text='Date', font=('TkDefaultFont', 20)).pack(pady=5, padx=5,anchor=NW)
    d = Entry(frame_right, width=60, state='readonly')
    d.pack(pady=5, padx=5,anchor=NW)
    Label(frame_right, text='Content', font=('TkDefaultFont', 20)).pack(pady=5, padx=5,anchor=NW)
    c = Text(frame_right, width=60, height=25, state=DISABLED)
    c.pack(pady=5, padx=5,anchor=NW)

root = Tk()
root.title('Welcom Scheduler!')
root.resizable(False, False)
center_window(root, 960, 640)

calendar()

root.mainloop()