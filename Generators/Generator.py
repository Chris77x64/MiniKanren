from abc import ABC, abstractmethod
import itertools as it

class Generator(ABC):

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def generate(self, state):
        pass


    def interleave(self,otherGenerator,state):

        stream1 = self.generate(state)
        stream2 = otherGenerator.generate(state)

        flag1 = True
        flag2 = True

        while (True):
            if flag1:
                try:
                    current = next(stream1)
                    if current == None:
                        continue
                    elif current != False:
                        yield current
                except StopIteration:
                    flag1 = False
                    if not flag2:
                        break
            if flag2:
                try:
                    current = next(stream2)
                    if current == None:
                        continue
                    elif current != False:
                        yield current
                except StopIteration:
                    flag2 = False
                    if not flag1:
                        break




    def appendMapInf(self, sInf):
            try:
                current = next(sInf)
                return it.chain(self.generate(current), self.appendMapInf(sInf))
            except StopIteration:
                return []

    def cons(self,otherGenerator,state):
        stream1 = self.generate(state)
        while(True):
            try:
                current = next(stream1)
                if current == None:
                    continue
                elif current != False:
                    yield current
            except StopIteration:
                    break
        stream2 = otherGenerator.generate(state)
        while (True):
            try:
                current = next(stream2)
                if current == None:
                    continue
                elif current != False:
                    yield current
            except StopIteration:
                break

