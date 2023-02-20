from naive import naive_search
from hash_search import rabin_karp_search
from boiler_moor import table_of_shift, boiler_moor_search
from kmp import prefix, kmp_search
import timeit
def finbonacci_string() -> str:
    n = 2
    a = 0
    b = 1
    fib_num = '01'
    while n < 500:
        fib_num += str(a + b)
        a, b = b, a + b
        n += 1
    return(fib_num)

fib_nums = finbonacci_string()

cnt1 = [0]*100
cnt2 = [0]*100
cnt3 = [0]*100
cnt4 = [0]*100
cnt5 = [0]*100
cnt6 = [0]*100

starttime = timeit.default_timer()
for i in range(10, 100):
    cnt1[i] = naive_search(str(i), fib_nums)
print('Naive search: ', timeit.default_timer() - starttime)
print(cnt1.index(max(cnt1)))

starttime = timeit.default_timer()
for i in range(10, 100):
    cnt2[i] = rabin_karp_search(str(i), fib_nums)
print('Rabin-Karp search: ', timeit.default_timer() - starttime)
print(cnt2.index(max(cnt2)))

starttime = timeit.default_timer()
for i in range(10, 100):
    cnt3[i] = boiler_moor_search(str(i), fib_nums)
print('Boiler-Moor search: ', timeit.default_timer() - starttime)
print(cnt3.index(max(cnt3)))

starttime = timeit.default_timer()
for i in range(10, 100):
    cnt5[i] = kmp_search(str(i), fib_nums)
print('KMP search: ', timeit.default_timer() - starttime)
print(cnt5.index(max(cnt5)))
