class Vector3D():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod

    def __add__(self, other):
        return (self.x + other, self.y + other, self.z + other)


    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)


    def __sub__(self, other):
        return (self.x - other, self.y - other,self.z - other)


V1 = Vector3D(12,13,1)
