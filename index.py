from tkinter import *
import requests
import tkinter.ttk as ttk
import json
from tkinter.messagebox import showinfo
import PIL

# "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity?earth_date=2021-06-15&api_key=DEMO_KEY"

# a = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2021-06-15&api_key=DEMO_KEY")
# b = json.loads(a.content)
# c = b["photos"]
# d = len(c)
# e = c[d-1]["img_src"]
# print(e)

class Images:
    def __init__(self):
        self.root = Tk()
        self.root.title("Nasa's Rovers Information")
        self.root.geometry("400x400")
        # self.img = "C:\\Users\\MICHEAL\\Pictures\\images.jfif"
        # self.image = PhotoImage(file = "C:\\Users\\MICHEAL\\Pictures\\cmd.png")
        # Label(image=self.image)
        self.frame = Frame(self.root)
        self.frame.grid()
        Label(self.frame, text="Choose any of the rovers: ").grid(row=0, column=0, pady=7)
        self.items = ["Curiosity", "Opportunity", "Spirit", "Perseverance"]
        self.user = ttk.Combobox(self.frame, values=self.items)
        self.user.current(0)
        self.user.grid(row=0, column=1)
        self.button = Button(self.frame, text="Submit", command=self.go)
        self.button.grid(row=1, column=0, columnspan=2)
        self.changeBg()
        self.root.mainloop()

    def changeBg(self):
        pass

    def go(self):
        try:
            self.api_req = requests.get("https://api.nasa.gov/mars-photos/api/v1/manifests/"+self.user.get().lower()+"?earth_date=2021-06-16&api_key=keHUtmpLYa4Tq4awHwKy62FAc2jLhMx40i5mGMDP")
            self.api = json.loads(self.api_req.content)
            # print(self.api)
            self.newFrame = Toplevel()
            self.newFrame.title(self.user.get().capitalize() + " Rover")
            self.newFrame.geometry('300x300')
            self.frame = Frame(self.newFrame)
            self.frame.grid()
            self.data = [
                self.api["photo_manifest"]["name"],
                self.api['photo_manifest']['landing_date'],
                self.api['photo_manifest']['launch_date'],
                self.api['photo_manifest']['status'],
                self.api['photo_manifest']['max_sol'],
                self.api['photo_manifest']['max_date'],
                self.api['photo_manifest']['total_photos'],
                # self.api['photo_manifest']['photos']

            ]
            self.keys = list(self.api["photo_manifest"].keys())
            # self.values = list(self.api["photo_manifest"].values())
            for i in range(len(self.data)):
                Label(self.frame, text=str(self.keys[i].capitalize()) +": "+ str(self.data[i])+ "\n").grid(row=i, column=0)
        except:
            showinfo("Error Message", "Oops, Information about {} is not available right now. Please try again later. Thank you.".format(self.user.get()))

Images()