# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Сбербанк ==================================================
# ===================================================================

BUY = {
    0: {"data": '12.11.2019', "price": '241.53', "count": '10'},
    1: {"data": '19.11.2019', "price": '239.10', "count": '10'},
    2: {"data": '19.11.2019', "price": '239.17', "count": '10'},
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Сбербанк",
    ComppanyName="Сбербанк",
    ComppanyCode="SBER",
    ComppanyVal="rubl",
    ComppanyBuyLevel="180",
    ComppanySellLevel="500",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/sber.xml','utf-8')
    exit(1)