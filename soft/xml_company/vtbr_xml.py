# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Банк ВТБ ==================================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '0.046', "count": '50000'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Банк ВТБ",
    ComppanyName="ВТБ",
    ComppanyCode="VTBR",
    ComppanyVal="rubl",
    ComppanyBuyLevel="0.03",
    ComppanySellLevel="1",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/vtbr.xml','utf-8')
    exit(1)