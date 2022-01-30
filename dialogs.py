# -*- coding: utf-8 -*-

import tkinter.messagebox
import tkinter.simpledialog

tkinter.messagebox.showinfo("showInfo", "This is an info msg")
tkinter.messagebox.showwarning("showWarning", "This is a warning")
tkinter.messagebox.showerror("showError", "This is an error")
isYes = tkinter.messagebox.askyesno("askYesNo", "Continue?")
print(isYes)
isOK = tkinter.messagebox.askokcancel("askYesNoCancel", "OK?")
print(isOK)
isYesNoCancel = tkinter.messagebox.askyesnocancel(
"askyesnocancel", "Yes, No, Cancel?") 
print(isYesNoCancel)
name = tkinter.simpledialog.askstring(
"askstring", "Enter your name")
print(name)
age = tkinter.simpledialog.askinteger(
"askinteger", "Enter your age")
print(age)
weight = tkinter.simpledialog.askfloat(
"askfloat", "Enter your weight")
print(weight)