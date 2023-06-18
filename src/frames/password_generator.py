import customtkinter
# from utils import colors


class PasswordGenerator(customtkinter.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.hello_button = customtkinter.CTkButton(master, text="Hello PasswordGenerator page", command=self.hello)
        self.hello_button.grid(row=0, column=0, padx=10, pady=10, sticky="n")

    def hello(self):
        print("PasswordGenerator button clicked")