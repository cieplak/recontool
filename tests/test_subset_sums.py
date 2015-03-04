from __future__ import unicode_literals
import unittest

from recontool.subset_sums import SubsetSums


class TestSubsetSums(unittest.TestCase):

    def test_subset_sums(self):
        seq = [1, 2, 3, 4, 5]
        subset_sums = SubsetSums.create(seq)
        expected_range_sums = [
            ((0, 5), 15),
            ((0, 4), 10),
            ((0, 3), 6),
            ((0, 2), 3),
            ((0, 1), 1),
            ((1, 5), 14),
            ((1, 4), 9),
            ((1, 3), 5),
            ((1, 2), 2),
            ((2, 5), 12),
            ((2, 4), 7),
            ((2, 3), 3),
            ((3, 5), 9),
            ((3, 4), 4),
            ((4, 5), 5),
        ]
        range_sums = list(subset_sums)
        self.assertEqual(range_sums, expected_range_sums)
        same_subset_sums = subset_sums.submatrix(0)
        self.assertEqual(subset_sums.table, same_subset_sums.table)
        self.assertEqual(subset_sums.sequence, same_subset_sums.sequence)
        submatrix1 = subset_sums.submatrix(1)
        self.assertEqual(submatrix1.sequence, seq[1:])
        self.assertEqual(submatrix1.table, subset_sums.table[1:])
        expected_submatrix_range_sums = [
            ((0, 4), 14),
            ((0, 3), 9),
            ((0, 2), 5),
            ((0, 1), 2),
            ((1, 4), 12),
            ((1, 3), 7),
            ((1, 2), 3),
            ((2, 4), 9),
            ((2, 3), 4),
            ((3, 4), 5),
        ]
        self.assertEqual(list(submatrix1), expected_submatrix_range_sums)
        self.assertEqual(
            subset_sums.submatrix(2).sequence,
            submatrix1.submatrix(1).sequence
        )
        self.assertEqual(
            subset_sums.submatrix(2).table,
            submatrix1.submatrix(1).table
        )
