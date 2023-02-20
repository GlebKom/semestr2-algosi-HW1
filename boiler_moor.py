def table_of_shift(needle: str) -> dict:
    shifts = {}
    for i in range(1, len(needle)):
        if needle[len(needle) - i - 1] not in shifts.keys():
            shifts[needle[len(needle) - i - 1]] = i
    if needle[-1] not in shifts.keys():
        shifts[needle[-1]] = len(needle)
    shifts['*'] = len(needle)
    return shifts

def boiler_moor_search(needle: str, haystack: str) -> int:
    coincidence_cnt = 0
    d = table_of_shift(needle)
    if len(haystack) >= len(needle):
        i = len(needle) - 1  # счетчик проверяемого символа в строке

        while (i < len(haystack)):
            k = 0
            flBreak = False
            for j in range(len(needle) - 1, -1, -1):
                if haystack[i - k] != needle[j]:
                    off = d[haystack[i - k]] if d.get(haystack[i - k], False) else d['*']
                    i += off  # смещение счетчика строки
                    flBreak = True  # если несовпадение символа, то flBreak = True
                    break

                k += 1  # смещение для сравниваемого символа в строке

            if not flBreak:  # если дошли до начала образа, значит, все его символы совпали
                coincidence_cnt += 1
                i += d[haystack[i - k]] if d.get(haystack[i - k]) else d['*']
    else:
        return 0
    return coincidence_cnt