# Create classes Pen, Pencil and Marker, each with a write() method that prints its own message. Put one of each in a list and call write() on every item in a loop.


class Pen:
    def write(self):
        print("Writing with a Pen")


class Pencil:
    def write(self):
        print("Writing with a Pencil")


class Marker:
    def write(self):
        print("Writing with a Marker")


pen = Pen()
pencil = Pencil()
marker = Marker()

items = [pen, pencil, marker]

for item in items:
    item.write()
