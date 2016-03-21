class Appointment:
    def __init__(self,doc_id_number=None,pat_idnumber=None,timestamp=None,memo=None):
        self.pat_idnumber=pat_idnumber
        self.doc_id_number=doc_id_number
        self.timestamp=timestamp
        self.memo=memo
    def __str__(self):
        return str(self.doc_id_number)+","+str(self.pat_idnumber)+","+str(self.timestamp)+","+self.memo
    