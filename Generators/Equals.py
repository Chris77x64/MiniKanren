from Generators.Generator import Generator
from States.State import State

class Equals(Generator):

    def __init__(self, term1,term2):
        self.term1 = term1
        self.term2 = term2
        super().__init__('EQ')

    def generate(self,state):
        result = self.term1.unify(self.term2,state.substitution,state)
        # if isinstance(result,dict):
        #     for key in result:
        #         print(result[key].toString())
        if result != False:
            yield State(state.variables,result)

    def toString(self):
        return self.term1.toString()+" || "+self.term2.toString()
