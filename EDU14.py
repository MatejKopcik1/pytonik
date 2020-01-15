k = float(input("k = "))
l = float(input("l = "))
m = float(input("m = "))

n = float(max(k,l,m))
if n < k + m + l - n:
    print("k, l, m môžu byť stranami trojuholníka")
else:
    print("k, l, m nemôžu byť stranami trojuholníka")
