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
created by shhuan at 2020/1/11 22:47

"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        ans = set()
        for l in range(2, N+1, 2):
            for i in range(N-l+1):
                if text[i: i + l // 2] == text[i + l // 2: i + l]:
                    ans.add(text[i: i+l])
        return len(ans)

s = Solution()
print(s.distinctEchoSubstrings('aaaaaaaaaa'))
print(s.distinctEchoSubstrings('abcabcabc'))
print(s.distinctEchoSubstrings('leetcodeleetcode'))
print(s.distinctEchoSubstrings("wdyihepunnmlqjkpnrrzjdnysubneoiafptyurqyoiglsodisssyouhcjpwvdwfnboodwukaizlsifotxxavqybwmxpanaswhhfikcucnmdeqiyttkdqyhomzpfasrmmiurrouxbotovucdmqesiyrdkhlxbnbowwuetdyzhbkimokqqpwhdlxxdbktstkvseiylcrfgmyiatkjqsuwhbkbxuatiolxnhespqvgppzczakrzvhmkxakyipjtsaiyfbxwgrbqqfdrebrtryxdzghlnqgttldoiwezugexbdqikooyccjbflfmowgugwnizlmbtlruldgjriyngfhcigonvdgtjclopdzzwslglnwxjnxepcxcxwofmnkbkpcntxxmoomluhzkjidzxbchtbctinlqrlgihrnppvvqhkeasftmsijgqgntpoxsfszuzpvhvrxbxpfqrlgafxssaiyiismmjiuopbslrdxdzcnupdaeprmgzujmznhmecpzppbkjhlueynamrjgpxqwsvoyyhbmtnexylmfuemcduusueuxpsgfooultqfeuzhlxiyjquagryzsxpabbtmmypbgjzqewsrvtnxvmoamnuamixublfcxlecdpjpdmcztdrygvukldkiooenwkuqkmgllhppvqiqbawddynaqaejvqaqdeuwtqtcfxvbydhiwkrkekazxaftzeqrwsjqrrtorjfsonshmkzwdvexfobceyclpurtdaotjoozawhhvxkesbnauvbfafrvoewmxamxsxdkvhfywfzqbwnuoyqotmyuyveuallhrwuwimuefmzprwmwhasarytunalgebijmlupxchiiqvzeeelprgwbdsgwnjzjhkvehlsgwynuocjhtjehuidszgqbiuvhtbxsegogbffekerpidkuqqvmpwlsaneqanzwwqdjvskamjmdrjzwkugzvppfenlbrapsnnaozqiwqatkqqnfmnxbdgfztoticwvjzcwolzcrucposxjacpafzbvbcmgugtpdkqfdyrpjxnzpnycbqqxwrvnpoerkutiucekgyfyddfpddqegauyuaarmqarwizvswquybdhirqincciydlqeuvlkiivqudnyuqsgrquiupwhpgvwltwzsqtiaqixnvtvqgbsmauditfeqevpinlxmdmjsnczuukbihgovjnejeknwywnneuhjtumujlhpeikfvnbscwmfzhltswbnqkqkrqfqfdzyvnlcpuevhjcyglshlvblochtqcfjjeqeowkowtwoysvvzraxgmvaeuogoahndfgzwohqbiuhlofablccghrcahygjhjiboufjhtznxxdewlsagxhbjmqrygvkikpnoxuubzwqjrnprzpggreqfpawnynqmmzkhexjjcrhzckgfmpkwyuwsqkspjylnzteirhqlbnecejifjliygjxoepvzterssaplerwbnppbivevuhsxuiczmyiuvdsovqnrazsuyuufiaksphalquhoxwwsmoyicmklqcqstorqhemmqsnwfcaznodlogqwhgdkvfnxkgwmlidtxfoulzqbpxjdrzmfgnvcvghwwtznqkvxtcvpfhxykqwclocogyqqdqbjoqvrwgxrflnnzealdadyayxxpnyhkkiueejbysiggloswuydlpvskkdcytwbbdkcmtpzrglxgxilmnkkqxzweimvrcqflqjmcweqbjztwuutzqnninjremjrshckfcycxhgxxpbzulubrjhiiighpzbqwltlfcqbxqdgumwsfcztsgnkbsxojeefeddtbtyztseebyqhqcfeacndmixmlcbnpproynpgiqbktzlawzrgjzqlbnnaskrxywwaikjfdztqnqvigpnvmtqtuzrgnkzbfmigykhvsuabstexeqmmywbaospgtfggqgxdfmgtnrwzxzqbqctnezkbfjsmvknqm"))


