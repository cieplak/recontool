from __future__ import unicode_literals


def visualize(left, right, reconciliation):
    rows = []
    for (left_start, left_end), (right_start, right_end) in reconciliation:
        rows.extend(
            _row_group(
                (left_start, left_end),
                (right_start, right_end),
                left[left_start: left_end],
                right[right_start: right_end]
            )
        )
    return '\n'.join(rows)


def _row_group(left_range, right_range, left, right):
    row_template = (
        lambda l, r, li, ri:
        '{:6}: ${:29,.2f}'.format(li or ' ', l) + ' ' * 4 +
        '{:6}: ${:29,.2f}'.format(ri or ' ', r)
    )
    totals_template = (
        lambda l, r:
        ' ' * 8 + '${:29,.2f}'.format(l) + ' ' * 12 +
        '${:29,.2f}'.format(r)
    )
    single_line = '-' * 80
    double_line = '=' * 80
    blank_line = ' ' * 80
    n = max(len(left), len(right))
    left_array = [(None, 0) for _ in xrange(n)]
    lrange = range(*left_range)
    for i, element in enumerate(left):
        left_array[i] = (lrange[i] + 1, element)
    right_array = [(None, 0) for _ in xrange(n)]
    for i, element in enumerate(right):
        right_array[i] = (range(*right_range)[i] + 1, element)
    rows = []
    rows.append(blank_line)
    rows.append(blank_line)
    for (li, l), (ri, r) in zip(left_array, right_array):
        rows.append(row_template(l, r, li, ri))
    rows.append(single_line)
    rows.append(totals_template(sum(left), sum(right)))
    rows.append(double_line)
    return rows
