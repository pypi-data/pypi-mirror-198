import tkinter as tk
from . import ManagerTk

window = tk.Tk()
window.title("ManagerTk Example")

main_page = [
    tk.Label(text="Main Page"),
    tk.Button(text="Go to Second Page", command=lambda: ManagerTk.redirect_pages(main_page, second_page))
]

second_page = [
    tk.Label(text="Second Page"),
    tk.Button(text="Go to Main Page", command=lambda: ManagerTk.redirect_pages(second_page, main_page))
]

create_mpage(window, main_page, "300x200")

window.mainloop()
