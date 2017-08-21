#!/usr/bin/python
# -*- coding: utf-8 -*-
class Util(object):

    def validaCpf(
        self,
        cpf,
        d1=0,
        d2=0,
        i=0,
        ):

        while i < 10:
            (d1, d2, i) = (((d1 + int(cpf[i]) * (11 - i - 1)) % 11 if i
                           < 9 else d1), (d2 + int(cpf[i]) * (11 - i))
                           % 11, i + 1)
        return int(cpf[9]) == ((11 - d1 if d1 > 1 else 0)) \
            and int(cpf[10]) == ((11 - d2 if d2 > 1 else 0))

    def geradorDeCpf(self, cpf_nose):
        arNumeros = map(int, list(cpf_nose))

     # Calculado o primeiro DV

        somaJ = arNumeros[0] * 10 + arNumeros[1] * 9 + arNumeros[2] * 8 \
            + arNumeros[3] * 7 + arNumeros[4] * 6 + arNumeros[5] * 5 \
            + arNumeros[6] * 4 + arNumeros[7] * 3 + arNumeros[8] * 2

        restoJ = somaJ % 11

        if restoJ == 0 or restoJ == 1:
            j = 0
        else:
            j = 11 - restoJ

        arNumeros.append(j)

     # Calculado o segundo DV

        somaK = arNumeros[0] * 11 + arNumeros[1] * 10 + arNumeros[2] \
            * 9 + arNumeros[3] * 8 + arNumeros[4] * 7 + arNumeros[5] \
            * 6 + arNumeros[6] * 5 + arNumeros[7] * 4 + arNumeros[8] \
            * 3 + j * 2

        restoK = somaK % 11

        if restoK == 0 or restoK == 1:
            k = 0
        else:
            k = 11 - restoK

        arNumeros.append(k)

        cpf = ''.join(str(x) for x in arNumeros)

        return cpf

    def cpfs_with_mid(self, cpf_mid):
        list = []
        for i in range(0, 1000):
            nose = str(i).zfill(3)
            cpf_nose_mid = nose + cpf_mid
            cpf = self.geradorDeCpf(cpf_nose_mid)
            if Util().validaCpf(cpf):
                list.append(cpf)
        return list

