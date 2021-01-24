import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import winsound
import getpass
import ctypes as types
import tkinter as tk
import time
from datetime import datetime as dt
import winreg
import random
import pickle
import tkinter as tk
import winreg as winreg
import ctypes 
import requests
import math
import re
import os
import webbrowser

INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
	r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
	0, winreg.KEY_ALL_ACCESS)

def set_key(name, value):
	_, reg_type = winreg.QueryValueEx(INTERNET_SETTINGS, name)
	winreg.SetValueEx(INTERNET_SETTINGS, name, 0, reg_type, value)

def proxy_on():
    set_key('ProxyEnable', 1)
    
    unblock = input('Enter the site you want to unblock - ONLY 1: ')
    print("If you accidentally close the application and block all the sites please contact this email /n noreply123.InTheZone@gmail.com")
    set_key('ProxyServer', '{}:443'.format(unblock))
    set_key('ProxyOverride', '{}:443'.format(unblock))

    INTERNET_OPTION_REFRESH = 37
    INTERNET_OPTION_SETTINGS_CHANGED = 39
    
    internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

    internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
    internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)

def proxy_off():
	set_key('ProxyEnable', 0)
	
	INTERNET_OPTION_REFRESH = 37
	INTERNET_OPTION_SETTINGS_CHANGED = 39

	internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

	internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
	internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)	

def focus_mode():
    root1 = tk.Tk()
    root1.title('In The Zone! - Focus Generator (Windows Only)')
        
    def block_sites_label():
        mylabel = tk.Label(root1, text = "Starting to block sites").grid(row = 3, column = 0)
        proxy_on()

    def unblock_sites_label():
        mylabel2 = tk.Label(root1, text="Starting to unblock sites").grid(row = 3, column = 1)
        proxy_off()

    focus_mode_off = tk.Button(root1, text = "Turn Focus-Mode off (Click to start)", padx = 55, pady = 45, command = unblock_sites_label, bg = "red")
    focus_mode_on = tk.Button(root1, text = "Turn Focus-Mode on (Click to start)", padx = 50, pady = 45, command = block_sites_label, bg = "green")
    
    focus_mode_on.grid(row = 2, column = 0)
    focus_mode_off.grid(row = 2, column = 1)
    
    root1.mainloop()

def block():
    root2 = tk.Tk()
    root2.title('In The Zone! - Website Blocker')
    tk.Label(root2, text ='WEBSITE BLOCKER' , font ='arial 20 bold').pack()
    Websites = tk.Text(root2, font = 'arial 10', height='2', width = '40', wrap = tk.WORD, padx=5, pady=5)
    Websites.place(x= 140, y = 60)

    def Blocker():
        operation = input('Enter your operating system: ')
        operation.lower()
        if operation == 'windows':
            workingheend, workingstart = 0, 0
            workingstart = int(input("When do you want to start working hours? on the 24 hour clock "))
            workingheend = int(input("When do you want to end working hours? on the 24 hour clock "))
            if workingstart > 24 or workingheend > 24:
                print('Not accepted!')
                workingstart = int(input("When do you want to start working hours? on the 24 hour clock "))
                workingheend = int(input("When do you want to end working hours? on the 24 hour clock "))
            else:
                print('Accepted!')
                
            hosts_path = r"C:\Windows\System32\drivers\etc\hosts"   # r is for raw string
            hosts_temp = "hosts"
            redirect = "127.0.0.1"
            websitblock = input("What sites do you want to block? Seperate them  with a comma.")
            
            web_sites_list = websitblock.split(',')     

            while True:
                if dt(dt.now().year, dt.now().month, dt.now().day, workingstart) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,workingheend):
                    print("Working hours")
                    with open(hosts_path, "r+") as file:
                        content = file.read()
                        for website in web_sites_list:
                            if website in content:
                                pass
                            else:
                                file.write(redirect+" "+website+"\n")
                else:
                    print("Fun time")
                    with open(hosts_path, "r+") as file:
                        content = file.readlines()
                        file.seek(0)  # reset the pointer to the top of the text file
                        for line in content:
                            # here comes the tricky line, basically we overwrite the whole file
                            if not any(website in line for website in web_sites_list):
                                file.write(line)
                            # do nothing otherwise
                        file.truncate() # this line is used to delete the trailing lines (that contain DNS)
                time.sleep(5)
        elif operation == 'linux':
            workingheend, workingstart = 0, 0
            workingstart = int(input("When do you want to start working hours? on the 24 hour clock "))
            workingheend = int(input("When do you want to end working hours? on the 24 hour clock "))
            if workingstart > 24 or workingheend > 24:
                print('Not accepted. Try again')
                workingstart = int(input("When do you want to start working hours? on the 24 hour clock "))
                workingheend = int(input("When do you want to end working hours? on the 24 hour clock "))
            else:
                print('Accepted!')

            hosts_path = r"/etc/hosts"   # r is for raw string
            hosts_temp = "hosts"
            redirect = "127.0.0.1"
            websitblock = input("What sites do you want to block? Seperate them  with a comma.")

            web_sites_list = websitblock.split(',')     

            while True:
                if dt(dt.now().year, dt.now().month, dt.now().day, workingstart) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,workingheend):
    
                    with open(hosts_path, "r+") as file:
                        content = file.read()
                        for website in web_sites_list:
                            if website in content:
                                pass
                            else:
                                file.write(redirect+" "+website+"\n")
                else:
                    print("Fun time")
                    with open(hosts_path, "r+") as file:
                        content = file.readlines()
                        file.seek(0)  
                        for line in content:
                            
                            if not any(website in line for website in web_sites_list):
                                file.write(line)
                            
                        file.truncate() # this line is used to delete the trailing lines (that contain DNS)
                time.sleep(5) 
        elif operation == 'mac':
            workingheend, workingstart = 0, 0
            workingstart = int(input("When do you want to start working hours? on the 24 hour clock "))
            workingheend = int(input("When do you want to end working hours? on the 24 hour clock "))
            if workingstart > 24 or workingheend > 24:
                print('Not accepted! - Try again!')
                workingstart = int(input("When do you want to start working hours? on the 24 hour clock "))
                workingheend = int(input("When do you want to end working hours? on the 24 hour clock "))                

            else:
                print('Accepted!')
                
            hosts_path = r"/private/etc/hosts"   # r is for raw string
            hosts_temp = "hosts"
            redirect = "127.0.0.1"
            websitblock = input("What sites do you want to block? Seperate them  with a comma.")
            
            web_sites_list = websitblock.split(',')     

            while True:
                if dt(dt.now().year, dt.now().month, dt.now().day, workingstart) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,workingheend):
                        print("Working hours")
                        with open(hosts_path, "r+") as file:
                            content = file.read()
                            for website in web_sites_list:
                                if website in content:
                                    pass
                                else:
                                    file.write(redirect+" "+website+"\n")
                else:
                    print("Fun time")
                    with open(hosts_path, "r+") as file:
                        content = file.readlines()
                        file.seek(0)  # reset the pointer to the top of the text file
                        for line in content:
                                # here comes the tricky line, basically we overwrite the whole file
                            if not any(website in line for website in web_sites_list):
                                file.write(line)
                                # do nothing otherwise
                            file.truncate() # this line is used to delete the trailing lines (that contain DNS)
                time.sleep(5)
    block = tk.Button(root2, text = 'Click to start',pady = 5,command = Blocker ,width = 10, bg = 'red', activebackground = 'sky blue')
    block.place(x = 230, y = 150)
    
    root2.mainloop()

def menu():
    root = tk.Tk()
    root.title('In The Zone - Main Menu')

    bring_focus = tk.Button(root, text = 'Go to Proxy Server', padx = 45, pady = 45, command = focus_mode).grid(row = 0, column = 0)
    bring_block = tk.Button(root, text = 'Go to Website Blocker', padx = 45, pady = 45, command = block).grid(row = 0, column = 1)

    root.mainloop()

def password():                                                       
    emailreciev = input('Enter your email: ')
    x = str(random.randint(1000,9999))
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("noreply123.InTheZone@gmail.com", "random123!") 
    message = f"{x} is your password"
    s.sendmail("noreply123.InTheZone@gmail.com", emailreciev, message) 
    s.quit()
    code = input('Check your mail - Enter the code you got: ')
    if code == x:
        print('Accepted!')
        print('You can access the software.')
        menu()
    else:
        for i in range(3):
            if code != x:
                print('Not accepted!')
                code = input('Check your mail - Enter the code you got: ') 
            elif code == x:
                print('Accepted!')
                print('You can access the software.')
                menu()

password()
