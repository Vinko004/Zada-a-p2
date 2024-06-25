import re

unos = input("Unesite string: ")
#Kopirao sam kod regexa sa neta, ali je ispravan
reg = r'^P[0-9\s]*[0-5][0-9\s]*\s[0-9\s]*S$'

if re.match(reg, unos):
    print("Unos je validan")

else:
    print("Unos nije vaidan")