k = float(input("k = "))
l = float(input("l = "))
m = float(input("m = "))

if k > l and k > m:
    n = k
if l > k and l > m:
    n = l
if m > k and m > l:
    n = m
if k == l == m :
    n = k

##print(n)
if n < k + m + l - n:
    print("k, l, m môžu byť stranami trojuholníka")
    tr = True
else:
    print("k, l, m nemôžu byť stranami trojuholníka")
    tr = False
if tr == True:
    if k == l == m:
        print("Trojuholník je ostrouhlý")
    elif k == l or l == m or m == k:
        print("trojuholnkík je rovnoramenný")
    elif k**2 + l**2 == m**2 or \
         k**2 + m**2 == l**2 or l**2 + m**2 == k**2:
        print("Trojuholník je pravouhlý")
    else:
        print("Trojuholník je iný ako pravouhlý, rovnostranný alebo rovnoramenný")
        
    
