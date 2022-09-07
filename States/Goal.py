from Terms import Nested


class Goal():

    def __init__(self,generator,state):
        self.generator = generator
        self.state = state

    def takeInf(self,n, sInf):
        if n == 0:
            return []
        else:
            try:
                current = next(sInf)
                if current != False:
                    # wont be practical because of limited recursion depth but yeah it works...
                    return [current] + self.takeInf(n - 1, sInf)
                else:
                    return self.takeInf(n - 1, sInf)
            except StopIteration:
                return []


    def runGoal(self,n):
        return self.takeInf(n, self.generator.generate(self.state))

    def printGoal(self,n):
        list = self.runGoal(n)
        for element in list:
            print(element.toString())
            print('______________________')