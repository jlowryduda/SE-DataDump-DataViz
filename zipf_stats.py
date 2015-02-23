"""
In all posts up to some date,
this was the distribution of alphanumeric characters.

Statistics from Posts.xml for Zipf's law - word and letter counts.
"""

alphanum_dict = {'0': 1648299,
                 '1': 2996460,
                 '2': 2413346,
                 '3': 897140,
                 '4': 547849,
                 '5': 436700,
                 '6': 325232,
                 '7': 266733,
                 '8': 258931,
                 '9': 316516,
                 'a': 21395841,
                 'b': 5123468,
                 'c': 8716892,
                 'd': 7731195,
                 'e': 29313928,
                 'f': 7524732,
                 'g': 5363535,
                 'h': 12245277,
                 'i': 20323649,
                 'j': 398841,
                 'k': 1938205,
                 'l': 11005304,
                 'm': 8307930,
                 'n': 19091353,
                 'o': 19817608,
                 'p': 10660882,
                 'q': 1382828,
                 'r': 15295527,
                 's': 16178000,
                 't': 25638091,
                 'u': 7521201,
                 'v': 2880701,
                 'w': 3969719,
                 'x': 3036065,
                 'y': 4465786,
                 'z': 522496}

#In terms of math characters:

mathchars_dict = {'!': 150861,
                  '#': 89714,
                  '$': 11171723,
                  '%': 103145,
                  '(': 3174906,
                  ')': 3218960,
                  '+': 1340083,
                  '-': 2087689,
                  '/': 3837002,
                  ':': 854477,
                  '<': 5679286,
                  '=': 2312498,
                  '>': 5691596,
                  '[': 292071,
                  '\\': 8736424,
                  ']': 285812,
                  '^': 2059044,
                  '_': 2612986,
                  '{': 4377012,
                  '}': 4374488}

#What's up with the discrepancies between left and right closures?

#Raw punctuation:

punct_dict = {'!': 150861,
              '"': 839690,
              "'": 725743,
              ',': 3960295,
              '.': 3812972,
              ':': 854477,
              ';': 986893,
              '?': 352332}

#####################################

#Sorted:


alphanum_sorted = [['e', 29313928],
                   ['t', 25638091],
                   ['a', 21395841],
                   ['i', 20323649],
                   ['o', 19817608],
                   ['n', 19091353],
                   ['s', 16178000],
                   ['r', 15295527],
                   ['h', 12245277],
                   ['l', 11005304],
                   ['p', 10660882],
                   ['c', 8716892],
                   ['m', 8307930],
                   ['d', 7731195],
                   ['f', 7524732],
                   ['u', 7521201],
                   ['g', 5363535],
                   ['b', 5123468],
                   ['y', 4465786],
                   ['w', 3969719],
                   ['x', 3036065],
                   ['1', 2996460],
                   ['v', 2880701],
                   ['2', 2413346],
                   ['k', 1938205],
                   ['0', 1648299],
                   ['q', 1382828],
                   ['3', 897140],
                   ['4', 547849],
                   ['z', 522496],
                   ['5', 436700],
                   ['j', 398841],
                   ['6', 325232],
                   ['9', 316516],
                   ['7', 266733],
                   ['8', 258931]]


mathchars_sorted = [['$', 11171723],
                    ['\\', 8736424],
                    ['>', 5691596],
                    ['<', 5679286],
                    ['{', 4377012],
                    ['}', 4374488],
                    ['/', 3837002],
                    [')', 3218960],
                    ['(', 3174906],
                    ['_', 2612986],
                    ['=', 2312498],
                    ['-', 2087689],
                    ['^', 2059044],
                    ['+', 1340083],
                    [':', 854477],
                    ['[', 292071],
                    [']', 285812],
                    ['!', 150861],
                    ['%', 103145],
                    ['#', 89714]]


punct_sorted = [[',', 3960295],
                ['.', 3812972],
                [';', 986893],
                [':', 854477],
                ['"', 839690],
                ["'", 725743],
                ['?', 352332],
                ['!', 150861]]

#in total:

total_sorted = [['e', 29313928],
                ['t', 25638091],
                ['a', 21395841],
                ['i', 20323649],
                ['o', 19817608],
                ['n', 19091353],
                ['s', 16178000],
                ['r', 15295527],
                ['h', 12245277],
                ['$', 11171723],
                ['l', 11005304],
                ['p', 10660882],
                ['\\', 8736424],
                ['c', 8716892],
                ['m', 8307930],
                ['d', 7731195],
                ['f', 7524732],
                ['u', 7521201],
                ['>', 5691596],
                ['<', 5679286],
                ['g', 5363535],
                ['b', 5123468],
                ['y', 4465786],
                ['{', 4377012],
                ['}', 4374488],
                ['w', 3969719],
                [',', 3960295],
                ['/', 3837002],
                ['.', 3812972],
                [')', 3218960],
                ['(', 3174906],
                ['x', 3036065],
                ['1', 2996460],
                ['v', 2880701],
                ['_', 2612986],
                ['2', 2413346],
                ['=', 2312498],
                ['-', 2087689],
                ['^', 2059044],
                ['k', 1938205],
                ['0', 1648299],
                ['q', 1382828],
                ['+', 1340083],
                [';', 986893],
                ['3', 897140],
                [':', 854477],
                [':', 854477],
                ['"', 839690],
                ["'", 725743],
                ['4', 547849],
                ['z', 522496],
                ['5', 436700],
                ['j', 398841],
                ['?', 352332],
                ['6', 325232],
                ['9', 316516],
                ['[', 292071],
                [']', 285812],
                ['7', 266733],
                ['8', 258931],
                ['!', 150861],
                ['!', 150861],
                ['%', 103145],
                ['#', 89714]]
