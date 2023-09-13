from enum import Enum
from abc import *
from SymbolTable import SymbolTable
from SymbolTable import SymbolTableEntry

DataType = Enum('DataType',['INT','DOUBLE'])

class AST(metaclass=ABCMeta):
        @abstractmethod
        def print(self):
                pass
        def typeCheckAST(self):
                pass
        def getDataType(self):
                pass

class NumberAst(AST):
        def __init__(self, number):
                self.value = number
        def print(self):
                print("Num : ",self.value,end="")
        def getDataType(self):
                return type(self.value)


class NameAst(AST):
        def __init__(self, symbolEntry):
                self.symbolEntry = symbolEntry
        def print(self):
                print("Name : ",self.symbolEntry.getSymbolName(),end="")
        def getDataType(self):
                return symbolEntry.getDataType()

class AssignAst(AST):
        def __init__(self,left,right):
                self.left = left
                self.right = right
        def typeCheckAST(self):
                if(left.getDataType()== right.getDataType()):
                        return True
                else:
                        return False
        def print(self):
                print("\t\tAsgn : ")
                print("\t\t\tLHS (",end="")
                self.left.print()
                print(")")
                print("\t\t\tRHS (",end="")
                self.right.print()
                print(")")

class PrintAst(AST):
        def __init__(self,symbolEntry):
                self.symbolEntry= symbolEntry
        def print(self):
                print("\t\tPrint : ")
                print("\t\t\t(",end="")
                self.symbolEntry.print()
                print(")")
