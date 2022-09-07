class State():

    def __init__(self,vars,substitution):
        self.variables = vars
        self.substitution = substitution

    def toString(self):
        if isinstance(self.substitution, bool):
            return "False"
        else:
           if len(self.substitution) == 0:
                return "EMPTY SUBSTITUTION"
        res = "NVARS: "+str(self.variables)+ " ||"
        for entry in self.substitution:
            res += str(entry)+ " "+ self.substitution[entry].toString()+ " |"
        return res
