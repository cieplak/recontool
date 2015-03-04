from __future__ import unicode_literals

from .subset_sums import SubsetSums


def reconcile(left, right):
    reconciliation_groups = []
    left_table = SubsetSums.create(left)
    right_table = SubsetSums.create(right)
    left_offset = 0
    right_offset = 0
    while left_offset < len(left):
        groups = _match_groups(left_table, right_table)
        if groups:
            for (left_start, left_end), (right_start, right_end) in groups:
                group = (
                    (left_start + left_offset, left_end + left_offset),
                    (right_start + right_offset, right_end + right_offset)
                )
                reconciliation_groups.append(group)
            left_table = left_table.submatrix(left_end)
            right_table = right_table.submatrix(right_end)
            left_offset += left_end
            right_offset += right_end
        else:
            unmatched_group = (
                (left_offset, len(left)),
                (right_offset, len(right))
            )
            reconciliation_groups.append(unmatched_group)
            left_offset = len(left)
            right_offset = len(right)
    if (len(left) - left_offset + len(right) - right_offset) > 0:
        unmatched_group = (
            (left_offset, len(left)),
            (right_offset, len(right))
        )
        reconciliation_groups.append(unmatched_group)
    return reconciliation_groups


def _match_groups(left_table, right_table):
    groups = []
    for (left_start, left_end), left_subset_sum in left_table:
        for (right_start, right_end), right_subset_sum in right_table:
            if left_subset_sum == right_subset_sum:
                if left_start + right_start > 0:
                    unmatched_group = ((0, left_start), (0, right_start))
                    groups.append(unmatched_group)
                matched_group = (
                    (left_start, left_end),
                    (right_start, right_end)
                )
                groups.append(matched_group)
                return groups
