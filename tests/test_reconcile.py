import csv
from decimal import Decimal
import unittest

from recontool import reconcile

from . import get_fixture_path


class TestReconcile(unittest.TestCase):

    def test_reconcile(self):
        left = [27, 29, 3, 5, 7]
        right = [9, 7, 5, 3, 4]
        expected = [
            ((0, 2), (0, 1)),
            ((2, 5), (1, 4)),
            ((5, 5), (4, 5)),
        ]
        recon = reconcile(left, right)
        self.assertEqual(recon, expected)

    def test_reconcile2(self):
        left = [13, 10, 3, 5, 7, 1, 5, 13, 3, 1, 2]
        right = [9, 7, 5, 3, 4, 5, 13, 1, 3]
        expected_recon = [
            ((0, 0), (0, 1)),
            ((0, 5), (1, 8)),
            ((5, 8), (8, 8)),
            ((8, 9), (8, 9)),
            ((9, 11), (9, 9)),
        ]
        recon = reconcile(left, right)
        self.assertEqual(recon, expected_recon)

    def test_real_world_example(self):
        left_csv = get_fixture_path('left.csv')
        right_csv = get_fixture_path('right.csv')
        with open(left_csv, 'cU') as fo:
            left_rows = filter(bool, list(csv.reader(fo, delimiter='|')))
        with open(right_csv, 'cU') as fo:
            right_rows = filter(bool, list(csv.reader(fo, delimiter='|')))
        clean_amount = lambda s: s.replace('$', '').replace(',', '')
        left = [Decimal(clean_amount(column[0])) for column in left_rows]
        right = [Decimal(clean_amount(column[0])) for column in right_rows]
        recon = reconcile(left, right)
        expected_reconciliation = [
            ((0, 1), (0, 0)),
            ((1, 10), (0, 9)),
            ((10, 12), (9, 10)),
            ((12, 18), (10, 12))
        ]
        self.assertEqual(recon, expected_reconciliation)
