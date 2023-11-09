from tkinter import *
import os
import shutil
from tkinter import messagebox as mb
from tkinter import filedialog as fd

#open a file
def openAfile():
    files=fd.askopenfilename(title="select a file to open",filetypes=[("All Files","*.*")])
    os.startfile(os.path.abspath(files))

#copy a file
def copyAfile():
    copyfile=fd.askopenfilename(title="select a file to copy",filetypes=[("All Files","*.*")])
    dtrtocopy=fd.askdirectory(title="Select directory to copy")
    try:
        shutil.copy(copyfile,dtrtocopy)
        mb.showinfo(title="File copied",message="File copied successfully.")
    except:
        mb.showerror(title="ERROR",message="File could not be copied.\nPlease try again.")

#delete a file
def deleteAfile():
    files=fd.askopenfilename(title="select a file to delete",filetypes=[("All Files","*.*")])
    os.remove(os.path.abspath(files))
    mb.showinfo(title="File deleted",message="File deleted successfully.")

#rename a file 
def rename():
    rnwin=Toplevel(root)
    rnwin.title("Rename a file")
    rnwin.geometry("300x100+300+250")
    rnwin.resizable(0,0)
    rnwin.configure(bg="blue")
    global file_name
    file_name=StringVar()

    rnlabel=Label(rnwin,text="Enter a name: ",font=("Arial",8),fg="black")
    rnlabel.pack(pady=4)
    rnentry=Entry(rnwin,textvariable=file_name,font=("Arial",8),bg="yellow",fg="black")
    rnentry.pack(pady=4,padx=4)
    rnbutton=Button(rnwin,text="Change",command=renamefile,relief="raised")
    rnbutton.pack()

def filetochange():
    files=fd.askopenfilename(title="select file to change name",filetypes=[("All Files","*.*")])
    return files

def renamefile():
    filename=file_name.get()
    files=filetochange()
    newfilename=os.path.join(os.path.dirname(files),filename+os.path.split(files)[1])
    os.rename(files,newfilename)
    mb.showinfo(title="Name changed",message="File name changed successfully.")

#open a folder
def openAfolder():
    folder=fd.askdirectory(title="Select a folder to open")
    os.startfile(folder)

#delete a folder
def deleteAfolder():
    folder=fd.askdirectory(title="Select a folder to open")
    os.rmdir(folder)
    mb.showinfo(title="Deleted folder",message="Deleted folder successfully.")

#move a folder
def moveAfolder():
    folder=fd.askdirectory(title="Select folder to move")
    mb.showinfo(title="Folder selected",message="Folder selected, now select a destination to move.")
    destination=fd.askdirectory(title="Select destination to move")
    try:
        shutil.move(folder,destination)
        mb.showinfo(title="Folder moved",message="Folder moved successfully.")
    except:
        mb.showinfo(title="Error",message="Folder couldn't be moved, please check if the destination exists.")

#list the files in a folder
def listAfolder():
    folder=fd.askdirectory(title="Select folder to list")
    files=os.listdir(os.path.abspath(folder))
    listfilewin=Toplevel(root)
    listfilewin.title(f'files in {folder}')
    listfilewin.geometry("300x100+300+200")
    listfilewin.resizable(0,0)
    listfilewin.configure(bg="white")

    list_box=list_box(listfilewin, font=("Arial",8),bg="white")
    list_box.place( relx=0, rely=0, relheight=1, relwidth=1)
    scroll_bar=Scrollbar(list_box,orient=VERTICAL, command=list_box.yview)
    scroll_bar.pack(side=RIGHT,fill="y")
    list_box.config(yscrollcommand=scroll_bar.set)
    i=0
    while i<len(files):
        list_box.insert(END,"("+str(i+1)+")"+files[i])
    list_box.insert(END,"")
    list_box.insert(END,"Total Files : "+str(len(files)))

if __name__=="__main__":
    root=Tk()
    root.title("File Explorer")
    root.geometry("600x400+300+250")
    root.resizable(0,0)
    root.configure(bg="white")

    header=Frame(root,bg="White")
    body=Frame(root,bg="Blue")

    header.pack(fill="both")
    body.pack(expand=True,fill="both")

    label=Label(header,text="File Explorer",font=("Arial",16),bg="white",fg="green")
    label.pack(expand=True,fill="both",pady=12)

    open_file_bt=Button(body,text="Open a File",bg="white",fg="green",command=openAfile)
    copy_file_bt=Button(body,text="Copy a File",bg="white",fg="green",command=copyAfile)
    delete_file_bt=Button(body,text="Delete a File",bg="white",fg="green",command=deleteAfile)
    rename_file_bt=Button(body,text="Rename a File",bg="white",fg="green",command=rename)
    open_folder_bt=Button(body,text="Open a Folder",bg="white",fg="green",command=openAfolder)
    delete_folder_bt=Button(body,text="Delete a Folder",bg="white",fg="green",command=deleteAfolder)
    move_folder_bt=Button(body,text="Move a Folder",bg="white",fg="green",command=moveAfolder)
    list_folder_bt=Button(body,text="List a Folder",bg="white",fg="green",command=listAfolder)
    open_file_bt.pack(pady=12)
    copy_file_bt.pack(pady=12)
    delete_file_bt.pack(pady=12)
    rename_file_bt.pack(pady=12)
    open_folder_bt.pack(pady=12)
    delete_folder_bt.pack(pady=12)
    move_folder_bt.pack(pady=12)
    list_folder_bt.pack(pady=12)
    root.mainloop()