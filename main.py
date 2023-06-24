import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.frames.password_generator import PasswordGenerator
from src.frames.password_manager import PasswordManager

APP_NAME = "Enku Vault"
APP_THEME = "darkly"
MIN_SCREEN_SIZE = (300, 500) # (width, height)
SCREEN_SIZE = (400, 600) # (width, height)
ICON = 'src/assets/icon.png'


root = ttk.Window(title=APP_NAME, minsize=MIN_SCREEN_SIZE, size=SCREEN_SIZE, themename=APP_THEME, iconphoto=ICON)

notebook = ttk.Notebook(root, bootstyle=SECONDARY)
notebook.pack(fill="both", expand=True)

# Create tabs in the main window

## tab 1
pwd_mgr_page = ttk.Frame(notebook)
notebook.add(pwd_mgr_page, text="Password Manager")
PasswordManager(pwd_mgr_page)

## tab 2
pwd_gen_page = ttk.Frame(notebook)
notebook.add(pwd_gen_page, text="Add Account")
PasswordGenerator(pwd_gen_page)

# notebook.select(pwd_gen_page)

root.mainloop()
