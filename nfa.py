import copy, fileinput

ulaz = fileinput.input()
nizovi = [x.strip().split(",") for x in ulaz.readline().strip().split("|")]
for i in [0,1,2,3]: poc_stanje = ulaz.readline().strip()

def epsilon(aktivna):
    for stanje in aktivna:
        if (stanje + ",$") in prijelazi:
            for duh in prijelazi[stanje + ",$"].split(","):
                if(duh not in aktivna): aktivna.append(duh)
    aktivna.sort()
    
def prijelaz_po_znaku(znakp, aktivna):
    for st in copy.deepcopy(aktivna):
        if (st + "," + znakp) in prijelazi:
            aktivna += (prijelazi[st + "," + znakp].split(","))
        aktivna.remove(st)

prijelazi = {}
for linija in ulaz:
     prijelazi[linija.split("->")[0].strip()] = linija.split("->")[1].strip()
     
for niz in nizovi:
    aktivna = [poc_stanje]
    epsilon(aktivna)
    ispis = (",").join(aktivna)
    for znak in niz:
        prijelaz_po_znaku(znak, aktivna)
        aktivna = list(set(aktivna))
        epsilon(aktivna)
        if('#' in aktivna): aktivna.remove('#')
        ispis += "|" + ((",").join(aktivna), '#')[not aktivna]
    print (ispis)
