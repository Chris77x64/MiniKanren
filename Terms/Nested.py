import Terms.Term,Terms.Variable


class Nested(Terms.Term):

    def unify(self, otherTerm, substitution,state):
        v = otherTerm.walk(substitution)

        if self.equals(v,state):
            return substitution
        elif isinstance(v, Terms.Variable) and v.index <= state.variables:
            return v.extendSubstitution(self,substitution)
        elif isinstance(v,Nested):
            return self.unifyWorker(v,substitution,state)
        return False

    def __init__(self, terms):
        self.list = terms
        self.length = len(terms)

    def unifyWorker(self,v,substitution,state):
        l1 = self.length
        l2 = v.length
        if l1 == l2:
            for (s,o) in zip(self.list,v.list):
                substitution = s.unify(o, substitution,state)
                if not isinstance(substitution, dict):
                    return False
            return substitution
        elif l1 > l2:
            for i in range(0,l2-1):
                substitution = self.list[i].unify(v.list[i], substitution, state)
                if not isinstance(substitution, dict):
                    return False
            return Nested(self.list[l2-1:l1]).unify(v.list[l2-1], substitution, state)
        else:
            for i in range(0,l1-1):
                substitution = self.list[i].unify(v.list[i], substitution, state)
                if not isinstance(substitution, dict):
                    return False
            return self.list[l1-1].unify(Nested(v.list[l1-1:l2]), substitution, state)

    def walk(self,substitution):
        return self

    def equals(self,otherTerm,state):
        if isinstance(otherTerm,Nested):
            if len(otherTerm.list) == self.length:
                representation = set( (element.toString()) for element in self.list)
                difference = [x for x in otherTerm.list if (x.toString()) not in representation]
                if len(difference) > 0:
                    return False
                else:
                    return True
        return False

    def toString(self):
        return '-'.join([elem.toString() for elem in self.list])