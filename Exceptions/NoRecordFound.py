class NoRecordError(Exception):
    def __init__(self, message="No record found") -> None:
        self.message = message
        super().__init__(self.message)
