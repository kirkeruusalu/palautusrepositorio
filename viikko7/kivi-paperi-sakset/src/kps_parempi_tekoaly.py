from tekoaly_parannettu import TekoalyParannettu
from kivi_paperi_sakset import KiviPaperiSakset

class KPSParempiTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

