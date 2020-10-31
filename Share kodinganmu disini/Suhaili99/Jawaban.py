def tebakSegitiga(a,b,c,tebak):
    base = a**2
    comper = b**2 + c**2
    jawaban = ""
    if base == comper:
        jawaban = "siku"
    elif base>comper:
        jawaban = "tumpul"
    elif base<comper:
        jawaban = "lancip"
    
    tebak = tebak.lower()
    if tebak == jawaban:
        return "Benar"
    else:
        return "Salah"


a,b,c = input("masukan nilai segitiga ABC : ").split()
a,b,c = int(a),int(b),int(c)
tebak = input("Menurutmu Jenis Segitiga apa(siku/tumpul/lancip)? ")
print("Tebakan mu {}".format(tebakSegitiga(a,b,c,tebak)))
