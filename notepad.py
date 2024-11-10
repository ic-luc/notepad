import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

current_file = None

def save_file(event=None):
  global current_file
  if current_file:
    with open(current_file, "w") as file_output:
      text = text_edit.get(1.0, tk.END)
      file_output.write(text)
    root.title(f"{current_file}")
  else:
    save_file_as()

def save_file_as(event=None):
  global current_file
  file_location = asksaveasfilename(
    defaultextension="txt", 
    filetypes=[("Text files", "*.txt"), ("All files","*.*")])
  
  if not file_location:
    return
  current_file = file_location
  with open(file_location,"w") as file_output:
    text = text_edit.get(1.0, tk.END)
    file_output.write(text)
  root.title(f"{current_file}")

def open_file(event=None):
  global current_file
  file_location = askopenfilename(
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
  
  if not file_location:
    return
  current_file = file_location
  text_edit.delete(1.0, tk.END)
  with open(file_location, "r") as file_input:
    text = file_input.read()
    text_edit.insert(tk.END, text)
  root.title(f"{current_file}")

def new_file(event=None):
  global current_file
  current_file = None
  text_edit.delete(1.0, tk.END)
  root.title("Untitled")

root = tk.Tk()
root.title("Notepad")

root.rowconfigure(0, minsize=800)
root.columnconfigure(1, minsize=800)

text_edit = tk.Text(root)
text_edit.grid(row=0, column=1, sticky="nsew")

# Menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save as", command=save_file_as, accelerator="Ctrl+Shift+S")

root.bind('Control-n', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-S>', save_file_as)

root.mainloop()