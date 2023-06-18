import customtkinter
from src.utils import colors
from src.utils.store import read_data


class PasswordManager(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        mainframe = customtkinter.CTkFrame(master, fg_color=colors.MAINFRAME_BG)
        mainframe.pack(fill="both", expand=True)

        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0)
        mainframe.rowconfigure(1, weight=1)

        heading_font = customtkinter.CTkFont(weight='bold', size=20)
        heading = customtkinter.CTkLabel(mainframe, text="Password Manager", font=heading_font)
        heading.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        scroll_frame = customtkinter.CTkScrollableFrame(mainframe)
        scroll_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        app_data = read_data()

        for i, data in enumerate(app_data["passwords"]):
            pw_info = customtkinter.CTkFrame(scroll_frame, border_width=1, border_color=colors.BG_COLOR)
            name = customtkinter.CTkLabel(pw_info, text=data["name"])
            name.grid(row=0, column=0, padx=10, pady=10)
            username = customtkinter.CTkLabel(pw_info, text=data["username"])
            username.grid(row=0, column=1, padx=10, pady=10)
            password = customtkinter.CTkLabel(pw_info, text=data["password"])
            password.grid(row=0, column=2, padx=10, pady=10)
            created_time = customtkinter.CTkLabel(pw_info, text=data["created_at"])
            created_time.grid(row=0, column=3, padx=10, pady=10)
            pw_info.pack(padx=10, pady=(10, 0), side=customtkinter.TOP)
