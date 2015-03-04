import csv
from decimal import Decimal
import unittest

from recontool import reconcile, visualize

from . import get_fixture_path


class TestVisualization(unittest.TestCase):

    def test_visualization(self):
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
        visualization = visualize(left, right, recon)
        with open( get_fixture_path('visualization.txt')) as fo:
            expected_visualization = fo.read()
        self.assertEqual(visualization, expected_visualization)
