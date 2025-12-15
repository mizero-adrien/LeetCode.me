class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        freq = Counter(s)
        chars = sorted(freq.keys(), key = lambda x: -freq[x]) #sorted by descending
        result = []
        for ch in chars:
            result.append(ch*freq[ch])
        return "".join(result)
