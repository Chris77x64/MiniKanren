import Terms.Term

class FreshVariable(Terms.Term):

    def __init__(self, index,identifier):
        self.index = index
        self.identifier = identifier

    def unify(self, otherTerm, substitution,state):
        pass

    def walk(self,substitution):
        pass

    def equals(self,otherTerm,state):
        pass

    def toString(self):
        return "FreshVariable: " + str(self.index)+" ID: "+str(self.identifier)

