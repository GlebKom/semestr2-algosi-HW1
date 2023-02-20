from pathlib import Path
from kmp import prefix, kmp_search
from naive import naive_search
from hash_search import rabin_karp_search
from boiler_moor import table_of_shift, boiler_moor_search
original_symbols = 0
copied_symbols = 0
import timeit

original = ''.join([w for w in Path("original.txt").read_text(encoding="utf-8").replace("\n", " ").split()])
copy = [w for w in Path("copy.txt").read_text(encoding="utf-8").replace("\n", " ").split()]

starttime = timeit.default_timer()
for i in range(len(copy) - 2):
    if naive_search(''.join(copy[i:i + 2]), original) > 0:
        copied_symbols += len(''.join(copy[i:i + 2]))
    else:
        original_symbols += len(''.join(copy[i:i + 2]))
print('Naive search time: ',  timeit.default_timer() - starttime)
print(original_symbols/(copied_symbols + original_symbols) * 100)
original_symbols = 0
copied_symbols = 0

starttime = timeit.default_timer()
for i in range(len(copy) - 2):
    if rabin_karp_search(''.join(copy[i:i + 2]), original) > 0:
        copied_symbols += len(''.join(copy[i:i + 2]))
    else:
        original_symbols += len(''.join(copy[i:i + 2]))
print('Rabin-Karp search time: ',  timeit.default_timer() - starttime)
print(original_symbols/(copied_symbols + original_symbols) * 100)
original_symbols = 0
copied_symbols = 0

starttime = timeit.default_timer()
for i in range(len(copy) - 2):
    if boiler_moor_search(''.join(copy[i:i + 2]), original) > 0:
        copied_symbols += len(''.join(copy[i:i + 2]))
    else:
        original_symbols += len(''.join(copy[i:i + 2]))
print('Boiler-Moor search time: ',  timeit.default_timer() - starttime)
print(original_symbols/(copied_symbols + original_symbols) * 100)
original_symbols = 0
copied_symbols = 0

starttime = timeit.default_timer()
for i in range(len(copy) - 2):
    if kmp_search(''.join(copy[i:i + 2]), original) > 0:
        copied_symbols += len(''.join(copy[i:i + 2]))
    else:
        original_symbols += len(''.join(copy[i:i + 2]))
print('KMP search time: ',  timeit.default_timer() - starttime)
print(original_symbols/(copied_symbols + original_symbols) * 100)
original_symbols = 0
copied_symbols = 0


