# -*- coding: utf-8 -*-
import unittest
from string_repetitions import StrPattern as sp

class TestStringRepetitions(unittest.TestCase):

    def setUp(self):
        self.str_ptrn = sp()  # ?? NameError: name 'str_ptrn' is not defined
        pass

    def test_fromStr2Tpl(self):
        str_ptrn = sp()

        a_li = []
        a_tpl = []
        b_li = [0, 1, 0, 1, ]
        b_tpl = [(0, 1), (0, 1), ]
        c_li = [0, 1, 3, 4, 4, 3, 3, 4, 4, 3]
        c_tpl = [(0, 1), (3, 4), (4, 3), (3, 4), (4, 3)]
        d_li = [0, 1, 3, 4, 2, 1, 1, 4]
        d_tpl = [(0, 1), (3, 4), (2, 1), (1, 4)]
        e_li = [0, 1, 3, ]
        e_tpl = None

        self.assertEqual(self.str_ptrn.fromStr2Tpl(a_li), a_tpl)
        self.assertEqual(self.str_ptrn.fromStr2Tpl(b_li), b_tpl)
        self.assertEqual(self.str_ptrn.fromStr2Tpl(c_li), c_tpl)
        self.assertEqual(self.str_ptrn.fromStr2Tpl(d_li), d_tpl)
        self.assertEqual(self.str_ptrn.fromStr2Tpl(e_li), e_tpl)

    def test_logic(self):
        a1_li = [(0, 1)]        # only one row
        a1_lo = [{"times": 1, "rows": [(0, 1), ]},]
        b0_li = [(0, 1), (0, 1)]
        b0_lo = [{"times": 2, "rows": [(0, 1)]}]
        b1_li = [(0, 1),(0, 1),(0, 1),(0, 1),(0, 1),]
        b1_lo = [{"times": 5, "rows": [(0, 1)]}]
        b2_li = [(0, 1), (4, 3)]   # two row not repeated
        b2_lo = [{"times": 1, "rows": [(0, 1), (4, 3),]},]
        c0_li = [(3, 4), (4, 3), (3, 4), (4, 3)]
        c0_lo = [{"times": 2, "rows": [(3, 4), (4, 3)]}]
        d0_li = [(0, 1), (3, 4), (2, 1), (1, 4)]
        d0_lo = [{"times": 1, "rows": [(0, 1), (3, 4), (2, 1), (1, 4),]},]
        e0_li = [(0, 1), (3, 4), (4, 3), (3, 4), (4, 3)]
        e0_lo = [{"times": 1, "rows": [(0, 1)]}, {"times": 2, "rows": [(3, 4), (4, 3)]}]
        f0_li = [(0, 1), (3, 4), (2, 1), (1, 4)]
        f0_lo = [{"times": 1, "rows": [(0, 1), (3, 4), (2, 1), (1, 4)]}]

        self.assertEqual(self.str_ptrn.logic([]), [])
        self.assertEqual(self.str_ptrn.logic(a1_li), a1_lo)
        self.assertEqual(self.str_ptrn.logic(b0_li), b0_lo)
        self.assertEqual(self.str_ptrn.logic(b1_li), b1_lo)
        self.assertEqual(self.str_ptrn.logic(b2_li), b2_lo)
        self.assertEqual(self.str_ptrn.logic(c0_li), c0_lo)
        self.assertEqual(self.str_ptrn.logic(d0_li), d0_lo)
        # self.assertEqual(self.str_ptrn.logic(e0_li), e0_lo)

'''
    def test_fromList2Logic(self):
        b1_li = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1,]
        b1_lo = [{"times": 5, "rows": [(0, 1)]}]

        c0_li = [ 1, 0, 3, 4, 4, 3, 3, 4, 4, 3]
        c0_lo = [{"times": 1, "rows": [(1, 0), ]}, {"times": 2, "rows": [(3, 4), (4, 3)]}]

        d0_li = [1, 0, 0, 2, 4, 3, 4, 3, 0, 2, 4, 3, 4, 3]
        d0_lo = [{"times": 1, "rows": [(1, 0), ]},
                 {"times": 2, "rows": [(0, 2),
                     {"times": 2, "rows": [(4, 3)]},], }
                ]

        self.assertEqual(self.str_ptrn.logic(b1_li), b1_lo)
'''

if __name__ == '__main__':
    unittest.main()

