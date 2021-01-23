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

def proxy_off():
	set_key('ProxyEnable', 0)
	
	INTERNET_OPTION_REFRESH = 37
	INTERNET_OPTION_SETTINGS_CHANGED = 39

	internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

	internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
	internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)	

def proxy_on():
	set_key('ProxyEnable', 1)

	set_key('ProxyServer', u'https://teams.microsoft.com:443')
	set_key('ProxyOverride', u'https://teams.microsoft.com:443')

	INTERNET_OPTION_REFRESH = 37
	INTERNET_OPTION_SETTINGS_CHANGED = 39

	internet_set_option = ctypes.windll.Wininet.InternetSetOptionW

	internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
	internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)

def focus_mode():
    root1 = tk.Tk()
    root1.title('In The Zone! - Focus Generator')
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

    root1.mainloop()

def block():
    root2 = tk.Tk()
    root2.title('In The Zone! - Website Blocker (MACOS)')
    host_path ='C:\Windows\System32\drivers\etc\hosts'
    ip_address = '127.0.0.1'
    tk.Label(root2, text ='WEBSITE BLOCKER' , font ='arial 20 bold').pack()
    Websites = tk.Text(root2, font = 'arial 10', height='2', width = '40', wrap = tk.WORD, padx=5, pady=5)
    Websites.place(x= 140,y = 60)

    def Blocker():
        sites_to_block = Websites.get(0.0, tk.END)
        sites_to_block = sites_to_block.split(',')
        Linux_host = '/etc/hosts'
        Window_host = r"C:\Windows\System32\drivers\etc\hosts"
        default_hoster = Linux_host
        redirect = "127.0.0.1"
        def block_websites(start_hour , end_hour):
            while True:
                if dt(dt.now().year, dt.now().month, dt.now().day,start_hour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour): 
                    with open(default_hoster, 'r+') as hostfile:
                        hosts = hostfile.read()
                        for site in sites_to_block:
                            if site not in hosts:
                                hostfile.write(redirect +' ' + site + '\n')
                else:
                    with open(default_hoster, 'r+') as hostfile:
                        hosts = hostfile.readlines()
                        hostfile.seek(0)
                        for host in hosts:
                            if not any(site in host for site in sites_to_block):
                                hostfile.write(host)
                        hostfile.truncate()
                time.sleep(3)
        block_websites(0, 1)
    block = tk.Button(root2, text = 'Block',pady = 5,command = Blocker ,width = 6, bg = 'red', activebackground = 'sky blue')
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
