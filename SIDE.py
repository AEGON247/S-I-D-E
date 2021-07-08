from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
from tkinter import simpledialog

print("Welcome To S-I-D-E ! \n Wait for 2-3 mins if the window isn't visible")

window = Tk()
window.title('S-I-D-E')

gpath = ''

def runMyCode():
    global gpath
    if gpath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="Please save the file first")
        msg.pack()
        return
    command = f'python {gpath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    output.insert('1.0',outputResult)
    output.insert('1.0',error)
     

def openMyFile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        textEditor.insert('1.0', code)
        global gpath
        gpath = path

def saveMyFileAs():
    global gpath
    if gpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = gpath    
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        file.write(code)

textEditor = Text()
textEditor.config(bg='#362f2e', fg='#d2ded1', insertbackground='white')
textEditor.pack()

def homeBrew():
  textEditor.config(bg='#000000', fg='#1dd604', insertbackground='blue')
  textEditor.pack()

def miniShell():
  textEditor.config(bg='#000000', fg='#ff0000', insertbackground='white')
  textEditor.pack()

def grassShell():
  textEditor.config(bg='#228B22', fg='#ed9121', insertbackground='white')
  textEditor.pack()

def oceanShell():
  textEditor.config(bg='#003153', fg='#add8e6', insertbackground='white')
  textEditor.pack()
  
def custom():
  fgcolor = simpledialog.askstring(title="Text Color", prompt="Enter the text color .... ")
  bgcolor = simpledialog.askstring(title="Bg Color", prompt="Enter the background color .... ")
  textEditor.config(fg=fgcolor, bg = bgcolor,  insertbackground='white')
  textEditor.pack()

output = Text(height=7)
output.config(bg='#362f2e', fg='#1dd604')
output.pack(side = BOTTOM)
 
menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Open', command = openMyFile)
fileBar.add_command(label='Save', command = saveMyFileAs)
fileBar.add_command(label='SaveAs', command = saveMyFileAs)
fileBar.add_command(label='Exit', command = exit)
menuBar.add_cascade(label='File', menu = fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command = runMyCode)
menuBar.add_cascade(label='Run', menu = runBar)

themeBar = Menu(menuBar, tearoff=0)
themeBar.add_command(label='HomeBrew', command= homeBrew)
themeBar.add_command(label='MiniShell', command=miniShell)
themeBar.add_command(label='Grass', command=grassShell)
themeBar.add_command(label='Ocean', command=oceanShell)
themeBar.add_command(label='Custom', command=custom)
menuBar.add_cascade(label='Theme', menu= themeBar)

window.config(menu=menuBar)
window.mainloop()
