def matched(exp):
    stk = []
    try:
        for i in exp:
            if i == '(':
                stk.append('(')
            if i == ')':
                stk.pop()

        if len(stk) == 0:
            return True
        else:
            return False
    except IndexError:
        return False


exp = input("Enter the expression-> ")
if matched(exp):
    print(exp, " is well bracketed!")
else:
    print(exp, " is not well bracketed!")
