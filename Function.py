from SymbolTable import SymbolTable
class Function:
        def __init__(self, returnType, name):
                self.returnType = returnType
                self.name       = name
                self.statementsAstList = []
                self.localSymbolTable = SymbolTable()
        def setStatementsAstList(self, sastList):
                self.statementsAstList = sastList
        def getStatementsAstList(self):
                return self.statementsAstList
        def setLocalSymbolTable(self,localList):
                self.localSymbolTable = localList
        def getLocalSymbolTable(self):
                return self.localSymbolTable
        def print(self):
                print(f"\tProcedure : {self.name} , Return Type : {self.returnType}")
                for i in self.statementsAstList:
                        i.print()
