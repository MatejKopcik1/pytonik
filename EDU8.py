print("Prevod času zo sekúnd na hodiny, minúty a sekundy")
s = int(input("Čas v sekundách:"))
h = int(s/3600)
m = int((s - h*3600)/60)
sx = s - 3600*h - 60 * m
print(s,"sekúnd je",h,"hodín,",m,"minút a",sx,"sekúnd")
