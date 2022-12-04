from __future__ import annotations
from enums.EntFieldEnums import EntFieldEnums


class EntField:
    def __init__(
        self,
        name: str,
        type: EntFieldEnums = EntFieldEnums.NULL,
        is_primary: bool = False,
        is_unique: bool = False,
    ) -> None:
        self.name = name
        self.type = type
        self.is_primary = is_primary
        self.is_unique = is_unique

    def getName(self) -> str:
        return self.name

    def __eq__(self, __o: EntField) -> bool:
        return self.__dict__ == __o.__dict__
