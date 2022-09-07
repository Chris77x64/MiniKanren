from Generators.Generator import Generator
from States.State import State

class Fail(Generator):

    def __init__(self):
        super().__init__('FAIL')

    def generate(self,state):
        if False:
            yield State(0,{})