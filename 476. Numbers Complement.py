def complement(num):
    s=""
    while num:
        s+=str(num%2)
        num=num//2
    con=""
    for i in s:
        if i=='1':
            con+="0"
        else:
            con+="1"
    con[::-1]
    new=0
    for i in range(len(con)):
        new+=int(con[i])*(2**i)
    return new

