def prefix(needle: str) -> list:
    p = [0] * len(needle)
    j = 0
    for i in range(1, len(needle)):
        if needle[j] == needle[i]:
            p[i] = j + 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
            else:
                j = p[j - 1]
    return p

def kmp_search(needle: str, haystack: str) -> int:
    coincidence_cnt = 0
    pi = prefix(needle)
    i = 0
    j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                coincidence_cnt += 1
                j = pi[j - 1]
        else:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
    return coincidence_cnt

