from Generators.Conj2 import Conj2
from Generators.Disj2 import Disj2
from Generators.Equals import Equals
from Generators.Fail import Fail
from Generators.Ifte import Ifte
from Generators.Success import Success
from Makros.CondE import CondE
from Makros.Fresh import Fresh
from States.Goal import Goal
from States.Relations import caro, cdro
from States.State import State
from Terms.FreshVariable import FreshVariable
from Terms.Variable import Variable
from Terms.Nested import Nested
from Terms.Atom import Atom


def walkTests():
    t1 = Variable(3).walk(
        {
            3: Atom('a'),
            1: Variable(6),
            2: Variable(3)
        }
    )
    print(t1.toString())

    t2 = Variable(2).walk(
        {
            3:Atom('a'),
            1:Variable(6),
            2:Variable(3)
         }
    )
    print(t2.toString())

    t3 = Variable(1).walk({
        3: Atom('a'),
        1: Variable(6),
        2: Variable(3)
    })
    print(t3.toString())

    t4 = Variable(1).walk({
        1: Variable(6),
        6: Nested([Variable(2), Atom('e'), Variable(3)])
    })
    print(t4.toString())

    t5 = Variable(1).walk({
        3: Atom('a'),
        1: Variable(6),
        2: Atom('b'),
        6: Nested([Variable(2),Atom('e'),Variable(3)])
    })
    print(t5.toString())



def occursTest():

    o1 = Variable(1).occurs(Variable(2),{
        2 : Variable(1)
    })
    print(o1)

    o2 = Variable(3).occurs(Variable(2),{
        2 : Variable(1)
    })
    print(o2)

    o3 = Variable(1).occurs(Variable(1),{
    })
    print(o3)

    o4 = Variable(2).occurs(Variable(3),{
        1: Variable(2),
        6: Atom('w'),
        3: Variable(1)
    })
    print(o4)

    o5 = Variable(2).occurs(Variable(6),{
        1: Variable(2),
        6: Atom('w'),
        3: Variable(1)
    })
    print(o5)

    o6 = Variable(2).occurs(Variable(1),{
        1: Nested([Atom('a'),Variable(2)]),
        3: Variable(4)
    })

    print(o6)

    o7 = Variable(2).occurs(Nested([Variable(1),Atom('b')]),{
        1: Nested([Atom('a'),Variable(2)]),
        3: Variable(6)
    })
    print(o7)

    o8 = Variable(2).occurs(Nested([Atom('b'),Atom('b')]),{
        1: Nested([Atom('a'),Variable(2)]),
        3: Variable(6)
    })
    print(o8)

def extendSubstitutionTest():
    e1 = Variable(1).extendSubstitution(Variable(2),{
        2 : Variable(1)
    })
    print(e1)
    e2 = Variable(1).extendSubstitution(Nested([Variable(2)]), {
        2: Variable(1)
    })
    print(e2)
    e3 = Variable(1).extendSubstitution(Variable(3),{
        2: Variable(1)
    })
    print('-------------------')
    printDict(e3)
    e4 = Variable(1).extendSubstitution(Atom('e'),{
        3: Variable(1),
        2: Variable(3)
    })
    print(Variable(3).walk(e4).toString())
    e5 = Variable(1).extendSubstitution(Nested([Variable(3),Atom('a')]),{
        2: Variable(1)
    })
    print('-------------------')
    printDict(e5)
    e7 = Variable(1).extendSubstitution(Nested([Variable(3),Variable(2)]),{
        2: Variable(1)
    })
    print(e7)



def printDict(dict):
    print("------------------")
    if isinstance(dict,bool):
        print("False")
    else:
        if len(dict) == 0:
            print("EMPTY SUBSTITUTION")
        else:
            for entry in dict:
                print(entry,dict[entry].toString())




def generatorStreamTestCases():
    t1 = Success()
    t2 = t1.generate(State(0, {1: Atom('A')}))

    asd = next(t2)
    print(asd.toString())

    asd = next(t2)
    print(asd.toString())

    asd = next(t2)
    print(asd.toString())

def generatorTest2():

    t1= Equals(Variable(1),Atom('W'))
    t2 = Equals(Variable(4),Atom('A'))
    t3 = Equals(Variable(1), Atom('A'))
    t4 = Equals(Variable(3), Atom('u'))


    #dt = Disj2(t1,t2)#.generate(State(5,{}))
    #dt2 = Disj2(t3, t4)
    #dt3= Disj2(dt,dt2).generate(State(5,{9: Atom('Y')}))

    #print(next(dt3).toString())
    #print(next(dt3).toString())
    #print(next(dt3).toString())
    #print(next(dt3).toString())

    test = t1.cons(t3,State(5,{}))



    #test = t1.cons(Success(), State(5, {}))
    #print(next(test).toString())
    #print(next(test).toString())
    #print(next(test).toString())

    #test = Success().cons(t1, State(5, {}))
    #print(next(test).toString())
    #print(next(test).toString())
    #print(next(test).toString())


def conj2Test():
    t1 = Equals(Variable(1), Atom('W'))
    t2 = Equals(Variable(4), Atom('A'))
    test1 = Conj2(t1,t2).generate(State(5,{1: Atom('W')}))
    print(next(test1).toString())


    t3 = Equals(Nested([Atom('B'), Variable(1)]),Nested([Atom('B'), Atom('C')]))
    t4 = Equals(Nested([Variable(2),Atom('C')]),Nested([Atom('B'), Atom('C')]))

    test2 = Conj2(t3, t4).generate(State(5, {}))
    print(next(test2).toString())

def ifteTest():
    condition1 = Equals(Variable(1),Atom('butterfly'))
    caseif1 = Equals(Variable(4), Atom(['cat']))
    caseelse1 = Equals(Variable(5), Atom(['dog']))
    stream1 = Ifte(condition1, caseif1, caseelse1).generate(State(5,{}))

    print(next(stream1).toString())

    condition2 = Equals(Variable(1),Atom('butterfly'))
    caseif2 = Equals(Variable(4), Atom(['cat']))
    caseelse2 = Equals(Variable(5), Atom(['dog']))
    stream2 = Ifte(condition2, caseif2, caseelse2).generate(State(5,{1:Atom('Lemon')}))
    print(next(stream2).toString())


def runGoalTest():
    G1 = Disj2(Disj2(
        Equals(Nested([Atom('Olive'),Variable(2)]), Nested([Variable(1),Atom('Apple'),])),
        Equals(Nested([Atom('Oil'), Variable(2)]), Nested([Variable(1), Atom('Panda'), ]))
                ),
               Equals(
                   Nested([Atom('Pie'),Variable(2)]),
                   Nested([Variable(1),Atom('Lemon')])))

    g = Goal(G1,State(5,{}))
    g.printGoal(20)

def firstLawOfEqual():
    Goal(Equals(Variable(1),Atom('pea')),State(5,{})).printGoal(2)
    Goal(Equals( Atom('pea'),Variable(1)), State(5, {})).printGoal(2)

def conjTest():
    #Goal(Conj2(Success(),Equals(Variable(1),Atom('pea'))),State(5,{})).printGoal(2)
    #Goal(Conj2(Fail(), Equals(Variable(1), Atom('pea'))), State(5, {})).printGoal(2)


    Goal(
        Disj2(
            Conj2(
                Equals(Atom('V'),Variable(1)),
                Fail()),
        Disj2(
            Equals(Atom('Olive'),Variable(1)),
            Disj2(
                Success(),
                Equals(Atom('Oil'),Variable(1))
                )
        )), State(5, {})).printGoal(2)





def caroTest():

    Goal(caro(Nested([Atom('A'), Atom('C'), Atom('O'), Atom('R'), Atom('N')]), Variable(1)), State(1, {})).printGoal(2)
    #Goal(cdro(Nested([Atom('A'), Atom('C'), Atom('O'), Atom('R'), Atom('N')]), Variable(1)), State(1, {})).printGoal(2)

    # Goal( Conj2(
    #     caro(Variable(2), Variable(1)),
    #     cdro(Nested([Atom('A'), Atom('C'), Atom('O'), Atom('R'), Atom('N')]), Variable(2))
    # ),State(2,{})
    # ).printGoal(2)






def main():

    caroTest()

    #goal = Equals(Nested([Atom('B'), Variable(1)]),Nested([Atom('B'), Atom('C'),Atom('X')]))
    #Goal(goal,State(1,{})).printGoal(1)


    #
    # goal2 = Success()
    # Goal(goal, State(0, {})).printGoal(10)
    #
    # Equals(
    #     Atom('pea'),
    #     Variable(1) )
    #
    # Equals(
    #     Nested([Atom('B'), Variable(1)]),
    #     Nested([Atom('B'), Atom('C'), Atom('X')]   ))
    #
    # Equals( Atom('pea'), Variable(1))
    #
    # Goal(Equals(Atom('pea'), Variable(1)), State(5, {})).printGoal(2)


    #
    # Conj2(
    #     Equals(Variable(1), Atom('W')),
    #     Equals(Variable(2), Atom('A')))
    #
    # Disj2(
    #     Equals(Variable(1),Atom('W')),
    #     Equals(Variable(1),Atom('A')))
    #
    # Disj2(
    #     Conj2(
    #         Equals(Atom('V'), Variable(1)),
    #         Fail()),
    #     Disj2(
    #         Equals(Atom('Olive'), Variable(1)),
    #         Disj2(
    #             Success(),
    #             Equals(Atom('Oil'), Variable(1))
    #         )))
    #
    #
    # G1 = Equals(Atom('Split'),Variable(1))
    # G2 = Equals(Atom('Pea'), Variable(2))
    # G3 = Equals(Atom('Red'), Variable(1))
    # G4 = Equals(Atom('Bean'), Variable(2))
    #
    # generator = Disj2(
    #     Conj2(
    #         Equals(Atom('Split'),Variable(1)),
    #         Equals(Atom('Pea'), Variable(2))),
    #     Conj2(
    #         Equals(Atom('Red'), Variable(1)),
    #         Equals(Atom('Bean'), Variable(2))))
    #
    # Goal(generator,
    #      State(
    #          3,
    #         {3: Atom('Oil')} )
    #      ).printGoal(2)
    #
    #
    # caseif1 = Equals(Variable(1),Atom('butterfly'))
    # casethen1 = Equals(Variable(2), Atom('cat'))
    # caseelse1 = Equals(Variable(1), Atom('dog'))
    # generator = Ifte(caseif1, casethen1, caseelse1)
    #
    # Goal(generator,
    #      State(
    #          2,
    #          {} )
    #      ).printGoal(2)


    # G1 = Equals(Atom('Split'),Variable(1))
    # G2 = Equals(Atom('Pea'), Variable(2))
    # G3 = Equals(Atom('Red'), Variable(1))
    # G4 = Equals(Atom('Bean'), Variable(2))
    #
    # Goal(
    #     CondE([G1,G2,G3,G4]),State(2,{})
    # ).printGoal(2)


    # g1 = Conj2(
    #      Equals(Atom('Split'),FreshVariable(1,'id')),
    #      Equals(Atom('Pea'), FreshVariable(2, 'id'))
    #  )
    #
    # g2 = Conj2(
    #      Equals(Atom('Red'),FreshVariable(1,'id')),
    #      Equals(Atom('Bean'), FreshVariable(2, 'id'))
    #  )
    #
    # g3 = Equals( Nested([FreshVariable(1,'id'),FreshVariable(2, 'id'),Atom('Soup')]),Variable(1))
    #
    # generator = Fresh(2, [Disj2(g1,g2),g3], 'id')
    #
    # Goal(
    #     generator,
    #     State(1,{})).printGoal(2)
    #
    # Goal(
    #    caro(
    #        Nested([Atom('A'), Atom('C'), Atom('O'), Atom('R'), Atom('N')]),
    #        Variable(1)),
    #    State(1, {})).printGoal(1)
    #
    # Goal(
    #     cdro(
    #         Nested([Atom('A'), Atom('C'), Atom('O'), Atom('R'), Atom('N')]),
    #         Variable(1)),
    #    State(1, {})).printGoal(1)

#Goal(Fresh(1,
     #          [
      #             caro(FreshVariable(1, 'v'), Variable(1)),
       #            cdro(Nested([Atom('A'), Atom('C'), Atom('O'), Atom('R'), Atom('N')]), FreshVariable(1,'v'))
        #           ],'v'), State(2, {})).printGoal(2)

if __name__ == "__main__":
    main()


