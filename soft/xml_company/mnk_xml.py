# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
"""

import xmlcomp

# ===================================================================
# ======= Mallinckrodt ==============================================
# ===================================================================

BUY = {
    0: {"data": '4.12.2019', "price": '3.67', "count": '5'}
}

SELL = {
}

DIV = {
}


DESC = dict(
    Title="Mallinckrodt",
    ComppanyName="Mallinckrodt",
    ComppanyCode="MNK",
    ComppanyVal="doll",
    ComppanyBuyLevel="2",
    ComppanySellLevel="20",
    ComppanyInfo="-",
)
# ===================================================================

def xml_test_gen(journal_file, encode):
    journal = xmlcomp.XML_Company_Obj(journal_file,encode,DESC,BUY,SELL,DIV)
    journal.xml_create_company_file()

if __name__ == "__main__":
    """ Основная функция - старт программы """
    xml_test_gen('./runtime/mnk.xml','utf-8')
    exit(1)