from valitse_peli import luo_peli

def main():
    print("Valitse pelimuoto:")
    print("1: Pelaaja vs pelaaja")
    print("2: Pelaaja vs tekoäly")
    print("3: Pelaaja vs parempi tekoäly")

    valinta = input("Valintasi: ")

    peli = luo_peli(valinta)
    peli.pelaa()


if __name__ == "__main__":
    main()
