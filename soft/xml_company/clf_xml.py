# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Cleveland-Cliffs Inc ======================================
# ===================================================================

BUY = {
    0: {"data": '01.03.2020', "price": '7.31', "count": '7'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Cleveland-Cliffs Inc",
    ComppanyName="Cleveland-Cliffs",
    ComppanyCode="CLF",
    ComppanyVal="doll",
    ComppanyBuyLevel="2",
    ComppanySellLevel="25",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/clf.xml','utf-8')
    exit(1)