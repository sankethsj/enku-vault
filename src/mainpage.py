import customtkinter

from src.frames.home import Home
from src.frames.password_manager import PasswordManager
from src.utils import colors


class MainPage(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        print("Iam in mainpage")

        self.display(master.side_bar.selected_menu)


    def display(self, page):

        print("main page :", page)

        for widget in self.winfo_children():
            widget.destroy()

        page(self)

