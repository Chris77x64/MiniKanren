from random import random

from Generators.Conj2 import Conj2
from Generators.Disj2 import Disj2
from Generators.Equals import Equals
from Makros.CondE import CondE
from Makros.Fresh import Fresh
from Terms import Nested, Variable, Atom
from Terms.FreshVariable import FreshVariable

def cdro(p,d):
    randomString = str(random()*20000)+"cdro"
    return Fresh(1,
        [
            Equals(
                Nested([FreshVariable(1,randomString),d]),
                p)
        ], randomString)

def caro(p,a):
    randomString = str(random() * 20000)+"caro"

    return Fresh(1,
                 [
                     Equals(
                         Nested([a,FreshVariable(1,randomString)]),
                         p)
                 ], randomString)

def teacup(t):
    return Disj2(Equals(Atom('tea'),t),Equals(Atom('cup'),t))

