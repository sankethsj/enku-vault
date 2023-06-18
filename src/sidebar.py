import customtkinter

from src.frames.home import Home
from src.frames.password_generator import PasswordGenerator
from src.frames.password_manager import PasswordManager
from src.utils import colors

MENU_ITEMS = [
    {
        "id": "home",
        "text": "Home",
        "page": Home
    },
    {
        "id": "passwordmanager",
        "text": "Password Manager",
        "page": PasswordManager
    },
    {
        "id": "passwordgenerator",
        "text": "Password Generator",
        "page": PasswordGenerator
    }
]


class Sidebar(customtkinter.CTkFrame):

    def __init__(self, master):

        print("Rendered Sidebar")

        super().__init__(master)

        self.pack(fill=customtkinter.BOTH, expand=True)

        self.menu_area = customtkinter.CTkFrame(self)
        self.menu_area.pack(fill=customtkinter.BOTH, expand=True)

        self.menu_items = []
        self.selected_menu_id = MENU_ITEMS[1]["id"] # first item will selected bu default
        self.selected_menu = None

        self.display_menu_items()


    def display_menu_items(self):

        for menu in self.menu_area.winfo_children():
            menu.destroy()

        for menu in MENU_ITEMS:
            print(menu["id"])
            menu_item = customtkinter.CTkButton(self.menu_area, text=menu["text"], 
                                                fg_color="transparent", 
                                                text_color=colors.TEXT_COLOR,
                                                hover_color=colors.HOVER_BG_COLOR
                                                )

            menu_item.configure(command = lambda menu_id=menu["id"]: self.select_menu(menu_id))

            if self.selected_menu_id == menu["id"]:
                menu_item.configure(fg_color=colors.MENU_SELECTED, text_color=colors.MENU_SELECTED_TEXT, hover=False)
                self.selected_menu = menu["page"]

            menu_item.pack(padx=10, pady=(10, 0), side=customtkinter.TOP)
            self.menu_items.append(menu_item)

        self.master.event_generate("<<MenuChanged>>")  # Raise the custom event


    def select_menu(self, menu_id):
    
        print("Menu button clicked :", menu_id)
        self.selected_menu_id = menu_id
        self.display_menu_items()

    