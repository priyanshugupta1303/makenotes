import tkinter as tk

class NotesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notes App")
        
        # Create text box for notes
        self.text = tk.Text(self.master)
        self.text.pack(fill='both', expand=True)
        
        # Create menu bar
        menubar = tk.Menu(self.master)
        
        # Create "File" menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Note", command=self.new_note)
        filemenu.add_command(label="Save Note", command=self.save_note)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        # Create "Edit" menu
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut", command=self.cut_text)
        editmenu.add_command(label="Copy", command=self.copy_text)
        editmenu.add_command(label="Paste", command=self.paste_text)
        menubar.add_cascade(label="Edit", menu=editmenu)
        
        # Set the menu
        self.master.config(menu=menubar)
    
    def new_note(self):
        # Clear the text box
        self.text.delete('1.0', 'end')
    
    def save_note(self):
        # Get the note text
        note = self.text.get('1.0', 'end-1c')
        
        # Save the note to a file
        with open('note.txt', 'w') as f:
            f.write(note)
    
    def cut_text(self):
        self.text.event_generate("<<Cut>>")
    
    def copy_text(self):
        self.text.event_generate("<<Copy>>")
    
    def paste_text(self):
        self.text.event_generate("<<Paste>>")

if __name__ == '__main__':
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
