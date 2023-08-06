[![Downloads](https://static.pepy.tech/personalized-badge/managertk?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/managertk)
#
# Documentation ManagerTk
ManagerTk is a Python module that helps you create and manage a graphical user interface (GUI) for projects created with Tkinter. 
This module provides simple functions for working with windows, pages, and interface elements.

###
## Download Package
```cmd
pip install ManagerTk
```

##
## Main Functions

##### coord_view(window, boolc) - Duplicates the window for viewing mouse coordinates (x, y) in the window and displays them in the terminal.
#
#
##### create_mpage(window, ui_page, size) - Creates the main page of the interface with the specified elements.
#
#
##### redirect_pages(page_ui_1, page_ui_2, side=None) - Allows you to switch between two interface pages by changing their contents.
#
#
##### window_exit(title: str, message: str) - Displays a window to confirm the exit from the program.
#
#
##### documentation() - Displays a link to the module documentation.

###
## Tutorial for using
```python
import tkinter as tk
from ManagerTk import *

window = tk.Tk()
window.title("ManagerTk Example")

main_page = [
    tk.Label(text="Main Page"),
    tk.Button(text="Go to Second Page", command=lambda: redirect_pages(main_page, second_page))
]

second_page = [
    tk.Label(text="Second Page"),
    tk.Button(text="Go to Main Page", command=lambda: redirect_pages(second_page, main_page))
]

create_mpage(window, main_page, "300x200")

window.mainloop()
```

This example creates a simple application with two pages that can be switched using buttons.

### Support
#
##### telegram - [@DK50503](https://t.me/DK50503)