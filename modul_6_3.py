class Horse:
    def __init__(self, x_distance, dx, y_distance, dy):
        super().__init__(y_distance, dy)
        sound="Frrr"
        self.x_distance = x_distance
        self.dx = dx
    def run(self, x_distance, dx):
        self.x_distance = self.x_distance + dx
        return self.x_distance


class Eagle:
    def __init__(self, y_distance, dy):
        self.y_distance = y_distance
        self.sound = 'I train, eat, sleep, and repeat'
        self.dy = dy

    def fly(self, y_distance, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance


class Pegasus (Horse, Eagle):

    def __init__(self, x_distance, dx, y_distance, dy):
        super ().__init__ (x_distance, dx, y_distance, dy)

    def move(self, dx, dy):
        c = []
        self.c = c
        a = (super ().run (self, dx))
        b = (super ().fly (self, dy))
        self.c.append ((a, b))

    def get_pos(self):
        return self.c

    def voice(self):
        print (self.sound)


p1 = Pegasus (0, 0, 0, 0)
print (Pegasus.mro ())
p1.move (0, 0)
print (p1.get_pos ())
p1.move (10, 15)
print (p1.get_pos ())
p1.move (-5, 20)
print (p1.get_pos ())
p1.voice ()
