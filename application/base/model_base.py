from infrastructure.components import methods


class Promissory:
    def __init__(self, promissoryAmount, promissoryNote, nationalID, address, promissoryAddress,
                 promissoryDate, promissoryLastDate, promissoryNoticeDate, promissoryCourt, date):
        self.promissoryAmount = promissoryAmount
        self.promissoryNote = promissoryNote
        self.nationalID = nationalID
        self.address = address
        self.promissoryAddress = promissoryAddress
        self.promissoryDate = promissoryDate
        self.promissoryLastDate = promissoryLastDate
        self.promissoryNoticeDate = promissoryNoticeDate
        self.promissoryCourt = promissoryCourt
        self.date = date
        pass

    @classmethod
    def from_json(cls, data):
        return cls(**methods.convert_from_json(data))
