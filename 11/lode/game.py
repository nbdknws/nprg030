

from view import GraphicalView as View


class Game:
    def __init__(self):
        self.gui = View()

    def play(self):
        field_size = self.gui.draw_initial_dialogue()

        print("Velikost pole", field_size)