import customtkinter

from src.mainpage import MainPage
from src.sidebar import Sidebar

customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

APP_NAME = "Enku Vault"
APP_THEME = "dark" # light, dark, System
MIN_SCREEN_SIZE = (500, 300) # width, height
SCREEN_SIZE = "800x500" # widthxheight


class App(customtkinter.CTk):

    def __init__(self, title, screen_size=f"{MIN_SCREEN_SIZE[0]}x{MIN_SCREEN_SIZE[1]}", app_theme="System"):
        super().__init__()
        self.title(title)
        self.app_theme = app_theme
        self.geometry(screen_size)
        self.minsize(MIN_SCREEN_SIZE[0], MIN_SCREEN_SIZE[1])
        
        self.grid_columnconfigure(0, weight=0) # for sidebar
        self.grid_columnconfigure(1, weight=1) # for main page
        self.grid_rowconfigure(0, weight=1)

        self.side_bar = Sidebar(self)
        self.side_bar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.main_page = MainPage(self)
        self.main_page.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="nsew")
        self.bind("<<MenuChanged>>", self.show_main_page)

        # app theme switcher
        self.other_mode = "light" if self.app_theme == "dark" else "dark"
        theme_button_text = f"Switch to {self.other_mode} mode"
        self.theme_button = customtkinter.CTkButton(self.side_bar, text=theme_button_text, command=self.theme_switcher)
        self.theme_button.pack(padx=10, pady=10, side=customtkinter.BOTTOM)


    def show_main_page(self, event):
        print("Event :",event.widget)
        self.main_page.display(self.side_bar.selected_menu)


    def theme_switcher(self):   
        print("Switch theme button clicked")
        if self.app_theme == "light":
            self.app_theme = "dark"
        elif self.app_theme == "dark":
            self.app_theme = "light"
        
        customtkinter.set_appearance_mode(self.app_theme)
        self.other_mode = "light" if self.app_theme == "dark" else "dark"
        self.theme_button.configure(text=f"Switch to {self.other_mode} mode")


app = App(title=APP_NAME, screen_size=SCREEN_SIZE, app_theme=APP_THEME)

app.mainloop()