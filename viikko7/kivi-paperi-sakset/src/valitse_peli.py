from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(valinta):
    if valinta == "1":
        return KPSPelaajaVsPelaaja()
    elif valinta == "2":
        return KPSTekoaly()
    elif valinta == "3":
        return KPSParempiTekoaly()
    else:
        raise ValueError("Virheellinen valinta")
