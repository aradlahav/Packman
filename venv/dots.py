class Dot:

    def __init__(self, first_color, second_color, horizontal, vertical, visited):
        self.first_color = first_color
        self.second_color = second_color
        self.horizontal = horizontal
        self.vertical = vertical
        self.visited = False

    def dot_color(self):
        if self.visited is False:
            color = self.first_color
        else:
            color = self.second_color
        return color
