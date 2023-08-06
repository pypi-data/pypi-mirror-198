# Copyright 2023 Krzysztof Wiśniewski <argmaster.world@gmail.com>
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the “Software”), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""Module contains helper global constants."""

from __future__ import annotations

import numpy as np

# fmt: off
PRIMES = np.array([
    2,      3,      5,      7,      11,     13,     17,     19,     23,     29,     31,     # noqa: E501
    37,     41,     43,     47,     53,     59,     61,     67,     71,     73,     79,     # noqa: E501
    83,     89,     97,     101,    103,    107,    109,    113,    127,    131,    137,    # noqa: E501
    139,    149,    151,    157,    163,    167,    173,    179,    181,    191,    193,    # noqa: E501
    197,    199,    211,    223,    227,    229,    233,    239,    241,    251,    257,    # noqa: E501
    263,    269,    271,    277,    281,    283,    293,    307,    311,    313,    317,    # noqa: E501
    331,    337,    347,    349,    353,    359,    367,    373,    379,    383,    389,    # noqa: E501
    397,    401,    409,    419,    421,    431,    433,    439,    443,    449,    457,    # noqa: E501
    461,    463,    467,    479,    487,    491,    499,    503,    509,    521,    523,    # noqa: E501
    541,    547,    557,    563,    569,    571,    577,    587,    593,    599,    601,    # noqa: E501
    607,    613,    617,    619,    631,    641,    643,    647,    653,    659,    661,    # noqa: E501
    673,    677,    683,    691,    701,    709,    719,    727,    733,    739,    743,    # noqa: E501
    751,    757,    761,    769,    773,    787,    797,    809,    811,    821,    823,    # noqa: E501
    827,    829,    839,    853,    857,    859,    863,    877,    881,    883,    887,    # noqa: E501
    907,    911,    919,    929,    937,    941,    947,    953,    967,    971,    977,    # noqa: E501
    983,    991,    997,    1009,   1013,   1019,   1021,   1031,   1033,   1039,   1049,   # noqa: E501
    1051,   1061,   1063,   1069,   1087,   1091,   1093,   1097,   1103,   1109,   1117,   # noqa: E501
    1123,   1129,   1151,   1153,   1163,   1171,   1181,   1187,   1193,   1201,   1213,   # noqa: E501
    1217,   1223,   1229,   1231,   1237,   1249,   1259,   1277,   1279,   1283,   1289,   # noqa: E501
    1291,   1297,   1301,   1303,   1307,   1319,   1321,   1327,   1361,   1367,   1373,   # noqa: E501
    1381,   1399,   1409,   1423,   1427,   1429,   1433,   1439,   1447,   1451,   1453,   # noqa: E501
    1459,   1471,   1481,   1483,   1487,   1489,   1493,   1499,   1511,   1523,   1531,   # noqa: E501
    1543,   1549,   1553,   1559,   1567,   1571,   1579,   1583,   1597,   1601,   1607,   # noqa: E501
    1609,   1613,   1619,   1621,   1627,   1637,   1657,   1663,   1667,   1669,   1693,   # noqa: E501
    1697,   1699,   1709,   1721,   1723,   1733,   1741,   1747,   1753,   1759,   1777,   # noqa: E501
    1783,   1787,   1789,   1801,   1811,   1823,   1831,   1847,   1861,   1867,   1871,   # noqa: E501
    1873,   1877,   1879,   1889,   1901,   1907,   1913,   1931,   1933,   1949,   1951,   # noqa: E501
    1973,   1979,   1987,   1993,   1997,   1999,
], dtype=np.int64)
# fmt: on
"""All prime numbers from 2 to 1999, used by algorithms in this package."""
