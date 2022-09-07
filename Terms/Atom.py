from Terms.Variable import Variable
import Terms.Term

class Atom(Terms.Term):

    def __init__(self, value):
        self.value = value

    def unify(self, otherTerm, substitution,state):
        v = otherTerm.walk(substitution)

        if self.equals(v,state):
            return substitution
        elif isinstance(v,Variable) and v.index <= state.variables:
            return v.extendSubstitution(self,substitution)
        return False

    def walk(self,substitution):
        return self

    def equals(self,otherTerm,state):
        if isinstance(otherTerm,Atom):
            if self.value == otherTerm.value:
                return True
        return False

    def toString(self):
        return " Atom: " +str(self.value)

