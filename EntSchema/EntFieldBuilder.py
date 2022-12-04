from __future__ import annotations
from EntSchema.EntField import EntField
from enums.EntFieldEnums import EntFieldEnums


class EntFieldBuilder:
    def __init__(self) -> None:
        self.field_name = ""
        self.field_type = EntFieldEnums.NULL
        self.is_primary = False
        self.is_unique = False

    @staticmethod
    def field() -> EntFieldBuilder:
        """Start the builder pattern"""
        return EntFieldBuilder()

    def build(self) -> EntField:
        """End the builder pattern, return an ent field based on the previous set up methods"""
        return EntField(
            name=self.field_name,
            type=self.field_type,
            is_primary=self.is_primary,
            is_unique=self.is_unique,
        )

    def type(self, type: EntFieldEnums) -> EntFieldBuilder:
        """Set the type of the entField"""
        self.field_type = type
        return self

    def name(self, name: str) -> EntFieldBuilder:
        """Set the name of the entField"""
        self.field_name = name
        return self

    def primary(self) -> EntFieldBuilder:
        """Set the entField to be primary key"""
        self.is_primary = True
        self.is_unique = True
        return self

    def unique(self) -> EntFieldBuilder:
        """Set the entField to be unique"""
        self.is_unique = True
        return self

    def __eq__(self, __o: EntFieldBuilder) -> bool:
        return self.field_name == __o.field_name and self.field_type == __o.field_type
