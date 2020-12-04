class Rect:
    filling_char = " "

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def perimeter(self):
        return 2 * (self.w + self.h)

    def area(self):
        return self.w * self.h

    def __eq__(self, o):
        return self.w == o.w \
             and self.h == o.h \
             and self.x == o.x \
             and self.y == o.y

    def __contains__(self, o):
        return o.x >= self.x \
            and o.y >= self.y \
            and o.x + o.w <= self.x + self.w \
            and o.y + o.h <= self.y + self.h

    def __and__(self, o):
        x = max(self.x, o.x)
        y = max(self.y, o.y)

        x_end = min(self.x + self.w, o.x + o.w)
        y_end = min(self.y + self.h, o.y + o.h)

        w = x_end - x
        h = y_end - y

        if w < 0 or h < 0:
            # žádný průnik
            return None

        return Rect(x, y, w, h)

    def _border_line(self):
        return " " * self.x + "-"*(self.w + 2)

    def __str__(self):
        s = []
        # odsazení shora
        for _ in range(self.y):
            s.append("")

        # odsazení zleva + horní strana
        s.append(self._border_line())

        # odsazení zleva + boční strany
        for i in range(self.h):
            s.append(" " * self.x 
                + "|" + self.filling_char*(self.w) + "|")

        # odsazení zleva + dolní strana
        s.append(self._border_line())

        return "\n".join(s)


class FilledRect(Rect):
    filling_char = "x"


class RoundedRect(Rect):
    def _border_line(self):
        return " " * (self.x+1) + "-"*(self.w)


class FilledRoundedRect(RoundedRect, FilledRect):
    pass


class Square(Rect):
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.w = a
        self.h = a

def draw(shapes):
    max_width = max([shape.x + shape.w for shape in shapes]) + 2
    max_height = max([shape.y + shape.h for shape in shapes]) + 2

    canvas = [[" " for _ in range(max_width)] for _ in range(max_height)]

    for shape in shapes:
        lines = shape.__str__().split("\n")

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != " ":
                    canvas[i][j] = char

    print("\n".join(["".join(line) for line in canvas]))

