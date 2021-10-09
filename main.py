import numpy as np
from scipy import interpolate

# Data van NTC
raw_NTC = [
    31281,      # -20
    29847,      # -19
    28489,      # -18
    27202.2,    # -17
    25983,      # -16
    24828,      # -15
    23732,      # -14
    22692,      # -13
    21706,      # -12
    20769,      # -11
    19879.5,    # -10
    19033,      # -9
    18229,      # -8
    17464,      # -7
    16736.8,    # -6
    16045,      # -5
    15386,      # -4
    14760,      # -3
    14163,      # -2
    13594,      # -1
    13052,      # 0
    12531,      # 1
    12033.5,    # 2
    11560,      # 3
    11107,      # 4
    10676,      # 5
    10265,      # 6
    9871,       # 7
    9496,       # 8
    9138,       # 9
    8795,       # 10
    8493,       # 11
    8203,       # 12
    7925,       # 13
    7659,       # 14
    7403,       # 15
    7157,       # 16
    6921,       # 17
    6695,       # 18
    6477,       # 19
    6268,       # 20
    5987,       # 21
    5721,       # 22
    5468,       # 23
    5228,       # 24
    5000,       # 25
    4815,       # 26
    4637,       # 27
    4468,       # 28
    4305,       # 29
    4150,       # 30
    3997,       # 31
    3850.2,     # 32
    3710,       # 33
    3576,       # 34
    3447,       # 35
    3323,       # 36
    3206,       # 37
    3092,       # 38
    2984,       # 39
    2880,       # 40
    2778,       # 41
    2681,       # 42
    2587,       # 43
    2497,       # 44
    2411,       # 45
    2329,       # 46
    2249,       # 47
    2173,       # 48
    2100.1,     # 49
    2030,       # 50
    1963,       # 51
    1898,       # 52
    1836,       # 53
    1776,       # 54
    1719,       # 55
    1664,       # 56
    1611,       # 57
    1560,       # 58
    1510.3,     # 59
    1463,       # 60
    1408,       # 61
    1355,       # 62
    1304,       # 63
    1256,       # 64
    1210,       # 65
    1165,       # 66
    1123,       # 67
    1082,       # 68
    1043,       # 69
    1006,       # 70
    981,        # 71
    957,        # 72
    934,        # 73
    912,        # 74
    890,        # 75
    869,        # 76
    848,        # 77
    828,        # 78
    809,        # 79
    790,        # 80
    767,        # 81
    745,        # 82
    724,        # 83
    703,        # 84
    683,        # 85
    664,        # 86
    645,        # 87
    627,        # 88
    610,        # 89
    593,        # 90
    577,        # 91
    561,        # 92
    545,        # 93
    531,        # 94
    516,        # 95
    502,        # 96
    489,        # 97
    476,        # 98
    463,        # 99
    451,        # 100
    440,        # 101
    428,        # 102
    418,        # 103
    407,        # 104
    397         # 105
]


# Vind de dichtsbijzijnde getal in lijst
def find_nearest(lst, val):
    lst = np.asarray(lst)
    idx = (np.abs(lst - val)).argmin()
    return idx


# Loopt van -20°C tot 105°C met stapgrote van 1°C
raw_temp = np.arange(-20, 105+1, 1)
# Loopt van -20°C tot 105°C met stapgrote van 0.1°C
interp_temp = np.arange(-20, 105+0.1, 0.1)

# Interpoleer naar van stapgrote van 1°C naar stapgrote van 0.1°C
interp = interpolate.interp1d(raw_temp, raw_NTC, kind='quadratic', fill_value='extrapolate')
interp_NTC = interp(interp_temp)

inpt = input("Voer gemeten waardes in Ohm in. Voorbeeld: '5921 5872 5721...'\n").rstrip().split()

# Loopt langs elke ingevoerde waarde
for n in inpt:
    print("%s ohm is %s° Celsius" % (n, round(interp_temp[find_nearest(interp_NTC, float(n))], 1)))

# Laat geïnterpoleerde tabel zien (voor excel)
if input("\nLaat geïnterpoleerde tabel zien? y/N\n").capitalize() == 'Y':
    for r in interp_NTC:
        # Rond af op 1 significante voor afronden
        print("%.1f" % r)
