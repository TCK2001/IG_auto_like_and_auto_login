from tkinter import*
from selenium import webdriver
import random
import time

win=Tk()
win.title("TCK IG AUTO LIKE")
win.geometry("600x400")
win.option_add("*Font","궁서 20")
win.configure(bg="pink")

#image
lab=Label(win)
img=PhotoImage(file="C:\Temp/ig.png")
img=img.subsample(2)
lab.config(image=img)
lab.pack()

#id
lab1=Label(win)
lab1.config(text="ID",fg="orange")
lab1.pack()

ent1=Entry(win)
ent1.insert(0,"abcd@abcd.com")
def clear(event):
    if ent1.get()=="abcd@abcd.com":
        ent1.delete(0,len(ent1.get()))
ent1.bind("<Button-1>",clear)
ent1.pack()

#password
lab2=Label(win)
lab2.config(text="PASSWORD",fg="orange")
lab2.pack()

ent2=Entry(win)
ent2.config(show="*")
ent2.pack()

#search
# lab3=Label(win)
# lab3.config(text="Search",fg="orange")
# lab3.pack()

# ent3=Entry(win)
# ent3.insert(0,"Hi TCK")
# def clear(event):
#     if ent3.get()=="Hi TCK":
#         ent3.delete(0,len(ent3.get()))
# ent3.config(bg="ivory")
# ent3.bind("<Button -1>",clear)
# ent3.pack()

def login():
    driver=webdriver.Chrome("C:\Temp/chromedriver.exe")  
    url="https://www.instagram.com/"
    driver.get(url)  
    driver.implicitly_wait(5)
    xpath1="//input[@name='username']"
    driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
    driver.implicitly_wait(5)
    xpath2="//input[@name='password']"
    driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
    driver.implicitly_wait(5)
    xpath3="//button[@class='sqdOP  L3NKy   y3zKF     ']"
    driver.find_element_by_xpath(xpath3).click()
    driver.implicitly_wait(5)
    # xpath4="//button[@class='sqdOP yWX7d    y3zKF     ']"
    # driver.find_elements_by_xpath(xpath4).click()
    # driver.implicitly_wait(5)
    # xpath5="//button[@class='aOOlW   HoLwm ']"
    # driver.find_elements_by_xpath(xpath5).click()
    # driver.implicitly_wait(5)


#login button
btn=Button(win)
btn.config(text="Login",fg="blue")
btn.config(command=login)
btn.pack()


# xpath="//button[@type='button']"

# while True:
    # click like
    # xpath="//article//section/span/button"
    # driver.find_elements_by_xpath(xpath)[0].click()
    # time.sleep(1+random.random())

    # next page
#     xpath2="//a"
#     el_list=driver.find_elements_by_xpath(xpath2)
#     for el in el_list:
#         if el.text=="다음":
#             el.click()
#             break
#     time.sleep(3+random.random())


win.mainloop()