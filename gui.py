from tkinter import Tk, Label, Button
import webbrowser as w

class MyGUI:
    said_hello = False
    said_bye = False
    def __init__(self, master):
        self.master = master
        master.title("Button Clicker")

        self.label = Label(master, text='Try the Buttons in my GUI!\n')
        self.label.pack()

        self.greet_button = Button(master, text='Say Hello', command=self.greet)
        self.greet_button.pack()

        self.farewell_button = Button(master, text='Say Good-Bye', command=self.farewell)
        self.farewell_button.pack()

        self.close_button = Button(master, text="Close", command=self.close_gui)
        self.close_button.pack()

        self.rr_button = Button(master, text="Do Not Click", command=self.rroll)
        self.rr_button.pack()

    def greet(self):
        print("Hello!")
        self.said_hello = True
    def farewell(self):
        if (self.said_hello):
            print("Good-Bye")
            self.said_bye = True
        else:
            print("You haven't said hello.")
    def rroll(self):
        w.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
    def close_gui(self):
        if (self.said_bye):
            self.master.quit()
        else:
            print("You haven't said good-bye.")
    
if __name__ == '__main__':
    root = Tk()
    root.geometry('350x150')
    my_gui = MyGUI(root)
    root.mainloop()
