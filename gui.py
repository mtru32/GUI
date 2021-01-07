from tkinter import Tk, Label, Button
import webbrowser as w

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Button Clicker")

        self.label = Label(master, text="Try the Buttons in my GUI!")
        self.label.pack()

        self.greet_button = Button(master, text='Say Hello', command=self.greet)
        self.greet_button.pack()

        self.rr_button = Button(master, text="Don't Click", command=self.rroll)
        self.rr_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Hello, World")
    def rroll(self):
        w.open('https://www.youtube.com/watch?v=DLzxrzFCyOs&ab_channel=AllKindsOfStuffs')
    
if __name__ == '__main__':
    root = Tk()
    root.geometry('350x100')
    my_gui = MyGUI(root)
    root.mainloop()