from john import TestCase

from .schematic import Schematic
from .kicad import parse_sexpr, build_sexpr

schematic_data = ['kicad_sch',
                  ['version', '20211123'], ['generator', 'eeschema'],
                  ]


class TestSchematic(TestCase):
    def test_init_with_None_raises(self):
        with self.assertRaisesAny():
            Schematic()

    def test_init_with_wrong_tag_raises(self):
        data = ['ZZ9PZA', ['version', '20211123'], ['generator', 'eeschema']]

        with self.assertRaisesAny():
            Schematic(data)


data = ['kicad_sch',
        ['version', '20211123'],
        ['generator', 'eeschema'],
        ['symbol',
         ['lib_id', 'power:GND'],
         ['at',  168.91, 93.98, 0],
         ['unit', 1],
         ['in_bom', 'yes'],
         ['on_board', 'yes'],
         ['uuid', '18af9582-7c92-46f1-9603-90a0db4828ae'],
         ['property', 'Reference', 'REF1',
          ['id', 1], ['at', 168.91, 100.33, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Value', 'GND', ['id', 1], ['at', 169.037, 98.3742, 0]],
         ['property', 'Footprint', '', ['id', 2], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Datasheet', '', ['id', 3], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['pin', '1', ['uuid', '0462adc4-54a7-4c18-967e-f6d78a20207f']],
         ['pin', '2', ['uuid', 'ab6930b8-e44b-4fa6-a4a5-0f73c81f4f14']],
         ],
        ['symbol',
         ['lib_id', 'power:GND'],
         ['at',  168.91, 93.98, 0],
         ['unit', 1],
         ['in_bom', 'yes'],
         ['on_board', 'yes'],
         ['uuid', '18af9582-7c92-46f1-9603-90a0db4828ae'],
         ['property', 'Reference', 'REF2',
          ['id', 1], ['at', 168.91, 100.33, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Value', 'GND', ['id', 1], ['at', 169.037, 98.3742, 0]],
         ['property', 'Footprint', '', ['id', 2], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Datasheet', '', ['id', 3], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['pin', '1', ['uuid', '0462adc4-54a7-4c18-967e-f6d78a20207f']],
         ['pin', '2', ['uuid', 'ab6930b8-e44b-4fa6-a4a5-0f73c81f4f14']],
         ]
        ]


class TestSimpleSchematic(TestCase):
    def setUp(self):
        self.sut = Schematic(data)

    def test_schematic_tag(self):
        self.assertEqual('kicad_sch', self.sut.tag)

    def test_read_symbol1_reference(self):
        self.assertEqual('REF1', self.sut.symbols[0].reference.value)

    def test_read_symbol2_reference(self):
        self.assertEqual('REF2', self.sut.symbols[1].reference.value)

    def test_write_symbol2_reference(self):
        expected = 'NEW_REF2'
        self.sut.symbols[1].reference.value = expected

        actual = self.sut._data[4][7][2]

        self.assertEqual(actual, expected)

# class TestRaw(TestCase):
#     def setUp(self):
#         self.filename = '/mnt/c/repos/guitar/guitar/guitar.kicad_sch'

#         # SExprBase._allow_instantiate_base = True
#         # SExprBase.allow_empty = True

#     def test_parse(self):
#         with open(self.filename, 'r') as f:
#             text = f.read()

#         data = parse_sexpr(text)

#         sut = Schematic(data=data)

#         self.assertEqual('kicad_sch', sut.tag)

#     def test_write(self):
#         with open(self.filename, 'r') as f:
#             sut = Schematic(data=parse_sexpr(f.read()))

#         s = build_sexpr(sut._data)

#         with open("test.kicad_sch", 'w') as f:
#             f.write(s)

#         # print(s)
