from tkinter import *
from time import sleep
import re
coords = [0,0]
debug = False
boolc = False
window = None
time_cview = 0
def interface(window):
    window.bind('<Motion>', move)
def move(event):
    global coords
    coords[0] = event.x
    coords[1] = event.y
    if(boolc):
        try:sleep(time_cview);print(coords[0], coords[1])
        except:raise TypeError("time_cview SHOULD be integer or float.")
        
def run(window):interface(window)

def coord_view(window,boolc):"Creating dublicate window for viewing coordinates(x,y)."; interface(window)
def typely(listm):
    "Looks on types."
    typely = True
    for coord in listm:
        for coords in coord[1]:
            try:
                ex = coord[1][0] + coord[1][1]
            except:
                typely = False
            finally:
                if(typely == True):return True
                else: return False
                    
def create_mpage(window,ui_page,size):
    if(typely(ui_page)):
        window.geometry(size)
        for ui in ui_page:
            ui.pack()
        if(debug == True):
            print("Page ui loaded.")
    else:
        raise TypeError("create_mpage(ui_page), ui_page SHOULD be list type.")

    
def redirect_pages(page_ui_1,page_ui_2,side=None):
    "This function makes redirecting from page_1 to page_2, ui reconstruction."
    if(type(page_ui_1) and type(page_ui_2) == list):
        if(type(side) != list and type(side) != str and side != None): raise TypeError("redirect_pages(ui_page_1,ui_page_2,side), side SHOULD be str type. \nEXAMPLE:\n\redirect_pages(main,second,'left')\nOR\redirect_pages(ui_page_1,ui_page_2,['top','right',left'])\n\n")
        else:
            if debug == True:print("Start Redirecting.")
            for ui_page_1 in page_ui_1:
                ui_page_1.pack_forget()
            if(type(side) != list and side != None and type()):
                for ui_page_2 in page_ui_2:
                    ui_page_2.pack(side=side)
                    if debug == True:print("Packed ui.")
            else:
                if(side in ["bottom","top","right","left"]):
                    side_index = 0
                    for ui_page_2 in page_ui_2:
                        try:
                            ui_page_2.pack(side=side[side_index])
                        except:
                            raise SyntaxError("if side is a list, count index side SHOULD be == count index ui_page_2.\n\n")
                    side_index += 1
                    if debug == True:print("Packed ui.")
                else:
                    if(typely(page_ui_2)):
                        for sidec in page_ui_2:
                            print(sidec[1][0])
                            try:
                                sidec[0].place(x=sidec[1][0],y=sidec[1][1])
                                print("x: {},\ny:{}.".format(sidec[1][0],sidec[1][1]))
                            except:
                                raise SyntaxError("if side is a list, count index side SHOULD be == count index ui_page_2.\n\n")
                            if debug == True:print("Packed ui.")
                    else:
                        print("ERROR SYNTAX list.")
                
    else:
        raise TypeError("redirect_pages(ui_page), page_ui_1 and page_ui_2 SHOULD be list type.")
            
def window_exit(title: str, message: str):
    "Message Box for Exit(two buttons 'Yes','No' and Title text and message text boxs)."
    output = messagebox.askyesno(title=title,message=message)
    if(output==True):
        if debug == True:
            print("Program Exit.")
        exit()


def documentation():
    "Show Documentation for ManagerTk."
    print("Documentation: https://pypi.org/project/ManagerTk/")
