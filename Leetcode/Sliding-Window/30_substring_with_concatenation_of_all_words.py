# Problem: https://leetcode.com/problems/substring-with-concatenation-of-all-words

# Time Complexity: O(n * m * k), where n = len(s), m = number of words, k = length of each word
# Space Complexity: O(m * k) for frequency maps

from collections import Counter, defaultdict

def findSubstring(s, words):
    """
    Approach:
        - Each word has the same length.
        - Total window length = len(words) * word length.
        - Slide over the string `s`, checking each window of that total length.
        - For each window, break it into equal-sized chunks and compare their frequency with `words`.
        - If all words are found exactly once, store the start index.
    """
    out = []
    if not s or not words or not words[0]:
        return out

    word_len = len(words[0])
    total_window = len(words) * word_len
    word_freq = Counter(words)  # Frequency of input words

    for i in range(len(s) - total_window + 1):
        substring_freq = defaultdict(int)
        j = i

        while j < i + total_window:
            cur_word = s[j:j + word_len]

            if cur_word not in word_freq:
                break  # Early exit if word not in required set

            substring_freq[cur_word] += 1

            if substring_freq[cur_word] > word_freq[cur_word]:
                break  # Exceeds required frequency

            j += word_len

        if j == i + total_window:
            out.append(i)  # Valid starting index

    return out

def main():
    # Test - 1
    s1 = "barfoothefoobarman"
    words1 = ["foo","bar"]
    print(f"output-1: {findSubstring(s1, words1)}")

    # Test - 2
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    print(f"output-2: {findSubstring(s2, words2)}")

    # Test - 3
    s3 = "barfoofoobarthefoobarman"
    words3 = ["bar","foo","the"]
    print(f"output-3: {findSubstring(s3, words3)}")

if __name__ == "__main__":
    main()
