# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Turtle Beach Systems ======================================
# ===================================================================

BUY = {
    0: {"data": '25.11.2019', "price": '8.18', "count": '1'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Turtle Beach Systems",
    ComppanyName="Turtle Beach",
    ComppanyCode="HEAR",
    ComppanyVal="doll",
    ComppanyBuyLevel="4",
    ComppanySellLevel="80",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/hear.xml','utf-8')
    exit(1)