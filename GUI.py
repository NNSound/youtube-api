import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 
 
class Example(QWidget):
    
    def __init__(self, parent = None):
        # 繼承的 parent 初始化 fucntion
        super().__init__(parent)
        
        self.initUI()
        
        
    def initUI(self):  
        # 設定位置尺寸
        # 同 self.move(300, 300)
        # 同 self.resize(250, 150)        
        self.setGeometry(300, 300, 250, 150)
        # 設定標題
        self.setWindowTitle('Simple')
        # 顯示，因圖形元件被創造時都是 hidden 狀態
        self.show()
        
        
if __name__ == '__main__':
    # Qt GUI 需要唯一一個 QApplication 負責管理，可傳入 sys.argv 參數
    app = QApplication(sys.argv)
    # 建立 Exxample instance
    ex = Example()
    # app.exec_() 讓 QApplication 進入 event loop
    # exec 是 Python keyword，所以會多出底線
    sys.exit(app.exec_())  