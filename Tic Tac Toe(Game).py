from tkinter import *
import tkinter.messagebox

root=Tk()
root.geometry("415x600")
root.title("Tic Tac Toe")

bclick = True
flag = 0

p1 = StringVar()
p2 = StringVar()

player1_name = Entry(root, textvariable=p1, bd=5, font='Times 18 bold')
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(root, textvariable=p2, bd=5, font='Times 18 bold')
player2_name.grid(row=2, column=1, columnspan=8)

def disableButton():
    b1.configure(state=DISABLED)
    b2.configure(state=DISABLED)
    b3.configure(state=DISABLED)
    b4.configure(state=DISABLED)
    b5.configure(state=DISABLED)
    b6.configure(state=DISABLED)
    b7.configure(state=DISABLED)
    b8.configure(state=DISABLED)
    b9.configure(state=DISABLED)

def enableButton():
    global flag
    b1.configure(state=NORMAL)
    if(b1['text'] == 'O' or b1['text'] == 'X'):
        b1['text'] = ' '
        
    b2.configure(state=NORMAL)
    if(b2['text'] == 'O' or b2['text'] == 'X'):
        b2['text'] = ' '
        
    b3.configure(state=NORMAL)
    if(b3['text'] == 'O' or b3['text'] == 'X'):
        b3['text'] = ' '
        
    b4.configure(state=NORMAL)
    if(b4['text'] == 'O' or b4['text'] == 'X'):
        b4['text'] = ' '
        
    b5.configure(state=NORMAL)
    if(b5['text'] == 'O' or b5['text'] == 'X'):
        b5['text'] = ' '
        
    b6.configure(state=NORMAL)
    if(b6['text'] == 'O' or b6['text'] == 'X'):
        b6['text'] = ' '
        
    b7.configure(state=NORMAL)
    if(b7['text'] == 'O' or b7['text'] == 'X'):
        b7['text'] = ' '
        
    b8.configure(state=NORMAL)
    if(b8['text'] == 'O' or b8['text'] == 'X'):
        b8['text'] = ' '
        
    b9.configure(state=NORMAL)
    if(b9['text'] == 'O' or b9['text'] == 'X'):
        b9['text'] = ' '

def show(buttons):
    global bclick, flag, pb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "O"
        bclick=False
        pb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag+=1

    elif buttons["text"] == " " and bclick==False:
        buttons["text"] = "X"
        bclick=True
        checkForWin()
        flag+=1
        
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def checkForWin():
    if (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
        b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
        b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
        b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
        b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
        b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O' or
        b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
        b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 8):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
          b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
          b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
          b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
          b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
          b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X' or
          b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
          b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pb)

label = Label( root, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = Label( root, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

b1 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b1))
b1.grid(row=3, column=0)

b2 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b2))
b2.grid(row=3, column=1)

b3 = Button(root, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b3))
b3.grid(row=3, column=2)

b4 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b4))
b4.grid(row=4, column=0)

b5 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b5))
b5.grid(row=4, column=1)

b6 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b6))
b6.grid(row=4, column=2)

b7 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b7))
b7.grid(row=5, column=0)

b8 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b8))
b8.grid(row=5, column=1)

b9 = Button(root, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: show(b9))
b9.grid(row=5, column=2)

b10 = Button(root, text='RESET', font='Times 20 bold', bg='Black', fg='white', height=2, width=26, command=enableButton)
b10.place(x=0,y=515)

root.mainloop()
