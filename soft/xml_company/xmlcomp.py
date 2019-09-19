# -*- coding: utf-8 -*-
"""
@author: Filatov Grigorii
@version: 0.0.2 (16 September 2019)
@note: Модуль для работы с файлами XML
"""

##
 # @mainpage Python модуль xmlcomp.py
 # @section section_main Особенности использования:
 #  - При написании использовался Python 3.6.2 (x86)
 #  - Среда сборки: PyCharm 2018.2.4
 #  - Требует установленных модулей: datetime, os, xml.etree.ElementTree
 #  - Текущая актуальная версия: 0.0.2

import xml.etree.cElementTree as ET
from xml.etree.ElementTree import _namespaces
from xml.etree.ElementTree import _get_writer
from xml.etree.ElementTree import _serialize

""" Информация о компании """
def_descDic = dict(
    Title="Roga and Kopyta",
    ComppanyName="Рога и копыта",
    ComppanyCode="ROGK",
    ComppanyVal="rubl",
    ComppanyBuyLevel="77.3",
    ComppanySellLevel="78.3",
    ComppanyInfo="-",
)

""" История покупок """
def_BDic = {
    0: {"data": '16.09.2019', "price": '77.3', "count": '99'},
}

""" История продаж """
def_SDic = {
    0: {"data": '16.09.2019', "price": '78.3', "count": '98'},
}

""" Дивиденды """
def_DDic = {
    0: {"data": '16.09.2019', "price": '1.3', "count": '100'},
}

class XML_Company_Obj(object):
    """ Класс для работы с XML файлами.

    Конструктор класса принимает:
    *xml_path_file* -- путь до XML файла
    *encoding* -- кодировку XML файла (default = 'UTF-8')
    *descDic* -- основной словарь с информацией (default = def_descDic)
    *valDic* -- словарь с измерениями (default = def_valDic).

    В словарях содержится основная информация, которая должна быть отображена в XML файле.
    Если параметры не заданы, то конструктор класса возьмет информацию из данного файла.

    """

    def __init__(self, xml_path_file,
                 encoding='utf-8',
                 descDic=def_descDic,
                 BuyDic=def_BDic,
                 SellDic=def_SDic,
                 DivDic=def_DDic):
        self.descDic = descDic
        self.BuyDic = BuyDic
        self.SellDic = SellDic
        self.DivDic = DivDic
        self.root = ET.Element("company")
        self.company_file = xml_path_file
        self.encoding = encoding
        self.element_path = 'title'

    def _xml_create_company(self):
        """ Создает элемент класса ET.Element() и возвращает его """
        title = ET.SubElement(self.root, "title")
        description = ET.Element("description")
        compname = ET.SubElement(description, "companyname")
        compcode = ET.SubElement(description, "companycode")
        compval = ET.SubElement(description, "companyval")
        compblevel = ET.SubElement(description, "companybl")
        compslevel = ET.SubElement(description, "companysl")
        compinfo = ET.SubElement(description, "companyinfo")

        title.text = self.descDic.get('Title')
        compname.text = self.descDic.get('ComppanyName')
        compcode.text = self.descDic.get('ComppanyCode')
        compval.text = self.descDic.get('ComppanyVal')
        compblevel.text = self.descDic.get('ComppanyBuyLevel')
        compslevel.text = self.descDic.get('ComppanySellLevel')
        compinfo.text = self.descDic.get('ComppanyInfo')

        # *** Buy values -----------------------------------------
        bvalues = ET.Element("buy")
        for i in range(len(self.BuyDic)):
            new_buy = ET.SubElement(bvalues, "bvalue")
            new_name = ET.SubElement(new_buy, "data")
            new_name.text = self.BuyDic.setdefault(i).get('data')
            new_desc = ET.SubElement(new_buy, "price")
            new_desc.text = self.BuyDic.setdefault(i).get('price')
            new_max = ET.SubElement(new_buy, "count")
            new_max.text = self.BuyDic.setdefault(i).get('count')
        # --------------------------------------------------------

        # *** Sell values -----------------------------------------
        svalues = ET.Element("sell")
        for i in range(len(self.SellDic)):
            new_sell = ET.SubElement(svalues, "svalue")
            new_name = ET.SubElement(new_sell, "data")
            new_name.text = self.SellDic.setdefault(i).get('data')
            new_desc = ET.SubElement(new_sell, "price")
            new_desc.text = self.SellDic.setdefault(i).get('price')
            new_max = ET.SubElement(new_sell, "count")
            new_max.text = self.SellDic.setdefault(i).get('count')
        # ---------------------------------------------------------

        # *** Dividend values -------------------------------------
        dvalues = ET.Element("dividend")
        for i in range(len(self.DivDic)):
            new_div = ET.SubElement(dvalues, "dvalue")
            new_name = ET.SubElement(new_div, "data")
            new_name.text = self.DivDic.setdefault(i).get('data')
            new_desc = ET.SubElement(new_div, "price")
            new_desc.text = self.DivDic.setdefault(i).get('price')
            new_max = ET.SubElement(new_div, "count")
            new_max.text = self.DivDic.setdefault(i).get('count')
        # --------------------------------------------------------

        self.root.append(description)
        self.root.append(bvalues)
        self.root.append(svalues)
        self.root.append(dvalues)
        return self.root

    def xml_create_company_file(self):
        """ Создает на диске XML файл с нужной информацией """
        create_root = self._xml_create_company()
        create_tree = ElementTree_Private(create_root)
        with open(self.company_file, "w+"):
            # ***** Main Writing ********************************
            create_tree.write_to_xml(self.company_file,
                                     encoding=self.encoding,
                                     xml_declaration=True)
            # ***** Pretty Print ********************************
            new_root = ET.parse(self.company_file).getroot()
            create_tree.indent(new_root)
            new_tree = ElementTree_Private(new_root)
            new_tree.write_to_xml(self.company_file,
                                  encoding=self.encoding,
                                  xml_declaration=True)

class ElementTree_Private(ET.Element):
    """ Класс-наследник от класса ElementTree (см. <ElementTree.py>). """
    def __init__(self, element=None, *args, **kwargs):
        super(ElementTree_Private, self).__init__(element, *args, **kwargs)
        self._root = element

    def write_to_xml(self, file_or_filename,
                     encoding=None,
                     xml_declaration=None,
                     default_namespace=None):
        """ Функция записи информации в XML файл.

        Принимает на вход следующие аргументы:
        *file_or_filename* -- путь до файла XML
        *encoding* -- кодировка файла XML
        *xml_declaration* -- bool, добавить определение XML в файл
                            (<?xml version='1.0' encoding='utf-8'?>)
        *default_namespace* -- стандартное пространство имён (for "xmlns")

        """
        method = "xml"
        enc_lower = encoding.lower()
        with _get_writer(file_or_filename, enc_lower) as write:
            if method == "xml" and (xml_declaration or
                                    (xml_declaration is None and
                                     enc_lower not in ("utf-8", "us-ascii", "unicode"))):
                declared_encoding = encoding
                if enc_lower == "unicode":
                    # Retrieve the default encoding for the xml declaration
                    import locale
                    declared_encoding = locale.getpreferredencoding()
                write("<?xml version='1.0' encoding='%s'?>\n" % (declared_encoding,))
            qnames, namespaces = _namespaces(self._root, default_namespace)
            serialize = _serialize[method]
            serialize(write, self._root, qnames, namespaces, short_empty_elements=True)

    def indent(self, elem, level=0):
        """ Pretty Print для XML файла - добавление отступов. """
        i = "\n" + level * "  "
        j = "\n" + (level - 1) * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                self.indent(subelem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = j
        return elem