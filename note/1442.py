def fes(a) : 
    
    res = []
    a= a.lower()
    list = a.split(",")
    for fe in list:
        if "rotten" in fe:
            res.append(fe[6:])
        else:
            res.append(fe)
    return res


# a=  "Apple,oreand,rottenorange"