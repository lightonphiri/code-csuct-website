from Person import Person
class Doctor(Person):
    def __init__(self,doc_id=None,doc_address=None,n="unknown",a=0):
        Person.__init__(self,n,a)
        self.doc_id=doc_id
        self.doc_address=doc_address
    def __str__(self):
        return str(self.name)+","+str(self.age)+","+str(self.doc_id)+","+str(self.doc_address)
    
