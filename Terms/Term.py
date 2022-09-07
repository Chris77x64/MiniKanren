from abc import ABC, abstractmethod

class Term(ABC):

    @abstractmethod
    def unify(self,otherTerm,substitution,state):
        pass

    @abstractmethod
    def walk(self,substitution):
        pass

    @abstractmethod
    def toString(self):
        pass

    @abstractmethod
    def equals(self,otherTerm,state):
        pass