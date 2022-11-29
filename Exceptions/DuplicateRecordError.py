class DuplicateRecordError(Exception):
    def __init__(
        self, message="This record is already inserted to the database"
    ) -> None:
        self.message = message
        super().__init__(self.message)
