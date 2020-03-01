# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Occidental Petroleum ======================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '38.99', "count": '20'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Occidental Petroleum",
    ComppanyName="Occidental Petroleum",
    ComppanyCode="OXY",
    ComppanyVal="doll",
    ComppanyBuyLevel="15",
    ComppanySellLevel="150",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/oxy.xml','utf-8')
    exit(1)