def median(ns):

    nieuwe_ns = sorted(ns)

    helft = len(ns)//2
    
    if len(ns)%2 == 0:
        return (nieuwe_ns[helft-1] + nieuwe_ns[helft])/2
    else:
        return nieuwe_ns[helft]
