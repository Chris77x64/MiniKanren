from Generators.Generator import Generator

class Ifte(Generator):

    def __init__(self, generator1,generator2,generator3):
        self.generator1 = generator1
        self.generator2 = generator2
        self.generator3 = generator3
        super().__init__('IFTE')


    def generate(self,state):
        stream = self.generator1.generate(state)
        while (True):
            try:
                current = next(stream)
                if current != False:
                    return self.generator2.appendMapInf(self.generator1.generate(state))
                else:
                    return self.generator3.generate(state)
            except StopIteration:
                return self.generator3.generate(state)


