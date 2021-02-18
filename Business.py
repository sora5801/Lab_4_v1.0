from SQLdatabase import SQLdatabase

class Business:
    def __init__(self):
        self.SQ = SQLdatabase()
        self.SQ.UNTable()
        self.SQ.insertUNData()