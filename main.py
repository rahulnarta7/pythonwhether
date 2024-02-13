import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests


def data_get():
    try:
        # Update weather information labels
        city=city_name.get()
        data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e74a5f0cc0c30dc9489ed7d82cdb0121").json()
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])
        temp_celsius = int(data["main"]["temp"] - 273.15)
        temp_label1.config(text=f"{temp_celsius}°C")
        pre_label1.config(text=data["main"]["humidity"])

    except Exception as e:
        # Display error message if data retrieval fails
        w_label1.config(text="N/A")
        wb_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        pre_label1.config(text="N/A")
        print("Error:", e)



background_image = Image.open("images.png")
resized_image= background_image.resize((500,500),Image.ANTIALIAS if hasattr(Image, "ANTIALIAS") else Image.BICUBIC)
# Create Tkinter window
win = tk.Tk()
win.title("wheatherSphere Pro")
win.config(bg="#008080")
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
win.geometry("500x500")



background_photo = ImageTk.PhotoImage(resized_image)
canvas = tk.Canvas(win, height=500, width=500)
canvas.pack()
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create Tkinter window

name_label = ttk.Label(win,text=" Welcome to WheatherSphere Pro",foreground="white", background="black", font=("Lato",20,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=tk.StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,values=list_name,font=("Lato",15),textvariable=city_name)
com.place(x=70,y=120,height=50,width=350)


w_label= ttk.Label(win,text="Weather Climate",  foreground="#007BFF", background="white",font=("Segoe UI",17,"bold"))
w_label.place(x=25,y=280,height=30,width=190)
w_label1= ttk.Label(win,text="",  foreground="#007BFF", background="white",font=("Segoe UI",17,"bold"))
w_label1.place(x=280,y=280,height=30,width=150)



wb_label= ttk.Label(win,text="Weather Description", foreground="#4CAF50", background="white", font=("Segoe UI",15,"bold"))
wb_label.place(x=25,y=330,height=30,width=200)
wb_label1= ttk.Label(win,text="", foreground="#4CAF50", background="white", font=("Segoe UI",15,"bold"))
wb_label1.place(x=280,y=330,height=30,width=150)

temp_label= ttk.Label(win,text="  Temprature",  foreground="#FF6347", background="white",font=("Segoe UI",16,"bold"))
temp_label.place(x=25,y=380,height=30,width=150)
temp_label1= ttk.Label(win,text="",  foreground="#FF6347", background="white",font=("Segoe UI",16,"bold"))
temp_label1.place(x=280,y=380,height=30,width=150)

pre_label= ttk.Label(win,text="  Humidity",  foreground="#008080", background="white",font=("Oswald",16,"bold"))
pre_label.place(x=25,y=430,height=30,width=150)
pre_label1= ttk.Label(win,text="",  foreground="#008080", background="white",font=("Oswald",16,"bold"))
pre_label1.place(x=280,y=430,height=30,width=150)

style_button = ttk.Style()
style_button.configure("Custom.TButton", foreground="black", background="white", font=("Segoe UI", 12, "bold"))
done_button= ttk.Button(win,text="Get Started",  style="Custom.TButton" , command=data_get)
done_button.place(x=200,y=200,height=50,width=100)
win.mainloop()
