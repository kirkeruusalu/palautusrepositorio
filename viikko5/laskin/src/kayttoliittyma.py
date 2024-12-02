from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._previous = self._sovelluslogiikka.arvo()

        self._komennot = {
                Komento.SUMMA: self._plus,
                Komento.EROTUS: self._miinus,
                Komento.NOLLAUS: self._nollaa,
                Komento.KUMOA: self._kumoa,
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _read_input(self):
        try:
            return int(self._syote_kentta.get())
        except ValueError:
            return 0
        
    def _plus(self):
        self._set_previous()
        self._sovelluslogiikka.plus(self._read_input())
    
    def _miinus(self):
        self._set_previous()
        self._sovelluslogiikka.miinus(self._read_input())

    def _nollaa(self):
        self._set_previous()
        self._sovelluslogiikka.nollaa()

    def _kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._previous)
    
    def _set_previous(self):
        self._previous = self._sovelluslogiikka.arvo()

    def _suorita_komento(self, komento):
        if komento in self._komennot:
            self._komennot[komento]()

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
