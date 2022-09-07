from Terms.Nested import Nested
import Terms.Term

class Variable(Terms.Term):

    def unify(self, otherTerm, substitution,state):
        u = self.walk(substitution)
        v = otherTerm.walk(substitution)

        if u.equals(v,state):
            return substitution
        elif isinstance(u,Variable) and u.index <= state.variables:
                return u.extendSubstitution(v,substitution)
        elif isinstance(v,Variable) and v.index <= state.variables:
                return v.extendSubstitution(u,substitution)
        return False

    def __init__(self, index):
        self.index = index


    def walk(self,substitution):
        if self.index in substitution:

            assv = substitution[self.index]

            if isinstance(assv,Variable):
                return assv.walk(substitution)
            else:
                return assv
        else:
            return self

    def occurs(self,term,substitution):
        term = term.walk(substitution)
        if isinstance(term,Variable):
            if self.index == term.index:
                return True
        elif isinstance(term,Nested):
            for entry in term.list:
                if isinstance(entry, Variable):
                    if self.occurs(entry, substitution):
                        return True
        return False

    def extendSubstitution(self, term, substitution):
        if self.occurs(term,substitution):
            return False
        else:
            result = dict(substitution)
            result[self.index] = term
            return result

    def equals(self,otherTerm,state):

        if isinstance(otherTerm,Variable) and otherTerm.index <= state.variables:
            if self.index == otherTerm.index:
                return True
        return False

    def toString(self):
        return "Variable: " + str(self.index)

