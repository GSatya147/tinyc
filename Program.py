class Program:
        def __init__(self):
                self.functions = {}
        def addFunctionDetails(self,name, function):
                self.functions[name] = function

        def print(self):
                print(f"Program : ")
                for funname in self.functions.keys():
                        self.functions[funname].print()

        def getMainFunction(self):
                for funname in self.functions.keys():
                        if(funname == 'main'):
                                return self.functions[funname]
        # def getFunctionDeatils(self, name):
        #       if name in functions:
        #               return functions[name]
