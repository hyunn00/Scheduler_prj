from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime

def get_screen_size(window) :
    return window.winfo_screenwidth(), window.winfo_screenheight()

def get_window_size(window) :
    return window.winfo_reqwidth(), window.winfo_reqheight()

def center_window(root, width, height) :
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 4)
    root.geometry(size)


def adminform() :
    global user, admin
    root.title('admin_view')

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

        def user_delete() :
            user["id"]=''
            user["name"]=''
            user["phone"]=''
            user["lastdate"]=''
            user["state"]=''
            view.destroy()
            treeview.delete(treeview.selection()[0])

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

    treelist=[(user["id"], user["name"], user["phone"], user["lastdate"], user['state'])]
    for i in range(len(treelist)) :
        treeview.insert('','end',text = i,values=treelist[i])

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

        def admin_save() :
            admin["id"]=id.get()
            admin["name"]=name.get()
            admin["phone"]=phone.get()
            admin["lastdate"]=date.get()
            admin["state"]=state.get()
            view.destroy()
            atreeview.delete(atreeview.selection()[0])
            atreelist=[(admin["id"], admin["name"], admin["phone"], admin["lastdate"], admin['state'])]
            for i in range(len(atreelist)) :
                atreeview.insert('','end',text = i,values=atreelist[i])

        def admin_cancle() :
            view.destroy()

        Button(view, text='Save', command=admin_save).place(x=20, y=450)
        Button(view, text='Cancle', command=admin_cancle).place(x=80, y=450)

    def admin_modi() :
        global item
        item=atreeview.item(atreeview.focus())
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

        def admin_save() :
            admin["id"]=id.get()
            admin["name"]=name.get()
            admin["phone"]=phone.get()
            admin["lastdate"]=date.get()
            admin["state"]=state.get()
            view.destroy()
            atreeview.delete(atreeview.selection()[0])
            atreelist=[(admin["id"], admin["name"], admin["phone"], admin["lastdate"], admin['state'])]
            for i in range(len(atreelist)) :
                atreeview.insert('','end',text = i,values=atreelist[i])

        def admin_delete() :
            user["id"]=''
            user["name"]=''
            user["phone"]=''
            user["lastdate"]=''
            user["state"]=''
            view.destroy()
            atreeview.delete(atreeview.selection()[0])

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
    
    atreelist=[(admin["id"], admin["name"], admin["phone"], admin["lastdate"], admin['state'])]
    for i in range(len(atreelist)) :
        atreeview.insert('','end',text = i,values=atreelist[i])

    Button(frame_admin, text='Register', command=admin_regi).place(x=380, y=590)
    Button(frame_admin, text='Modification', command=admin_modi).place(x=500, y=590)

user={}
user['id'] = 'hyunn00'
user['name'] = 'dahyun'
user['phone'] = '01012345678'
user['lastdate'] = datetime.datetime.now()
user['state'] = 'Normal'

admin={}
admin['id'] = 'admin01'
admin['name'] = 'ko'
admin['phone'] = '01098765432'
admin['lastdate'] = datetime.datetime.now()
admin['state'] = 'Normal'

# main
root = Tk()
root.title('Welcom Scheduler!')
root.resizable(False, False)
center_window(root, 960, 640)

adminform()

root.mainloop()