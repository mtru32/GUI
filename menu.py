from tkinter import *
import webbrowser as w
import page


class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Button Clicker")
        Label(master, text='Try the Buttons in my GUI!\n').pack()
        Button(master, text='Say Hello', command=self.greet).pack()
        Button(master, text='Create New Window',
               command=self.openNewWindow).pack()
        Button(master, text="Close", command=self.close_gui).pack()
        Button(master, text="Do Not Click", command=self.rroll).pack()

    def greet(self):
        print("Hello!")

    def openNewWindow(self):
        newWindow = Toplevel(self.master)
        newWindow.title("New Window")
        newWindow.geometry('350x150')
        Label(newWindow, text="new window").pack

    def rroll(self):
        w.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')

    def close_gui(self):
        self.master.quit()


if __name__ == '__main__':
    root = Tk()
    root.geometry('350x150')
    my_gui = MyGUI(root)
    root.mainloop()
