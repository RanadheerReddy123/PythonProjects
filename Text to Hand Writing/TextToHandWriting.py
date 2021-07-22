from tkinter import *
from tkinter import filedialog
#from tkinter import messagebox
#from moviepy.editor import *
from threading import *
import pywhatkit as kit
mw = Tk()
mw.title('Text to Hand Writing!')
mw.iconbitmap('icon.ico')
mw.geometry('640x200')
filepath = ''
def open_file():
    global filepath
    filepath = filedialog.askopenfilename(title='Select a Text File', filetypes = (("Text Files", "*.txt"),("All Files","*.*")))
    db.config(state='normal')
    db.delete(0, END)
    db.insert(0, filepath)
    db.config(state='disabled')


def start_conversion():
    global filepath
    if filepath != '':
        select_btn.config(state='disabled')
        cvt_btn.config(text="Please wait..!", state='disabled')
        lbl.config(text='Writing.....',fg='red')
        pngfilename = filepath.replace('.txt','.png')
        tf = open(filepath, 'r',encoding='utf8')
        text = tf.read()
        kit.text_to_handwriting(string = text, save_to=pngfilename, rgb=(3,22,145))
        lbl.config(text='Your file is ready!',fg='green')
        select_btn.config(state='normal')
        cvt_btn.config(text="Text to Hand Writing!", state='normal')

def convert():
    t1 = Thread(target=start_conversion)
    t1.daemon = True
    t1.start()

db = Entry(mw, width=30, font=('',20), state='disabled', bd=2)
db.grid(row=0, column=0, padx=(20,10), pady=20)
select_btn = Button(mw, text="Select a File", font=('', 14), command=open_file)
select_btn.grid(row=0, column=1, padx=(10, 20), pady=20)
cvt_btn = Button(mw, text="Convert", font=('', 14), command=convert)
cvt_btn.grid(row=1, column=0, pady=(10, 20), columnspan=2)
lbl = Label(mw, text='', font=('', 14), fg='green')
lbl.grid(row=2, column=0, padx=20, pady=(10, 20), columnspan=2, sticky=W)
mw.mainloop()