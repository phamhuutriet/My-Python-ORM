from __future__ import annotations
from enums.PredicatorEnums import PredicatorEnums
from typing import List


class Predicator:
    def __init__(
        self,
        field_name,
        comparator: PredicatorEnums,
        value,
        is_not: bool = False,
    ) -> None:
        self.field_name = field_name
        self.comparator = comparator
        self.value = value
        self.is_not = is_not
        self.is_nested = False

    def setNested(self) -> None:
        self.is_nested = True

    def convertValueToString(self) -> str:
        if isinstance(self.value, List):
            # Add "" for each string value
            for i, value in enumerate(self.value):
                if isinstance(value, str):
                    self.value[i] = f'"{value}"'
            return "(" + ",".join(str(value) for value in self.value) + ")"
        elif isinstance(self.value, str):
            return f'"{self.value}"'
        return str(self.value)

    def __str__(self) -> str:
        not_str = "NOT" if self.is_not else ""
        body = f"{not_str} {str(self.field_name)} {self.comparator.value} {self.convertValueToString()}".strip()
        return f"({body})" if self.is_nested else body

    def __eq__(self, __o: Predicator) -> bool:
        return (
            self.field_name == __o.field_name
            and self.comparator == __o.comparator
            and self.value == __o.value
            and self.is_not == __o.is_not
        )
