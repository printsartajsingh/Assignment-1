def longest_common_subsequence_consonants(str1, str2):
    def is_consonant(char):
        return char.isalpha() and char.lower() not in 'aeiou'

    m, n = len(str1), len(str2)

    # Initialize a 2D array to store the LCS lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1] and is_consonant(str1[i - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from dp table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1] and is_consonant(str1[i - 1]):
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

# Input strings
input_str1 = input("Enter the first string: ").strip()
input_str2 = input("Enter the second string: ").strip()

lcs = longest_common_subsequence_consonants(input_str1, input_str2)

if len(lcs) > 0:
    print(f"The longest common subsequence of consonants is: {lcs}")
else:
    print("No common subsequence of consonants found.")