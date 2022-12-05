from EntSchema.EntSchemaInterface import EntSchemaInterface
from enums.EntFieldEnums import EntFieldEnums


class EntClassCodegenHelper:
    def __init__(self, schema: EntSchemaInterface) -> None:
        self.schema = schema
        self.DEFAULT_VALUE_DICT = {
            EntFieldEnums.INT: 0,
            EntFieldEnums.STRING: '""',
            EntFieldEnums.FLOAT: 0.0,
        }

    def getTableDescriptionString(self) -> str:
        field_desc_list = []
        for field in self.schema.getFields():
            unique = "UNIQUE" if field.isUnique() else ""
            field_desc_list.append(
                f"{field.getName()} {field.getType().value} {unique}"
            )
        field_desc_str = ", ".join(field_desc_list)
        return f"id integer, {field_desc_str}, PRIMARY KEY (id)"

    def getInitString(self) -> str:
        set_fields_strings = []
        for field_name in self.schema.getFieldsNames():
            set_fields_strings.append(f'{field_name}=result["{field_name}"]')
        return ", ".join(set_fields_strings)

    def getInitStringWithDefault(self) -> str:
        set_fields_strings = []
        for field in self.schema.getFields():
            set_field_string = f"{field.getName()}: {field.getType().value} = {self.DEFAULT_VALUE_DICT[field.getType()]}"
            set_fields_strings.append(set_field_string)
        return ", ".join(set_fields_strings)

    def getSetFieldsString(self) -> str:
        set_fields_strings = []
        for i, field_name in enumerate(self.schema.getFieldsNames()):
            set_field_string = f"self.{field_name} = {field_name}"
            if i != 0:
                set_field_string = "        " + set_field_string
            set_fields_strings.append(set_field_string)
        return "\n".join(set_fields_strings)

    def getFieldsGetterAndSetterMethods(self) -> str:
        set_fields_strings = []
        for i, field in enumerate(self.schema.getFields()):
            is_first = i == 0
            set_fields_strings.append(
                self.getFieldGetterAndSetterMethod(
                    field.getName(), field.getType(), is_first
                )
            )
        return "\n".join(set_fields_strings)

    def getFieldGetterAndSetterMethod(
        self, field_name: str, field_type: EntFieldEnums, is_first: bool
    ) -> str:
        uppercase_field_name = field_name[0].upper() + field_name[1:].lower()
        first_tab = "    "
        if is_first:
            first_tab = ""
        getter_s = f"""{first_tab}def get{uppercase_field_name}(self) -> {field_type.value}:
        return self.{field_name}
        """
        setter_s = f"""    def set{uppercase_field_name}(self, {field_name}: {field_type.value}) -> None:
        self.{field_name} = {field_name}
        """
        return getter_s + "\n" + setter_s
