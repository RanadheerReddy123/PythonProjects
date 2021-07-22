from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from moviepy.editor import *
from threading import *

mw = Tk()
mw.title('Video to Mp3 Converter')
mw.iconbitmap('assets/icon.ico')
filename = ''

filepath = ''
def open_video():
    global filepath
    filename = filedialog.askopenfilename(initialdir='c:/', title='Select a Video File')
    display_box.config(state='normal')
    display_box.delete(0, END)
    display_box.insert(0, filename)
    display_box.config(state='readonly')


def start_conversion():
    global filename
    if filename != '':
        status_lbl.config(text='')
        final_filename = filename + '_converted.mp3'
        cvt_btn.config(text='Converting....', state='disabled')
        video = VideoFileClip(filename)
        audio = video.audio
        audio.write_audiofile(final_filename)
        cvt_btn.config(text='Convert', state='normal')
        status_lbl.config(text="File has been Converted!")
    else:
        messagebox.showerror('RR-Web Developers', 'Please Select a Video File')
        open_video()


def convert():
    t1 = Thread(target=start_conversion)
    t1.daemon = True
    t1.start()


display_box = Entry(mw, font=('', 16), width=30, state='readonly', bd=2)
display_box.grid(row=0, column=0, padx=(20, 10), pady=20)
select_btn = Button(mw, text="Select Video File", font=('', 14), command=open_video)
select_btn.grid(row=0, column=1, padx=(10, 20), pady=20)
cvt_btn = Button(mw, text="Convert", font=('', 14), command=convert)
cvt_btn.grid(row=1, column=0, pady=(10, 20), columnspan=2)
status_lbl = Label(mw, text='', font=('', 14), fg='green')
status_lbl.grid(row=2, column=0, padx=20, pady=(10, 20), columnspan=2, sticky=W)
mw.mainloop()
