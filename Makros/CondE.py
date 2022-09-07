from Generators.Conj2 import Conj2
from Generators.Disj2 import Disj2
from Generators.Fail import Fail
from Generators.Generator import Generator

class CondE(Generator):

    def __init__(self, list):
        self.list = list
        self.length = len(list)
        super().__init__('CONDE')


    def worker(self,index):
        if index >= self.length:
            return Fail()
        g1 = self.list[index]
        if index == self.length-1:
            return g1
        else:
            g2 = self.list[index+1]
            return Disj2(Conj2(g1,g2),self.worker(index+2))

    def generate(self,state):

        stream = self.worker(0).generate(state)

        while (True):
            try:
                current = next(stream)
                if current == None:
                    continue
                elif current != False:
                    yield current
            except StopIteration:
                break
