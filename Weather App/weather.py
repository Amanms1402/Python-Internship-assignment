
from tkinter import *
import tkinter.font as font
import requests
import json

root=Tk()
root.title("Weather Conditions")

myfont= font.Font(family='Helvetica',size=20,weight='bold')
myfontbig= font.Font(family='Helvetica',size=60,weight='bold')
myfontsmall= font.Font(family='Helvetica',size=15)


frame=LabelFrame(root)
frame.pack(padx=10,pady=10)


def submit():
    top=Toplevel()

    frame2=LabelFrame(top)
    frame2.pack(padx=10,pady=10)


    city=entry.get()
    entry.delete(0,END)

    complete_url=base_url+"appid="+api_key+"&q="+city

    response=requests.get(complete_url)
    x=response.json()
    

    cityog=x['name']
    country=x['sys']['country']
    current_temp=round(x['main']['temp']-273.15,1)
    feels_like=round(x['main']['feels_like']-273.15,1)
    weather=x['weather'][0]['main']
    min_temp=round(x['main']['temp_min']-273.15,1)
    max_temp=round(x['main']['temp_max']-273.15,1)


    label1=Label(frame2,text=cityog+","+country)
    label1['font']=myfont
    label1.grid(column=1,row=0)

    label2=Label(frame2,text=str(current_temp)+" °C")
    label2['font']=myfontbig
    label2.grid(column=1,row=1)

    frame3=LabelFrame(frame2)
    frame3.grid(column=1,row=2,pady=5)

    label3=Label(frame3,text="feels like "+str(feels_like)+" °C",anchor=W)
    label3['font']=myfontsmall
    label3.grid(column=1,row=3,columnspan=2)

    label4=Label(frame3,text=weather)
    label4['font']=myfont
    label4.grid(column=1,row=2)

    label5=Label(frame3,text="min/max temp: "+str(min_temp)+"°/"+str(max_temp)+"°")
    label5['font']=myfontsmall
    label5.grid(column=1,row=4)
    
api_key="3e048c850e7bcecc34437519ce82156a"

base_url="https://api.openweathermap.org/data/2.5/weather?"

Label(frame,text="Enter City Name:",font=myfont).grid(column=1,row=0)
entry=Entry(frame)
entry['font']=myfont
entry.grid(column=0,row=1,columnspan=3,padx=10,pady=10,ipadx=50,ipady=5)

button=Button(frame,text="Submit",command=submit)
button['font']=myfont
button.grid(column=1,row=2,ipadx=20,pady=10)


root.mainloop()