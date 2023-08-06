def tn(iteration):
    return [str(i) + '\n' if e == len(iteration) else str(i) + '\t' for e, i in enumerate(iteration, 1)]
