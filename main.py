class Cars(object):
    def __init__(self,name,company,type,model,speedlimit,color):
        self.name=name
        self.company=company
        self.type=type
        self.model=model
        self.speedlimit=speedlimit
        self.color=color

    def start(self):
        print(self.name + " has started")
    def stop(self):
        print(self.name + " has stoped")
Audi=Cars("R8 Matte","Audi","Classic Sport","ABCD","312","Black")
Ford=Cars("Gt Mustang","Ford","super luxury","ABCD","214","Chormic Green")
print(Ford.start())
print(Ford.stop())
print(Ford.speedlimit)