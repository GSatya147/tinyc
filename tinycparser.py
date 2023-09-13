from sly import Parser
from tinyclexer import tinyclexer
from argparse import ArgumentParser
from Ast import *
from SymbolTable import *
from Program import *
from Function import *
class tinycparser(Parser):
        tokens = tinyclexer.tokens
        literals = tinyclexer.literals
        memory = {}
        lst = []
        localsymboltable = SymbolTable()
        prog = Program()
        @_(' TYPE ID "(" ")" "{" statements "}" ')
        def program(self,value):
                fun = Function(value.TYPE,value.ID)
                fun.setStatementsAstList(value.statements)
                fun.setLocalSymbolTable(self.localsymboltable)
                self.prog.addFunctionDetails(value.ID,fun)
                self.prog.print()
        @_(' TYPE ')
        def return_type(self,value):
                return value[0]
        @_(' statement ";" statements ')
        def statements(self,value):
                return value.statements
        @_(' statement ";" ')
        def statements(self,value):
                return value.statement
        @_('dec_st')
        def statement(self,value):
                pass
        @_('ass_st','print_st')
        def statement(self,value):
                self.lst.append(value[0])
                return self.lst
        @_(' return_type list_var')
        def dec_st(self,value):
                for i in value.list_var:
                        obj = SymbolTableEntry(i,value.return_type)
                        self.localsymboltable.addSymbol(obj)
        @_(' ID "," list_var ')
        def list_var(self,value):
                return [value.ID]+value.list_var
        @_(' ID ')
        def list_var(self,value):
                return [value.ID]
        @_(' ID "=" ID')
        def ass_st(self,value):
                symentry = self.localsymboltable.getSymbolInTable(value.ID0)
                left = NameAst(symentry)
                symentry = self.localsymboltable.getSymbolInTable(value.ID1)
                right = NameAst(symentry)
                return AssignAst(left,right)
        @_(' ID "=" CONSTANT ')
        def ass_st(self,value):
                symentry = self.localsymboltable.getSymbolInTable(value.ID)
                left = NameAst(symentry)
                right = NumberAst(value.CONSTANT)
                return AssignAst(left,right)
        @_(' PRINT ID ')
        def print_st(self,value):
                symentry = self.localsymboltable.getSymbolInTable(value.ID)
                name = NameAst(symentry)
                return PrintAst(name)
lexobj = tinyclexer()
parseobj = tinycparser()
argobj = ArgumentParser()
argobj.add_argument('filename')
argobj.add_argument('-t',nargs=1)
arg = argobj.parse_args()
with open(arg.filename) as f:
        exp = f.read()
if arg.t:
        with open(arg.t[0],'w') as f:
                for token in lexobj.tokenize(exp):
                        f.write(f"type : {token.type}      ,   value : {token.value}\n")
parseobj.parse(lexobj.tokenize(exp))
