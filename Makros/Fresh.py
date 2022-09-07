from Generators.Conj2 import Conj2
from Generators.Disj2 import Disj2
from Generators.Equals import Equals
from Generators.Generator import Generator
from Generators.Ifte import Ifte
from Makros.CondE import CondE
from States.State import State
from Terms import Variable, Nested
from Terms.FreshVariable import FreshVariable


class Fresh(Generator):

    def __init__(self,num, list,identifier):
        self.num = num
        self.list = list
        self.length = len(list)
        self.identifier = identifier
        super().__init__('CONDE')


    def worker(self,index,previousVariables):

        currentGenerator = self.list[index]
        # print('BEVORE')
        # print(currentGenerator.generator1)
        # print(currentGenerator.generator1.term1.toString())
        # print(currentGenerator.generator1.term2.toString())
        # print(currentGenerator.generator2)
        # print(currentGenerator.generator2.term1.toString())
        # print(currentGenerator.generator1.term2.toString())
        self.freshGenerator(currentGenerator,previousVariables)
        # print('After')
        # print(currentGenerator.generator1)
        # print(currentGenerator.generator1.term1.toString())
        # print(currentGenerator.generator1.term2.toString())
        # print(currentGenerator.generator2)
        # print(currentGenerator.generator2.term1.toString())
        # print(currentGenerator.generator1.term2.toString())

       # print(currentGenerator)
       # print(currentGenerator.term1.toString(),currentGenerator.term2.toString())

        if index == self.length-1:

            return currentGenerator
        else:
            return Conj2(currentGenerator,self.worker(index+1,previousVariables))

    def test(self,state):
        #print(state.substitution)
        #for key in state.substitution:
            #state.substitution[key] = self.freshTerm( state.substitution[key],state)
           # print(state.substitution[key].toString())
        pass


    def viewGenerator(self,currentGenerator):


        if isinstance(currentGenerator, Equals):
            pass
            #print(currentGenerator.term1.toString())
            #print(currentGenerator.term2.toString())
        elif isinstance(currentGenerator, Conj2) or isinstance(currentGenerator, Disj2):
            self.viewGenerator(currentGenerator.generator1)
            self.viewGenerator(currentGenerator.generator2)
        elif isinstance(currentGenerator, Ifte):
            self.viewGenerator(currentGenerator.generator1)
            self.viewGenerator(currentGenerator.generator2)
            self.viewGenerator(currentGenerator.generator3)
        elif isinstance(currentGenerator, CondE):
            for generator in currentGenerator.list:
                self.viewGenerator(generator)
        elif isinstance(currentGenerator,Fresh):
            for generator in currentGenerator.list:
                self.viewGenerator(generator)



    def freshGenerator(self,currentGenerator,previousVariables):

        #print(currentGenerator)

        if isinstance(currentGenerator, Equals):
            #print(currentGenerator.term1.toString())
            currentGenerator.term1 = self.freshTerm(currentGenerator.term1,previousVariables)
            #print(currentGenerator.term1.toString())
            currentGenerator.term2 = self.freshTerm(currentGenerator.term2,previousVariables)
        elif isinstance(currentGenerator, Conj2) or isinstance(currentGenerator, Disj2):
            self.freshGenerator(currentGenerator.generator1,previousVariables)
            self.freshGenerator(currentGenerator.generator2, previousVariables)
        elif isinstance(currentGenerator, Ifte):
            self.freshGenerator(currentGenerator.generator1, previousVariables)
            self.freshGenerator(currentGenerator.generator2, previousVariables)
            self.freshGenerator(currentGenerator.generator3, previousVariables)
        elif isinstance(currentGenerator, CondE):
            for generator in currentGenerator.list:
                self.freshGenerator(generator, previousVariables)
        elif isinstance(currentGenerator,Fresh):
            for generator in currentGenerator.list:
                self.freshGenerator(generator, previousVariables)



    def maxIncrement(self):
        pass



    def freshTerm(self,term,previousVariables):

        if isinstance(term, FreshVariable):
            if term.identifier == self.identifier:
                var = Variable(term.index + previousVariables)
                return var
            else:
                return term
        elif isinstance(term, Nested):
            res = []
            for i in term.list:
                if isinstance(i, FreshVariable):
                    if i.identifier == self.identifier:
                        var = Variable(i.index + previousVariables)
                        res.append(var)
                    else:
                        res.append(i)
                else:
                    res.append(i)
            return Nested(res)
        else:
            return term

    def generate(self,state):
        numvars = state.variables
        state = State(state.variables+self.num,state.substitution)
        newGoal = self.worker(0,numvars)
        self.viewGenerator(newGoal)

        #print('------------------------')
#        print(newGoal.term1.toString())
  #      print(newGoal.term2.toString())
   #     print(state.toString())
       # print('------------------------')


        stream = newGoal.generate(state)

        while (True):
            try:
                current = next(stream)
                if current == None:
                    continue
                elif current != False:
                    yield current
            except StopIteration:
                break

    def toString(self):
        return str(self.list)