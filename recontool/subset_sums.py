from __future__ import unicode_literals


class SubsetSums(object):

    def __init__(self, sequence, table):
        self.sequence = sequence
        self.table = table

    def __iter__(self):
        n = len(self.sequence)
        for row in xrange(n):
            for column in list(reversed(xrange(n)))[0:n - row]:
                yield (row, column + 1), self.get(row, column)

    @classmethod
    def create(cls, sequence):
        table = cls.calculate_subset_sums(sequence)
        return cls(sequence, table)

    @classmethod
    def calculate_subset_sums(cls, sequence):
        n = len(sequence)
        table = [[None for i in xrange(n - j)] for j in xrange(n)]
        for start, end in cls.range_indices(sequence):
            table[start][end - start] = sum(sequence[start:end + 1])
        return table

    @classmethod
    def range_indices(cls, sequence):
        return [
            (b, a) for a in xrange(len(sequence)) for b in xrange(a + 1)
        ]

    def get(self, row, column):
        return self.table[row][column - row]

    def submatrix(self, index):
        return SubsetSums(self.sequence[index:], self.table[index:])
