import tkinter as tk

class MyApp:
    def __init__(self):
        # Creation of the page
        self.window = tk.Tk()

        # Settings of the page
        self.window.title("Calculatrice")
        self.window.geometry("550x700")#550x700
        self.window.resizable(0, 0)
        
        # Keep the action you did
        self.register = []

        self.create_widgets()
    
    def create_widgets(self):
        """
        This module create all the widgets of the window.
        """
        self.create_entry()
        self.create_button()

    def create_entry(self):
        """
        This module create the entry.
        """
        self.affichage = tk.Entry(self.window, font=("Helvetica", 50))
        self.affichage.place(relx=0, rely=0, relwidth=1, relheight=1/6)

    def create_button(self):
        """
        This module create all buttons of the page.
        """
        elementButton = ["AC", "+/-", "%", '/',
                         '7', '8', '9', '*',
                         '4', '5', '6', '-',
                         '1', '2', '3', '+',
                         '0', '.', '=']

        self.button = [tk.Button(self.window, text=elmt, font=('Helvetica', 30)) for elmt in elementButton]

        # Place all the button on the page
        for i in range(len(elementButton)):
            print(i)
            self.button[i]['command'] = lambda: self.click(elementButton[i])

            if 16 > i:
                self.button[i].place(relx=(0.25 * int(i%4)), rely=(1/6 * (int(i/4) + 1)), relwidth=0.25, relheight=1/6)

        # The last line
        self.button[16].place(relx=0, rely=1/6 * 5, relwidth=0.5, relheight=1/6)
        self.button[17].place(relx=0.5, rely=1/6 * 5, relwidth=0.25, relheight=1/6)
        self.button[18].place(relx=0.75, rely=1/6 * 5, relwidth=0.25, relheight=1/6)

    def click(self, name):
        """
        When you click on one button, I will process.
        On function of which one something different will happen.

        param name: str, the name of the button you click on.
        """
        
        print(f"Tu as cliqué sur la touche {name}")

        if self.button[0]['text'] != "C" and (self.affichage.get() != '' or self.register != []):
            self.button[0]['text'] = 'C'

    def resultat(self, element):
        """
        This module calcul the result of the operation
        """