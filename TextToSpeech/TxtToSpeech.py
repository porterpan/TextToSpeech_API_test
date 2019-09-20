# -*- coding: utf-8 -*-

"""
Module implementing TxtToSpeech.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_TxtToSpeech import Ui_TxtToSpeech
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QFileDialog
# import PyQt5.QtMultimedia as QtMultimedia

import yuyinf
from yuyinf import yuyi_hec
import os

import pygame
import time

class TxtToSpeech(QDialog, Ui_TxtToSpeech):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(TxtToSpeech, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.plainTextEdit.setHorizontalScrollBarPolicy(0)
        self.textEdit_tips.setVerticalScrollBarPolicy(0)
        self.textEdit_tips.setHorizontalScrollBarPolicy(0)
        self.textEdit_tips.setReadOnly(True)
        self.textEdit_tips.setText("下拉选项中从讯飞小东开始，都是体验都是不错的，具体可以自己实验")
        self.label_tips.setText("请求结果显示窗：")
        self.comboBox_voice_name.setCurrentText('讯飞小魏')
        self.checkBox.setChecked(True)
        self.checkBox.setEnabled(False)
        # self.comboBox_voice_name.scroll(5,2)
        self.voice_name_selecct = {
        '讯飞小燕': 'xiaoyan', '讯飞许久': 'aisjiuxu','讯飞小萍': 'aisxping', '讯飞小婧': 'aisjinger',
        '讯飞许小宝': 'aisbabyxu','讯飞小东': 'x_xiaodong', '讯飞小王': 'x_xiaowang','讯飞萌萌': 'x_mengmengneutral',
        '讯飞宁宁': 'x_ningning','讯飞小南': 'x_xiaonan', '讯飞玲姐姐': 'x_xiaoling', '讯飞小坤': 'x_xiaokun',
        '讯飞小梅': 'x_xiaomei', '讯飞小瑞': 'x_xiaonuo_novel', '讯飞小师': 'x_xiaoshi_cts', '讯飞小梦': 'x_xiaomeng',
        '讯飞小施': 'x_xiaoshi', '讯飞小强': 'x_xiaoqiang', '讯飞一峰': 'x_yifeng', '讯飞小媛': 'x_xiaoyuan',
        '讯飞晓倩': 'x_xiaoqian', '讯飞小莹': 'x_xiaoying', '讯飞小乔': 'x_xiaoqiao', '讯飞小瑶': 'x_xiaoyao',
        '讯飞萌萌-悲伤': 'x_mengmengsad', '讯飞小春': 'x_mengchun', '讯飞马叔': 'x_laoma', '讯飞小蓉': 'x_xiaorong',
        '讯飞芳芳': 'x_xiaofang', '讯飞晓峰': 'x_xiaofeng', '讯飞小魏': 'x_xiaowei', '讯飞楠楠': 'x_nannan',
        '讯飞小肥': 'x_xiaofei', '讯飞小雪': 'x_xiaoxue', '讯飞晓琳': 'x_xiaolin', '讯飞小包': 'x_xiaobao',
        '讯飞小华': 'x_xiaoyang_story', '讯飞宋宝宝': 'x_xiaosong', '讯飞玉儿': 'x_yuer', '讯飞萌萌-高兴': 'x_mengmenghappy'
        }

    def readtxt(self):
        filename, filetype = QFileDialog.getOpenFileName(self,"选取文件","./","Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(filename, filetype)

        self.user_dict = {}
        with open(filename, 'r', encoding='UTF-8') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                self.plainTextEdit.setPlainText(self.plainTextEdit.toPlainText() + lines)
    @pyqtSlot()
    def on_pushButton_hec_clicked(self):
        """
        Slot documentation goes here.
        """
        # # TODO: not implemented yet
        # raise NotImplementedError
        print("语音合成")
        yuyin_app = yuyi_hec()
        str_voice_name = self.comboBox_voice_name.currentText()
        InText_neirong = self.plainTextEdit.toPlainText().strip()
        print("zhi:", str_voice_name)
        if not InText_neirong:
            print("空文本警告")
            self.label_tips.setText("空文本警告,非法请求！")
            return 0
        else:
            self.label_tips.setText("请求结果显示窗：")
        yuyin_app.yuyinhec(InText_neirong, self.voice_name_selecct[str_voice_name])
        self.textEdit_tips.setText("语音合成结果提示：\n"+yuyin_app.Erro_Tips)
        os.system('./output.mp3')
        file = r'./output.mp3'
        pygame.mixer.init()
        track = pygame.mixer.music.load(file)

        pygame.mixer.music.play()
        # time.sleep(5)
        # pygame.mixer.music.stop()


    @pyqtSlot()
    def on_pushButton_load_file_clicked(self):
        """
        Slot documentation goes here.
        """
        # # TODO: not implemented yet
        # raise NotImplementedError
        print("加载本地txt文件")
        self.readtxt()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TxtToSpeech()
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("myico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    ui.setWindowIcon(icon)
    ui.show()
    sys.exit(app.exec_())