# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 21, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 54, 12))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(50, 10, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 10, 21, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "url:"))
        self.label_2.setText(_translate("Form", "nums:"))
        self.pushButton.setText(_translate("Form", "新建"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_2.setToolTip(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.lineEdit_2.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wight = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(wight)
    wight.show()
    sys.exit(app.exec_())
