import datetime as dt
import customtkinter
from src.utils import colors
from src.utils.store import save_password_to_file

class Home(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        print("I am in home class")

        mainframe = customtkinter.CTkFrame(master, fg_color=colors.MAINFRAME_BG)
        mainframe.pack(fill="both", expand=True)

        heading_font = customtkinter.CTkFont(weight='bold', size=35)
        heading = customtkinter.CTkLabel(mainframe, text="Secure Password Store", font=heading_font, padx=10, pady=30)
        heading.grid(row=0, column=0, columnspan=2)

        label_wesbite = customtkinter.CTkLabel(mainframe, text="Website/App name:")
        label_wesbite.grid(row=1, column=0, sticky="e")
        self.name = customtkinter.CTkEntry(mainframe)
        self.name.grid(row=1, column=1)

        username_label = customtkinter.CTkLabel(mainframe, text="Username:")
        username_label.grid(row=2, column=0, sticky="e")
        self.username = customtkinter.CTkEntry(mainframe, placeholder_text="Enter your username")
        self.username.grid(row=2, column=1)

        label_password = customtkinter.CTkLabel(mainframe, text="Password:")
        label_password.grid(row=3, column=0, sticky="e")
        self.password = customtkinter.CTkEntry(mainframe, placeholder_text="Enter your password", show="●")  # Hide password input
        self.password.grid(row=3, column=1)

        # Create a submit button
        submit_button = customtkinter.CTkButton(mainframe, text="Submit", command=self.submit_form)
        submit_button.grid(row=4, columnspan=2)

        self.error_label = customtkinter.CTkLabel(mainframe, text="")
        self.error_label.grid(row=5, columnspan=2)


    def submit_form(self):

        self.error_label.configure(text = "")
        self.error_label.update()

        name = self.name.get()
        username = self.username.get()
        password = self.password.get()

        print(name, username, password)

        if name.strip()=="" or username.strip()=="" or password.strip()=="":
            self.error_label.configure(text = "Error : Empty inputs found", text_color="red")
            self.error_label.update()

        else:
            save_password_to_file({
                "name": name,
                "username": username,
                "password": password,
                "created_at": dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M:%S"),
                "last_updated": dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H:%M:%S")
            })

            self.error_label.configure(text = "Password successfully stored", text_color=colors.TEXT_COLOR)
            self.error_label.update()

        print("Submit button clicked")