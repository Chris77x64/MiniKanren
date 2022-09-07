from Generators.Generator import Generator


class Disj2(Generator):

    def __init__(self, generator1,generator2):
        self.generator1 = generator1
        self.generator2 = generator2
        super().__init__('DISJ2')

    def generate(self,state):
        if self.generator1.type == 'SUCC':
            stream = self.generator2.cons(self.generator1,state)
        elif self.generator2.type == 'SUCC':
            stream = self.generator1.cons(self.generator2, state)
        else:
            stream = self.generator1.interleave(self.generator2,state)

        while (True):
            try:
                #print(stream)
                current = next(stream)
                if current == None:
                    continue
                elif current != False:
                    yield current
            except StopIteration:
                break
