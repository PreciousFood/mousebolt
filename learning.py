from typing import List, Optional, Tuple, Union
import customtkinter


class Login(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)

        self.label = customtkinter.CTkLabel(master=self, text="LOGIN")
        self.label.grid(row=0, column=0, pady=20, padx=20, sticky='ew')

        self.username = customtkinter.CTkEntry(master=self, placeholder_text="Username")
        self.username.grid(row=1, column=0, pady=20, padx=20, sticky='ew')

        self.password = customtkinter.CTkEntry(master=self, placeholder_text="Password", show="*")
        self.password.grid(row=2, column=0, pady=(0, 20), padx=20, sticky='ew')

        self.button = customtkinter.CTkButton(master=self, text="Login", command=self.login)
        self.button.grid(row=3, column=0, pady=(0, 20), padx=20, sticky='ew')

    def login(self):
        if self.username.get() == "PreciousFood" and self.password.get() == "1234":
            print("LOGGED IN!")
        else:
            print("INVALID")


class Permisions(customtkinter.CTkScrollableFrame):
    def __init__(self, master, checks: list):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.checkboxes: List[customtkinter.CTkCheckBox] = []
        for i, c in enumerate(checks):
            checkbox = customtkinter.CTkCheckBox(master=self, text=c)
            checkbox.grid(row=i, column=0, padx=10, pady=10, sticky='w')
            self.checkboxes.append(checkbox)
    
    def get(self):
        r = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                r.append(checkbox.cget("text"))
        return r




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title = "Login"
        self.geometry("400x400")

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.login = Login(self)
        self.login.grid(row=0, column=0, stick='nesw')

        checks =["Cookies", "Location", "SSN", "Address", "PhoneNumber", "Friends House", "Local Pool", "Favorite Video Game"]
        self.boxes = Permisions(self, checks)
        self.boxes.grid(row=0, column=1, stick='nesw')

        self.button = customtkinter.CTkButton(master=self, text="PERMISSIONS!", command=self.report_perm)
        self.button.grid(row=1, column=0, columnspan=2, stick='nesw', padx=25, pady=25)

    def report_perm(self):
        print(self.boxes.get())

        

app = App()
app.mainloop()