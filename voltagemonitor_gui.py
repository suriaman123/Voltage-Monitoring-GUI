

from PyQt5 import QtCore, QtGui, QtWidgets


class vm_ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 399)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 531, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.graph = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.graph.setContentsMargins(0, 0, 0, 0)
        self.graph.setObjectName("showmap")
        self.pb_start = QtWidgets.QPushButton(Form)
        self.pb_start.setGeometry(QtCore.QRect(100, 350, 131, 31))
        self.pb_start.setObjectName("pb_start")
        self.pb_stop = QtWidgets.QPushButton(Form)
        self.pb_stop.setGeometry(QtCore.QRect(330, 350, 131, 31))
        self.pb_stop.setObjectName("pb_stop")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_start.setText(_translate("Form", "Start"))
        self.pb_stop.setText(_translate("Form", "Stop"))
