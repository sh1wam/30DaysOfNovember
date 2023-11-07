class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        max_pref_len = min(map(len, strs))

        result = []
        is_valid = True
        while i < max_pref_len:
            val = strs[0][i]
            for s in strs[1:]:
                if val != s[i]:
                    is_valid = False
                    break

            if not is_valid:
                break
            else:
                result.append(val)
                i += 1

        return ''.join(result)