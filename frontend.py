from tkinter import *
import backend

window = Tk()

#labels
lbl_title = Label(window, text="Title")
lbl_title.grid(row=0, column=0)

lbl_author = Label(window, text="Author")
lbl_author.grid(row=0, column=2)

lbl_year = Label(window, text="Year")
lbl_year.grid(row=1, column=0)

lbl_isbn = Label(window, text="ISBN")
lbl_isbn.grid(row=1, column=2)

#entry boxes
title_text = StringVar()
ent_title = Entry(window, textvariable=title_text)
ent_title.grid(row=0, column=1)

author_text = StringVar()
ent_author = Entry(window, textvariable=author_text)
ent_author.grid(row=0, column=3)

year_text = StringVar()
ent_year = Entry(window, textvariable=year_text)
ent_year.grid(row=1, column=1)

isbn_text = StringVar()
ent_isbn = Entry(window, textvariable=isbn_text)
ent_isbn.grid(row=1, column=3)

#list box & scrollbar
lb_output = Listbox(window, height=6, width=35)
lb_output.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

lb_output.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb_output.yview)

#buttons
btn_view = Button(window, text="View All", width=12)
btn_view.grid(row=2, column=3)

btn_search = Button(window, text="Search Entry", width=12)
btn_search.grid(row=3, column=3)

btn_add = Button(window, text="Add Entry", width=12)
btn_add.grid(row=4, column=3)

btn_update = Button(window, text="Update", width=12)
btn_update.grid(row=5, column=3)

btn_delete = Button(window, text="Delete", width=12)
btn_delete.grid(row=6, column=3)

btn_close = Button(window, text="Close", width=12)
btn_close.grid(row=7, column=3)

window.mainloop()

