import datetime as dt
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.utils.store import save_password_to_file
from src.utils.pwd_generator import generate_password


class PasswordGenerator(ttk.Frame):

    def __init__(self, pwd_gen_page):
        super().__init__(master=pwd_gen_page, padding=10)

        heading = ttk.Label(pwd_gen_page, text="Add new Account information", font=("Helvetica", 16))
        heading.pack(pady=20)

        self.mainframe = ttk.Frame(pwd_gen_page, padding=10, style=DARK)
        self.mainframe.pack(fill=BOTH, expand=True)

        self.generator_frame = ttk.Frame(self.mainframe, padding=10, style=DARK)
        self.generator_frame.grid(row=0, column=0, sticky=NSEW)

        self.generator_frame.columnconfigure(0, weight=1)
        self.generator_frame.columnconfigure(1, weight=2)
        self.generator_frame.columnconfigure(2, weight=3)

        self.pwd_length = ttk.IntVar(value=14)
        self.gen_pwd = ttk.StringVar(value="")
        new_pwd = generate_password(length=self.pwd_length.get())
        self.gen_pwd.set(new_pwd)

        ttk.Label(self.generator_frame, 
                  text="Random Password Generator", 
                  font=("Helvetica", 12), 
                  background="#303030", 
                  anchor=CENTER
                ).grid(row=0, column=0, columnspan=3, pady=15)

        ttk.Label(self.generator_frame, text="Password length :", font=("Helvetica", 10), background="#303030").grid(row=1, column=0)
        ttk.Label(self.generator_frame, textvariable=self.pwd_length, font=("Helvetica", 10, "bold"), background="#303030").grid(row=1, column=1)
        pwd_length_scale = ttk.Scale(self.generator_frame, 
                                     value=int(self.pwd_length.get()), 
                                     from_=8, to=20, 
                                     style=PRIMARY,
                                     cursor="hand2",
                                     command=self.update_pwd_length
                                    )
        pwd_length_scale.grid(row=1, column=2, ipadx=4, ipady=4)

        pwd_entry = ttk.Entry(self.generator_frame, textvariable=self.gen_pwd, font=("Helvetica", 12))
        pwd_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        pwd_regen_btn = ttk.Button(self.generator_frame, text="Re-generate", cursor="hand2", command=self.regenerate_password)
        pwd_regen_btn.grid(row=2, column=2)

        pwd_copy_btn = ttk.Button(self.generator_frame, text="Copy", cursor="hand2", command=self.copy_to_clipboard)
        pwd_copy_btn.grid(row=2, column=3)

        ttk.Separator(self.mainframe, bootstyle=INFO).grid(row=1, column=0, sticky=EW)
        
        # second frame - to add new account details

        self.content_frame = ttk.Frame(self.mainframe, padding=10, style=DARK)
        self.content_frame.grid(row=2, column=0)
        self.content_frame.columnconfigure(0, weight=0)
        self.content_frame.columnconfigure(1, weight=2)
        self.content_frame.columnconfigure(2, weight=3)

        ttk.Label(self.content_frame, 
                  text="Enter account details", 
                  font=("Helvetica", 12), 
                  background="#303030", 
                  anchor=CENTER
                ).grid(row=0, column=0, columnspan=3, pady=15)

        # form variables
        self.name = ttk.StringVar(value="")
        self.username = ttk.StringVar(value="")
        self.password = ttk.StringVar(value="")
        self.toast_value = ttk.StringVar(value="")

        # form entries
        entries = [
            ("Account Name", self.name),
            ("Username", self.username),
            ("Password", self.password),
        ]
        row_no = 1
        for ent in entries:

            ttk.Label(self.content_frame, 
                    text=ent[0], 
                    background="#303030", 
                    width=15, 
                    font=("Helvetica", 10)
                    ).grid(row=row_no, column=0, pady=5)

            ttk.Entry(self.content_frame,
                      textvariable=ent[1],
                      font=("Helvetica", 12)
                    ).grid(row=row_no, column=1, columnspan=2, pady=5, sticky=EW)
            
            row_no += 1

        self.toast_label = ttk.Label(self.content_frame, 
                                     textvariable=self.toast_value, 
                                     background="#303030", 
                                     wraplength= 300,
                                     font=("Helvetica", 10)
                                    )
        self.toast_label.grid(row=row_no, column=0, columnspan=3, pady=5)

        row_no += 1

        ttk.Button(self.content_frame,
                   text="Clear",
                   command=self.on_clear,
                   cursor="hand2",
                   bootstyle=DANGER
                   ).grid(row=row_no, column=1, pady=5)

        ttk.Button(self.content_frame,
                   text="Submit",
                   command=self.submit_form,
                   width=15,
                   cursor="hand2",
                   bootstyle=SUCCESS
                   ).grid(row=row_no, column=2, pady=5)
        

    def on_clear(self):
        self.name.set("")
        self.username.set("")
        self.password.set("")
        self.toast_value.set("")


    def submit_form(self):
        self.toast_value.set("")

        name = self.name.get()
        username = self.username.get()
        password = self.password.get()

        if name.strip()=="" or username.strip()=="" or password.strip()=="":
            self.toast_value.set("Please enter all the fields.")
            self.toast_label["foreground"] = "red"

        else:

            try:
                save_password_to_file({
                    "name": name.strip(),
                    "username": username.strip(),
                    "password": password.strip(),
                    "created_at": dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M:%S"),
                    "last_updated": dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M:%S")
                })
                self.toast_value.set("Successfully saved")
                self.toast_label["foreground"] = "green"

            except Exception as e:
                self.toast_value.set("Error : " + str(e))
                self.toast_label["foreground"] = "#f39c12"


    def regenerate_password(self):
        new_pwd = generate_password(length=self.pwd_length.get())
        self.gen_pwd.set(new_pwd)


    def copy_to_clipboard(self):
        self.clipboard_clear()
        self.clipboard_append(self.gen_pwd.get())


    def update_pwd_length(self, value):
        self.pwd_length.set(int(float(value)))