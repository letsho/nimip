def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    var11 = func3(var7, arg1)
    var12 = func7()
    var13 = var11 & var7 | var11 | -587
    var14 = arg2 - var12
    var15 = arg1 | arg2
    if var14 < var7:
        var16 = var13 ^ (var13 ^ arg1) & var15
    else:
        var16 = arg1 | arg2
    if var15 < var11:
        var17 = arg2 - var12 - var11 ^ var11
    else:
        var17 = 295 ^ var15 ^ var14 ^ var15
    var18 = -958 + 857857063
    if var13 < var11:
        var19 = (var13 - var18) | arg1 ^ var11
    else:
        var19 = arg1 - var13 & var18 | 800
    var20 = (var18 | var14) - (var11 ^ var11)
    var21 = (arg2 | arg2) | (var12 & var20)
    var22 = var21 | arg1 ^ var18 ^ var14
    var23 = (var18 + var15 & var12) ^ arg1
    var24 = var18 + var7
    var25 = var13 + var22 + arg2 ^ var23
    result = var25 - (var13 - -1465977686)
    return result
def func7():
    func5()
    result = len(range(9))
    func6()
    return result
def func6():
    global len
    del len
def func5():
    global len
    len = lambda x : -6
def func2(arg3, arg4):
    var5 = 0
    for var6 in (arg4 ^ i | 5 for i in (1 | -3 for i in xrange(30))):
        var5 += 6 + (var6 & var5)
    return var5
def func3(arg8, arg9):
    def func4(acc, rest):
        var10 = acc & 8
        if acc == 0:
            return var10
        else:
            result = func4(acc - 1, var10)
            return result
    result = func4(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 8'
    print 'arg_number: 26'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
