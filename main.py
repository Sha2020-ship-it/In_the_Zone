import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import winsound
import getpass
import ctypes as types
import tkinter as tk
import winreg
from time import *
from datetime import *
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

    unblock = str(e.get())
    unblock.split(',')
    for website in unblock:
        if 'https' in website:
            set_key('ProxyServer', u'{}:443'.format(website))
            set_key('ProxyOverride', u'{}:443'.format(website))
        elif 'http' in website:
            set_key('ProxyServer', u'{}:80'.format(website))
            set_key('ProxyOverride', u'{}:80'.format(website))
        elif 'ftp' in website:
            set_key('ProxyServer', u'{}:21'.format(website))
            set_key('ProxyOverride', u'{}:21'.format(website))

    e.grid(row = 0, column = 0, columnspan = 4)

    focus_mode_on.grid(row = 2, column = 0)
    focus_mode_off.grid(row = 2, column = 1)

    root1.mainloop()

def block():
    root2 = tk.Tk()
    host_path ='C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'
    tk.Label(root2, text ='WEBSITE BLOCKER' , font ='arial 20 bold').pack()
    Websites = tk.Text(root2, font = 'arial 10', height='2', width = '40', wrap = tk.WORD, padx=5, pady=5)
    Websites.place(x= 140,y = 60)

    def Blocker():
        host_path = r"C:\\Windows\\System32\\drivers\\etc\\hosts"  
        redirect = "127.0.0.1"  

        while True:  
            if datetime(datetime.now().year,datetime.now().month,datetime.now().day,9)<datetime.now()<datetime(datetime.now().year,datetime.now().month,datetime.now().day,17):  
                with open(host_path,"r+") as fileptr:  
                    content = fileptr.read()  
                    for website in websites:  
                        if website in content:  
                            pass  
                        else:  
                            fileptr.write(redirect+"        "+website+"\n")  
            else:  
                with open(host_path,'r+') as file:  
                    content = file.readlines();  
                    file.seek(0)  
                    for line in content:  
                        if not any(website in line for website in websites):  
                            file.write(line)  
                    file.truncate()  
    sleep(5)  

    block = tk.Button(root2, text = 'Block',pady = 5,command = Blocker ,width = 6, bg = 'red', activebackground = 'sky blue')
    block.place(x = 230, y = 150)
    
    root2.mainloop()

def menu():
    root = tk.Tk()
    root.title('Focus Mode Activation')

    bring_focus = tk.Button(root, text = 'Go to Proxy Server', padx = 45, pady = 45, command = focus_mode).grid(row = 0, column = 0)
    bring_block = tk.Button(root, text = 'Go to Website Blocker', padx = 45, pady = 45, command = block).grid(row = 0, column = 1)

    root.mainloop()

def password():
    x = str(random.randint(1000,9999))
    emailreciev = input("Please enter your email address, Only gmail: ")
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("noreply123.InTheZone@gmail.com", "random123!") 
    message = f"{x} is your password"
    s.sendmail("noreply123.InTheZone@gmail.com", emailreciev, message) 
    s.quit()
    code = input('Check your mail - Enter the code you got: ')
    if code == x:
        print('Accepted!')
        print('You can acess the software.')
        menu()
    else:
        for i in range(3):
            if code != x:
                print('Not accepted!')
                code = input('Check your mail - Enter the code you got: ') 
            elif code == x:
                print('Accepted!')
                print('You can acess the software.')
                menu()

password()
