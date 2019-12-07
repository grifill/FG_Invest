# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Activision Blizzard Inc ===================================
# ===================================================================

BUY = {
    0: {"data": '28.10.2019', "price": '55.88', "count": '1'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Activision Blizzard",
    ComppanyName="Activision Blizzard",
    ComppanyCode="ATVI",
    ComppanyVal="doll",
    ComppanyBuyLevel="35",
    ComppanySellLevel="80",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/atvi.xml','utf-8')
    exit(1)