from tabulate import tabulate

class Formula(object):
    pass

class Value(Formula):
    def __init__(self,value):
        self.value=value
    def __repr__(self):
        return "Value(" + repr(self.value) + ")"
    def variables(self):
        return set()
    def evaluate(self,values):
        return self.value
    
class Variable(Formula):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "Variable(" + repr(self.name) + ")"
    def variables(self):
        return {self.name}
    def evaluate(self,values):
        return values[self.name];
    
class And(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "And(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return self.first.evaluate(values) and self.second.evaluate(values)

class Nand(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Nand(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return not (self.first.evaluate(values) and self.second.evaluate(values))

class Or(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Or(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return self.first.evaluate(values) or self.second.evaluate(values)

class Implies(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Implies(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return (not self.first.evaluate(values)) or (self.second.evaluate(values))

class Not(Formula):
    def __init__(self,sub):
        self.sub=sub
    def __repr__(self):
        return "Not(" + repr(self.sub) + ")"
    def variables(self):
        return self.sub.variables()
    def evaluate(self,values):
        return not self.sub.evaluate(values)
        
class Iff(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Iff(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return ((self.first.variables() and self.second.variables()) or (not self.first.variables() and not self.second.variables()))

class Xor(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Xor(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return (not self.first.evaluate(values) and self.second.evaluate(values)) or (self.first.evaluate(values) and not self.second.evaluate(values))

class Xnor(Formula):
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def __repr__(self):
        return "Xnor(" + repr(self.first) + "," + repr(self.second) + ")"
    def variables(self):
        return self.first.variables().union(self.second.variables())
    def evaluate(self,values):
        return not ((not self.first.evaluate(values) and self.second.evaluate(values)) or (self.first.evaluate(values) and not self.second.evaluate(values)))

# listAllPossibleValues takes a list of variable names, it returns a list of pairs,
#   giving all possible combinations of True/False values for the given variables
#   Each list can be converted to a dictionary by passing it to dict(),
#   and then passed to the evaluate() method defined above.

def listAllPossibleValues(varlist):
    if varlist==[]:
        return [[]]
    else:
        firstvar, restvars = varlist[0], varlist[1:]
        restValues = listAllPossibleValues(restvars)
        prependTrue = [[(firstvar,True)] + r for r in restValues]
        prependFalse = [[(firstvar,False)] + r for r in restValues]
        return prependTrue + prependFalse

def truthValues(formula):
    return [formula.evaluate(dict(vals))
            for vals in listAllPossibleValues(list(formula.variables()))]

# truthTable(formula) returns the truth table of the provided formula
def truthTable(formula):
    variableList=list(formula.variables())
    variableList.sort()
    headers = variableList+[str(formula)]
    rows = [[v[1] for v in vals] + [formula.evaluate(dict(vals))]
             for vals in listAllPossibleValues(variableList)]
    return tabulate(rows, headers=headers)

def isTautology(formula):
    for i in truthValues(formula):
        if not i:
            return False
    return True
         
def isContradiction(formula):
    for i in truthValues(formula):
        if i:
            return False
    return True

def isSatisfiable(formula):
    if not isContradiction(formula):
        return True
    return False

# to DNF(formula) returns the Disjunctive Normal Form of the given formula
# Disjunctive Normal Form (DNF) => "sum of products"
def toDNF(formula):
    variableList=list(formula.variables())
    variableList.sort()
    rows = [[v[1] for v in vals] + [formula.evaluate(dict(vals))]
             for vals in listAllPossibleValues(variableList)]
    num_vars = len(variableList)
    dnf_arr = []
    dnf_str = "("

    # get variable values where output is True
    for i in range(0, len(rows)):
        if rows[i][num_vars]:
            dnf_arr.append(rows[i])
    
    # remove the output variable from end of each subarray
    for i in range(0, len(dnf_arr)):
        dnf_arr[i].pop()
    
    # convert dnf_arr T/F values to variable / not variable
    for i in range(0, len(dnf_arr)):
        for j in range(0, num_vars):
            if dnf_arr[i][j]:
                dnf_arr[i][j] = variableList[j]
            if not dnf_arr[i][j]:
                dnf_arr[i][j] = "not " + variableList[j]
            #convert array to string, add connectives
            if j<num_vars-1:
                dnf_str = dnf_str + dnf_arr[i][j] + " AND "
            elif i<len(dnf_arr)-1:
                dnf_str = dnf_str + dnf_arr[i][j] + ") OR ("
            else: 
                dnf_str = dnf_str + dnf_arr[i][j] + ")" 

    return dnf_str

# toCNF(formula) returns the Conjuctive Normal Form of the given formula
# Conjunctive Normal Form (CNF) => "product of sums"
def toCNF(formula):
    variableList=list(formula.variables())
    variableList.sort()
    rows = [[v[1] for v in vals] + [formula.evaluate(dict(vals))]
             for vals in listAllPossibleValues(variableList)]
    num_vars = len(variableList)
    cnf_arr = []
    cnf_str = "("

    # get variable values where output is False
    for i in range(0, len(rows)):
        if not rows[i][num_vars]:
            cnf_arr.append(rows[i])
    
    # remove the output variable from end of each subarray
    for i in range(0, len(cnf_arr)):
        cnf_arr[i].pop()
    
    # convert cnf_arr T/F values to variable / not variable
    for i in range(0, len(cnf_arr)):
        for j in range(0, num_vars):
            if cnf_arr[i][j]:
                cnf_arr[i][j] = variableList[j]
            if not cnf_arr[i][j]:
                cnf_arr[i][j] = "not " + variableList[j]
            #convert array to string, add connectives
            if j<num_vars-1:
                cnf_str = cnf_str + cnf_arr[i][j] + " OR "
            elif i<len(cnf_arr)-1:
                cnf_str = cnf_str + cnf_arr[i][j] + ") AND ("
            else: 
                cnf_str = cnf_str + cnf_arr[i][j] + ")" 

    return cnf_str

            
myformula=And(Implies(Variable('p'),Variable('q')),
             Implies(Variable('p'),Variable('r')))

#myformula=Xor(Variable('p'),Variable('q'))

print(truthTable(myformula))
print()
print("DNF:", toDNF(myformula))
print("CNF:", toCNF(myformula))



