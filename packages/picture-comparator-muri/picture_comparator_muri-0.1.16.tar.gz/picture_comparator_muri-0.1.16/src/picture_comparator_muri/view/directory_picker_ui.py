# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'directory_picker.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QHeaderView, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QTreeView,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.file_system_tree_view = QTreeView(Dialog)
        self.file_system_tree_view.setObjectName(u"file_system_tree_view")

        self.horizontalLayout.addWidget(self.file_system_tree_view)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.add_button = QPushButton(Dialog)
        self.add_button.setObjectName(u"add_button")

        self.verticalLayout_2.addWidget(self.add_button)

        self.remove_button = QPushButton(Dialog)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setEnabled(False)

        self.verticalLayout_2.addWidget(self.remove_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.directories_list = QListView(Dialog)
        self.directories_list.setObjectName(u"directories_list")

        self.horizontalLayout.addWidget(self.directories_list)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.check_subdirectories_box = QCheckBox(Dialog)
        self.check_subdirectories_box.setObjectName(u"check_subdirectories_box")
        self.check_subdirectories_box.setChecked(True)

        self.verticalLayout.addWidget(self.check_subdirectories_box)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Directory Selection", None))
        self.add_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.remove_button.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.check_subdirectories_box.setText(QCoreApplication.translate("Dialog", u"Check subdirectories ", None))
    # retranslateUi

