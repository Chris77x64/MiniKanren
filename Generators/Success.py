from Generators.Generator import Generator
from States.State import State

class Success(Generator):

    def __init__(self):
        super().__init__('SUCC')

    def generate(self,state):
        while True:
            yield State(state.variables,state.substitution)
