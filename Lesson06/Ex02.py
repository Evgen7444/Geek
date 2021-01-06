class Road:
    def __init__(self, _len, _wight):
        self._len = _len
        self._wight = _wight

    def mass(self):
        return self._len * self._wight


class MassCount(Road):
    def __init__(self, _len, _wight, volume):
        super().__init__(_len, _wight)
        self.volume = volume


r = MassCount(20, 10000, 20)
print(r.mass())
