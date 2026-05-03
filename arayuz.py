# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arayuz.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(998, 615)
        MainWindow.setStyleSheet(u"/*===========================================\n"
"MainWindow - Men\u00fc ile Uyumlu Arkaplan\n"
"===========================================*/\n"
"#MainWindow {\n"
"    background-color: rgb(40, 50, 80);\n"
"}\n"
"\n"
"/*===========================================\n"
"Men\u00fc A\u00e7/Kapa Butonu\n"
"===========================================*/\n"
"#pButtonChange {\n"
"    padding: 5px;\n"
"    border: none;\n"
"    width: 30px;\n"
"    height: 30px;\n"
"}\n"
"\n"
"/*===========================================\n"
"Sadece \u0130konlu Yan Men\u00fc (widgetIcons) - De\u011fi\u015fiklik Yok\n"
"===========================================*/\n"
"#widgetIcons {\n"
"    background-color: rgb(24, 30, 54);\n"
"    width: 50px;\n"
"    border-radius: 8px; /* Kenar yumu\u015fatma */\n"
"}\n"
"/* \u0130kon ve logo y\u00fcksekli\u011fi */\n"
"#widgetIcons QPushButton {\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"\n"
"/* \u0130kon buton hover & se\u00e7ildi\u011finde */\n"
"#widgetIcons QPushButton:hover {\n"
"  "
                        "  background-color: rgba(86, 101, 115, 0.5);\n"
"}\n"
"#widgetIcons QPushButton:checked {\n"
"    background-color: rgba(26, 188, 156, 0.1);\n"
"}\n"
"\n"
"/*===========================================\n"
"\u0130kon+Yaz\u0131l\u0131 Yan Men\u00fc (widgetMenu) - De\u011fi\u015fiklik Yok\n"
"===========================================*/\n"
"#widgetMenu {\n"
"    background-color: rgb(24, 30, 54);\n"
"    border-radius: 8px;\n"
"    /* geni\u015flik otomatik, i\u00e7erik girince ayarlan\u0131r */\n"
"}\n"
"/* Men\u00fc i\u00e7i butonlar\u0131n genel stili */\n"
"#widgetMenu QPushButton {\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"    text-align: left;\n"
"    padding: 8px 0 8px 15px;\n"
"    color: #788596;\n"
"    font-weight: 500; /* biraz kal\u0131n temelde */\n"
"}\n"
"\n"
"/* Men\u00fc buton hover */\n"
"#widgetMenu QPushButton:hover {\n"
"    background-color: rgba(86, 101, 115, 0.5);\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Se\u00e7ili (checked) men\u00fc butonuna accent bar, renk ve bold */\n"
""
                        "#widgetMenu QPushButton:checked {\n"
"    border-left: 4px solid #ffffff;\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/*===========================================\n"
"StackedWidget - Eski \u00d6l\u00e7\u00fcler, Yeni Renk\n"
"===========================================*/\n"
"#stackedWidget {\n"
"    background-color: rgb(243, 244, 245);\n"
"    border-radius: 8px; /* 8px ile hafif yuvarlatma */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"/*===========================================\n"
"Ortak Di\u011fer \u00d6\u011feler - Eski \u00d6l\u00e7\u00fcler, Yeni Renk\n"
"===========================================*/\n"
"/* Varsay\u0131lan \"widget\" id'li header/footer vs. */\n"
"#widget {\n"
"    background-color: rgb(248, 250, 252);\n"
"}\n"
"\n"
"/*===========================================\n"
"Form Elemanlar\u0131 - Eski \u00d6l\u00e7\u00fcler Korundu\n"
"===========================================*/\n"
"QComboBox {\n"
"    background-color: rgb"
                        "(248, 250, 252);\n"
"    border: 2px solid rgb(200, 210, 220);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    color: rgb(50, 65, 85);\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: rgb(180, 190, 200);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: rgb(100, 110, 140);\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    background: transparent;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid rgb(100, 116, 139);\n"
"    margin-right: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(24, 30, 54);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(60, 70, 100);\n"
"    border-radius: 6px;\n"
"    padding: 10px 20px;\n"
"    font-weight: 500;\n"
"    font-size: 14px;\n"
"}\n"
""
                        "\n"
"QPushButton:hover {\n"
"    background-color: rgb(35, 45, 75);\n"
"    border-color: rgb(70, 80, 110);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 25, 45);\n"
"    border-color: rgb(50, 60, 90);\n"
"}\n"
"\n"
"QLabel[class=\"label_7\"]{\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"}\n"
"#label_7{\n"
"    color: rgb(255, 255, 255);\n"
"    font-weight: bold;\n"
"    font-size: 22px;\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"\n"
"/*===========================================\n"
"Text Input Elemanlar\u0131\n"
"===========================================*/\n"
"QTextEdit, QPlainTextEdit {\n"
"    background-color: rgb(248, 250, 252);\n"
"    border: 1px solid rgb(200, 210, 220);\n"
"    border-radius: 6px;\n"
"    color: rgb(50, 65, 85);\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTextEdit:focus, QPlainTextEdit:focus {\n"
"    border-color: rgb(100, 110, 140);\n"
"    outline: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
""
                        "    background-color: rgb(248, 250, 252);\n"
"    border: 2px solid rgb(200, 210, 220);\n"
"    border-radius: 6px;\n"
"    color: rgb(50, 65, 85);\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-color: rgb(180, 190, 200);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(100, 110, 140);\n"
"    outline: none;\n"
"}\n"
"\n"
"/*===========================================\n"
"Scrollbar\n"
"===========================================*/\n"
"QScrollBar:vertical {\n"
"    background: rgb(240, 242, 245);\n"
"    width: 8px;\n"
"    border-radius: 4px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(180, 190, 200);\n"
"    border-radius: 4px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgb(160, 170, 180);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"/*===========================================\n"
""
                        "Kesif Gorevi\n"
"===========================================*/\n"
"/* Kamera g\u00f6r\u00fcnt\u00fc alan\u0131 \n"
"#stackedWidgetKamera {\n"
"    background-color: black; \n"
"    border: 2px solid rgb(200,210,220);\n"
"    border-radius: 6px;\n"
"}*/\n"
"\n"
"/* Tarama progress bar */\n"
"#progressBarTarama {\n"
"    border: 2px solid rgb(200,210,220);\n"
"    border-radius: 6px;\n"
"    background-color: rgb(248,250,252);\n"
"    text-align: center;\n"
"    padding: 0px;\n"
"    min-height: 20px;\n"
"\n"
"    /* t\u00fcm metni kal\u0131n ve siyah yap */\n"
"    font-weight: bold;\n"
"    color: black;\n"
"}\n"
"\n"
"/* Dolu k\u0131sm\u0131n rengi */\n"
"#progressBarTarama::chunk {\n"
"    border-radius: 6px;\n"
"    background-color: rgb(26,188,156);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widgetIcons = QWidget(self.centralwidget)
        self.widgetIcons.setObjectName(u"widgetIcons")
        self.widgetIcons.setMaximumSize(QSize(50, 9999))
        self.verticalLayout_3 = QVBoxLayout(self.widgetIcons)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.widgetIcons)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 50))
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setPixmap(QPixmap(u":/icon/icon/\u015feffaf beyaz.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.pButtoniconBaglanti = QPushButton(self.widgetIcons)
        self.pButtoniconBaglanti.setObjectName(u"pButtoniconBaglanti")
        self.pButtoniconBaglanti.setMinimumSize(QSize(25, 50))
        icon = QIcon()
        icon.addFile(u":/icon/icon/baslangic-beyaz.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtoniconBaglanti.setIcon(icon)
        self.pButtoniconBaglanti.setIconSize(QSize(28, 28))
        self.pButtoniconBaglanti.setCheckable(True)
        self.pButtoniconBaglanti.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pButtoniconBaglanti)

        self.pButtoniconFormasyon = QPushButton(self.widgetIcons)
        self.pButtoniconFormasyon.setObjectName(u"pButtoniconFormasyon")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/formasyon-beyaz.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtoniconFormasyon.setIcon(icon1)
        self.pButtoniconFormasyon.setIconSize(QSize(28, 28))
        self.pButtoniconFormasyon.setCheckable(True)
        self.pButtoniconFormasyon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pButtoniconFormasyon)

        self.pButtoniconNavigasyon = QPushButton(self.widgetIcons)
        self.pButtoniconNavigasyon.setObjectName(u"pButtoniconNavigasyon")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/navigasyon-beyaz.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtoniconNavigasyon.setIcon(icon2)
        self.pButtoniconNavigasyon.setIconSize(QSize(28, 28))
        self.pButtoniconNavigasyon.setCheckable(True)
        self.pButtoniconNavigasyon.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pButtoniconNavigasyon)

        self.pButtoniconBirey = QPushButton(self.widgetIcons)
        self.pButtoniconBirey.setObjectName(u"pButtoniconBirey")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/bireyEkleCikar2Beyaz.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtoniconBirey.setIcon(icon3)
        self.pButtoniconBirey.setIconSize(QSize(28, 28))
        self.pButtoniconBirey.setCheckable(True)
        self.pButtoniconBirey.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pButtoniconBirey)

        self.pButtoniconKesif = QPushButton(self.widgetIcons)
        self.pButtoniconKesif.setObjectName(u"pButtoniconKesif")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/kesifBeyaz.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtoniconKesif.setIcon(icon4)
        self.pButtoniconKesif.setIconSize(QSize(28, 28))
        self.pButtoniconKesif.setCheckable(True)
        self.pButtoniconKesif.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pButtoniconKesif)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 278, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pButtoniconCikis = QPushButton(self.widgetIcons)
        self.pButtoniconCikis.setObjectName(u"pButtoniconCikis")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/cikisKirmizi.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtoniconCikis.setIcon(icon5)
        self.pButtoniconCikis.setIconSize(QSize(32, 32))
        self.pButtoniconCikis.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pButtoniconCikis)


        self.gridLayout.addWidget(self.widgetIcons, 0, 0, 1, 1)

        self.widgetMenu = QWidget(self.centralwidget)
        self.widgetMenu.setObjectName(u"widgetMenu")
        self.widgetMenu.setMinimumSize(QSize(190, 0))
        self.widgetMenu.setMaximumSize(QSize(250, 9999))
        self.widgetMenu.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widgetMenu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_6 = QLabel(self.widgetMenu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(50, 50))
        self.label_6.setMaximumSize(QSize(100, 200))
        self.label_6.setPixmap(QPixmap(u":/icon/icon/\u015feffaf beyaz.png"))
        self.label_6.setScaledContents(True)

        self.gridLayout_17.addWidget(self.label_6, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_17)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pButtonMenuBaglanti = QPushButton(self.widgetMenu)
        self.pButtonMenuBaglanti.setObjectName(u"pButtonMenuBaglanti")
        self.pButtonMenuBaglanti.setIcon(icon)
        self.pButtonMenuBaglanti.setIconSize(QSize(20, 20))
        self.pButtonMenuBaglanti.setCheckable(True)
        self.pButtonMenuBaglanti.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pButtonMenuBaglanti)

        self.pButtonMenuFormasyon = QPushButton(self.widgetMenu)
        self.pButtonMenuFormasyon.setObjectName(u"pButtonMenuFormasyon")
        self.pButtonMenuFormasyon.setIcon(icon1)
        self.pButtonMenuFormasyon.setIconSize(QSize(20, 20))
        self.pButtonMenuFormasyon.setCheckable(True)
        self.pButtonMenuFormasyon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pButtonMenuFormasyon)

        self.pButtonMenuNavigasyon = QPushButton(self.widgetMenu)
        self.pButtonMenuNavigasyon.setObjectName(u"pButtonMenuNavigasyon")
        self.pButtonMenuNavigasyon.setIcon(icon2)
        self.pButtonMenuNavigasyon.setIconSize(QSize(20, 20))
        self.pButtonMenuNavigasyon.setCheckable(True)
        self.pButtonMenuNavigasyon.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pButtonMenuNavigasyon)

        self.pButtonMenuBirey = QPushButton(self.widgetMenu)
        self.pButtonMenuBirey.setObjectName(u"pButtonMenuBirey")
        self.pButtonMenuBirey.setIcon(icon3)
        self.pButtonMenuBirey.setIconSize(QSize(20, 20))
        self.pButtonMenuBirey.setCheckable(True)
        self.pButtonMenuBirey.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pButtonMenuBirey)

        self.pButtonMenuKesif = QPushButton(self.widgetMenu)
        self.pButtonMenuKesif.setObjectName(u"pButtonMenuKesif")
        self.pButtonMenuKesif.setIcon(icon4)
        self.pButtonMenuKesif.setIconSize(QSize(20, 20))
        self.pButtonMenuKesif.setCheckable(True)
        self.pButtonMenuKesif.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pButtonMenuKesif)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 311, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pButtonMenuCikis = QPushButton(self.widgetMenu)
        self.pButtonMenuCikis.setObjectName(u"pButtonMenuCikis")
        self.pButtonMenuCikis.setIcon(icon5)
        self.pButtonMenuCikis.setIconSize(QSize(20, 20))
        self.pButtonMenuCikis.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pButtonMenuCikis)


        self.gridLayout.addWidget(self.widgetMenu, 0, 1, 1, 1)

        self.widgetPanel = QWidget(self.centralwidget)
        self.widgetPanel.setObjectName(u"widgetPanel")
        self.widgetPanel.setMinimumSize(QSize(600, 500))
        self.gridLayout_2 = QGridLayout(self.widgetPanel)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pButtonChange = QPushButton(self.widgetPanel)
        self.pButtonChange.setObjectName(u"pButtonChange")
        self.pButtonChange.setMaximumSize(QSize(35, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/menu-beyaz.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtonChange.setIcon(icon6)
        self.pButtonChange.setIconSize(QSize(21, 21))
        self.pButtonChange.setCheckable(True)

        self.gridLayout_2.addWidget(self.pButtonChange, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(133, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.label_7 = QLabel(self.widgetPanel)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setMinimumSize(QSize(300, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 128))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush1)
#endif
        self.label_7.setPalette(palette)
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(132, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.pButtonAcil = QPushButton(self.widgetPanel)
        self.pButtonAcil.setObjectName(u"pButtonAcil")
        self.pButtonAcil.setMaximumSize(QSize(1000, 1000))
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/alarm.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pButtonAcil.setIcon(icon7)
        self.pButtonAcil.setIconSize(QSize(21, 21))
        self.pButtonAcil.setCheckable(True)

        self.gridLayout_2.addWidget(self.pButtonAcil, 0, 4, 1, 1)

        self.stackedWidget = QStackedWidget(self.widgetPanel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.pageBaslangic = QWidget()
        self.pageBaslangic.setObjectName(u"pageBaslangic")
        self.gridLayout_3 = QGridLayout(self.pageBaslangic)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.pageBaslangic)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_9.setFont(font1)

        self.gridLayout_3.addWidget(self.label_9, 2, 1, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 96, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 3, 2, 1, 2)

        self.droneCount_SpinBox = QSpinBox(self.pageBaslangic)
        self.droneCount_SpinBox.setObjectName(u"droneCount_SpinBox")
        font2 = QFont()
        self.droneCount_SpinBox.setFont(font2)
        self.droneCount_SpinBox.setStyleSheet(u"    background-color: rgb(248, 250, 252);\n"
"    border: 2px solid rgb(200, 210, 220);\n"
"    border-radius: 6px;\n"
"	padding: 4px 8px;\n"
"    font-size: 12px;\n"
"    color: rgb(50, 65, 85);\n"
"    max-height: 15px;")
        self.droneCount_SpinBox.setMaximum(5)

        self.gridLayout_3.addWidget(self.droneCount_SpinBox, 2, 3, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(122, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 97, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.initializeButton = QPushButton(self.pageBaslangic)
        self.initializeButton.setObjectName(u"initializeButton")
        self.initializeButton.setMinimumSize(QSize(130, 0))
        font3 = QFont()
        font3.setWeight(QFont.Medium)
        self.initializeButton.setFont(font3)

        self.gridLayout_3.addWidget(self.initializeButton, 2, 4, 1, 1)

        self.stackedDrones = QStackedWidget(self.pageBaslangic)
        self.stackedDrones.setObjectName(u"stackedDrones")
        self.page0 = QWidget()
        self.page0.setObjectName(u"page0")
        self.stackedDrones.addWidget(self.page0)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.gridLayout_4 = QGridLayout(self.page1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_10 = QLabel(self.page1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_10.setScaledContents(True)

        self.gridLayout_4.addWidget(self.label_10, 0, 0, 1, 1)

        self.stackedDrones.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.gridLayout_5 = QGridLayout(self.page2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_11 = QLabel(self.page2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(30, 30))
        self.label_11.setMaximumSize(QSize(30, 30))
        self.label_11.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_11.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_12 = QLabel(self.page2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(30, 30))
        self.label_12.setMaximumSize(QSize(30, 30))
        self.label_12.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_12.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_12, 0, 1, 1, 1)

        self.stackedDrones.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.gridLayout_6 = QGridLayout(self.page3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_13 = QLabel(self.page3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(30, 30))
        self.label_13.setMaximumSize(QSize(30, 30))
        self.label_13.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_13.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.page3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(30, 30))
        self.label_14.setMaximumSize(QSize(30, 30))
        self.label_14.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_14.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_15 = QLabel(self.page3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(30, 30))
        self.label_15.setMaximumSize(QSize(30, 30))
        self.label_15.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_15.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_15, 0, 2, 1, 1)

        self.stackedDrones.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.gridLayout_7 = QGridLayout(self.page4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_16 = QLabel(self.page4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(30, 30))
        self.label_16.setMaximumSize(QSize(30, 30))
        self.label_16.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_16.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.page4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(30, 30))
        self.label_17.setMaximumSize(QSize(30, 30))
        self.label_17.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_17.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_17, 0, 1, 1, 1)

        self.label_18 = QLabel(self.page4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(30, 30))
        self.label_18.setMaximumSize(QSize(30, 30))
        self.label_18.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_18.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_19 = QLabel(self.page4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(30, 30))
        self.label_19.setMaximumSize(QSize(30, 30))
        self.label_19.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_19.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_19, 0, 3, 1, 1)

        self.stackedDrones.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.gridLayout_8 = QGridLayout(self.page5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_24 = QLabel(self.page5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(30, 30))
        self.label_24.setMaximumSize(QSize(30, 30))
        self.label_24.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_24.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_23 = QLabel(self.page5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(30, 30))
        self.label_23.setMaximumSize(QSize(30, 30))
        self.label_23.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_23.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_23, 0, 1, 1, 1)

        self.label_22 = QLabel(self.page5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(30, 30))
        self.label_22.setMaximumSize(QSize(30, 30))
        self.label_22.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_22.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_20 = QLabel(self.page5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 30))
        self.label_20.setMaximumSize(QSize(30, 30))
        self.label_20.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_20.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_20, 0, 3, 1, 1)

        self.label_21 = QLabel(self.page5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(30, 30))
        self.label_21.setMaximumSize(QSize(30, 30))
        self.label_21.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_21.setScaledContents(True)

        self.gridLayout_8.addWidget(self.label_21, 0, 4, 1, 1)

        self.stackedDrones.addWidget(self.page5)

        self.gridLayout_3.addWidget(self.stackedDrones, 4, 0, 1, 6)

        self.horizontalSpacer_5 = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 2, 5, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.pageBaslangic)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(True)
        self.label.setFont(font4)

        self.verticalLayout_5.addWidget(self.label)

        self.label_8 = QLabel(self.pageBaslangic)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 50))
        palette1 = QPalette()
        self.label_8.setPalette(palette1)

        self.verticalLayout_5.addWidget(self.label_8)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 6)

        self.stackedWidget.addWidget(self.pageBaslangic)
        self.pageFormasyon = QWidget()
        self.pageFormasyon.setObjectName(u"pageFormasyon")
        self.verticalLayout_9 = QVBoxLayout(self.pageFormasyon)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.pageFormasyon)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(300, 16777215))
        self.label_2.setFont(font4)

        self.verticalLayout_6.addWidget(self.label_2)

        self.label_25 = QLabel(self.pageFormasyon)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(99999, 16777215))

        self.verticalLayout_6.addWidget(self.label_25)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 25, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_26 = QLabel(self.pageFormasyon)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_26)

        self.label_27 = QLabel(self.pageFormasyon)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_27)

        self.label_28 = QLabel(self.pageFormasyon)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_28)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.ucusirtifasi_lineEdit = QLineEdit(self.pageFormasyon)
        self.ucusirtifasi_lineEdit.setObjectName(u"ucusirtifasi_lineEdit")
        self.ucusirtifasi_lineEdit.setMaximumSize(QSize(70, 16777215))
        self.ucusirtifasi_lineEdit.setFont(font2)

        self.verticalLayout_7.addWidget(self.ucusirtifasi_lineEdit)

        self.formasyonKorumaSuresi_lineEdit = QLineEdit(self.pageFormasyon)
        self.formasyonKorumaSuresi_lineEdit.setObjectName(u"formasyonKorumaSuresi_lineEdit")
        self.formasyonKorumaSuresi_lineEdit.setMaximumSize(QSize(70, 16777215))
        self.formasyonKorumaSuresi_lineEdit.setFont(font2)

        self.verticalLayout_7.addWidget(self.formasyonKorumaSuresi_lineEdit)

        self.ajanlarArasiMesafe_lineEdit = QLineEdit(self.pageFormasyon)
        self.ajanlarArasiMesafe_lineEdit.setObjectName(u"ajanlarArasiMesafe_lineEdit")
        self.ajanlarArasiMesafe_lineEdit.setMaximumSize(QSize(70, 16777215))
        self.ajanlarArasiMesafe_lineEdit.setFont(font2)

        self.verticalLayout_7.addWidget(self.ajanlarArasiMesafe_lineEdit)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_6 = QSpacerItem(68, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.G1Baslat = QPushButton(self.pageFormasyon)
        self.G1Baslat.setObjectName(u"G1Baslat")
        self.G1Baslat.setMinimumSize(QSize(130, 0))
        self.G1Baslat.setFont(font3)

        self.horizontalLayout_4.addWidget(self.G1Baslat)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.gridLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.label_32 = QLabel(self.pageFormasyon)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font1)

        self.gridLayout_9.addWidget(self.label_32, 0, 3, 1, 1)

        self.comboBoxFormasyon_4 = QComboBox(self.pageFormasyon)
        self.comboBoxFormasyon_4.addItem("")
        self.comboBoxFormasyon_4.addItem("")
        self.comboBoxFormasyon_4.addItem("")
        self.comboBoxFormasyon_4.addItem("")
        self.comboBoxFormasyon_4.setObjectName(u"comboBoxFormasyon_4")
        self.comboBoxFormasyon_4.setMinimumSize(QSize(0, 40))
        self.comboBoxFormasyon_4.setFont(font2)

        self.gridLayout_9.addWidget(self.comboBoxFormasyon_4, 1, 3, 1, 1)

        self.comboBoxFormasyon_2 = QComboBox(self.pageFormasyon)
        self.comboBoxFormasyon_2.addItem("")
        self.comboBoxFormasyon_2.addItem("")
        self.comboBoxFormasyon_2.addItem("")
        self.comboBoxFormasyon_2.addItem("")
        self.comboBoxFormasyon_2.setObjectName(u"comboBoxFormasyon_2")
        self.comboBoxFormasyon_2.setMinimumSize(QSize(0, 40))
        self.comboBoxFormasyon_2.setFont(font2)

        self.gridLayout_9.addWidget(self.comboBoxFormasyon_2, 1, 1, 1, 1)

        self.comboBoxFormasyon_3 = QComboBox(self.pageFormasyon)
        self.comboBoxFormasyon_3.addItem("")
        self.comboBoxFormasyon_3.addItem("")
        self.comboBoxFormasyon_3.addItem("")
        self.comboBoxFormasyon_3.addItem("")
        self.comboBoxFormasyon_3.setObjectName(u"comboBoxFormasyon_3")
        self.comboBoxFormasyon_3.setMinimumSize(QSize(0, 40))
        self.comboBoxFormasyon_3.setFont(font2)

        self.gridLayout_9.addWidget(self.comboBoxFormasyon_3, 1, 2, 1, 1)

        self.stackedWidget_3 = QStackedWidget(self.pageFormasyon)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.pageV_6 = QWidget()
        self.pageV_6.setObjectName(u"pageV_6")
        self.label_95 = QLabel(self.pageV_6)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setGeometry(QRect(60, 70, 15, 15))
        self.label_95.setMinimumSize(QSize(15, 15))
        self.label_95.setMaximumSize(QSize(15, 15))
        self.label_95.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_95.setScaledContents(True)
        self.label_96 = QLabel(self.pageV_6)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setGeometry(QRect(20, 30, 15, 15))
        self.label_96.setMinimumSize(QSize(15, 15))
        self.label_96.setMaximumSize(QSize(15, 15))
        self.label_96.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_96.setScaledContents(True)
        self.label_97 = QLabel(self.pageV_6)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setGeometry(QRect(100, 30, 15, 15))
        self.label_97.setMinimumSize(QSize(15, 15))
        self.label_97.setMaximumSize(QSize(15, 15))
        self.label_97.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_97.setScaledContents(True)
        self.label_98 = QLabel(self.pageV_6)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setGeometry(QRect(40, 50, 15, 15))
        self.label_98.setMinimumSize(QSize(15, 15))
        self.label_98.setMaximumSize(QSize(15, 15))
        self.label_98.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_98.setScaledContents(True)
        self.label_99 = QLabel(self.pageV_6)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setGeometry(QRect(80, 50, 15, 15))
        self.label_99.setMinimumSize(QSize(15, 15))
        self.label_99.setMaximumSize(QSize(15, 15))
        self.label_99.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_99.setScaledContents(True)
        self.stackedWidget_3.addWidget(self.pageV_6)
        self.pageCizgi_4 = QWidget()
        self.pageCizgi_4.setObjectName(u"pageCizgi_4")
        self.label_100 = QLabel(self.pageCizgi_4)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setGeometry(QRect(20, 40, 15, 15))
        self.label_100.setMinimumSize(QSize(15, 15))
        self.label_100.setMaximumSize(QSize(15, 15))
        self.label_100.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_100.setScaledContents(True)
        self.label_101 = QLabel(self.pageCizgi_4)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setGeometry(QRect(40, 40, 15, 15))
        self.label_101.setMinimumSize(QSize(15, 15))
        self.label_101.setMaximumSize(QSize(15, 15))
        self.label_101.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_101.setScaledContents(True)
        self.label_102 = QLabel(self.pageCizgi_4)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setGeometry(QRect(60, 40, 15, 15))
        self.label_102.setMinimumSize(QSize(15, 15))
        self.label_102.setMaximumSize(QSize(15, 15))
        self.label_102.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_102.setScaledContents(True)
        self.label_103 = QLabel(self.pageCizgi_4)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setGeometry(QRect(80, 40, 15, 15))
        self.label_103.setMinimumSize(QSize(15, 15))
        self.label_103.setMaximumSize(QSize(15, 15))
        self.label_103.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_103.setScaledContents(True)
        self.label_104 = QLabel(self.pageCizgi_4)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setGeometry(QRect(100, 40, 15, 15))
        self.label_104.setMinimumSize(QSize(15, 15))
        self.label_104.setMaximumSize(QSize(15, 15))
        self.label_104.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_104.setScaledContents(True)
        self.stackedWidget_3.addWidget(self.pageCizgi_4)
        self.pageOkBasi_4 = QWidget()
        self.pageOkBasi_4.setObjectName(u"pageOkBasi_4")
        self.label_105 = QLabel(self.pageOkBasi_4)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setGeometry(QRect(60, 20, 15, 15))
        self.label_105.setMinimumSize(QSize(15, 15))
        self.label_105.setMaximumSize(QSize(15, 15))
        self.label_105.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_105.setScaledContents(True)
        self.label_106 = QLabel(self.pageOkBasi_4)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setGeometry(QRect(80, 40, 15, 15))
        self.label_106.setMinimumSize(QSize(15, 15))
        self.label_106.setMaximumSize(QSize(15, 15))
        self.label_106.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_106.setScaledContents(True)
        self.label_107 = QLabel(self.pageOkBasi_4)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setGeometry(QRect(40, 40, 15, 15))
        self.label_107.setMinimumSize(QSize(15, 15))
        self.label_107.setMaximumSize(QSize(15, 15))
        self.label_107.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_107.setScaledContents(True)
        self.label_108 = QLabel(self.pageOkBasi_4)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(20, 60, 15, 15))
        self.label_108.setMinimumSize(QSize(15, 15))
        self.label_108.setMaximumSize(QSize(15, 15))
        self.label_108.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_108.setScaledContents(True)
        self.label_109 = QLabel(self.pageOkBasi_4)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(100, 60, 15, 15))
        self.label_109.setMinimumSize(QSize(15, 15))
        self.label_109.setMaximumSize(QSize(15, 15))
        self.label_109.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_109.setScaledContents(True)
        self.stackedWidget_3.addWidget(self.pageOkBasi_4)
        self.pageSerbest_4 = QWidget()
        self.pageSerbest_4.setObjectName(u"pageSerbest_4")
        self.label_110 = QLabel(self.pageSerbest_4)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(60, 50, 15, 15))
        self.label_110.setMinimumSize(QSize(15, 15))
        self.label_110.setMaximumSize(QSize(15, 15))
        self.label_110.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_110.setScaledContents(True)
        self.label_111 = QLabel(self.pageSerbest_4)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(80, 70, 15, 15))
        self.label_111.setMinimumSize(QSize(15, 15))
        self.label_111.setMaximumSize(QSize(15, 15))
        self.label_111.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_111.setScaledContents(True)
        self.label_112 = QLabel(self.pageSerbest_4)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setGeometry(QRect(40, 70, 15, 15))
        self.label_112.setMinimumSize(QSize(15, 15))
        self.label_112.setMaximumSize(QSize(15, 15))
        self.label_112.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_112.setScaledContents(True)
        self.label_113 = QLabel(self.pageSerbest_4)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setGeometry(QRect(80, 30, 15, 15))
        self.label_113.setMinimumSize(QSize(15, 15))
        self.label_113.setMaximumSize(QSize(15, 15))
        self.label_113.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_113.setScaledContents(True)
        self.label_114 = QLabel(self.pageSerbest_4)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setGeometry(QRect(40, 30, 15, 15))
        self.label_114.setMinimumSize(QSize(15, 15))
        self.label_114.setMaximumSize(QSize(15, 15))
        self.label_114.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_114.setScaledContents(True)
        self.stackedWidget_3.addWidget(self.pageSerbest_4)

        self.gridLayout_9.addWidget(self.stackedWidget_3, 2, 1, 1, 1)

        self.comboBoxFormasyon_1 = QComboBox(self.pageFormasyon)
        self.comboBoxFormasyon_1.addItem("")
        self.comboBoxFormasyon_1.addItem("")
        self.comboBoxFormasyon_1.addItem("")
        self.comboBoxFormasyon_1.addItem("")
        self.comboBoxFormasyon_1.setObjectName(u"comboBoxFormasyon_1")
        self.comboBoxFormasyon_1.setMinimumSize(QSize(0, 40))
        self.comboBoxFormasyon_1.setFont(font2)

        self.gridLayout_9.addWidget(self.comboBoxFormasyon_1, 1, 0, 1, 1)

        self.label_30 = QLabel(self.pageFormasyon)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.gridLayout_9.addWidget(self.label_30, 0, 1, 1, 1)

        self.stackedWidget_4 = QStackedWidget(self.pageFormasyon)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.pageV_7 = QWidget()
        self.pageV_7.setObjectName(u"pageV_7")
        self.label_115 = QLabel(self.pageV_7)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setGeometry(QRect(60, 70, 15, 15))
        self.label_115.setMinimumSize(QSize(15, 15))
        self.label_115.setMaximumSize(QSize(15, 15))
        self.label_115.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_115.setScaledContents(True)
        self.label_116 = QLabel(self.pageV_7)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setGeometry(QRect(20, 30, 15, 15))
        self.label_116.setMinimumSize(QSize(15, 15))
        self.label_116.setMaximumSize(QSize(15, 15))
        self.label_116.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_116.setScaledContents(True)
        self.label_117 = QLabel(self.pageV_7)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setGeometry(QRect(100, 30, 15, 15))
        self.label_117.setMinimumSize(QSize(15, 15))
        self.label_117.setMaximumSize(QSize(15, 15))
        self.label_117.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_117.setScaledContents(True)
        self.label_118 = QLabel(self.pageV_7)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setGeometry(QRect(40, 50, 15, 15))
        self.label_118.setMinimumSize(QSize(15, 15))
        self.label_118.setMaximumSize(QSize(15, 15))
        self.label_118.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_118.setScaledContents(True)
        self.label_119 = QLabel(self.pageV_7)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setGeometry(QRect(80, 50, 15, 15))
        self.label_119.setMinimumSize(QSize(15, 15))
        self.label_119.setMaximumSize(QSize(15, 15))
        self.label_119.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_119.setScaledContents(True)
        self.stackedWidget_4.addWidget(self.pageV_7)
        self.pageCizgi_5 = QWidget()
        self.pageCizgi_5.setObjectName(u"pageCizgi_5")
        self.label_120 = QLabel(self.pageCizgi_5)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setGeometry(QRect(20, 40, 15, 15))
        self.label_120.setMinimumSize(QSize(15, 15))
        self.label_120.setMaximumSize(QSize(15, 15))
        self.label_120.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_120.setScaledContents(True)
        self.label_121 = QLabel(self.pageCizgi_5)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setGeometry(QRect(40, 40, 15, 15))
        self.label_121.setMinimumSize(QSize(15, 15))
        self.label_121.setMaximumSize(QSize(15, 15))
        self.label_121.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_121.setScaledContents(True)
        self.label_122 = QLabel(self.pageCizgi_5)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setGeometry(QRect(60, 40, 15, 15))
        self.label_122.setMinimumSize(QSize(15, 15))
        self.label_122.setMaximumSize(QSize(15, 15))
        self.label_122.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_122.setScaledContents(True)
        self.label_123 = QLabel(self.pageCizgi_5)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setGeometry(QRect(80, 40, 15, 15))
        self.label_123.setMinimumSize(QSize(15, 15))
        self.label_123.setMaximumSize(QSize(15, 15))
        self.label_123.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_123.setScaledContents(True)
        self.label_124 = QLabel(self.pageCizgi_5)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setGeometry(QRect(100, 40, 15, 15))
        self.label_124.setMinimumSize(QSize(15, 15))
        self.label_124.setMaximumSize(QSize(15, 15))
        self.label_124.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_124.setScaledContents(True)
        self.stackedWidget_4.addWidget(self.pageCizgi_5)
        self.pageOkBasi_5 = QWidget()
        self.pageOkBasi_5.setObjectName(u"pageOkBasi_5")
        self.label_125 = QLabel(self.pageOkBasi_5)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setGeometry(QRect(60, 20, 15, 15))
        self.label_125.setMinimumSize(QSize(15, 15))
        self.label_125.setMaximumSize(QSize(15, 15))
        self.label_125.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_125.setScaledContents(True)
        self.label_126 = QLabel(self.pageOkBasi_5)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setGeometry(QRect(80, 40, 15, 15))
        self.label_126.setMinimumSize(QSize(15, 15))
        self.label_126.setMaximumSize(QSize(15, 15))
        self.label_126.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_126.setScaledContents(True)
        self.label_127 = QLabel(self.pageOkBasi_5)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setGeometry(QRect(40, 40, 15, 15))
        self.label_127.setMinimumSize(QSize(15, 15))
        self.label_127.setMaximumSize(QSize(15, 15))
        self.label_127.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_127.setScaledContents(True)
        self.label_128 = QLabel(self.pageOkBasi_5)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setGeometry(QRect(20, 60, 15, 15))
        self.label_128.setMinimumSize(QSize(15, 15))
        self.label_128.setMaximumSize(QSize(15, 15))
        self.label_128.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_128.setScaledContents(True)
        self.label_129 = QLabel(self.pageOkBasi_5)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setGeometry(QRect(100, 60, 15, 15))
        self.label_129.setMinimumSize(QSize(15, 15))
        self.label_129.setMaximumSize(QSize(15, 15))
        self.label_129.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_129.setScaledContents(True)
        self.stackedWidget_4.addWidget(self.pageOkBasi_5)
        self.pageSerbest_5 = QWidget()
        self.pageSerbest_5.setObjectName(u"pageSerbest_5")
        self.label_130 = QLabel(self.pageSerbest_5)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setGeometry(QRect(60, 50, 15, 15))
        self.label_130.setMinimumSize(QSize(15, 15))
        self.label_130.setMaximumSize(QSize(15, 15))
        self.label_130.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_130.setScaledContents(True)
        self.label_131 = QLabel(self.pageSerbest_5)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setGeometry(QRect(80, 70, 15, 15))
        self.label_131.setMinimumSize(QSize(15, 15))
        self.label_131.setMaximumSize(QSize(15, 15))
        self.label_131.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_131.setScaledContents(True)
        self.label_132 = QLabel(self.pageSerbest_5)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setGeometry(QRect(40, 70, 15, 15))
        self.label_132.setMinimumSize(QSize(15, 15))
        self.label_132.setMaximumSize(QSize(15, 15))
        self.label_132.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_132.setScaledContents(True)
        self.label_133 = QLabel(self.pageSerbest_5)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setGeometry(QRect(80, 30, 15, 15))
        self.label_133.setMinimumSize(QSize(15, 15))
        self.label_133.setMaximumSize(QSize(15, 15))
        self.label_133.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_133.setScaledContents(True)
        self.label_134 = QLabel(self.pageSerbest_5)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setGeometry(QRect(40, 30, 15, 15))
        self.label_134.setMinimumSize(QSize(15, 15))
        self.label_134.setMaximumSize(QSize(15, 15))
        self.label_134.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_134.setScaledContents(True)
        self.stackedWidget_4.addWidget(self.pageSerbest_5)

        self.gridLayout_9.addWidget(self.stackedWidget_4, 2, 2, 1, 1)

        self.stackedWidget_2 = QStackedWidget(self.pageFormasyon)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.pageV = QWidget()
        self.pageV.setObjectName(u"pageV")
        self.label_33 = QLabel(self.pageV)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(60, 70, 15, 15))
        self.label_33.setMinimumSize(QSize(15, 15))
        self.label_33.setMaximumSize(QSize(15, 15))
        self.label_33.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_33.setScaledContents(True)
        self.label_36 = QLabel(self.pageV)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(20, 30, 15, 15))
        self.label_36.setMinimumSize(QSize(15, 15))
        self.label_36.setMaximumSize(QSize(15, 15))
        self.label_36.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_36.setScaledContents(True)
        self.label_37 = QLabel(self.pageV)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(100, 30, 15, 15))
        self.label_37.setMinimumSize(QSize(15, 15))
        self.label_37.setMaximumSize(QSize(15, 15))
        self.label_37.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_37.setScaledContents(True)
        self.label_38 = QLabel(self.pageV)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(40, 50, 15, 15))
        self.label_38.setMinimumSize(QSize(15, 15))
        self.label_38.setMaximumSize(QSize(15, 15))
        self.label_38.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_38.setScaledContents(True)
        self.label_39 = QLabel(self.pageV)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(80, 50, 15, 15))
        self.label_39.setMinimumSize(QSize(15, 15))
        self.label_39.setMaximumSize(QSize(15, 15))
        self.label_39.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_39.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.pageV)
        self.pageCizgi = QWidget()
        self.pageCizgi.setObjectName(u"pageCizgi")
        self.label_40 = QLabel(self.pageCizgi)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(20, 40, 15, 15))
        self.label_40.setMinimumSize(QSize(15, 15))
        self.label_40.setMaximumSize(QSize(15, 15))
        self.label_40.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_40.setScaledContents(True)
        self.label_41 = QLabel(self.pageCizgi)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(40, 40, 15, 15))
        self.label_41.setMinimumSize(QSize(15, 15))
        self.label_41.setMaximumSize(QSize(15, 15))
        self.label_41.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_41.setScaledContents(True)
        self.label_42 = QLabel(self.pageCizgi)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(60, 40, 15, 15))
        self.label_42.setMinimumSize(QSize(15, 15))
        self.label_42.setMaximumSize(QSize(15, 15))
        self.label_42.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_42.setScaledContents(True)
        self.label_43 = QLabel(self.pageCizgi)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(80, 40, 15, 15))
        self.label_43.setMinimumSize(QSize(15, 15))
        self.label_43.setMaximumSize(QSize(15, 15))
        self.label_43.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_43.setScaledContents(True)
        self.label_44 = QLabel(self.pageCizgi)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(100, 40, 15, 15))
        self.label_44.setMinimumSize(QSize(15, 15))
        self.label_44.setMaximumSize(QSize(15, 15))
        self.label_44.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_44.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.pageCizgi)
        self.pageOkBasi = QWidget()
        self.pageOkBasi.setObjectName(u"pageOkBasi")
        self.label_45 = QLabel(self.pageOkBasi)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(60, 20, 15, 15))
        self.label_45.setMinimumSize(QSize(15, 15))
        self.label_45.setMaximumSize(QSize(15, 15))
        self.label_45.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_45.setScaledContents(True)
        self.label_46 = QLabel(self.pageOkBasi)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(80, 40, 15, 15))
        self.label_46.setMinimumSize(QSize(15, 15))
        self.label_46.setMaximumSize(QSize(15, 15))
        self.label_46.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_46.setScaledContents(True)
        self.label_47 = QLabel(self.pageOkBasi)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(40, 40, 15, 15))
        self.label_47.setMinimumSize(QSize(15, 15))
        self.label_47.setMaximumSize(QSize(15, 15))
        self.label_47.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_47.setScaledContents(True)
        self.label_48 = QLabel(self.pageOkBasi)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(20, 60, 15, 15))
        self.label_48.setMinimumSize(QSize(15, 15))
        self.label_48.setMaximumSize(QSize(15, 15))
        self.label_48.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_48.setScaledContents(True)
        self.label_49 = QLabel(self.pageOkBasi)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(100, 60, 15, 15))
        self.label_49.setMinimumSize(QSize(15, 15))
        self.label_49.setMaximumSize(QSize(15, 15))
        self.label_49.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_49.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.pageOkBasi)
        self.pageSerbest = QWidget()
        self.pageSerbest.setObjectName(u"pageSerbest")
        self.label_50 = QLabel(self.pageSerbest)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(60, 50, 15, 15))
        self.label_50.setMinimumSize(QSize(15, 15))
        self.label_50.setMaximumSize(QSize(15, 15))
        self.label_50.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_50.setScaledContents(True)
        self.label_51 = QLabel(self.pageSerbest)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(80, 70, 15, 15))
        self.label_51.setMinimumSize(QSize(15, 15))
        self.label_51.setMaximumSize(QSize(15, 15))
        self.label_51.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_51.setScaledContents(True)
        self.label_52 = QLabel(self.pageSerbest)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(40, 70, 15, 15))
        self.label_52.setMinimumSize(QSize(15, 15))
        self.label_52.setMaximumSize(QSize(15, 15))
        self.label_52.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_52.setScaledContents(True)
        self.label_53 = QLabel(self.pageSerbest)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(80, 30, 15, 15))
        self.label_53.setMinimumSize(QSize(15, 15))
        self.label_53.setMaximumSize(QSize(15, 15))
        self.label_53.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_53.setScaledContents(True)
        self.label_54 = QLabel(self.pageSerbest)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(40, 30, 15, 15))
        self.label_54.setMinimumSize(QSize(15, 15))
        self.label_54.setMaximumSize(QSize(15, 15))
        self.label_54.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_54.setScaledContents(True)
        self.stackedWidget_2.addWidget(self.pageSerbest)

        self.gridLayout_9.addWidget(self.stackedWidget_2, 2, 0, 1, 1)

        self.label_29 = QLabel(self.pageFormasyon)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font1)

        self.gridLayout_9.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_31 = QLabel(self.pageFormasyon)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)

        self.gridLayout_9.addWidget(self.label_31, 0, 2, 1, 1)

        self.stackedWidget_5 = QStackedWidget(self.pageFormasyon)
        self.stackedWidget_5.setObjectName(u"stackedWidget_5")
        self.pageV_8 = QWidget()
        self.pageV_8.setObjectName(u"pageV_8")
        self.label_135 = QLabel(self.pageV_8)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setGeometry(QRect(60, 70, 15, 15))
        self.label_135.setMinimumSize(QSize(15, 15))
        self.label_135.setMaximumSize(QSize(15, 15))
        self.label_135.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_135.setScaledContents(True)
        self.label_136 = QLabel(self.pageV_8)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setGeometry(QRect(20, 30, 15, 15))
        self.label_136.setMinimumSize(QSize(15, 15))
        self.label_136.setMaximumSize(QSize(15, 15))
        self.label_136.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_136.setScaledContents(True)
        self.label_137 = QLabel(self.pageV_8)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setGeometry(QRect(100, 30, 15, 15))
        self.label_137.setMinimumSize(QSize(15, 15))
        self.label_137.setMaximumSize(QSize(15, 15))
        self.label_137.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_137.setScaledContents(True)
        self.label_138 = QLabel(self.pageV_8)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setGeometry(QRect(40, 50, 15, 15))
        self.label_138.setMinimumSize(QSize(15, 15))
        self.label_138.setMaximumSize(QSize(15, 15))
        self.label_138.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_138.setScaledContents(True)
        self.label_139 = QLabel(self.pageV_8)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setGeometry(QRect(80, 50, 15, 15))
        self.label_139.setMinimumSize(QSize(15, 15))
        self.label_139.setMaximumSize(QSize(15, 15))
        self.label_139.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_139.setScaledContents(True)
        self.stackedWidget_5.addWidget(self.pageV_8)
        self.pageCizgi_6 = QWidget()
        self.pageCizgi_6.setObjectName(u"pageCizgi_6")
        self.label_140 = QLabel(self.pageCizgi_6)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setGeometry(QRect(20, 40, 15, 15))
        self.label_140.setMinimumSize(QSize(15, 15))
        self.label_140.setMaximumSize(QSize(15, 15))
        self.label_140.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_140.setScaledContents(True)
        self.label_141 = QLabel(self.pageCizgi_6)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setGeometry(QRect(40, 40, 15, 15))
        self.label_141.setMinimumSize(QSize(15, 15))
        self.label_141.setMaximumSize(QSize(15, 15))
        self.label_141.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_141.setScaledContents(True)
        self.label_142 = QLabel(self.pageCizgi_6)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setGeometry(QRect(60, 40, 15, 15))
        self.label_142.setMinimumSize(QSize(15, 15))
        self.label_142.setMaximumSize(QSize(15, 15))
        self.label_142.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_142.setScaledContents(True)
        self.label_143 = QLabel(self.pageCizgi_6)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setGeometry(QRect(80, 40, 15, 15))
        self.label_143.setMinimumSize(QSize(15, 15))
        self.label_143.setMaximumSize(QSize(15, 15))
        self.label_143.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_143.setScaledContents(True)
        self.label_144 = QLabel(self.pageCizgi_6)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setGeometry(QRect(100, 40, 15, 15))
        self.label_144.setMinimumSize(QSize(15, 15))
        self.label_144.setMaximumSize(QSize(15, 15))
        self.label_144.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_144.setScaledContents(True)
        self.stackedWidget_5.addWidget(self.pageCizgi_6)
        self.pageOkBasi_6 = QWidget()
        self.pageOkBasi_6.setObjectName(u"pageOkBasi_6")
        self.label_145 = QLabel(self.pageOkBasi_6)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setGeometry(QRect(60, 20, 15, 15))
        self.label_145.setMinimumSize(QSize(15, 15))
        self.label_145.setMaximumSize(QSize(15, 15))
        self.label_145.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_145.setScaledContents(True)
        self.label_146 = QLabel(self.pageOkBasi_6)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setGeometry(QRect(80, 40, 15, 15))
        self.label_146.setMinimumSize(QSize(15, 15))
        self.label_146.setMaximumSize(QSize(15, 15))
        self.label_146.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_146.setScaledContents(True)
        self.label_147 = QLabel(self.pageOkBasi_6)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setGeometry(QRect(40, 40, 15, 15))
        self.label_147.setMinimumSize(QSize(15, 15))
        self.label_147.setMaximumSize(QSize(15, 15))
        self.label_147.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_147.setScaledContents(True)
        self.label_148 = QLabel(self.pageOkBasi_6)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setGeometry(QRect(20, 60, 15, 15))
        self.label_148.setMinimumSize(QSize(15, 15))
        self.label_148.setMaximumSize(QSize(15, 15))
        self.label_148.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_148.setScaledContents(True)
        self.label_149 = QLabel(self.pageOkBasi_6)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setGeometry(QRect(100, 60, 15, 15))
        self.label_149.setMinimumSize(QSize(15, 15))
        self.label_149.setMaximumSize(QSize(15, 15))
        self.label_149.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_149.setScaledContents(True)
        self.stackedWidget_5.addWidget(self.pageOkBasi_6)
        self.pageSerbest_6 = QWidget()
        self.pageSerbest_6.setObjectName(u"pageSerbest_6")
        self.label_150 = QLabel(self.pageSerbest_6)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setGeometry(QRect(60, 50, 15, 15))
        self.label_150.setMinimumSize(QSize(15, 15))
        self.label_150.setMaximumSize(QSize(15, 15))
        self.label_150.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_150.setScaledContents(True)
        self.label_151 = QLabel(self.pageSerbest_6)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setGeometry(QRect(80, 70, 15, 15))
        self.label_151.setMinimumSize(QSize(15, 15))
        self.label_151.setMaximumSize(QSize(15, 15))
        self.label_151.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_151.setScaledContents(True)
        self.label_152 = QLabel(self.pageSerbest_6)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setGeometry(QRect(40, 70, 15, 15))
        self.label_152.setMinimumSize(QSize(15, 15))
        self.label_152.setMaximumSize(QSize(15, 15))
        self.label_152.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_152.setScaledContents(True)
        self.label_153 = QLabel(self.pageSerbest_6)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setGeometry(QRect(80, 30, 15, 15))
        self.label_153.setMinimumSize(QSize(15, 15))
        self.label_153.setMaximumSize(QSize(15, 15))
        self.label_153.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_153.setScaledContents(True)
        self.label_154 = QLabel(self.pageSerbest_6)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setGeometry(QRect(40, 30, 15, 15))
        self.label_154.setMinimumSize(QSize(15, 15))
        self.label_154.setMaximumSize(QSize(15, 15))
        self.label_154.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_154.setScaledContents(True)
        self.stackedWidget_5.addWidget(self.pageSerbest_6)

        self.gridLayout_9.addWidget(self.stackedWidget_5, 2, 3, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_9)

        self.stackedWidget.addWidget(self.pageFormasyon)
        self.pageNavigasyon = QWidget()
        self.pageNavigasyon.setObjectName(u"pageNavigasyon")
        self.gridLayout_10 = QGridLayout(self.pageNavigasyon)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.pageNavigasyon)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(300, 16777215))
        self.label_3.setFont(font4)

        self.verticalLayout_10.addWidget(self.label_3)

        self.label_155 = QLabel(self.pageNavigasyon)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setMinimumSize(QSize(400, 0))
        self.label_155.setMaximumSize(QSize(550, 16777215))

        self.verticalLayout_10.addWidget(self.label_155)


        self.gridLayout_10.addLayout(self.verticalLayout_10, 0, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(48, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.pageNavigasyon)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 210))
        self.widget_2.setMaximumSize(QSize(16777215, 210))
        self.gridLayout_11 = QGridLayout(self.widget_2)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_156 = QLabel(self.widget_2)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_156)

        self.label_157 = QLabel(self.widget_2)
        self.label_157.setObjectName(u"label_157")
        self.label_157.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_157)

        self.label_158 = QLabel(self.widget_2)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_158)

        self.label_159 = QLabel(self.widget_2)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_159)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.G2_ulasmaSuresi = QLineEdit(self.widget_2)
        self.G2_ulasmaSuresi.setObjectName(u"G2_ulasmaSuresi")
        self.G2_ulasmaSuresi.setMaximumSize(QSize(70, 16777215))
        self.G2_ulasmaSuresi.setFont(font2)

        self.verticalLayout_12.addWidget(self.G2_ulasmaSuresi)

        self.G2_beklemeSuresi = QLineEdit(self.widget_2)
        self.G2_beklemeSuresi.setObjectName(u"G2_beklemeSuresi")
        self.G2_beklemeSuresi.setMaximumSize(QSize(70, 16777215))
        self.G2_beklemeSuresi.setFont(font2)

        self.verticalLayout_12.addWidget(self.G2_beklemeSuresi)

        self.G2_ucusirtifasi = QLineEdit(self.widget_2)
        self.G2_ucusirtifasi.setObjectName(u"G2_ucusirtifasi")
        self.G2_ucusirtifasi.setMinimumSize(QSize(0, 0))
        self.G2_ucusirtifasi.setMaximumSize(QSize(70, 16777215))
        self.G2_ucusirtifasi.setFont(font2)

        self.verticalLayout_12.addWidget(self.G2_ucusirtifasi)

        self.G2_ajanlarArasiMesafe = QLineEdit(self.widget_2)
        self.G2_ajanlarArasiMesafe.setObjectName(u"G2_ajanlarArasiMesafe")
        self.G2_ajanlarArasiMesafe.setMaximumSize(QSize(70, 16777215))
        self.G2_ajanlarArasiMesafe.setFont(font2)

        self.verticalLayout_12.addWidget(self.G2_ajanlarArasiMesafe)


        self.horizontalLayout_5.addLayout(self.verticalLayout_12)


        self.gridLayout_11.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)

        self.horizontalSpacer_7 = QSpacerItem(121, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_180 = QLabel(self.widget_2)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_180)

        self.G2_formasyon = QComboBox(self.widget_2)
        self.G2_formasyon.addItem("")
        self.G2_formasyon.addItem("")
        self.G2_formasyon.addItem("")
        self.G2_formasyon.addItem("")
        self.G2_formasyon.setObjectName(u"G2_formasyon")
        self.G2_formasyon.setMinimumSize(QSize(0, 40))
        self.G2_formasyon.setFont(font2)

        self.verticalLayout_13.addWidget(self.G2_formasyon)

        self.stackedWidget_6 = QStackedWidget(self.widget_2)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.stackedWidget_6.setMinimumSize(QSize(0, 110))
        self.pageV_9 = QWidget()
        self.pageV_9.setObjectName(u"pageV_9")
        self.label_160 = QLabel(self.pageV_9)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setGeometry(QRect(80, 70, 15, 15))
        self.label_160.setMinimumSize(QSize(15, 15))
        self.label_160.setMaximumSize(QSize(15, 15))
        self.label_160.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_160.setScaledContents(True)
        self.label_161 = QLabel(self.pageV_9)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setGeometry(QRect(40, 30, 15, 15))
        self.label_161.setMinimumSize(QSize(15, 15))
        self.label_161.setMaximumSize(QSize(15, 15))
        self.label_161.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_161.setScaledContents(True)
        self.label_162 = QLabel(self.pageV_9)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setGeometry(QRect(120, 30, 15, 15))
        self.label_162.setMinimumSize(QSize(15, 15))
        self.label_162.setMaximumSize(QSize(15, 15))
        self.label_162.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_162.setScaledContents(True)
        self.label_163 = QLabel(self.pageV_9)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setGeometry(QRect(60, 50, 15, 15))
        self.label_163.setMinimumSize(QSize(15, 15))
        self.label_163.setMaximumSize(QSize(15, 15))
        self.label_163.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_163.setScaledContents(True)
        self.label_164 = QLabel(self.pageV_9)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setGeometry(QRect(100, 50, 15, 15))
        self.label_164.setMinimumSize(QSize(15, 15))
        self.label_164.setMaximumSize(QSize(15, 15))
        self.label_164.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_164.setScaledContents(True)
        self.stackedWidget_6.addWidget(self.pageV_9)
        self.pageCizgi_7 = QWidget()
        self.pageCizgi_7.setObjectName(u"pageCizgi_7")
        self.label_165 = QLabel(self.pageCizgi_7)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setGeometry(QRect(40, 40, 15, 15))
        self.label_165.setMinimumSize(QSize(15, 15))
        self.label_165.setMaximumSize(QSize(15, 15))
        self.label_165.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_165.setScaledContents(True)
        self.label_166 = QLabel(self.pageCizgi_7)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setGeometry(QRect(60, 40, 15, 15))
        self.label_166.setMinimumSize(QSize(15, 15))
        self.label_166.setMaximumSize(QSize(15, 15))
        self.label_166.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_166.setScaledContents(True)
        self.label_167 = QLabel(self.pageCizgi_7)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setGeometry(QRect(80, 40, 15, 15))
        self.label_167.setMinimumSize(QSize(15, 15))
        self.label_167.setMaximumSize(QSize(15, 15))
        self.label_167.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_167.setScaledContents(True)
        self.label_168 = QLabel(self.pageCizgi_7)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setGeometry(QRect(100, 40, 15, 15))
        self.label_168.setMinimumSize(QSize(15, 15))
        self.label_168.setMaximumSize(QSize(15, 15))
        self.label_168.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_168.setScaledContents(True)
        self.label_169 = QLabel(self.pageCizgi_7)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setGeometry(QRect(120, 40, 15, 15))
        self.label_169.setMinimumSize(QSize(15, 15))
        self.label_169.setMaximumSize(QSize(15, 15))
        self.label_169.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_169.setScaledContents(True)
        self.stackedWidget_6.addWidget(self.pageCizgi_7)
        self.pageOkBasi_7 = QWidget()
        self.pageOkBasi_7.setObjectName(u"pageOkBasi_7")
        self.label_170 = QLabel(self.pageOkBasi_7)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setGeometry(QRect(80, 20, 15, 15))
        self.label_170.setMinimumSize(QSize(15, 15))
        self.label_170.setMaximumSize(QSize(15, 15))
        self.label_170.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_170.setScaledContents(True)
        self.label_171 = QLabel(self.pageOkBasi_7)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setGeometry(QRect(100, 40, 15, 15))
        self.label_171.setMinimumSize(QSize(15, 15))
        self.label_171.setMaximumSize(QSize(15, 15))
        self.label_171.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_171.setScaledContents(True)
        self.label_172 = QLabel(self.pageOkBasi_7)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setGeometry(QRect(60, 40, 15, 15))
        self.label_172.setMinimumSize(QSize(15, 15))
        self.label_172.setMaximumSize(QSize(15, 15))
        self.label_172.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_172.setScaledContents(True)
        self.label_173 = QLabel(self.pageOkBasi_7)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setGeometry(QRect(40, 60, 15, 15))
        self.label_173.setMinimumSize(QSize(15, 15))
        self.label_173.setMaximumSize(QSize(15, 15))
        self.label_173.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_173.setScaledContents(True)
        self.label_174 = QLabel(self.pageOkBasi_7)
        self.label_174.setObjectName(u"label_174")
        self.label_174.setGeometry(QRect(120, 60, 15, 15))
        self.label_174.setMinimumSize(QSize(15, 15))
        self.label_174.setMaximumSize(QSize(15, 15))
        self.label_174.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_174.setScaledContents(True)
        self.stackedWidget_6.addWidget(self.pageOkBasi_7)
        self.pageSerbest_7 = QWidget()
        self.pageSerbest_7.setObjectName(u"pageSerbest_7")
        self.label_175 = QLabel(self.pageSerbest_7)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setGeometry(QRect(80, 50, 15, 15))
        self.label_175.setMinimumSize(QSize(15, 15))
        self.label_175.setMaximumSize(QSize(15, 15))
        self.label_175.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_175.setScaledContents(True)
        self.label_176 = QLabel(self.pageSerbest_7)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setGeometry(QRect(100, 70, 15, 15))
        self.label_176.setMinimumSize(QSize(15, 15))
        self.label_176.setMaximumSize(QSize(15, 15))
        self.label_176.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_176.setScaledContents(True)
        self.label_177 = QLabel(self.pageSerbest_7)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setGeometry(QRect(60, 70, 15, 15))
        self.label_177.setMinimumSize(QSize(15, 15))
        self.label_177.setMaximumSize(QSize(15, 15))
        self.label_177.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_177.setScaledContents(True)
        self.label_178 = QLabel(self.pageSerbest_7)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setGeometry(QRect(100, 30, 15, 15))
        self.label_178.setMinimumSize(QSize(15, 15))
        self.label_178.setMaximumSize(QSize(15, 15))
        self.label_178.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_178.setScaledContents(True)
        self.label_179 = QLabel(self.pageSerbest_7)
        self.label_179.setObjectName(u"label_179")
        self.label_179.setGeometry(QRect(60, 30, 15, 15))
        self.label_179.setMinimumSize(QSize(15, 15))
        self.label_179.setMaximumSize(QSize(15, 15))
        self.label_179.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_179.setScaledContents(True)
        self.stackedWidget_6.addWidget(self.pageSerbest_7)

        self.verticalLayout_13.addWidget(self.stackedWidget_6)


        self.gridLayout_11.addLayout(self.verticalLayout_13, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(231, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.G2Baslat = QPushButton(self.widget_2)
        self.G2Baslat.setObjectName(u"G2Baslat")
        self.G2Baslat.setMinimumSize(QSize(130, 0))
        self.G2Baslat.setFont(font3)

        self.gridLayout_11.addWidget(self.G2Baslat, 1, 1, 1, 2)

        self.horizontalSpacer_9 = QSpacerItem(167, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_9, 1, 3, 1, 1)


        self.gridLayout_10.addWidget(self.widget_2, 2, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(48, 59, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_6, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.pageNavigasyon)
        self.pageBirey = QWidget()
        self.pageBirey.setObjectName(u"pageBirey")
        self.gridLayout_13 = QGridLayout(self.pageBirey)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.verticalSpacer_9 = QSpacerItem(20, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_9, 4, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(17, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(13, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_7, 1, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(17, 22, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_10, 4, 2, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_181 = QLabel(self.pageBirey)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setMaximumSize(QSize(300, 16777215))
        self.label_181.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_181)

        self.label_182 = QLabel(self.pageBirey)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setMinimumSize(QSize(400, 0))
        self.label_182.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_14.addWidget(self.label_182)


        self.gridLayout_13.addLayout(self.verticalLayout_14, 0, 0, 1, 4)

        self.widget_3 = QWidget(self.pageBirey)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(200, 350))
        self.G3Baslat = QPushButton(self.widget_3)
        self.G3Baslat.setObjectName(u"G3Baslat")
        self.G3Baslat.setGeometry(QRect(30, 230, 131, 41))
        self.G3Baslat.setMinimumSize(QSize(130, 0))
        self.G3Baslat.setFont(font3)
        self.layoutWidget = QWidget(self.widget_3)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 171, 191))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_186 = QLabel(self.layoutWidget)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setFont(font1)

        self.verticalLayout_17.addWidget(self.label_186)

        self.G3_formasyon = QComboBox(self.layoutWidget)
        self.G3_formasyon.addItem("")
        self.G3_formasyon.addItem("")
        self.G3_formasyon.addItem("")
        self.G3_formasyon.addItem("")
        self.G3_formasyon.setObjectName(u"G3_formasyon")
        self.G3_formasyon.setMinimumSize(QSize(0, 40))
        self.G3_formasyon.setMaximumSize(QSize(170, 16777215))
        self.G3_formasyon.setFont(font2)

        self.verticalLayout_17.addWidget(self.G3_formasyon)

        self.stackedWidget_7 = QStackedWidget(self.layoutWidget)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.stackedWidget_7.setMinimumSize(QSize(0, 110))
        self.stackedWidget_7.setMaximumSize(QSize(170, 16777215))
        self.pageV_10 = QWidget()
        self.pageV_10.setObjectName(u"pageV_10")
        self.label_187 = QLabel(self.pageV_10)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setGeometry(QRect(80, 70, 15, 15))
        self.label_187.setMinimumSize(QSize(15, 15))
        self.label_187.setMaximumSize(QSize(15, 15))
        self.label_187.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_187.setScaledContents(True)
        self.label_188 = QLabel(self.pageV_10)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setGeometry(QRect(40, 30, 15, 15))
        self.label_188.setMinimumSize(QSize(15, 15))
        self.label_188.setMaximumSize(QSize(15, 15))
        self.label_188.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_188.setScaledContents(True)
        self.label_189 = QLabel(self.pageV_10)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setGeometry(QRect(120, 30, 15, 15))
        self.label_189.setMinimumSize(QSize(15, 15))
        self.label_189.setMaximumSize(QSize(15, 15))
        self.label_189.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_189.setScaledContents(True)
        self.label_190 = QLabel(self.pageV_10)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setGeometry(QRect(60, 50, 15, 15))
        self.label_190.setMinimumSize(QSize(15, 15))
        self.label_190.setMaximumSize(QSize(15, 15))
        self.label_190.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_190.setScaledContents(True)
        self.label_191 = QLabel(self.pageV_10)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setGeometry(QRect(100, 50, 15, 15))
        self.label_191.setMinimumSize(QSize(15, 15))
        self.label_191.setMaximumSize(QSize(15, 15))
        self.label_191.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_191.setScaledContents(True)
        self.stackedWidget_7.addWidget(self.pageV_10)
        self.pageCizgi_8 = QWidget()
        self.pageCizgi_8.setObjectName(u"pageCizgi_8")
        self.label_192 = QLabel(self.pageCizgi_8)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setGeometry(QRect(40, 40, 15, 15))
        self.label_192.setMinimumSize(QSize(15, 15))
        self.label_192.setMaximumSize(QSize(15, 15))
        self.label_192.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_192.setScaledContents(True)
        self.label_193 = QLabel(self.pageCizgi_8)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setGeometry(QRect(60, 40, 15, 15))
        self.label_193.setMinimumSize(QSize(15, 15))
        self.label_193.setMaximumSize(QSize(15, 15))
        self.label_193.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_193.setScaledContents(True)
        self.label_194 = QLabel(self.pageCizgi_8)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setGeometry(QRect(80, 40, 15, 15))
        self.label_194.setMinimumSize(QSize(15, 15))
        self.label_194.setMaximumSize(QSize(15, 15))
        self.label_194.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_194.setScaledContents(True)
        self.label_195 = QLabel(self.pageCizgi_8)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setGeometry(QRect(100, 40, 15, 15))
        self.label_195.setMinimumSize(QSize(15, 15))
        self.label_195.setMaximumSize(QSize(15, 15))
        self.label_195.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_195.setScaledContents(True)
        self.label_196 = QLabel(self.pageCizgi_8)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setGeometry(QRect(120, 40, 15, 15))
        self.label_196.setMinimumSize(QSize(15, 15))
        self.label_196.setMaximumSize(QSize(15, 15))
        self.label_196.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_196.setScaledContents(True)
        self.stackedWidget_7.addWidget(self.pageCizgi_8)
        self.pageOkBasi_8 = QWidget()
        self.pageOkBasi_8.setObjectName(u"pageOkBasi_8")
        self.label_197 = QLabel(self.pageOkBasi_8)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setGeometry(QRect(80, 20, 15, 15))
        self.label_197.setMinimumSize(QSize(15, 15))
        self.label_197.setMaximumSize(QSize(15, 15))
        self.label_197.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_197.setScaledContents(True)
        self.label_198 = QLabel(self.pageOkBasi_8)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setGeometry(QRect(100, 40, 15, 15))
        self.label_198.setMinimumSize(QSize(15, 15))
        self.label_198.setMaximumSize(QSize(15, 15))
        self.label_198.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_198.setScaledContents(True)
        self.label_199 = QLabel(self.pageOkBasi_8)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setGeometry(QRect(60, 40, 15, 15))
        self.label_199.setMinimumSize(QSize(15, 15))
        self.label_199.setMaximumSize(QSize(15, 15))
        self.label_199.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_199.setScaledContents(True)
        self.label_200 = QLabel(self.pageOkBasi_8)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setGeometry(QRect(40, 60, 15, 15))
        self.label_200.setMinimumSize(QSize(15, 15))
        self.label_200.setMaximumSize(QSize(15, 15))
        self.label_200.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_200.setScaledContents(True)
        self.label_201 = QLabel(self.pageOkBasi_8)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setGeometry(QRect(120, 60, 15, 15))
        self.label_201.setMinimumSize(QSize(15, 15))
        self.label_201.setMaximumSize(QSize(15, 15))
        self.label_201.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_201.setScaledContents(True)
        self.stackedWidget_7.addWidget(self.pageOkBasi_8)
        self.pageSerbest_8 = QWidget()
        self.pageSerbest_8.setObjectName(u"pageSerbest_8")
        self.label_202 = QLabel(self.pageSerbest_8)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setGeometry(QRect(80, 50, 15, 15))
        self.label_202.setMinimumSize(QSize(15, 15))
        self.label_202.setMaximumSize(QSize(15, 15))
        self.label_202.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_202.setScaledContents(True)
        self.label_203 = QLabel(self.pageSerbest_8)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setGeometry(QRect(100, 70, 15, 15))
        self.label_203.setMinimumSize(QSize(15, 15))
        self.label_203.setMaximumSize(QSize(15, 15))
        self.label_203.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_203.setScaledContents(True)
        self.label_204 = QLabel(self.pageSerbest_8)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setGeometry(QRect(60, 70, 15, 15))
        self.label_204.setMinimumSize(QSize(15, 15))
        self.label_204.setMaximumSize(QSize(15, 15))
        self.label_204.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_204.setScaledContents(True)
        self.label_205 = QLabel(self.pageSerbest_8)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setGeometry(QRect(100, 30, 15, 15))
        self.label_205.setMinimumSize(QSize(15, 15))
        self.label_205.setMaximumSize(QSize(15, 15))
        self.label_205.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_205.setScaledContents(True)
        self.label_206 = QLabel(self.pageSerbest_8)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setGeometry(QRect(60, 30, 15, 15))
        self.label_206.setMinimumSize(QSize(15, 15))
        self.label_206.setMaximumSize(QSize(15, 15))
        self.label_206.setPixmap(QPixmap(u":/icon/icon/drone-siyah.svg"))
        self.label_206.setScaledContents(True)
        self.stackedWidget_7.addWidget(self.pageSerbest_8)

        self.verticalLayout_17.addWidget(self.stackedWidget_7)


        self.gridLayout_13.addWidget(self.widget_3, 2, 2, 2, 1)

        self.widget = QWidget(self.pageBirey)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(250, 300))
        self.widget.setStyleSheet(u"/* Sadece \u201cmyContainer\u201d adl\u0131 widget\u2019\u0131 transparan yap */\n"
"QWidget#widget {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Ayn\u0131 kapsay\u0131c\u0131n\u0131n i\u00e7indeki alt elemanlar\u0131 beyaz arka planla geri getir */\n"
"QWidget#widget QLineEdit,\n"
"QWidget#widget QComboBox,\n"
"QWidget#widget QPushButton {\n"
"    background-color: white;\n"
"}")
        self.layoutWidget1 = QWidget(self.widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 0, 207, 139))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_183 = QLabel(self.layoutWidget1)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_183)

        self.label_184 = QLabel(self.layoutWidget1)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_184)

        self.label_185 = QLabel(self.layoutWidget1)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_185)


        self.horizontalLayout_6.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.G3_ucusirtifasi = QLineEdit(self.layoutWidget1)
        self.G3_ucusirtifasi.setObjectName(u"G3_ucusirtifasi")
        self.G3_ucusirtifasi.setMaximumSize(QSize(70, 16777215))
        self.G3_ucusirtifasi.setFont(font2)

        self.verticalLayout_16.addWidget(self.G3_ucusirtifasi)

        self.G3_sure = QLineEdit(self.layoutWidget1)
        self.G3_sure.setObjectName(u"G3_sure")
        self.G3_sure.setMaximumSize(QSize(70, 16777215))
        self.G3_sure.setFont(font2)

        self.verticalLayout_16.addWidget(self.G3_sure)

        self.G3_mesafe = QLineEdit(self.layoutWidget1)
        self.G3_mesafe.setObjectName(u"G3_mesafe")
        self.G3_mesafe.setMaximumSize(QSize(70, 16777215))
        self.G3_mesafe.setFont(font2)

        self.verticalLayout_16.addWidget(self.G3_mesafe)


        self.horizontalLayout_6.addLayout(self.verticalLayout_16)

        self.layoutWidget2 = QWidget(self.widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 160, 202, 128))
        self.gridLayout_12 = QGridLayout(self.layoutWidget2)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_207 = QLabel(self.layoutWidget2)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setFont(font1)

        self.gridLayout_12.addWidget(self.label_207, 0, 0, 1, 1)

        self.Port_comboBox = QComboBox(self.layoutWidget2)
        self.Port_comboBox.setObjectName(u"Port_comboBox")
        self.Port_comboBox.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setBold(True)
        self.Port_comboBox.setFont(font5)

        self.gridLayout_12.addWidget(self.Port_comboBox, 1, 0, 1, 2)

        self.AjanCikar = QPushButton(self.layoutWidget2)
        self.AjanCikar.setObjectName(u"AjanCikar")
        self.AjanCikar.setMinimumSize(QSize(40, 50))
        self.AjanCikar.setFont(font3)
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/drone-cikar.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AjanCikar.setIcon(icon8)
        self.AjanCikar.setIconSize(QSize(32, 32))

        self.gridLayout_12.addWidget(self.AjanCikar, 2, 0, 1, 1)

        self.AjanEkle = QPushButton(self.layoutWidget2)
        self.AjanEkle.setObjectName(u"AjanEkle")
        self.AjanEkle.setMinimumSize(QSize(40, 50))
        self.AjanEkle.setFont(font3)
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/drone-ekle.svg.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.AjanEkle.setIcon(icon9)
        self.AjanEkle.setIconSize(QSize(32, 32))

        self.gridLayout_12.addWidget(self.AjanEkle, 2, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget, 2, 1, 2, 1)

        self.horizontalSpacer_12 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_12, 2, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(57, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_13, 3, 3, 1, 1)

        self.stackedWidget.addWidget(self.pageBirey)
        self.pageKesif = QWidget()
        self.pageKesif.setObjectName(u"pageKesif")
        self.gridLayout_15 = QGridLayout(self.pageKesif)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.widget_5 = QWidget(self.pageKesif)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 80))
        self.layoutWidget_2 = QWidget(self.widget_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 491, 72))
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(300, 16777215))
        self.label_4.setFont(font4)

        self.verticalLayout_18.addWidget(self.label_4)

        self.label_208 = QLabel(self.layoutWidget_2)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setMinimumSize(QSize(400, 0))
        self.label_208.setMaximumSize(QSize(550, 16777215))

        self.verticalLayout_18.addWidget(self.label_208)


        self.gridLayout_15.addWidget(self.widget_5, 0, 0, 1, 3)

        self.widgetKamera = QWidget(self.pageKesif)
        self.widgetKamera.setObjectName(u"widgetKamera")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetKamera.sizePolicy().hasHeightForWidth())
        self.widgetKamera.setSizePolicy(sizePolicy)
        self.widgetKamera.setMinimumSize(QSize(491, 341))
        self.widgetKamera.setStyleSheet(u"")
        self.gridLayout_16 = QGridLayout(self.widgetKamera)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.stackedWidgetKamera = QStackedWidget(self.widgetKamera)
        self.stackedWidgetKamera.setObjectName(u"stackedWidgetKamera")
        self.stackedWidgetKamera.setStyleSheet(u"   background-image: url(\"icon/t3-logo-TR.jpg\");   /* senin resmin */\n"
"    background-size: contain;             /* kutunun i\u00e7ine tamamen s\u0131\u011fd\u0131r\u0131r */\n"
"    background-repeat: no-repeat;         /* tekrar etmez */\n"
"    background-position: center center;   /* ortalar */")
        self.pageKamera = QWidget()
        self.pageKamera.setObjectName(u"pageKamera")
        self.stackedWidgetKamera.addWidget(self.pageKamera)

        self.gridLayout_16.addWidget(self.stackedWidgetKamera, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widgetKamera, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.pageKesif)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(130, 130))
        self.widget_4.setMaximumSize(QSize(130, 135))
        self.gridLayout_14 = QGridLayout(self.widget_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_209 = QLabel(self.widget_4)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setFont(font1)

        self.gridLayout_14.addWidget(self.label_209, 0, 0, 1, 1)

        self.G3_alandegeri = QLineEdit(self.widget_4)
        self.G3_alandegeri.setObjectName(u"G3_alandegeri")
        self.G3_alandegeri.setMaximumSize(QSize(100, 16777215))
        self.G3_alandegeri.setFont(font2)

        self.gridLayout_14.addWidget(self.G3_alandegeri, 1, 0, 1, 1)

        self.G4Baslat = QPushButton(self.widget_4)
        self.G4Baslat.setObjectName(u"G4Baslat")
        self.G4Baslat.setMinimumSize(QSize(100, 0))
        self.G4Baslat.setFont(font3)

        self.gridLayout_14.addWidget(self.G4Baslat, 2, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_4, 1, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(25, 18, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_14, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.pageKesif)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 5)


        self.gridLayout.addWidget(self.widgetPanel, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pButtonChange.toggled.connect(self.widgetMenu.setHidden)
        self.pButtonChange.toggled.connect(self.widgetIcons.setVisible)
        self.pButtoniconBirey.toggled.connect(self.pButtonMenuBirey.setChecked)
        self.pButtonMenuBirey.toggled.connect(self.pButtoniconBirey.setChecked)
        self.pButtonMenuNavigasyon.toggled.connect(self.pButtoniconNavigasyon.setChecked)
        self.pButtoniconNavigasyon.toggled.connect(self.pButtonMenuNavigasyon.setChecked)
        self.pButtoniconFormasyon.toggled.connect(self.pButtonMenuFormasyon.setChecked)
        self.pButtonMenuFormasyon.toggled.connect(self.pButtoniconFormasyon.setChecked)
        self.pButtoniconBaglanti.toggled.connect(self.pButtonMenuBaglanti.setChecked)
        self.pButtonMenuBaglanti.toggled.connect(self.pButtoniconBaglanti.setChecked)
        self.pButtoniconCikis.toggled.connect(self.pButtonMenuCikis.setChecked)
        self.pButtonMenuCikis.toggled.connect(self.pButtoniconCikis.setChecked)
        self.pButtonMenuCikis.clicked.connect(MainWindow.close)
        self.pButtoniconCikis.clicked.connect(MainWindow.close)
        self.droneCount_SpinBox.valueChanged.connect(self.stackedDrones.setCurrentIndex)
        self.comboBoxFormasyon_1.currentIndexChanged.connect(self.stackedWidget_2.setCurrentIndex)
        self.comboBoxFormasyon_2.currentIndexChanged.connect(self.stackedWidget_3.setCurrentIndex)
        self.comboBoxFormasyon_3.currentIndexChanged.connect(self.stackedWidget_4.setCurrentIndex)
        self.comboBoxFormasyon_4.currentIndexChanged.connect(self.stackedWidget_5.setCurrentIndex)
        self.G2_formasyon.currentIndexChanged.connect(self.stackedWidget_6.setCurrentIndex)
        self.G3_formasyon.currentIndexChanged.connect(self.stackedWidget_7.setCurrentIndex)
        self.pButtonMenuKesif.toggled.connect(self.pButtoniconKesif.setChecked)
        self.pButtoniconKesif.toggled.connect(self.pButtonMenuKesif.setChecked)

        self.stackedWidget.setCurrentIndex(4)
        self.stackedDrones.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(0)
        self.stackedWidget_7.setCurrentIndex(0)
        self.stackedWidgetKamera.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI-forX Aray\u00fcz", None))
        self.label_5.setText("")
        self.pButtoniconBaglanti.setText("")
        self.pButtoniconFormasyon.setText("")
        self.pButtoniconNavigasyon.setText("")
        self.pButtoniconBirey.setText("")
        self.pButtoniconKesif.setText("")
        self.pButtoniconCikis.setText("")
        self.label_6.setText("")
        self.pButtonMenuBaglanti.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flang\u0131\u00e7", None))
        self.pButtonMenuFormasyon.setText(QCoreApplication.translate("MainWindow", u"Formasyon", None))
        self.pButtonMenuNavigasyon.setText(QCoreApplication.translate("MainWindow", u"Navigasyon", None))
        self.pButtonMenuBirey.setText(QCoreApplication.translate("MainWindow", u"Birey Ekle \u00c7\u0131kar", None))
        self.pButtonMenuKesif.setText(QCoreApplication.translate("MainWindow", u"Ke\u015fif", None))
        self.pButtonMenuCikis.setText(QCoreApplication.translate("MainWindow", u"\u00c7\u0131k\u0131\u015f", None))
        self.pButtonChange.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AI-FORX TEKNOFEST TAKIMI", None))
        self.pButtonAcil.setText(QCoreApplication.translate("MainWindow", u"Acil \u0130ni\u015f", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Drone Say\u0131s\u0131:", None))
        self.initializeButton.setText(QCoreApplication.translate("MainWindow", u"Ba\u011flan", None))
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_24.setText("")
        self.label_23.setText("")
        self.label_22.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ba\u015flang\u0131\u00e7 & Ba\u011flant\u0131", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Sim\u00fclasyonu ba\u015flatmadan \u00f6nce ka\u00e7 adet dronla \u00e7al\u0131\u015f\u0131laca\u011f\u0131n\u0131 se\u00e7menizi sa\u011flar. <span style=\" font-weight:700;\">\u201cDrone Say\u0131s\u0131\u201d</span> <br>kutusundan istedi\u011finiz adedi belirleyip <span style=\" font-weight:700;\">\u201cBa\u011flan\u201d</span> butonuna t\u0131klay\u0131n.</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Otonom G\u00f6rev 3B Formasyon", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Dronlar\u0131n irtifa, formasyon s\u00fcresi ve mesafe ayarlar\u0131n\u0131 yaparak d\u00f6rt a\u015famal\u0131 formasyonu se\u00e7in. <span style=\" font-weight:700;\">G1-Ba\u015flat</span><br> ile otonom <span style=\" font-weight:700;\">3B formasyon</span> g\u00f6revi ba\u015flar.</p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"U\u00e7u\u015f \u0130rtifas\u0131 (Z):", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Formasyon Koruma S\u00fcresi (T):", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ajanlar Aras\u0131 Mesafe (X):", None))
        self.G1Baslat.setText(QCoreApplication.translate("MainWindow", u"G1-Ba\u015flat", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"4.Formasyon", None))
        self.comboBoxFormasyon_4.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBoxFormasyon_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c7izgi", None))
        self.comboBoxFormasyon_4.setItemText(2, QCoreApplication.translate("MainWindow", u"Ok Ba\u015f\u0131", None))
        self.comboBoxFormasyon_4.setItemText(3, QCoreApplication.translate("MainWindow", u"Serbest", None))

        self.comboBoxFormasyon_2.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBoxFormasyon_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c7izgi", None))
        self.comboBoxFormasyon_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Ok Ba\u015f\u0131", None))
        self.comboBoxFormasyon_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Serbest", None))

        self.comboBoxFormasyon_3.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBoxFormasyon_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c7izgi", None))
        self.comboBoxFormasyon_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Ok ba\u015f\u0131", None))
        self.comboBoxFormasyon_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Serbest", None))

        self.label_95.setText("")
        self.label_96.setText("")
        self.label_97.setText("")
        self.label_98.setText("")
        self.label_99.setText("")
        self.label_100.setText("")
        self.label_101.setText("")
        self.label_102.setText("")
        self.label_103.setText("")
        self.label_104.setText("")
        self.label_105.setText("")
        self.label_106.setText("")
        self.label_107.setText("")
        self.label_108.setText("")
        self.label_109.setText("")
        self.label_110.setText("")
        self.label_111.setText("")
        self.label_112.setText("")
        self.label_113.setText("")
        self.label_114.setText("")
        self.comboBoxFormasyon_1.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.comboBoxFormasyon_1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c7izgi", None))
        self.comboBoxFormasyon_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Ok Ba\u015f\u0131", None))
        self.comboBoxFormasyon_1.setItemText(3, QCoreApplication.translate("MainWindow", u"Serbest", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"2.Formasyon", None))
        self.label_115.setText("")
        self.label_116.setText("")
        self.label_117.setText("")
        self.label_118.setText("")
        self.label_119.setText("")
        self.label_120.setText("")
        self.label_121.setText("")
        self.label_122.setText("")
        self.label_123.setText("")
        self.label_124.setText("")
        self.label_125.setText("")
        self.label_126.setText("")
        self.label_127.setText("")
        self.label_128.setText("")
        self.label_129.setText("")
        self.label_130.setText("")
        self.label_131.setText("")
        self.label_132.setText("")
        self.label_133.setText("")
        self.label_134.setText("")
        self.label_33.setText("")
        self.label_36.setText("")
        self.label_37.setText("")
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.label_41.setText("")
        self.label_42.setText("")
        self.label_43.setText("")
        self.label_44.setText("")
        self.label_45.setText("")
        self.label_46.setText("")
        self.label_47.setText("")
        self.label_48.setText("")
        self.label_49.setText("")
        self.label_50.setText("")
        self.label_51.setText("")
        self.label_52.setText("")
        self.label_53.setText("")
        self.label_54.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"1.Formasyon", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"3.Formasyon", None))
        self.label_135.setText("")
        self.label_136.setText("")
        self.label_137.setText("")
        self.label_138.setText("")
        self.label_139.setText("")
        self.label_140.setText("")
        self.label_141.setText("")
        self.label_142.setText("")
        self.label_143.setText("")
        self.label_144.setText("")
        self.label_145.setText("")
        self.label_146.setText("")
        self.label_147.setText("")
        self.label_148.setText("")
        self.label_149.setText("")
        self.label_150.setText("")
        self.label_151.setText("")
        self.label_152.setText("")
        self.label_153.setText("")
        self.label_154.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Navigasyon ", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ula\u015fma ve bekleme s\u00fcreleri ile u\u00e7u\u015f irtifas\u0131 ve dronlar aras\u0131 mesafeyi ayarlay\u0131p navigasyon <br> formasyonunu se\u00e7in. <span style=\" font-weight:700;\">G2-Ba\u015flat</span> ile otonom <span style=\" font-weight:700;\">navigasyon</span> g\u00f6revi ba\u015flat\u0131l\u0131r.</p></body></html>", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"Ula\u015fma S\u00fcresi  (T1):", None))
        self.label_157.setText(QCoreApplication.translate("MainWindow", u"Bekleme S\u00fcresi (T2):", None))
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"U\u00e7u\u015f \u0130rtifas\u0131 (Z):", None))
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Ajanlar Aras\u0131 Mesafe (X):", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Navigasyon Formasyonu", None))
        self.G2_formasyon.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.G2_formasyon.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c7izgi", None))
        self.G2_formasyon.setItemText(2, QCoreApplication.translate("MainWindow", u"Ok Ba\u015f\u0131", None))
        self.G2_formasyon.setItemText(3, QCoreApplication.translate("MainWindow", u"Serbest", None))

        self.label_160.setText("")
        self.label_161.setText("")
        self.label_162.setText("")
        self.label_163.setText("")
        self.label_164.setText("")
        self.label_165.setText("")
        self.label_166.setText("")
        self.label_167.setText("")
        self.label_168.setText("")
        self.label_169.setText("")
        self.label_170.setText("")
        self.label_171.setText("")
        self.label_172.setText("")
        self.label_173.setText("")
        self.label_174.setText("")
        self.label_175.setText("")
        self.label_176.setText("")
        self.label_177.setText("")
        self.label_178.setText("")
        self.label_179.setText("")
        self.G2Baslat.setText(QCoreApplication.translate("MainWindow", u"G2-Ba\u015flat", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"Birey Ekle \u00c7\u0131kar", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Formasyon, irtifa, s\u00fcre ve mesafe de\u011ferlerini girip <span style=\" font-weight:700;\">G3-Ba\u015flat</span>\u2019a bas\u0131n; <span style=\" font-weight:700;\">Ajan Ekle/\u00c7\u0131kar</span> ile dron say\u0131s\u0131n\u0131 ayarlay\u0131n.</p></body></html>", None))
        self.G3Baslat.setText(QCoreApplication.translate("MainWindow", u"G3-Ba\u015flat", None))
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"Formasyon", None))
        self.G3_formasyon.setItemText(0, QCoreApplication.translate("MainWindow", u"V", None))
        self.G3_formasyon.setItemText(1, QCoreApplication.translate("MainWindow", u"\u00c7izgi", None))
        self.G3_formasyon.setItemText(2, QCoreApplication.translate("MainWindow", u"Ok Ba\u015f\u0131", None))
        self.G3_formasyon.setItemText(3, QCoreApplication.translate("MainWindow", u"Serbest", None))

        self.label_187.setText("")
        self.label_188.setText("")
        self.label_189.setText("")
        self.label_190.setText("")
        self.label_191.setText("")
        self.label_192.setText("")
        self.label_193.setText("")
        self.label_194.setText("")
        self.label_195.setText("")
        self.label_196.setText("")
        self.label_197.setText("")
        self.label_198.setText("")
        self.label_199.setText("")
        self.label_200.setText("")
        self.label_201.setText("")
        self.label_202.setText("")
        self.label_203.setText("")
        self.label_204.setText("")
        self.label_205.setText("")
        self.label_206.setText("")
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"U\u00e7u\u015f \u0130rtifas\u0131 (Z):", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"S\u00fcre (T) :", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Mesafe (X) :", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"Drone", None))
        self.AjanCikar.setText("")
        self.AjanEkle.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ke\u015fif", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ula\u015fma ve bekleme s\u00fcreleri ile u\u00e7u\u015f irtifas\u0131 ve dronlar aras\u0131 mesafeyi ayarlay\u0131p navigasyon <br> formasyonunu se\u00e7in. <span style=\" font-weight:700;\">G2-Ba\u015flat</span> ile otonom <span style=\" font-weight:700;\">navigasyon</span> g\u00f6revi ba\u015flat\u0131l\u0131r.</p></body></html>", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Alan De\u011feri", None))
        self.G4Baslat.setText(QCoreApplication.translate("MainWindow", u"G4-Ba\u015fat", None))
    # retranslateUi

