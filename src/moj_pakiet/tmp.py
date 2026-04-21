import functools

class A:
    @property
    def atr1(self):
        if not hasattr(self, '_atr1'):
            print('wyliczam')
            self._atr1 = 66
            return 66
        else:
            return self._atr1


class A:
    @property
    @functools.lru_cache()
    def atr1(self):
        print('wyliczam')
        return 66

a = A()
print(a.atr1)
# a.atr1 = 11
print(a.atr1)
