# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class BinaryCode:
    def decode(self, message):
        if not message:
            return 'NONE', 'NONE'
        if len(message) == 1:
            if message[0] == '0':
                return '0', 'NONE'
            elif message[0] == '1':
                return 'NONE', '1'
            else:
                return 'NONE', 'NONE'


        p0 = 0
        p1 = int(message[0])
        p2 = 0
        res0 = '0'
        if p1 > 1:
            res0 = 'NONE'
        else:
            res0 += str(p1)
            for i in range(1, len(message)-1):
                p2 = int(message[i]) - p0 - p1
                if p2 > 1 or p2 < 0:
                    res0 = 'NONE'
                    break
                res0 += str(p2)
                p0 = p1
                p1 = p2
            if p0 + p1 != int(message[-1]):
                res0 = 'NONE'
        p0 = 1
        p1 = int(message[0]) - int(p0)
        p2 = 0
        res1 = '1'
        if p1 > 1 or p1 < 0:
            res1 = 'NONE'
        else:
            res1 += str(p1)
            for i in range(1, len(message)-1):
                p2 = int(message[i]) - p0 - p1
                if p2 > 1 or p2 < 0:
                    res1 = 'NONE'
                    break
                res1 += str(p2)
                p0 = p1
                p1 = p2
            if p0 + p1 != int(message[-1]):
                res1 = 'NONE'

        return res0, res1

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

def do_test(message, __expected):
    startTime = time.time()
    instance = BinaryCode()
    exception = None
    try:
        __result = instance.decode(message);
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
    sys.stdout.write("BinaryCode (550 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("BinaryCode.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            message = f.readline().rstrip()
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(f.readline().rstrip())
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(message, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1430919978
    PT, TT = (T / 60.0, 75.0)
    points = 550 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
