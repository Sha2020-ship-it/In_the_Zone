import os
import winsound
import ctypes as types
import tkinter as tk
import winreg

root = tk.Tk()
root.title('IN THE ZONE....')

def block_sites_label():
    mylabel = tk.Label(root, text = "Starting to block sites").grid(row = 2, column = 0)

def unblock_sites_label():
    mylabel2 = tk.Label(root, text="Starting to unblock sites").grid(row = 7, column = 0)

focus_mode_off = tk.Button(root, text = "Turn Focus-Mode off", padx = 55, pady = 45, command = unblock_sites_label, bg = "red")
focus_mode_on = tk.Button(root, text = "Turn Focus-Mode on", padx = 50, pady = 45, command = block_sites_label, bg = "green")

e = tk.Entry(root, width = 70)

e.insert(0, "Add sites that you want to unblock. Seperate with comma ','")

e.grid(row = 0, column = 0, columnspan = 4)

focus_mode_on.grid(row = 2, column = 0)
focus_mode_off.grid(row = 2, column = 1)

root.mainloop()

