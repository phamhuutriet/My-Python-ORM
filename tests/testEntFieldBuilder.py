from unittest import TestCase
from unittest_data_provider import data_provider
from EntSchema.EntFieldBuilder import EntFieldBuilder
from EntSchema.EntField import EntField
from enums.EntFieldEnums import EntFieldEnums


class TestEntFieldBuilder(TestCase):
    def testField(self):
        self.assertEqual(EntFieldBuilder.field(), EntFieldBuilder())

    def testBuild(self):
        self.assertEqual(
            EntFieldBuilder.field().build(), EntField(name="", type=EntFieldEnums.NULL)
        )

    def typeDataProvider():
        field_type_list = [EntFieldEnums.INT, EntFieldEnums.STRING]
        ent_field_list = [
            EntField(name="", type=EntFieldEnums.INT),
            EntField(name="", type=EntFieldEnums.STRING),
        ]
        return (
            (field_type, ent_field)
            for field_type, ent_field in zip(field_type_list, ent_field_list)
        )

    @data_provider(typeDataProvider)
    def testType(self, field_type: EntFieldEnums, ent_field: EntField):
        self.assertEqual(EntFieldBuilder.field().type(field_type).build(), ent_field)

    def nameDataProvider():
        name_list = ["Triet", "Mai"]
        ent_field_list = [EntField(name="Triet"), EntField(name="Mai")]
        return ((name, ent_field) for name, ent_field in zip(name_list, ent_field_list))

    @data_provider(nameDataProvider)
    def testName(self, name: str, ent_field: EntField):
        self.assertEqual(EntFieldBuilder.field().name(name).build(), ent_field)

    def testPrimary(self):
        self.assertEqual(
            EntFieldBuilder.field().primary().build(),
            EntField(name="", is_primary=True, is_unique=True),
        )

    def testUnique(self):
        self.assertEqual(
            EntFieldBuilder.field().unique().build(), EntField(name="", is_unique=True)
        )

    def testIntegrationTests(self):
        self.assertEqual(
            EntFieldBuilder.field().name("Triet").type(EntFieldEnums.FLOAT).build(),
            EntField(name="Triet", type=EntFieldEnums.FLOAT),
        )
        self.assertEqual(
            EntFieldBuilder.field()
            .name("Triet")
            .type(EntFieldEnums.FLOAT)
            .primary()
            .build(),
            EntField(
                name="Triet", type=EntFieldEnums.FLOAT, is_primary=True, is_unique=True
            ),
        )
        self.assertEqual(
            EntFieldBuilder.field()
            .name("Triet")
            .type(EntFieldEnums.FLOAT)
            .primary()
            .unique()
            .build(),
            EntField(
                name="Triet", type=EntFieldEnums.FLOAT, is_primary=True, is_unique=True
            ),
        )
