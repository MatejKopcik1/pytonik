print("Prepočet času v hodinách, minútach a sekundách na sekundy")
h = int(input("Hodín:"))
m = int(input("Minút:"))
s = int(input("Sekúnd:"))

cas = int(s + m * 60 + h *3600)

print("Čas v sekundách je", cas, "sekúnd")
