# -*- coding:utf-8 -*-

"""

created by shuangquan.huang at 2019-07-11

"""

import typing


def build_suffix_array(anStr):
    """
    https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/
    :param anStr:
    :return:
    """
    if not anStr:
        return []
    
    chs = list(sorted(set(anStr)))
    ranks = {c: i for i, c in enumerate(chs)}
    
    # rank, prank, index
    n = len(anStr)
    suffix = [[ranks[v], ranks[anStr[i + 1]] if i < n - 1 else -1, i] for i, v in enumerate(anStr)]
    suffix.sort()
    
    k = 1
    ind = [0] * n
    while k < n:
        rank, prank = suffix[0][0], suffix[0][0]
        for i in range(1, n):
            if suffix[i][0] != prank or suffix[i][1] != suffix[i - 1][1]:
                rank += 1
            prank = suffix[i][0]
            suffix[i][0] = rank
            ind[suffix[i][2]] = i
        
        for i in range(n):
            nextInd = suffix[i][2] + k
            suffix[i][1] = suffix[ind[nextInd]][0] if nextInd < n else -1
        
        suffix.sort()
        k *= 2
    
    return [v[2] for v in suffix]


def search_in_suffix_array(suffix: typing.List[int], pattern: str, txt: str) -> int:
    """
    https://www.geeksforgeeks.org/suffix-array-set-1-introduction/
    To search a pattern in a text, we preprocess the text and build a suffix array of the text.
    Since we have a sorted array of all suffixes, Binary Search can be used to search.
    Following is the search function. Note that the function doesn’t report all occurrences of pattern,
    it only report one of them.
    :param txt:
    :param suffix:
    :param pattern:
    :return:
    """
    
    m, n = len(pattern), len(suffix)
    left, right = 0, n - 1  # type: (int, int)
    while left <= right:
        mid = left + (right - left) // 2
        s = txt[suffix[mid]:][:m]
        if pattern == s:
            return suffix[mid]
        elif pattern < s:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    suffixArr = build_suffix_array('banana')
    print(suffixArr)
    ans = search_in_suffix_array(suffixArr, 'nan', 'banana')
    print(ans)