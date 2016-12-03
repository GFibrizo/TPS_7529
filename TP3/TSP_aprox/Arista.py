class Arista:

    def __init__(self, src, dst, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def src(self):
        return self.src

    def dst(self):
        return self.dst

    def weight(self):
        return self.weight

    def __str__(self):
        return str(self.src)+"-->"+str(self.dst)

    def __repr__(self):
        return str(self.src) + "-->" + str(self.dst)