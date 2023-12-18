from typing import Optional, Tuple, Union
import customtkinter as ctk


WIDTH, HEIGHT = 400, 400
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.title = "MOUSEBOLT"
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.wm_title("MOUSEBOLT")


        self.grid_columnconfigure(0, weight=1)

        self.only_num = ctk.CTkLabel(master=self, text="CPS must be a number", text_color="red", fg_color="pink", corner_radius=8)

        self.cps_entry = ctk.CTkEntry(master=self, placeholder_text="CPS")
        self.cps_entry.grid(column=0, row=2, padx=10, pady=10, sticky="ew")
        
        options = ["Left Click", "Right Click"]
        self.mouse_botton_menu = ctk.CTkOptionMenu(master=self, values=options)
        self.mouse_botton_menu.grid(column=0, row=3, padx=10, pady=10, sticky="ew")

        self.go = ctk.CTkButton(master=self, text="GO!", command=self.on_go)
        self.go.grid(column=0, row=4, padx=10, pady=10, sticky="ew")

        self.cps: int = 0

    
    def on_go(self):
        e = self.get()
        if e != None:
            self.cps = e
    
    def get(self):
        e = self.cps_entry.get()
        if e.isdigit():
            self.only_num.grid_forget()
            return e
        else:
            self.only_num.grid(column=0, row=1, padx=10, pady=(10, 0), sticky="ew")


if __name__ == "__main__":
    app = App()
    app.mainloop()
