import tkinter as tk
import json, requests



# get the joke from the api, configure label_ans
def get_joke():
    url = 'https://icanhazdadjoke.com/'
    heads = {'Accept': 'application/json'} # required on this one
    # get the response, configure label_ans


# get the reponse from the api, configure label_ans
def get_agify():
    user_name = agify_entry.get() # get the name from the text entry box
    url = 'https://api.agify.io/?name=' + user_name
    # get the response, configure label_ans


  

# setup main window
root = tk.Tk()
root.wm_geometry("300x300")
root.title("My GUI")


# create frame1 - joke_btn, agify_entry, agify_btn, label_ans
frame1 = tk.Frame(root)
frame1.grid(row=0, column=0, sticky='news')





# 'raise' the frame you want visible first
frame1.tkraise()
root.mainloop()
