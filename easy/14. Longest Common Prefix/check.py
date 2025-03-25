from typing import List

def longestCommonPrefix(strs: List[str]) -> str:               
    pref = strs[0]
    for i in range(1, len(strs)):
        j = 0
        min_len = min(len(pref), len(strs[i]))
        while pref[j] == strs[i][j] and j < min_len:
            j += 1
            if j == min_len:
                break
        if pref == '':
            return pref
        
        pref = pref[:j]

    return pref

if __name__ == '__main__':
    strs = ["dog","racecar","car"]
    strs_1 = ['ab', 'a']

    pref = longestCommonPrefix(strs_1)
    print(pref)