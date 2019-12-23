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
created by shhuan at 2019/12/22 20:37

"""


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        wi = collections.defaultdict(list)
        for i, v in enumerate(source):
            wi[v].append(i)

        ans = 1
        i = -1
        for ch in target:
            if ch not in wi:
                return -1
            idx = wi[ch]
            i = bisect.bisect_right(idx, i)
            if i == len(idx):
                ans += 1
                i = idx[0]
            else:
                i = idx[i]

        return ans

s = Solution()
print(s.shortestWay("aaaaa", "aaaaaaaaaaaaa"))
print(s.shortestWay('abc', 'abcbc'))
print(s.shortestWay('abc', 'acdbc'))
print(s.shortestWay('xyz', 'xzyxz'))

t0 = time.time()
print(s.shortestWay("emjohvkpmowgvcelwvcsmuwcvabqpnywcssceruvmmdfdsyewzrwjxnytiityfbnekizhrxukhjkyydsnocxblhuvncxzdyrrkkfbrynuoalfhcdxgjlpbvfvehuokxszeggkghjcneefrfyntnwobavnaxkkqpdvvqunwzziwnfvrwntscrzrjzspkteyznrhgmnnbzxlreupkobfweoyuhfjtffrcvmoksxhhqlepwwtaazdsqeliyqbctkvjohfznwqzwcotpyfjwnbinakuhmrzgqdobdjhztaxiootarfetrnkkvcmhgnbavrfncccbcizgztijwnbxjpxfujbjmuquajjbrelxmdxtvlaxuqozojjaebkenjwagbgumwwjcsxvfngaflwvosgrpsexugtkmfgvvwphpdjffmcnwqxtffvtyvlgfdgtflndyhhhgulzxlklotricosryvnwqfifpsupddafvycqxdgagecgnntzavzjruoxrvistcsdjbmljzorrzhtljiphwwiouqdacooubazpqlbawjnbgjmaekytilyiygpnrugsvuvwoedixkwbydqpmmlrknohhstjudijqaxzfymlhjciufghixsuggcbtpzlbgnxarjcovnxyxjhwgnkdnotntnuoixvsxlxurigzcnwflrvyvxrlbufynirpahwkvffkksarqppoinmmmfziuibzqemjbbvxpsntrutestixcanksrchkprzbagileowbprnmayodccjxehcsmaolvakpdcgiuzkilluhvpnnewnietbyvgwnnjeuaxnscztnfdnqvxuemtxxpgrxhuyobepncaiiegiyqqfmmjfpudlodlvmadnpuevholkvfdaqxiehqqybldijnxksjzsjsvmsdvzsxrfkfhidvblbjxsiryypzimkzkpxaelopwrvvzevhnxatkxmnnuwvavhjhlxkiymintrwiaruitij", "wijzkueuvdokxksrrdcyqbonsbehcscocseybpfuojgcxfaejoybgmeeloxfodjqfcmxmwvtfbbbhtzzevfsjaqnegbjdjjcxwyefdjgxfnejvrbtgbvewbmbreioidiymurqfsidrplohldiqofqsbzmgcumrwsbnawaznpwifahqlwdbnyjljdhhfmsmbyvidnaedinaautzsbfthtkmbebyxlijwsavpfytplzruzpkzesvwhmipwrufowwopxxjsfkcspiqkdgbujlcpbwwnpvxglvdrmfxlfxwhkzajhohxqzfuyybradugmywibknlrfsmjobhhiqtlawqtrjzqvhwhdvwdqjhgccoscwlcdxpvwhgaklqpgufqsxamxooaqndkdlvlcnbrrdxrhukarpsqvqqtdogtpxojzpaxdhingqgkgfbdhicesvuexoikefkfhphapwjvjtwfmoftxgskvamdlrlcygmrfvzyrzzoqunjnjzkquqlpiublnafkxeprxjkiapminstxdnudvfwqkmqswcwugkcpjsjiqdmzmezouosgycxghopuofilfnfkvmcnzkardyzzfkvbpweogdbbhcjkbuwoiebegkcamnzrmbfkgiadgfsadszrlelppeatbjtjrftzkyglrgovuokncefrnoumcwayvzduobjvfuhzlhsjbbrkklmzziwlwgwzmutbzmskqtocfmtuckcizowdejmfezmurlilkvqpiueazwypzyofnzawblgaycgbguoulhuaozvoswttdotbmdyrviuwtolqqvxucjbuubjqssaeymbuhrpeofkvliuvqgbeeetqimnztfcwzwfpyzmctmhfovykhjxezanzupprtoeeylxwetxuypehgkxhqlwsctsxmlsgugcdudjbrueamezzndpyhcujgpuazmdfdulibqadwgmxhnmmbtzloolpnvbokwaqsvxegonmfgmyie"))
print(time.time() - t0)