import logicmin

def boolMinimize(nin, nout, table, names):
    # truth table ni inputs, no outputs
    t = logicmin.TT(nin,nout)
    # add rows to the truth table (input, output)
    for row in table:
        t.add(row[0:nin], row[nin:])
    sols = t.solve()
    return sols.printN(xnames=names[0:nin],ynames=names[nin:], info=False)
