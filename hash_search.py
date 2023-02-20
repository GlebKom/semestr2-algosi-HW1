def rabin_karp_search(needle: str, haystack: str) -> int:
    coincidence_cnt = 0
    n, m = len(haystack), len(needle)
    hpattern = hash(needle)
    for i in range(n-m+1):
        hs = hash(haystack[i:i+m])
        if hs == hpattern:
            if haystack[i:i+m] == needle:
                coincidence_cnt += 1
    return coincidence_cnt

