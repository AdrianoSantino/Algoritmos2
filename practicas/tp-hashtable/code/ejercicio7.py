def compress(s):
    """Returns a compressed string. O(n), just a while with no iterative functions inside."""
    if len(s) <= 1:
        return s

    comp = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            comp += s[i-1] + str(count)
            count = 1

        if len(comp) >= len(s):
            return s

    comp += s[-1] + str(count)
    return comp if len(comp) < len(s) else s


if __name__ == "__main__":
    print(compress("aabcccccaaa"))
    print(compress("aabcccccmmsadfaaaa"))
