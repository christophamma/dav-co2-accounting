from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit",
                            command=self.quit)
        quitButton.place(x=50, y=50)


def main():
    root = Tk()
    root.geometry("500x400+300+300")
    root.title('CO2data')
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
