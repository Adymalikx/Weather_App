from tkinter import *
from tkinter import  ttk
import requests

def data_get():
    city= city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=0c5e444829801363540bf23b23778ba7")
    W_label1.config(text=data["weather"][0]["main"])
    Wd_label1.config(text=data["weather"][0]["description"])
    temp_label.config(text=data["main"]["temp"])
    pr_label1.config(text=data["main"]["pressure"])
win = Tk()
win.title("addy weather")
win.config(bg="light green")
win.geometry("750x750")
name_label= Label(win , text = "Addy Weather App",
                  font=("Roboto",35,"bold"))
name_label.place(x=150,y=50,height=50,width=450)

name_label.place(x=150,y=50,height=50,width=450)
city_name= StringVar()
list_name =[ "Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win,text="Addy Weather App",values=list_name,
                   font=("Roboto Bold ",30,"bold"),textvariable=city_name)
com.place(x=150,y=120,height=50,width=450)

W_label= Label(win , text = "Weather Climate ",
                  font=("Roboto",15,))
W_label.place(x=150,y=300,height=50,width=200)

W_label1= Label(win , text = "",
                  font=("Roboto",15,))
W_label1.place(x=360,y=300,height=50,width=200)

Wd_label= Label(win , text = "Weather Description ",
                  font=("Roboto",15,))
Wd_label.place(x=150,y=360,height=50,width=200)

Wd_label1= Label(win , text = "",
                  font=("Roboto",15,))
Wd_label1.place(x=360,y=360,height=50,width=200)


temp_label= Label(win , text = " Temperature ",
                  font=("Roboto",15,))
temp_label.place(x=150,y=420,height=50,width=200)

temp_label1= Label(win , text = "",
                  font=("Roboto",15,))
temp_label1.place(x=360,y=420,height=50,width=200)

tempmin_label= Label(win , text = " Temperature Min ",
                  font=("Roboto",15,))
tempmin_label.place(x=150,y=480,height=50,width=200)

tempmin_label1= Label(win , text = "",
                  font=("Roboto",15,))
tempmin_label1.place(x=360,y=480,height=50,width=200)


tempmax_label= Label(win , text = " Temperature max ",
                  font=("Roboto",15,))
tempmax_label.place(x=150,y=540,height=50,width=200)

tempmax_label1= Label(win , text = "",
                  font=("Roboto",15,))
tempmax_label1.place(x=360,y=540,height=50,width=200)

pr_label= Label(win , text = " Pressure",
                  font=("Roboto",15,))
pr_label.place(x=150,y=600,height=50,width=200)

pr_label1= Label(win , text = " ",
                  font=("Roboto",15,))
pr_label1.place(x=360,y=600,height=50,width=200)
done_button= Button(win,text="Done",
                    font=("techno board",20,"bold"))
done_button.place(x=325,y=190,height=50,width=100)





win.mainloop()

