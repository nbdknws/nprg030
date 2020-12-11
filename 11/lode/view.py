

import tkinter as tk

class View:
    def draw_initial_dialogue(self):
        raise NotImplementedError

class TerminalView(View):
    def draw_initial_dialogue(self):
        field_size = int(input("Zadejte velikost pole: "))
        return field_size


class GraphicalView(View):
    def start_game(self):
        self.field_size = int(self.ent_field_size.get())

        self.window.destroy()

    def draw_initial_dialogue(self):
        self.window = tk.Tk()

        self.lbl_field_size = tk.Label(text="Zadejte velikost pole: ")
        self.ent_field_size = tk.Entry()
        self.btn_field_size = tk.Button(text="START", command=self.start_game)

        self.lbl_field_size.pack()
        self.ent_field_size.pack()
        self.btn_field_size.pack()

        self.window.mainloop()

        return self.field_size