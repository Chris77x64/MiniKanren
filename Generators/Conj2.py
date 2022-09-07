from Generators.Generator import Generator
import itertools as it

class Conj2(Generator):

    def __init__(self, generator1,generator2):
        self.generator1 = generator1
        self.generator2 = generator2
        #print(self.generator1,self.generator2)
        super().__init__('CONJ2')

    def conj2Worker(self,g1, g2,state):
        q = g2.generate(state)
        res = g1.appendMapInf(q)
        return res

    def generate(self,state):
        stream = self.conj2Worker(self.generator1,self.generator2,state)
        while (True):
            try:
                if stream == []:
                    break
                current = next(stream)
                if current == None :
                    continue
                elif current != False:
                    yield current
            except StopIteration:
                break
