import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.components.collapsible_frame import CollapsingFrame
from src.utils.store import read_data, write_data
from src.utils.path_handler import resource_path



class PasswordManager(ttk.Frame):

    def __init__(self, pwd_mgr_page):
        super().__init__(master=pwd_mgr_page)

        heading = ttk.Label(pwd_mgr_page, text="Manage your passwords", font=("Helvetica", 18))
        heading.pack(pady=20)

        refresh_btn = ttk.Button(pwd_mgr_page, 
                                 text="Refresh",
                                 bootstyle=INFO,
                                 cursor="hand2",
                                 image=ttk.PhotoImage(file=resource_path('src/assets/refresh-regular-24.png')),
                                 command=self.list_passwords
                                )
        refresh_btn.pack(side=TOP, padx=8, pady=8, anchor="e")

        self.content_frame = ttk.Frame(pwd_mgr_page, style=DARK)
        self.content_frame.pack(fill=BOTH, expand=True)
        self.app_data = None
        self.list_passwords()

        
    def list_passwords(self):

        for child in self.content_frame.winfo_children():
            child.destroy()

        cf = CollapsingFrame(self.content_frame)
        cf.pack(fill=BOTH)

        self.app_data = read_data()

        passwords_data = self.app_data["passwords"]
        for data in passwords_data:
            group = ttk.Frame(cf, padding=10, style=PRIMARY, border=1, borderwidth=2)

            w = ttk.Text(group, height=1, borderwidth=0)
            w.insert(1.0, data["username"])
            w.pack()
            w.configure(state="disabled")

            w = ttk.Text(group, height=1, borderwidth=0)
            w.insert(1.0, data["password"])
            w.pack()
            w.configure(state="disabled")

            ttk.Label(group, text=data["created_at"]).pack(fill=X)
            ttk.Button(group, text="Delete", cursor="hand2", style=DANGER, command= lambda x=data["name"]: self._delete_password_info(x)).pack(fill=X)
            cf.add(child=group, title=data["name"])


    def _delete_password_info(self, id):
        passwords = self.app_data["passwords"]
        self.app_data["passwords"] = [p for p in passwords if p["name"] != id]

        write_data(self.app_data)

        self.list_passwords()

