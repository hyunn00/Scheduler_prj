from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime 
import calendar

def get_screen_size(window) :
    return window.winfo_screenwidth(), window.winfo_screenheight()

def get_window_size(window) :
    return window.winfo_reqwidth(), window.winfo_reqheight()

def center_window(root, width, height) :
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 4)
    root.geometry(size)

def login_view() :
    global frame_login
    root.title('Scheduler_login')

    frame_login = Frame(root)
    frame_login.pack(fill = BOTH, expand = 1)

    frame = Frame(frame_login, bd = 1, relief = 'solid')
    frame.pack(padx=5, pady = 5, fill = BOTH, expand = 1)

    logo = Label(frame, text = "📅 DAILY SCHEDULER", font = 12)
    label_ID = Label(frame, text = "ID")
    entry_ID = Entry(frame, width = 40)
    label_PW = Label(frame, text = 'PW')
    entry_pw = Entry(frame, width = 40)
    btnLogin = Button(frame, text = "LOGIN", width = 40)
    label1 = Label(frame, text = '회원가입')
    label2 = Label(frame, text = "lost password?")

    logo.grid(row = 0, column=1,pady=50)
    label_ID.grid(row=1, column=1, pady = 10)
    label_PW.grid(row=2, column=1, pady = 10)
    btnLogin.grid(row=3, column=2, pady = 10)
    label1.grid(row=4, column=1)
    entry_ID.grid(row=1, column=2, columnspan=2)
    entry_pw.grid(row=2, column=2, columnspan=2)
    label2.grid(row=4, column=2)


def signup_view() :
    global frame_signup
    root.title('Scheduler_signup')

    frame_signup = Frame(root)
    frame_signup.pack(fill=BOTH, expand=1)

    frame = Frame(frame_signup, bd = 1, relief = 'solid')
    frame.pack(padx=5, pady=5, fill=BOTH, expand=1)

    signup = Label(frame, text = '📝 회원가입', font=12).grid(row=0, column=0, pady = 20)
    label_name = Label(frame, text = '이름').grid(row=1, column=0, pady=10)
    entry_name = Entry(frame).grid(row=1, column=1)
    label_phone = Label(frame, text = '휴대전화').grid(row=2, column=0, pady=10)
    list_phone = ttk.Combobox(frame, height=0, width=10)
    list_phone['value'] = ('SKT', 'KT', 'U+')
    list_phone.grid(row=2, column=1, padx=5)
    entry_phone1 = Entry(frame, width=10).grid(row=2, column=2)
    lb1 = Label(frame, text='-').grid(row=2, column=3)
    entry_phone2 = Entry(frame, width=10).grid(row=2, column=4)
    label_ID = Label(frame, text="ID").grid(row=3, column=0, pady=10)
    entry_ID = Entry(frame).grid(row=3, column=1)
    btn_ID = Button(frame, text='중복확인').grid(row=3, column=2)
    label_pw = Label(frame, text="PW").grid(row=4, column=0, pady=10)
    entry_pw = Entry(frame).grid(row=4, column=1)
    label_repw = Label(frame, text="PW 확인").grid(row=5, column=0, pady=10)
    entry_repw = Entry(frame).grid(row=5, column=1)
    label_address = Label(frame, text="주소").grid(row=6, column=0, pady=10)
    entry_address = Entry(frame).grid(row=6, column=1)
    btn_check=Button(frame, text='가입하기').grid(row=7, column=2)
    
def findPW_view() :
    global frame_findPW
    root.title('Schedule_findPW')
    
    frame_findPW = Frame(root)
    frame_findPW.pack(fill=BOTH, expand=1)

    frame=Frame(frame_findPW, bd=1, relief = 'solid')
    frame.pack(padx=5, pady=5, fill=BOTH, expand=1)

    findPW = Label(frame, text='💡 비밀번호 찾기', font=12).grid(row=0, column=0, pady=50)
    label_ID = Label(frame, text="ID").grid(row=1, column=0, pady=10)
    entry_ID = Entry(frame).grid(row=1, column=1)
    label_name = Label(frame, text = '이름').grid(row=2, column=0, pady=10)
    entry_name = Entry(frame).grid(row=2, column=1)
    label_phone = Label(frame, text = '휴대전화').grid(row=3, column=0, pady=10)
    list_phone = ttk.Combobox(frame, height=0, width=10)
    list_phone['value'] = ('SKT', 'KT', 'U+')
    list_phone.grid(row=3, column=1, pady=10)
    entry_phone1 = Entry(frame, width=10).grid(row=3, column=2)
    lb1 = Label(frame, text='-').grid(row=3, column=3)
    entry_phone2 = Entry(frame, width=10).grid(row=3, column=4)
    btn_check=Button(frame, text='찾기').grid(row=4, column=1, pady=10)


def calendar() :
    global frame_right, now
    root.title('Schedule_calendar')

    now = datetime.datetime.now()

    frame_cal = Frame(root)
    frame_cal.pack(fill=BOTH, expand=1)

    frame_left = Frame(frame_cal, bd=1, relief='solid')
    frame_left.pack(padx=5, pady=5, fill=BOTH, expand=1, side=LEFT)

    cal = Calendar(frame_left,selectmode = "day",year=2022,month=11,date=1)
    cal.pack()

    def fetch_date():
        date.config(text =cal.get_date())

    but = Button(frame_left,text="Select Date",command=fetch_date)
    but.pack()

    date = Label(frame_left,text="")
    date.pack()

    list_sche=Listbox(frame_left, selectmode='extended', height=0)
    list_sche.insert(0, '오늘 할일')
    list_sche.pack(fill=BOTH, expand=1)

    frame_right = Frame(frame_cal, bd=1, relief='solid')
    frame_right.pack(padx=5, pady=5, fill=BOTH, expand=1, side=RIGHT)

    #참조
    years = Label(frame_right, height =3, text = str(now.year) + "년", font = ("bold", 14))
    years.grid(row = 0, column= 0, columnspan= 7)

    pastbutton = Button(frame_right, text = "←")
    pastbutton.grid(row = 2, column= 2)

    months = Label(frame_right, height = 1, text= str(now.month) + "월", font = ("bold", 14))
    months.grid(row = 2, column= 3)

    futerbutton = Button(frame_right, text="→")
    futerbutton.grid(row = 2, column= 4)


    mon = Label(frame_right,text = "MON",width=7)
    mon.grid(row= 5, column = 0)

    tue = Label(frame_right,text = "TUE",width=7)
    tue.grid(row= 5, column = 1)

    wed = Label(frame_right,text = "WED",width=7)
    wed.grid(row= 5, column = 2)

    thu = Label(frame_right,text = "THU",width=7)
    thu.grid(row= 5, column = 3)

    fri = Label(frame_right,text = "FRI",width=7)
    fri.grid(row= 5, column = 4)

    sat = Label(frame_right,text = "SAT",width=7)
    sat.grid(row= 5, column = 5)

    sun = Label(frame_right,text = "SUN",width=7)
    sun.grid(row= 5, column = 6)


    def calendars(yyyy,mm):
        weekday = datetime.date(yyyy,mm,11).weekday() -2
        weekstack = 0

        day = list(range(32))
        for i in range(1, 30 + 1):
            day[i] = Button(frame_right, text = i, width=7, height= 2)
            day[i].grid(row = 6 + weekstack, column= weekday)
            weekday += 1
            if weekday == 7:
                weekday = 0
                weekstack += 1

    calendars(now.year, now.month)            

def sche_Detail() :
    root.title('Schedule_Detail')

    frame_sche = Frame(root, bd=1, relief='solid')
    frame_sche.pack(fill=BOTH, expand=1)

    title = Label(frame_sche, text = 'Text', font=12).pack(anchor=W)
    en_title = Entry(frame_sche, state='readonly').pack(anchor=W, padx=10)

    date = Label(frame_sche, text = 'Date', font=12).pack(anchor=W)
    en_date = Entry(frame_sche, state='readonly').pack(anchor=W,padx=10)

    content = Label(frame_sche, text = 'Content', font=12).pack(anchor=W)
    en_content = Text(frame_sche, state=DISABLED, height=19).pack(anchor=W, padx=10)

    btn_check = Button(frame_sche, text='확인').pack()
    btn_modify=Button(frame_sche, text='수정').pack()
    btn_delete=Button(frame_sche, text='삭제').pack()

def sche_add() :
    root.title('Schedule_add')

    frame_add = Frame(root, bd=1, relief='solid')
    frame_add.pack(fill=BOTH, expand=1)

    title = Label(frame_add, text = 'Text', font=12).pack(anchor=W)
    en_title = Entry(frame_add).pack(anchor=W, padx=10)

    date = Label(frame_add, text = 'Date', font=12).pack(anchor=W)
    en_date = Entry(frame_add).pack(anchor=W,padx=10)

    content = Label(frame_add, text = 'Content', font=12).pack(anchor=W)
    en_content = Text(frame_add, height=19).pack(anchor=W, padx=10)

    btn_check = Button(frame_add, text='등록').pack(side=LEFT)
    btn_check = Button(frame_add, text='취소').pack(side=LEFT)

def sche_modify() :
    root.title('Schedule_modify')

    frame_modify = Frame(root, bd=1, relief='solid')
    frame_modify.pack(fill=BOTH, expand=1)

    title = Label(frame_modify, text = 'Text', font=12).pack(anchor=W)
    en_title = Entry(frame_modify).pack(anchor=W, padx=10)

    date = Label(frame_modify, text = 'Date', font=12).pack(anchor=W)
    en_date = Entry(frame_modify).pack(anchor=W,padx=10)

    content = Label(frame_modify, text = 'Content', font=12).pack(anchor=W)
    en_content = Text(frame_modify, height=19).pack(anchor=W, padx=10)

    btn_check = Button(frame_modify, text='수정').pack(side=LEFT)
    btn_check = Button(frame_modify, text='취소').pack(side=LEFT)

def admin() :
    root.title('admin_view')

    frame_admin = Frame(root, bd=1, relief='solid')
    frame_admin.pack(fill=BOTH, expand=1)

    lbl = Label(frame_admin, text="User List")
    lbl.pack(anchor=W)

    treeview=ttk.Treeview(frame_admin, columns=["one", "two","three"], displaycolumns=["one","two","three"])
    treeview.pack(anchor=W)

    treeview.column("#0", width=100,)
    treeview.heading("#0", text="UserID")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="name", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Phone", anchor="center")

    treeview.column("#3", width=150, anchor="center")
    treeview.heading("three", text="Last Connection Date", anchor="center")

    btn_check = Button(frame_admin, text='확인').pack(side=LEFT, padx=10)
    btn_modify=Button(frame_admin, text='수정').pack(side=LEFT, padx=10)
    btn_delete=Button(frame_admin, text='삭제').pack(side=LEFT, padx=10)

root = Tk()
root.title('Scheduler')
center_window(root, 640, 400)
admin()

root.mainloop()