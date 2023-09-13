from sly import Lexer
class tinyclexer(Lexer):
        literals = {'+','-','*','/','=','(',')','{','}',',',';'}
        tokens = {TYPE,ID,PRINT,CONSTANT}
        ignore = ' \t\n'
        ignore_comment = '\#.*'
        ID = r'[a-zA-Z][a-zA-Z_]*'
        ID['print'] = PRINT
        ID['int'] = TYPE
        CONSTANT = r'[0-9]+'
        def CONSTANT(self,t):
                t.value = int(t.value)
                return t
