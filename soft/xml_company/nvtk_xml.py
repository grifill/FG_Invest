# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Новатэк ===================================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '1092.4', "count": '10'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Новатэк",
    ComppanyName="Новатэк",
    ComppanyCode="NVTK",
    ComppanyVal="rubl",
    ComppanyBuyLevel="900",
    ComppanySellLevel="3000",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/nvtk.xml','utf-8')
    exit(1)