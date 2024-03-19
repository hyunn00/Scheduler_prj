from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkcalendar import Calendar
import datetime

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

# 화면 전환 함수
def restart_s() : # 회원가입 페이지 -> 로그인 페이지
    frame_sign.destroy()
    loginform()

def restart_f() : # 비빌번호 찾기 페이지 -> 로그인 페이지
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
    
    # 회원가입 상황별 메시지창 띄우기
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

# 회원가입 화면
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

    # 비밀번호 찾기 상황별 메시지창 띄우기
    if id =='' or name=='' or phone=='' :
        tkinter.messagebox.showerror('Search fail', 'fill the empty field.')
    else :
        if id==user['id'] and name ==user['name'] and phone==user['phone'] :
            tkinter.messagebox.showinfo('Search Complete', 'PW : %s' % user['pwd'])
            restart_f()
        else :
            tkinter.messagebox.showerror('Search fail', 'No matching members.\n Check your entries.')

# 비밀번호 찾기 화면
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

    # 로그인 상황별 메시지창 띄우기
    if id=='' or pwd =='' :
        tkinter.messagebox.showerror('Login fail', 'fill the empty field.')
    else :
        if id ==user['id'] and pwd==user['pwd'] :
            tkinter.messagebox.showinfo('Login Success', 'Welcome Scheduler.')
            calendar()
        elif id==admin['id'] and pwd==admin['pwd'] :
            tkinter.messagebox.showinfo('Login Success', 'Admin Account.\nWelcome Scheduler.')
            adminform()
        elif user['id']=='' and user['pwd']=='' :
            tkinter.messagebox.showerror('Login fail', 'There are no members.\n Please sign up first.')
        
        else :           
            tkinter.messagebox.showerror('Login fail', 'Wrong ID or password.')

# 로그인 화면
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

# 달력 화면
def calendar() :
    frame_login.destroy()
    root.title('Schedule_calendar')

    # 등록 화면에서의 취소 함수
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
    
    # 수정 화면에서의 취소 함수
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

    # 날짜 저장 및 설정
    def fetch_date():
        date.config(text = cal.get_date())
        
        if sche['date'] == cal.get_date() :
            list.insert(END, sche['title'])
        else :
            list.delete(0, END)

    # 일정 등록 저장 기능
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
    
    # 일정 등록 화면
    def sche_regi() :
        global reb1, reb2
        t.config(state=NORMAL)
        d.config(state=NORMAL)
        d.insert(0, cal.get_date())
        d.config(state='readonly')
        c.config(state=NORMAL)
        reb1 = Button(frame_right, text='Register', command=sche_regi_save)
        reb1.pack(padx=10, pady=5, side=LEFT)
        reb2 = Button(frame_right, text='Cancle', command=cancle_regi)
        reb2.pack(padx=10, pady=5, side=LEFT)

    # 일정 수정 저장 기능
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

    # 일정 수정 화면
    def sche_modi() :
        global mob1, mob2

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

    # 일정 삭제 기능
    def sche_dele() :
        sche['content'] = ''
        sche['date'] = ''
        sche['title'] = ''
        list.delete(END)

    # 달력 화면
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
    Button(frame_left, text="Schedule Selection", command=sche_modi).pack(pady=5, padx=5, side=LEFT)
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

# 관리자 화면
def adminform() :
    global user, admin
    root.title('admin_view')
    frame_login.destroy()

    # 사용자 정보 상세 화면
    def user_modi() :
        global item
        item=treeview.item(treeview.focus())
        view=Toplevel()
        view.title('%s Detail'%item['values'][0])
        center_window(view, 480, 560)
        Label(view, text='ID', font=('TkDefaultFont', 20)).place(x=20, y=10)
        id = Entry(view, width=50)
        id.place(x=20,y=50)
        Label(view, text='Name', font=('TkDefaultFont', 20)).place(x=20, y=90)
        name = Entry(view, width=50)
        name.place(x=20,y=130)
        Label(view, text='Phone', font=('TkDefaultFont', 20)).place(x=20, y=170)
        phone = Entry(view, width=50)
        phone.place(x=20,y=210)
        Label(view, text='Last Connection Date', font=('TkDefaultFont', 20)).place(x=20, y=250)
        date = Entry(view, width=50)
        date.place(x=20,y=290)
        Label(view, text='state', font=('TkDefaultFont', 20)).place(x=20, y=330)
        state = Entry(view, width=50)
        state.place(x=20,y=370)

        # 사용자 정보 저장 기능
        def user_save() :
            user["id"]=id.get()
            user["name"]=name.get()
            user["phone"]=phone.get()
            user["lastdate"]=date.get()
            user["state"]=state.get()
            view.destroy()
            treeview.delete(treeview.selection()[0])
            treelist=[(user["id"], user["name"], user["phone"], user["lastdate"], user['state'])]
            for i in range(len(treelist)) :
                treeview.insert('','end',text = i,values=treelist[i])

        # 사용자 정보 삭제 기능
        def user_delete() :
            user["id"]=''
            user["name"]=''
            user["phone"]=''
            user["lastdate"]=''
            user["state"]=''
            view.destroy()
            treeview.delete(treeview.selection()[0])

        # 사용자 정보 상세 화면에서의 취소 기능
        def user_cancle() :
            view.destroy()

        Button(view, text='Save', command=user_save).place(x=20, y=450)
        Button(view, text='Delete', command=user_delete).place(x=75, y=450)
        Button(view, text='Cancle', command=user_cancle).place(x=140, y=450)

        id.insert(0, user["id"])
        name.insert(0, user["name"])
        phone.insert(0, user["phone"])
        date.insert(0, user["lastdate"])
        state.insert(0, user["state"])

    # 사용자 treeview 화면
    frame_admin = Frame(root, bd=1, relief='solid')
    frame_admin.pack(padx=5, pady=5, fill=BOTH, expand=1)

    Label(frame_admin, text="User List", font=('TkDefaultFont', 20)).place(x=430, y=5)

    treeview=ttk.Treeview(frame_admin, columns=["one", "two","three", "four", "five"], displaycolumns=["one","two","three", "four", "five"])
    treeview.place(x=150, y=40)

    treeview.column("#0", width=100, anchor="center")
    treeview.heading("#0", text="UserNum", anchor="center")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="UserID", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="name", anchor="center")

    treeview.column("#3", width=100, anchor="center")
    treeview.heading("three", text="Phone", anchor="center")

    treeview.column("#4", width=150, anchor="center")
    treeview.heading("four", text="Last Connection Date", anchor="center")

    treeview.column("#5", width=100, anchor="center")
    treeview.heading("five", text="state", anchor="center")

    Button(frame_admin, text='Modification', command=user_modi).place(x=450, y=280)

    # 사용자 treeview에 정보 넣기
    treelist=[(user["id"], user["name"], user["phone"], user["lastdate"], user['state'])]
    for i in range(len(treelist)) :
        treeview.insert('','end',text = i,values=treelist[i])

    # 관리자 정보 등록 화면
    def admin_regi() :
        view=Toplevel()
        view.title('Admin Register')
        center_window(view, 480, 560)
        Label(view, text='ID', font=('TkDefaultFont', 20)).place(x=20, y=10)
        id = Entry(view, width=50)
        id.place(x=20,y=50)
        Label(view, text='Name', font=('TkDefaultFont', 20)).place(x=20, y=90)
        name = Entry(view, width=50)
        name.place(x=20,y=130)
        Label(view, text='Phone', font=('TkDefaultFont', 20)).place(x=20, y=170)
        phone = Entry(view, width=50)
        phone.place(x=20,y=210)
        Label(view, text='Last Connection Date', font=('TkDefaultFont', 20)).place(x=20, y=250)
        date = Entry(view, width=50)
        date.place(x=20,y=290)
        Label(view, text='state', font=('TkDefaultFont', 20)).place(x=20, y=330)
        state = Entry(view, width=50)
        state.place(x=20,y=370)
        
        # 관리자 정보 저장 기능
        def admin_save() :
            admin["id"]=id.get()
            admin["name"]=name.get()
            admin["phone"]=phone.get()
            admin["lastdate"]=date.get()
            admin["state"]=state.get()
            view.destroy()

            #관리자 정보 업데이트
            atreeview.delete(atreeview.selection()[0])
            atreelist=[(admin["id"], admin["name"], admin["phone"], admin["lastdate"], admin['state'])]
            for i in range(len(atreelist)) :
                atreeview.insert('','end',text = i,values=atreelist[i])

        #관리자 등록 화면에서의 취소 기능
        def admin_cancle() :
            view.destroy()

        Button(view, text='Save', command=admin_save).place(x=20, y=450)
        Button(view, text='Cancle', command=admin_cancle).place(x=80, y=450)

    # 관리자 정보 상세 화면
    def admin_modi() :
        global item
        item=atreeview.item(atreeview.focus())
        view=Toplevel()
        view.title('Admin Detail')
        center_window(view, 480, 560)
        Label(view, text='ID', font=('TkDefaultFont', 20)).place(x=20, y=10)
        id = Entry(view, width=50)
        id.place(x=20,y=50)
        Label(view, text='Name', font=('TkDefaultFont', 20)).place(x=20, y=90)
        name = Entry(view, width=50)
        name.place(x=20,y=130)
        Label(view, text='Phone', font=('TkDefaultFont', 20)).place(x=20, y=170)
        phone = Entry(view, width=50)
        phone.place(x=20,y=210)
        Label(view, text='Last Connection Date', font=('TkDefaultFont', 20)).place(x=20, y=250)
        date = Entry(view, width=50)
        date.place(x=20,y=290)
        Label(view, text='state', font=('TkDefaultFont', 20)).place(x=20, y=330)
        state = Entry(view, width=50)
        state.place(x=20,y=370)

        # 관리자 정보 저장 기능
        def admin_save() :
            admin["id"]=id.get()
            admin["name"]=name.get()
            admin["phone"]=phone.get()
            admin["lastdate"]=date.get()
            admin["state"]=state.get()
            view.destroy()

            # 관리자 정보 업데이트
            atreeview.delete(atreeview.selection()[0])
            atreelist=[(admin["id"], admin["name"], admin["phone"], admin["lastdate"], admin['state'])]
            for i in range(len(atreelist)) :
                atreeview.insert('','end',text = i,values=atreelist[i])

        # 관리자 정보 삭제 기능
        def admin_delete() :
            user["id"]=''
            user["name"]=''
            user["phone"]=''
            user["lastdate"]=''
            user["state"]=''
            view.destroy()
            atreeview.delete(atreeview.selection()[0])

        # 관리자 정보 상세 화면 및 관리자 정보 등록 화면에서의 취소 기능
        def admin_cancle() :
            view.destroy()

        Button(view, text='Save', command=admin_save).place(x=20, y=450)
        Button(view, text='Delete', command=admin_delete).place(x=75, y=450)
        Button(view, text='Cancle', command=admin_cancle).place(x=140, y=450)

        id.insert(0, admin["id"])
        name.insert(0, admin["name"])
        phone.insert(0, admin["phone"])
        date.insert(0, admin["lastdate"])
        state.insert(0, admin["state"])
    

    # 관리자 treeview 화면
    Label(frame_admin, text="Manager List", font=('TkDefaultFont', 20)).place(x=390,y=315)

    atreeview=ttk.Treeview(frame_admin, columns=["one", "two","three", "four", "five"], displaycolumns=["one","two","three", "four", "five"])
    atreeview.place(x=150, y=350)

    atreeview.column("#0", width=100, anchor="center")
    atreeview.heading("#0", text="ManagerNum", anchor="center")

    atreeview.column("#1", width=100, anchor="center")
    atreeview.heading("one", text="ManagerID", anchor="center")

    atreeview.column("#2", width=100, anchor="center")
    atreeview.heading("two", text="name", anchor="center")

    atreeview.column("#3", width=100, anchor="center")
    atreeview.heading("three", text="Phone", anchor="center")

    atreeview.column("#4", width=150, anchor="center")
    atreeview.heading("four", text="Last Connection Date", anchor="center")

    atreeview.column("#5", width=100, anchor="center")
    atreeview.heading("five", text="state", anchor="center")
    
    # 관리자 treeview에 정보 넣기
    atreelist=[(admin["id"], admin["name"], admin["phone"], admin["lastdate"], admin['state'])]
    for i in range(len(atreelist)) :
        atreeview.insert('','end',text = i,values=atreelist[i])

    Button(frame_admin, text='Register', command=admin_regi).place(x=380, y=590)
    Button(frame_admin, text='Modification', command=admin_modi).place(x=500, y=590)

# dic
sche={'title':'', 'date':'', 'content':''}
user={}
user['id'] = 'hyunn00'
user['pwd'] = 'ko0123'
user['name'] = 'dahyun'
user['phone'] = '01012345678'
user['lastdate'] = datetime.datetime.now()
user['state'] = 'Normal'

admin={}
admin['id'] = 'admin01'
admin['pwd'] = 'ad0123'
admin['name'] = 'ko'
admin['phone'] = '01098765432'
admin['lastdate'] = datetime.datetime.now()
admin['state'] = 'Normal'

# window
root = Tk()
root.title('Welcom Scheduler!')
root.resizable(False, False)
center_window(root, 960, 640)

loginform()

root.mainloop()