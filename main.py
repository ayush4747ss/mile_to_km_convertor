import tkinter
from tkinter import *
#
#
# def calci():
#     val = int(input_.get())
#     new_val = val * 1.60934
#     ans.config(text=new_val)
#
#
# window = Tk()
# window.title("miles to km convertor")
# window.minsize(width=300, height=150)
#
# button = Button(text="calculate", command=calci)
# button.grid(column=2, row=3)
#
# equal = tkinter.Label(text="is equal to ")
# equal.grid(column=1, row=2)
#
# mile = tkinter.Label(text="Miles")
# mile.grid(column=3, row=1)
#
# km = tkinter.Label(text="km")
# km.grid(column=3, row=2)
#
# ans = tkinter.Label(text=0)
# ans.grid(column=2, row=2)
#
# input_ = Entry(width=10)
# input_.grid(column=2, row=1)
#
# window.mainloop()



window=Tk()
window.title("miles to km convertor")
window.config(padx=20,pady=20)

def m_to_km():
    miles=float(miles_input.get())
    km_=miles*1.609
    km_result.config(text=str(km_))

miles_input=Entry(width=10)
miles_input.grid(column=1 , row=0)

miles_label=Label(text="is equal to")
miles_label.config(background="pink")
miles_label.grid(column=2 , row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0 , row=1)

km_result=Label(text="0")
km_result.grid(column=1 , row=1)

KM_label=Label(text="km")
KM_label.grid(column=2 , row=1)

calculate_button=Button(text="calculate",command=m_to_km)
calculate_button.grid(column=1, row=2)




window.mainloop()