import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import winsound
import getpass
import ctypes as types
import tkinter as tk
import winreg
import random

INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
    r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
    0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
    _, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
    winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

def proxy_off():
    set_key('ProxyEnable', 0)
    
    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39

    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)   

def proxy_on():
    set_key('ProxyEnable', 1)

    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39

    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)

def focus_mode():
    root1 = tk.Tk()
    def block_sites_label():
        mylabel = tk.Label(root1, text = "Starting to block sites").grid(row = 3, column = 0)
        proxy_on()

    def unblock_sites_label():
        mylabel2 = tk.Label(root1, text="Starting to unblock sites").grid(row = 3, column = 1)
        proxy_off()

    focus_mode_off = tk.Button(root1, text = "Turn Focus-Mode off", padx = 55, pady = 45, command = unblock_sites_label, bg = "red")
    focus_mode_on = tk.Button(root1, text = "Turn Focus-Mode on", padx = 50, pady = 45, command = block_sites_label, bg = "green")

    e = tk.Entry(root1, width = 70)

    e.insert(0, "Add sites that you want to unblock. Seperate with comma ','")

    e.grid(row = 0, column = 0, columnspan = 4)

    focus_mode_on.grid(row = 2, column = 0)
    focus_mode_off.grid(row = 2, column = 1)

    root.mainloop()

def block():
    root2 = tk.Tk()
    host_path ='C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'
    tk.Label(root2, text ='WEBSITE BLOCKER' , font ='arial 20 bold').pack()
    Websites = tk.Text(root2, font = 'arial 10', height='2', width = '40', wrap = tk.WORD, padx=5, pady=5)
    Websites.place(x= 140,y = 60)

    def Blocker():
        website_lists = Websites.get(1.0,END)
        Website = list(website_lists.split(","))
        with open (host_path , 'r+') as host_file:
            file_content = host_file.read()
            for website in Website:
                if website in file_content:
                    tk.Label(root2, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                    pass
                else:
                    host_file.write(ip_address + " " + website + '\n')
                    tk.Label(root2, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

    block = tk.Button(root2, text = 'Block',pady = 5,command = Blocker ,width = 6, bg = 'red', activebackground = 'sky blue')
    block.place(x = 230, y = 150)

    root2.mainloop()

def password():
    x = str(random.randint(1000,9999))
    emailreciev = input("Please enter your email address, Only gmail: ")
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("noreply123.InTheZone@gmail.com", "random123!") 
    message = f"{x} is your password"
    s.sendmail("noreply123.InTheZone@gmail.com", emailreciev, message) 
    s.quit()
    

password()

if password() == True:
    root = tk.Tk()
    root.title('Focus Mode Activation')

    bring_focus = tk.Button(root, text = 'Go to Proxy Server', padx = 45, pady = 45, command = focus_mode).grid(row = 0, column = 0)
    bring_block = tk.Button(root, text = 'Go to Website Blocker', padx = 45, pady = 45, command = block).grid(row = 0, column = 1)

    root.mainloop()
