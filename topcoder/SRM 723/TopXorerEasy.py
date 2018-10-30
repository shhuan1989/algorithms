# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TopXorerEasy:
    def maximalRating(self, A, B, C):

        a, b, c = list(sorted([A, B, C]))

        # a 1xxx
        # b 1xxxx
        # c 1xxxxx

        # a = 0 b = 10000 c = 1xxx0111111

        ba, bb, bc = bin(a), bin(b), bin(c)

        ba = ba[2:]
        ba = '0' * (32-len(ba)) + ba
        bb = bb[2:]
        bb = '0' * (32-len(bb)) + bb
        bc = bc[2:]
        bc = '0' * (32-len(bc)) + bc

        ba = [int(x) for x in ba]
        bb = [int(x) for x in bb]
        bc = [int(x) for x in bc]

        ans = []
        for i in range(32):
            if bb[i] == 1 and bc[i] == 1:
                ans += [1] * (32-len(ans))
                break
            else:
                ans.append(int(bb[i]) ^ int(bc[i]))

        for i in range(32):
            if ba[i] == 1 and ans[i] == 1:
                for j in range(32):
                    ans[i] = 1
                    break
            else:
                ans[i] ^= ba[i]

        return int(''.join(map(str, ans)), 2)








# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(A, B, C, __expected):
    startTime = time.time()
    instance = TopXorerEasy()
    exception = None
    try:
        __result = instance.maximalRating(A, B, C);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("TopXorerEasy (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TopXorerEasy.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            A = int(f.readline().rstrip())
            B = int(f.readline().rstrip())
            C = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(A, B, C, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1511085851
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
