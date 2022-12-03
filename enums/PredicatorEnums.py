from enum import Enum


class PredicatorEnums(Enum):
    # IN A CONDITION
    EQUAL = "="
    LIKE = "LIKE"
    IN = "IN"
    GREATER_THAN = ">"
    GREATER_THAN_OR_EQUAL = ">="
    LOWER_THAN = "<"
    LOWER_THAN_OR_EQUAL = "<="

    # BETWEEN CONDITIONS
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
