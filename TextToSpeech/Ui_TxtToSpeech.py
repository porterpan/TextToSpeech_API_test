# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/porter/文档/github workspace/TextToSpeech_API_test/TextToSpeech/TxtToSpeech.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TxtToSpeech(object):
    def setupUi(self, TxtToSpeech):
        TxtToSpeech.setObjectName("TxtToSpeech")
        TxtToSpeech.resize(542, 355)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(TxtToSpeech)
        self.plainTextEdit.setGeometry(QtCore.QRect(280, 50, 261, 281))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_3 = QtWidgets.QLabel(TxtToSpeech)
        self.label_3.setGeometry(QtCore.QRect(190, 0, 151, 31))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(TxtToSpeech)
        self.checkBox.setGeometry(QtCore.QRect(20, 270, 118, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.pushButton_hec = QtWidgets.QPushButton(TxtToSpeech)
        self.pushButton_hec.setGeometry(QtCore.QRect(150, 260, 111, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pushButton_hec.setFont(font)
        self.pushButton_hec.setObjectName("pushButton_hec")
        self.comboBox_voice_name = QtWidgets.QComboBox(TxtToSpeech)
        self.comboBox_voice_name.setGeometry(QtCore.QRect(70, 50, 101, 31))
        self.comboBox_voice_name.setObjectName("comboBox_voice_name")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.comboBox_voice_name.addItem("")
        self.pushButton_load_file = QtWidgets.QPushButton(TxtToSpeech)
        self.pushButton_load_file.setGeometry(QtCore.QRect(180, 50, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.pushButton_load_file.setFont(font)
        self.pushButton_load_file.setObjectName("pushButton_load_file")
        self.label = QtWidgets.QLabel(TxtToSpeech)
        self.label.setGeometry(QtCore.QRect(10, 50, 61, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox_more = QtWidgets.QCheckBox(TxtToSpeech)
        self.checkBox_more.setGeometry(QtCore.QRect(20, 230, 118, 22))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.checkBox_more.setFont(font)
        self.checkBox_more.setObjectName("checkBox_more")
        self.label_tips = QtWidgets.QLabel(TxtToSpeech)
        self.label_tips.setGeometry(QtCore.QRect(20, 100, 241, 21))
        self.label_tips.setText("")
        self.label_tips.setObjectName("label_tips")
        self.textEdit_tips = QtWidgets.QTextEdit(TxtToSpeech)
        self.textEdit_tips.setEnabled(True)
        self.textEdit_tips.setGeometry(QtCore.QRect(10, 134, 251, 71))
        self.textEdit_tips.setObjectName("textEdit_tips")

        self.retranslateUi(TxtToSpeech)
        QtCore.QMetaObject.connectSlotsByName(TxtToSpeech)

    def retranslateUi(self, TxtToSpeech):
        _translate = QtCore.QCoreApplication.translate
        TxtToSpeech.setWindowTitle(_translate("TxtToSpeech", "语音合成系统"))
        self.label_3.setText(_translate("TxtToSpeech", "语音合成系统V1.0"))
        self.checkBox.setText(_translate("TxtToSpeech", "是否保存MP3"))
        self.pushButton_hec.setText(_translate("TxtToSpeech", "语音合成"))
        self.comboBox_voice_name.setItemText(0, _translate("TxtToSpeech", "讯飞小燕"))
        self.comboBox_voice_name.setItemText(1, _translate("TxtToSpeech", "讯飞许久"))
        self.comboBox_voice_name.setItemText(2, _translate("TxtToSpeech", "讯飞小萍"))
        self.comboBox_voice_name.setItemText(3, _translate("TxtToSpeech", "讯飞小婧"))
        self.comboBox_voice_name.setItemText(4, _translate("TxtToSpeech", "讯飞许小宝"))
        self.comboBox_voice_name.setItemText(5, _translate("TxtToSpeech", "讯飞小东"))
        self.comboBox_voice_name.setItemText(6, _translate("TxtToSpeech", "讯飞小王"))
        self.comboBox_voice_name.setItemText(7, _translate("TxtToSpeech", "讯飞萌萌"))
        self.comboBox_voice_name.setItemText(8, _translate("TxtToSpeech", "讯飞小梅"))
        self.comboBox_voice_name.setItemText(9, _translate("TxtToSpeech", "讯飞小瑞"))
        self.comboBox_voice_name.setItemText(10, _translate("TxtToSpeech", "讯飞小师"))
        self.comboBox_voice_name.setItemText(11, _translate("TxtToSpeech", "讯飞小梦"))
        self.comboBox_voice_name.setItemText(12, _translate("TxtToSpeech", "讯飞小施"))
        self.comboBox_voice_name.setItemText(13, _translate("TxtToSpeech", "讯飞小强"))
        self.comboBox_voice_name.setItemText(14, _translate("TxtToSpeech", "讯飞一峰"))
        self.comboBox_voice_name.setItemText(15, _translate("TxtToSpeech", "讯飞小媛"))
        self.comboBox_voice_name.setItemText(16, _translate("TxtToSpeech", "讯飞晓倩"))
        self.comboBox_voice_name.setItemText(17, _translate("TxtToSpeech", "讯飞小莹"))
        self.comboBox_voice_name.setItemText(18, _translate("TxtToSpeech", "讯飞小乔"))
        self.comboBox_voice_name.setItemText(19, _translate("TxtToSpeech", "讯飞小瑶"))
        self.comboBox_voice_name.setItemText(20, _translate("TxtToSpeech", "讯飞萌萌-悲伤"))
        self.comboBox_voice_name.setItemText(21, _translate("TxtToSpeech", "讯飞小春"))
        self.comboBox_voice_name.setItemText(22, _translate("TxtToSpeech", "讯飞马叔"))
        self.comboBox_voice_name.setItemText(23, _translate("TxtToSpeech", "讯飞小蓉"))
        self.comboBox_voice_name.setItemText(24, _translate("TxtToSpeech", "讯飞芳芳"))
        self.comboBox_voice_name.setItemText(25, _translate("TxtToSpeech", "讯飞晓峰"))
        self.comboBox_voice_name.setItemText(26, _translate("TxtToSpeech", "讯飞小魏"))
        self.comboBox_voice_name.setItemText(27, _translate("TxtToSpeech", "讯飞楠楠"))
        self.comboBox_voice_name.setItemText(28, _translate("TxtToSpeech", "讯飞小肥"))
        self.comboBox_voice_name.setItemText(29, _translate("TxtToSpeech", "讯飞小雪"))
        self.comboBox_voice_name.setItemText(30, _translate("TxtToSpeech", "讯飞晓琳"))
        self.comboBox_voice_name.setItemText(31, _translate("TxtToSpeech", "讯飞小包"))
        self.comboBox_voice_name.setItemText(32, _translate("TxtToSpeech", "讯飞小华"))
        self.comboBox_voice_name.setItemText(33, _translate("TxtToSpeech", "讯飞宋宝宝"))
        self.comboBox_voice_name.setItemText(34, _translate("TxtToSpeech", "讯飞玉儿"))
        self.comboBox_voice_name.setItemText(35, _translate("TxtToSpeech", "讯飞萌萌-高兴"))
        self.pushButton_load_file.setText(_translate("TxtToSpeech", "加载TXT"))
        self.label.setText(_translate("TxtToSpeech", "发音人："))
        self.checkBox_more.setText(_translate("TxtToSpeech", "太少,要更多"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TxtToSpeech = QtWidgets.QDialog()
    ui = Ui_TxtToSpeech()
    ui.setupUi(TxtToSpeech)
    TxtToSpeech.show()
    sys.exit(app.exec_())
