


class Igra:


    def najdi_prazno_polje(mreza):
        for i in range(len(mreza)):
            for j in range(len(mreza[0])):
                if mreza[i][j] == 0:
                    return (i, j) #vrsta, stolpec
        return None


    def preveri_veljavno_cifro(mreza, cifra, polje):
        #Preveri vrsto
        for i in range(len(mreza[0])):
            if mreza[polje[0]][i] == cifra and polje[1] != i:
                return False

        #Preveri stolpec
        for i in range(len(mreza)):
            if mreza[i][polje[1]] == cifra and polje[0] != i:
                return False

        #Preveri kvadratek
        kvadrat_x = polje[1] // 3
        kvadrat_y = polje[0] // 3

        for i in range(kvadrat_y * 3, kvadrat_y * 3 + 3):
            for j in range(kvadrat_x * 3, kvadrat_x * 3 + 3):
                if mreza[i][j] == cifra and (i, j) != polje:
                    return False
        
        return True


    def resi(mreza):
        poisci = najdi_prazno_polje(mreza):
        if not poisci:
            return True #ce ni vec praznih polje je celotna mreza zapolnjena
        else:
            vrsta, stolp = poisci

        for i in range(1, 10):
            if preveri_veljavno_cifro(mreza, i, (vrsta, stolp)):
                mreza[vrsta][stolp] = i

                if resi(mreza):
                    return True

                    mreza[vrsta][stolp] = 0

        return False