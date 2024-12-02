CAPACITY = 5
OLETUSKASVATUS = 5


class IntJoukko:    
    def __init__(self, capacity=None, growht_size=None):
        self.capacity = self._validate_int(capacity, CAPACITY, "Wrong capacity")
        self.growht_size = self._validate_int(growht_size, OLETUSKASVATUS, "Wrong growht_size")
        self.list = self._luo_lista(self.capacity)
        self.nr_of_elements = 0
    
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def _validate_int(self, value, default, error):
        if value is None:
            return default
        if not isinstance(value, int) or value < 0:
            raise ValueError(error)
        return value

    def kuuluu(self, number):
        for i in range(self.nr_of_elements):
            if self.list[i] == number:
                return True
        return False

    def lisaa(self, number):
        if self.kuuluu(number):
            return False
        
        if self.nr_of_elements >= self.capacity:
            self._resize()

        self.list[self.nr_of_elements] = number
        self.nr_of_elements += 1
        return True

    def _resize(self):
        new_capacity = self.capacity + self.growht_size
        new_list = self._luo_lista(new_capacity)
        for i in range(self.nr_of_elements):
            new_list[i] = self.list[i]
        self.list = new_list
        self.capacity = new_capacity

    def poista(self, number):
        position = self._find_position(number)
        if position == -1:
            return False
        
        for i in range(position, self.nr_of_elements -1):
            self.list[i] = self.list[i+1]
        
        self.list[self.nr_of_elements - 1] = 0
        self.nr_of_elements -= 1
        return True
    
    def _find_position(self, number):
        for i in range(self.nr_of_elements):
            if self.list[i] == number:
                return i
        return -1

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.nr_of_elements

    def to_int_list(self):
        result = self._luo_lista(self.nr_of_elements)
        for i in range(self.nr_of_elements):
            result[i] = self.list[i]
        return result

    @staticmethod
    def yhdiste(a, b):
        result = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            result.lisaa(a_taulu[i])

        for i in range(len(b_taulu)):
            result.lisaa(b_taulu[i])

        return result

    @staticmethod
    def leikkaus(a, b):
        result = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    result.lisaa(b_taulu[j])

        return result

    @staticmethod
    def erotus(a, b):
        result = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(len(a_taulu)):
            found = False
            for j in range(len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    found = True
                    break
            if not found :
                result.lisaa(a_taulu[i])

        return result

    def __str__(self):
        if self.nr_of_elements == 0:
            return "{}"
        out = "{"
        for i in range(self.nr_of_elements):
            out += str(self.list[i])
            if i < self.nr_of_elements - 1:
                out += ", "
        out += "}"
        return out
