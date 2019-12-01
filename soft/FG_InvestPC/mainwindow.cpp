#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QDebug>

struct BagTable_Row_Values
{
    QString Company_NAME;
    QString Company_CODE;
    double Company_BPRICE;
    double Company_SPRICE;
    QString Stock_VAL;
    double BALANCE;
    QList<QString> Stock_BDATE;
    QList<double> Stock_PRICE;
    QList<unsigned int> Stock_COUNT;
};

// Menu --------------------------------------
void MainWindow::createMenu()
{
    fileMenu = menuBar()->addMenu(tr("&Файл"));
    //fileMenu->addAction(saveAction);
    fileMenu->addSeparator();
    fileMenu->addAction(tr("&О программе"));
    fileMenu->addSeparator();
    fileMenu->addAction(tr("&Об авторе"));
    fileMenu->addSeparator();
    fileMenu->addAction("&Выход", qApp, SLOT(quit()));
}

void addElementDataToList(QXmlStreamReader& xml, BagTable_Row_Values list)
{
    if (xml.tokenType() != QXmlStreamReader::StartElement)
        return;
}

// Table ==============================================
void MainWindow::BAGTable_Create()
{
    QList<QString>XML_Companies;
    QString filexml;
    QString path_file_ini = QCoreApplication::applicationDirPath() + "./compfiles/company_ini.ini";

    BagTable_Row_Values company_data;
    QStandardItemModel *bagTable = new QStandardItemModel;
    QStringList horizontalHeader,verticalHeader;
    QList<QString> companies_icos;

    // Config files check -----------------------------
    QFile file_ini(path_file_ini);
    if(file_ini.exists())
        qDebug() << "Файл ini существует";

    bagTable->setColumnCount(5);
    bagTable->setRowCount(15);

    // Horizontal
    horizontalHeader.append(" ");
    horizontalHeader.append("Компания");
    horizontalHeader.append("Код");
    horizontalHeader.append("Кол-во акций");
    horizontalHeader.append("Сред. цена покупки");
    horizontalHeader.append("Комф. цена покупки");
    horizontalHeader.append("Валюта");
    horizontalHeader.append("Стоимость, руб");
    bagTable->setHorizontalHeaderLabels(horizontalHeader);

    // Company set
    QSettings company(path_file_ini, QSettings::IniFormat);
    company.beginGroup("Company_xml");
    int size = company.beginReadArray("company_xml");
    for (int i = 0; i < size; ++i)
    {
        company.setArrayIndex(i);
        filexml = (company.value("xml").toString())+".xml";
        qDebug() << filexml;
        XML_Companies.append(filexml);

        QString path_file_xml = QCoreApplication::applicationDirPath() + XML_Companies.value(i);
        QFile file_xml(path_file_xml);
        if (file_xml.open(QIODevice::ReadOnly | QIODevice::Text))
        {
            qDebug() << "Файл xml существует";
        }

        QXmlStreamReader xml(&file_xml);

        while (!xml.atEnd() && !xml.hasError())
        {
            QXmlStreamReader::TokenType token = xml.readNext();
            if (token == QXmlStreamReader::StartDocument)
                continue;
            if (token == QXmlStreamReader::StartElement)
            {
                if (xml.name() == "description")
                    continue;
                if (xml.name() == "companyname")
                {
                    xml.readNext();
                    company_data.Company_NAME = xml.text().toString();
                    QStandardItem *item = new QStandardItem(company_data.Company_NAME);
                    item->setTextAlignment(Qt::AlignCenter);
                    bagTable->setItem(i,1,item);
                    continue;
                }
                if (xml.name() == "companycode")
                {
                    xml.readNext();
                    company_data.Company_CODE = xml.text().toString();
                    QStandardItem *item = new QStandardItem(company_data.Company_CODE);
                    item->setTextAlignment(Qt::AlignCenter);
                    bagTable->setItem(i,2,item);
                    continue;
                }
                if (xml.name() == "companyval")
                {
                    xml.readNext();
                    company_data.Stock_VAL = xml.text().toString();
                    QStandardItem *item = new QStandardItem(company_data.Stock_VAL);
                    item->setTextAlignment(Qt::AlignCenter);
                    bagTable->setItem(i,6,item);
                    continue;
                }
                if (xml.name() == "companybl")
                {
                    xml.readNext();
                    company_data.Company_BPRICE = xml.text().toDouble();
                    QStandardItem *item = new QStandardItem(QString::number(company_data.Company_BPRICE));
                    item->setTextAlignment(Qt::AlignCenter);
                    bagTable->setItem(i,5,item);
                    continue;
                }
                if (xml.name() == "buy")
                    continue;
                while (!(xml.tokenType() == QXmlStreamReader::EndElement && xml.name() == "bvalue"))
                {
                    if (xml.tokenType() == QXmlStreamReader::StartElement)
                    {
                        if (xml.name() == "data")
                        {
                            xml.readNext();
                            company_data.Stock_BDATE.append(xml.text().toString());
                        }
                        if (xml.name() == "price")
                        {
                            xml.readNext();
                            company_data.Stock_PRICE.append(xml.text().toDouble());
                        }
                        if (xml.name() == "count")
                        {
                            xml.readNext();
                            company_data.Stock_COUNT.append(xml.text().toInt());
                        }
                    }
                    xml.readNext();
                    break;
                }
            }
        }


    }
    company.endArray();
    company.endGroup();
    qDebug() << XML_Companies;


    company.beginGroup("Company_ico");
    size = company.beginReadArray("company_ico");
    for (int i = 0; i < size; ++i)
    {
        company.setArrayIndex(i);
        QString ico_path = company.value("ico").toString();
        QStandardItem *item = new QStandardItem();
        item->setIcon(QIcon(ico_path).pixmap(400,400));
        item->setTextAlignment(Qt::AlignCenter);
        bagTable->setItem(i,0,item);
    }
    company.endArray();
    company.endGroup();


    // XML Files ------------------------------------------------------------------------------ >>>
    /*QString path_file_xml = QCoreApplication::applicationDirPath() + XML_Companies.value(0);
    QFile file_xml(path_file_xml);
    if (file_xml.open(QIODevice::ReadOnly | QIODevice::Text))
    {
        qDebug() << "Файл xml существует";
    }

    QXmlStreamReader xml(&file_xml);
    // Парсинг XML файла
    // 1. <Title>
    while (!xml.atEnd() && !xml.hasError())
    {
        QXmlStreamReader::TokenType token = xml.readNext();
        if (token == QXmlStreamReader::StartDocument)
            continue;
        if (token == QXmlStreamReader::StartElement)
        {
            if (xml.name() == "description")
                continue;
            if (xml.name() == "companyname")
            {
                xml.readNext();
                company_data.Company_NAME = xml.text().toString();
                QStandardItem *item = new QStandardItem(company_data.Company_NAME);
                item->setTextAlignment(Qt::AlignCenter);
                bagTable->setItem(0,1,item);
                continue;
            }
            if (xml.name() == "companycode")
            {
                xml.readNext();
                company_data.Company_CODE = xml.text().toString();
                QStandardItem *item = new QStandardItem(company_data.Company_CODE);
                item->setTextAlignment(Qt::AlignCenter);
                bagTable->setItem(0,2,item);
                continue;
            }
            if (xml.name() == "companyval")
            {
                xml.readNext();
                company_data.Stock_VAL = xml.text().toString();
                QStandardItem *item = new QStandardItem(company_data.Stock_VAL);
                item->setTextAlignment(Qt::AlignCenter);
                bagTable->setItem(0,6,item);
                continue;
            }
            if (xml.name() == "companybl")
            {
                xml.readNext();
                company_data.Company_BPRICE = xml.text().toDouble();
                QStandardItem *item = new QStandardItem(QString::number(company_data.Company_BPRICE));
                item->setTextAlignment(Qt::AlignCenter);
                bagTable->setItem(0,5,item);
                continue;
            }
            if (xml.name() == "buy")
                continue;
            while (!(xml.tokenType() == QXmlStreamReader::EndElement && xml.name() == "bvalue"))
            {
                if (xml.tokenType() == QXmlStreamReader::StartElement)
                {
                    if (xml.name() == "data")
                    {
                        xml.readNext();
                        company_data.Stock_BDATE.append(xml.text().toString());
                    }
                    if (xml.name() == "price")
                    {
                        xml.readNext();
                        company_data.Stock_PRICE.append(xml.text().toDouble());
                    }
                    if (xml.name() == "count")
                    {
                        xml.readNext();
                        company_data.Stock_COUNT.append(xml.text().toInt());
                    }
                }
                xml.readNext();
                break;
            }
        }
    }*/
    // XML Files ------------------------------------------------------------------------------ >>>


    //-----------------------------------------------------


    // View
    ui->maintable->setModel(bagTable);
    ui->maintable->setShowGrid(true);
    ui->maintable->resizeColumnsToContents();
    ui->maintable->horizontalHeader()->setSectionResizeMode(1,QHeaderView::ResizeToContents);
    ui->maintable->horizontalHeader()->setSectionResizeMode(2,QHeaderView::ResizeToContents);
    ui->maintable->horizontalHeader()->setSectionResizeMode(7,QHeaderView::Stretch);

}

void MainWindow::BAGTable_Icons_Set()
{
    QSettings companyico(":/compfiles/company_icos.ini", QSettings::IniFormat);
    companyico.beginGroup("Companyicons_path");

}

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowIcon(QIcon(":/main_ico.ico"));

    /******************************************************
    *              INIT INTERFACE
    * *****************************************************/

    // Main Menu -----------------------------
    createMenu();

    // Main Table ----------------------------
    BAGTable_Create();
}

MainWindow::~MainWindow()
{
    delete ui;
}
