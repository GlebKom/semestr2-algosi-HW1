def naive_search(needle: str, haystack: str) -> int:
    coincidence_cnt = 0
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            coincidence_cnt += 1
    return coincidence_cnt
