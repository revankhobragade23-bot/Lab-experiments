def lcs(X, Y):
    """
    Find the Longest Common Subsequence between X and Y.
    Returns both the length and the actual subsequence.
    """
    m, n = len(X), len(Y)

    # dp[i][j] will hold the LCS length between the first i chars of X
    # and the first j chars of Y. Extra row/column of zeros = empty string case.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table row by row
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                # characters match -> extend the LCS we already found
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # no match -> carry forward whichever option was better
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Now walk backwards through the table to actually reconstruct
    # the subsequence (not just its length)
    i, j = m, n
    result = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            # this character is part of the LCS
            result.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            # moving up gave a bigger value, so go that way
            i -= 1
        else:
            # otherwise move left
            j -= 1

    # we built it backwards, so flip it around
    result.reverse()

    return dp[m][n], result


# quick test
if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"

    length, subseq = lcs(X, Y)

    print("X:", X)
    print("Y:", Y)
    print("LCS length:", length)
    print("LCS:", "".join(subseq))