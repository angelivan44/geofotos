# Import the required Libraries
from mimetypes import init
from tkinter import *
from tkinter import ttk, filedialog
import script
from tkinter.filedialog import askopenfile

import os

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("650x350")
win.title('GeoFotos')
win.resizable(0,0)



foto_path = ""
dir_path = ""

def open_file():
   file = filedialog.askdirectory()
   if file:
      filepath = os.path.abspath(file)
      global foto_path
      foto_path =  filepath
      Label(win, text="The Files are located at : " + str(filepath), font=('Aerial 11')).pack(pady= 5)

def save_file():
   file = filedialog.askdirectory()
   if file:
      filepath = os.path.abspath(file)
      global dir_path
      dir_path =  filepath
      Label(win, text="The Export will save at : " + str(filepath), font=('Aerial 11')).pack(pady= 5)
# Add a Label widget



def start():
   if foto_path and dir_path:
      finish = script.script_main(foto_path, dir_path)
      if finish:
         Label(win, text="Tarea Finalizada", font=('Aerial 11'),bg='#fff', fg='#f00',pady = 5).pack()
   else:
      if foto_path:
         Label(win, text="please chose a directory", font=('Aerial 11'),pady = 5).pack()
      else:
         Label(win, text="please chose a foto directory", font=('Aerial 11'),pady = 5).pack()



# Create a Button
  
# Show image using label
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = '#03A062', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','red')])
ttk.Button(win, text="Cargar Fotos", command=open_file).pack(pady=20)
ttk.Button(win, text="Guardar en", command=save_file).pack(pady=20)

ttk.Button(win, text="Start", command=start).pack(pady=20)

class Frame():
   def __init__(self):
      self = self
   def show_frame(self,win):
      win.mainloop()

if __name__ == "__main__":
   app = Frame()
   app.show_frame(win)     


