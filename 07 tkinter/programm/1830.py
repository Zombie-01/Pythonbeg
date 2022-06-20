from tkinter import *
import tkinter.messagebox as tkMessageBox

window = Tk()
window.title('Бүртгэлийн программ')
width = 350
height = 200
window.geometry('{}x{}'.format(width, height))
window.resizable(0,0)

def clear_entries():
    text_reg.set('')
    text_phone.set('')
    text_owog.set('')
    text_ner.set('')

# Register dgr
text_reg = StringVar()
Label(window, text='Регистр:').grid(row=0,column=0)
Entry(window, bd=1, textvariable=text_reg).grid(row=0, column=1)

# Utasni dugar
text_phone = StringVar()
Label(window, text='Утас:').grid(row=1, column=0)
Entry(window, bd=1, textvariable=text_phone).grid(row=1, column=1)

# Owog
text_owog = StringVar()
Label(window, text='Овог:').grid(row=0, column=3)
Entry(window, bd=1, textvariable=text_owog).grid(row=0, column=4)

# Ner
text_ner = StringVar()
Label(window, text='Нэр:').grid(row=1, column=3)
Entry(window, bd=1, textvariable=text_ner).grid(row=1, column=4)


# Хадгалах товч
def user_create():
    if text_reg.get() == '' or text_phone.get() == '' or text_owog.get() == '' or text_ner.get()=='':
        tkMessageBox.showwarning("Анхаар", "Мэдээллийг бүрэн оруулна уу")
    else:
        new=text_reg.get()+','+text_phone.get()+','+text_owog.get()+','+text_ner.get()
        clear_entries()
        list_data.insert(END, new)

btn_create = Button(window, text='Бүртгэх', command=user_create)
btn_create.grid(row=3, column=0)

# Засварлах товч
def user_update():
    print('update ...')

btn_update = Button(window, text='Засварлах', command=user_update)
btn_update.grid(row=3, column=1)

# Устгах товчлуур
def user_delete():
    list_data.delete(list_data.curselection()[0])
    clear_entries()

btn_delete = Button(window, text='Устгах', command=user_delete)
btn_delete.grid(row=3, column=2)

# Listbox
list_data = Listbox(window, bd=0,width=40, height=6)
list_data.grid(row=4, column=0, rowspan=4, columnspan=3)
list_data.insert(END, 'ii89012023,99102356,bold,baatar')
list_data.insert(END, 'uu95020306,89561212,tumur,tuguldur')
list_data.insert(END, 'ub90090130,99111212,dorj,baldan')

# Scrollbar тохируулах
scroll = Scrollbar(window)
scroll.grid(row=4,rowspan=4, column=3)
list_data.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_data.yview)

def select_user(event):
    selected_user = list_data.get(list_data.curselection()[0])
    data = selected_user.split(',')
    text_reg.set(data[0])
    text_phone.set(data[1])
    text_owog.set(data[2])
    text_ner.set(data[3])

list_data.bind('<<ListboxSelect>>', select_user)


# 1. Дунд нь таслал нэм
# 2. Бүртгэсний дараа бүх entry-г хоосон болго / text_reg.set('')
# 3. Бүх мэдээллийг бүрэн бөглөөгүй тохиолдолд анхааруулга гарга (messagebox)
# 4. Бүртгэгдсэн мэдээллийг дахин бүртгэхгүй анхааруулга өг
# 5. Бүх entry дотор байгаа өгөгдлийг арилгах 'цэвэрлэх' гэсэн нэртэй товчлуур
# 6. Сонгогдсон дата-г устга
# 7. Сонгогдсон дата-г засварла

window.mainloop()
