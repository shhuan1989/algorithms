# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys
from typing import List

"""
created by shhuan at 2019/12/22 00:41

"""


class Solution:
    def search(self, L: int, n: int, S: str) -> int:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            h = hash(tmp)
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)

        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1





s = Solution()
print(s.longestRepeatingSubstring('abcd'))
print(s.longestRepeatingSubstring('abbaba'))
print(s.longestRepeatingSubstring('aabcaabdaab'))
print(s.longestRepeatingSubstring('aaaaa'))
print(s.longestRepeatingSubstring('bbwfowdeauwderbddpwzrfowybhpvfoyvfdrsgjiytfxxawkctyfvrywxqwwoculuoiqzmsbaonhtswpmachjaademrwznqbkrravioseyibmqeuuayrnxzyptpuwlblkpvhgkufnjhprgsecqzpgfdjdgagjgiifjiftyiimgegotdylcxhdakzwgicnbzefvmdbhbbgbvxbdueewyzrpvxfcbigaprdudvbxreavzgwpcxldwcfnqrbbfvcmeiyafbhtixegibfnugfytiqczwqclfsksameergvxljtxeranlnozzhpdexkfwysuzeavvzqoxogxsixiczwrwrefqnefkumlzdzknqwizvqzyginiakjxllvpttdrhorinzhkxirfkryymvqezvdifjbndxdlflzsbigypltvuyocbudqidyxfknoslylcwwvidlrfjntfkgmzpvkkzscspslrnypbgziknzawqpfvmarzjwdwbezcudhmedfcmdwutehzeayufgmkbnuxaozypkakonotapbzeambrileusrfzhijejuggvtakwsnxuzubdojfgkzwrvsetjvmwqobtagebxgicsgrtgzmrzjnzitxknocptmayabfwrupscpwmclknwqlhkyejhyfxuiunasfbiuttrfotckztxozawqgqwswvwfdnozbmocmdmlyupaoayxnzwrvapputncymzpefiozqimezggqvwlhtpdaseputojdrjxfueemvzdjhhwhfvsauvhpkhldwvwuvonpginysnltfgqawamilcpxdreyjwnmlxcbdurpeasxnabftirkappyrbwsuccrkrzsvlwrwyivctvdmrmdrrxipbqusmicdbqasklcadkianuctcxkewctdrdllodyrpskipsybwrldbsvpjuxmgdbxwhuweizihgiulzrsjsdesdodhmqzwtayfpdtbhnjyjvsilfspghnwytn'))
print(s.longestRepeatingSubstring('gymjkqexonleccucwuofmuirwtdvjescmjvdulychgavmbbgcluxbjrewurytkwxnpvgssttlcbrwysncyqxxmpajrgibnihjxchtsnwcwsmhndomnthvlehuynimnskqgeqbtyvcecdjrjtkuamswamunxhwlmiorxtlkogxetsuhijesobgsoylxqpmrolkhwywyktxthrhgiejavdjsxhhriamvegqeghmvbqxyetptucgtfmfjobqbunlxsoehkysdnqsxtdyjlrwifvytfgpsycaanqeusuluwyuclvybgnajospbhtjgfwujxorrtpnvcquecatqhvlitibjtclhqxjwjybggucayaifoidjupjixudfnehiuflscvejxvytsxobriympthgbtyllhcrfyblylsqrcmjvpatixxlgxlmftuildsukpiuvqnkkgblohmnbktdvqoaixxnmntjkjamodnkownuyypipmmtdcbxgxjkwsjlyehothcnkbtoyeyhclmpfygmtpvpyggbyjsbqpbidvrvukwdbconiuqcetidiwuxldmcufxjqpdnuwjyfcfbjxvwsboqnbeghsulsjiceavpqeeixjgekgkppgqominhvsdfelxgjbapkhqfuyrdcugcphejatwnlcbgthirvwuhnecragftulfgkyvtrdnuycbpetoucrktynkdixnuxjwrsopofmkwclmtxexbkgywymsfphmvxcenhancsyeiwuqtewjvdvybfxjlppftktcwyphsyknhbucytepbokkvvhyklpuglhgcuonovhtdgifoxkqqvjnqctatdkeqaueygdptllxswgrrebmhrdedhhpnftmadskejjjwpvkfubonuoscyxkccsnskclfqfnjwgtmuxmttowolhxiwojhqnasxkikmpiolnqlvfroyvajjcqambwtfholxtnwfuylvnycoinulwargrikogjub'))