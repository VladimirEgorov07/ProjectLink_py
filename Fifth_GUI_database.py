import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Tk
from tkinter import Spinbox
from time import sleep
from threading import Thread
from tkinter import *
#import test_13_04 as db1
import mysql.connector
from mysql.connector import errorcode

#==========================================
class ToolTip(object):
    def __init__(self,widget):
        self.widget =widget
        self.tip_window =None 
    def show_tip(self,tip_text):
        if self.tip_window or not tip_text:
            return
        x,y, _cx, cy =self.widget.bbox("insert")
        x =x+ self.widget.winfo_rootx() +25
        y = y+cy +self.widget.winfo_rooty() +25
        self.tip_window =tw =tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x,y))

        label =tk.Label(tw, text =tip_text, justify =tk.LEFT,
                      background ="#ffffe0",relief =tk.SOLID, borderwidth =1,
                      font =("tahoma", "8", "normal"))
        label.pack(ipadx =1)

    def hide_tip(self):
        tw = self.tip_window
        self.tip_window = None 
        if tw:
            tw.destroy()

#==========================================

def create_ToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.show_tip(text)
    def leave(event):
        toolTip.hide_tip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

#===========================================
root =Tk()
root.withdraw()

win = tk.Tk()
win.title("Python GUI")
tabControl =ttk.Notebook(win)
tab1 =ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1') 
tab2 =ttk.Frame(tabControl)
tabControl.add(tab2, text ='Tab 2')

tab3 = ttk.Frame(tabControl)            # 
tabControl.add(tab3, text='Tab 3')      # Add a third tab

tabControl.pack(expand =1, fill ="both")

mighty =ttk.LabelFrame(tab1, text ='Mighty Python')
mighty.grid(column =0, row =0, padx =8, pady =4)

a_label= ttk.Label(mighty,text="A Label")
a_label.grid(column=0, row=0, sticky ='W')

def click_me():
    try:
      cnx = mysql.connector.connect(user='vladimir', password='12345',
                                  host='127.0.0.1',
                                  database='publications')
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
        cursor = cnx.cursor() 
        cursor.execute("DESCRIBE classics") 
        nis= cursor.fetchall() 
        scr.insert(tk.INSERT, nis)
    cnx.close()


#def click_me():
#    value =cursor.get()
#    print(value)
#   scr.insert(tk.INSERT, value + '\n')
                     
ttk.Label(mighty,text="Enter a name:").grid(column=0, row = 0)
name =tk.StringVar()
name_entered = ttk.Entry(mighty, width = 24, textvariable = name)
name_entered.grid(column =0, row = 1, sticky =tk.W)
  

    # Adding a Button
action = ttk.Button(mighty,text ='Click Me!', command=click_me)
action.grid(column=2, row=1)

ttk.Label(mighty, text = "Choose a number:").grid(column = 1,row = 0)
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width =14, textvariable = number, state = 'readonly')
number_chosen['values'] = (1,2,3,42,100)
number_chosen.grid(column =1, row = 1)
number_chosen.current(0)


mighty2 =ttk.LabelFrame(tab2, text =' The Snake')
mighty2.grid(column =0, row =0, padx=8, pady =4)


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text = "Disabled", variable = chVarDis, state ='disabled')
check1.select()
check1.grid(column=0, row = 4, sticky = tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text = "UnChecked", variable = chVarUn)
check2.deselect()
check2.grid(column=1, row = 4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text ="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row = 4, sticky=tk.W)

colors = ["Blue", "Gold", "Red"]

def radCall():
    radSel= radVar.get()
    if   radSel == 0: mighty2.configure(background ='Blue')
    elif radSel == 1: mighty2.configure(background ='Gold')
    elif radSel == 2: mighty2.configure(background ='Red')

radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text =colors[col], variable =radVar,
                            value =col,command=radCall)
    curRad.grid(column=col, row =6, sticky =tk.W)


#====================================================
#COLOR1 = "Blue"
#COLOR2 = "Gold"
#COLOR3 = "Red"

#def radcall2():
#    radPad = radMed.get()
 #   if radPad ==1:
 #       mighty2.configure(background=COLOR1)
 #   elif radPad == 2:
 #       mighty2.configure(background=COLOR2)
  #  elif radPad == 3:
 #       mighty2.configure(background=COLOR3)

#creating 3 radiobuttons
#radMed=tk.IntVar()
#rad1 = tk.Radiobutton(mighty2, text =COLOR1, variable=radMed, value=1,
#                        command=radcall2)
#rad1.grid(column=0,row=8)                       
#rad2 = tk.Radiobutton(mighty2, text = COLOR2, variable=radMed, value=2,
#                        command=radcall2)
#rad2.grid(column=1,row=8)
#rad3 = tk.Radiobutton(mighty2, text = COLOR3, variable=radMed, value=3,
#                        command=radcall2)                        
#rad3.grid(column=2,row=8)

#
#class radbut():
#
 #   def __init__(self,mighty2,text,variable,value,col2,ro):
 #       self.text=text
 #       self.variable=variable
 #       self.value=value
 #       self.col2=col2
 ##
  #  def configure(self):
  #      if self.variable==1:
 #           print("in if statement")
 #           self.mighty2.configure(background=COLOR1)
 #           return tk.Radiobutton(self.mighty2,self.text,self.variable,self.value).grid(column = self.col2,row = self.ro)
 #       elif self.variable == 2:
 #           self.mighty2.configure(background=COLOR2)
#            return tk.Radiobutton(self.mighty2,self.text,self.variable,self.value).grid(column = self.col2,row = self.ro)
#        elif self.variable == 3:
#            self.mighty2.configure(background=COLOR3)
#            return tk.Radiobutton(self.mighty2,self.text,self.variable,self.value).grid(column = self.col2,row = self.ro)
#cast = radbut(mighty2,COLOR1,'BLUE',1,0,4)
#cast.configure()
#=================================================================================

#OOP Programming в данном случае, остальные элементы вне класса 

colors = ['red', 'blue', 'green']

class radbut(Frame):
    def __init__(self, master, colors, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.colors = colors

        self.choice = IntVar()
        self.choice.set(0)

        # Using a loop to create all alternatives in the list: colors
        for index, color in enumerate(colors):
            b = Radiobutton(self, text=color, variable=self.choice,
                            value=index, command=self.change)
            b.grid(row=0, column=index)

    def change(self):
        self.master.config(bg=self.colors[self.choice.get()])
        print('change')

cast = radbut(mighty2, colors)
cast.grid(row=8, column=0)

# ===========================================================================================

def _spin():
    value =spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

def _spin2():
    value =spin2.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

spin2 =Spinbox(mighty, values =(1,2,4,42,100),width =5, bd =8,
              command =_spin2)
spin2.grid(column =1, row =2)
spin = Spinbox(mighty,from_=0,to =10, width=5, bd =4, command =_spin)
spin.grid(column =0, row =2)
create_ToolTip(spin, 'This is a Spin control')

scrol_w = 40
scrol_h =10
scr= scrolledtext.ScrolledText(mighty,width= scrol_w, height = scrol_h, wrap = tk.WORD)
scr.grid(column=0, row=5, sticky='W', columnspan=3)
create_ToolTip(scr, 'This is a ScrolledText control')
name_entered.focus()

#buttons_frame1 =ttk.LabelFrame(mighty, text =' Labels in a Frame')
#buttons_frame1.grid(column =1, row =7)

#ttk.Label(buttons_frame1, text ="Label1").grid(column =1, row =0)
#ttk.Label(buttons_frame1, text ="Label2").grid(column =2, row =0)
#ttk.Label(buttons_frame1, text ="Label3").grid(column =3, row =0)

#for child in buttons_frame1.winfo_children():
#    child.grid_configure(padx=8, pady=4)


#==============================================
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2) 

# update progressbar in callback loop
def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        progress_bar.update()       # have to call update() in loop
    progress_bar["value"] = 0       # reset/clear progressbar  

def start_progressbar():
    progress_bar.start()
    
def stop_progressbar():
    progress_bar.stop()
 
def progressbar_stop_after(wait_ms=1000):    
    win.after(wait_ms, progress_bar.stop)

buttons_frame =ttk.LabelFrame(mighty2, text ='ProgressBar')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_progressbar).grid(column=0, row=0, sticky='W')  
ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')  
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=2, sticky='W')  
ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='W')  
 
for child in mighty2.winfo_children():  
    child.grid_configure(padx=8, pady=2) 

    

#==============================================

tab3_frame =tk.Frame(tab3, bg ='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas =tk.Canvas(tab3_frame, width =150, height =80,
                      highlightthickness =0, bg ='orange')
    canvas.grid(row =orange_color, column =orange_color)

#==============================================

def _msgBox():
  #  msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:'
  # '\nThe years is 2019.')
  #  msg.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:'
  #                '\nWarning: There might be a bug in this code.')
  #  msg.showerror('Python Message Error Box', 'A python GUI created using tkinter:'
  #             '\nError: Houston we have a serious Problem')
  msg.showinfo('lolipop', 'Python GUI created using tkinter:\nThe year is 2017')

def _quit():
    win.quit()
    win.destroy()
    exit()


menu_bar =Menu(win)
win.config(menu =menu_bar)

file_menu =Menu(menu_bar, tearoff =0)
file_menu.add_command(label ="New")
file_menu.add_separator()
file_menu.add_command(label ="Exit", command =_quit)
menu_bar.add_cascade(label ="File", menu =file_menu)

help_menu =Menu(menu_bar, tearoff =0)
help_menu.add_command(label ="About", command =_msgBox)
menu_bar.add_cascade(label ="Help", menu =help_menu)


#====================
# Start GUI
#====================

win.mainloop()


