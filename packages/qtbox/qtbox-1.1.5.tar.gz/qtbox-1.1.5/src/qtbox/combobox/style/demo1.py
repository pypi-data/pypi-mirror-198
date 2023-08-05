# PyQt
from PyQt5.QtWidgets import QComboBox
from qtbox.utils.menu import createWidgetMenuBase
from pathlib import Path

QComboBox = createWidgetMenuBase(QComboBox)
PATH_TO_IMG1 = str(Path(__file__).parent.parent.parent / "res/images/down.png").replace("\\", "/")
PATH_TO_IMG2 = str(Path(__file__).parent.parent.parent / "res/images/up.png").replace("\\", "/")

class QtBoxStyleComboBox1(QComboBox):
    def __init__(self):
        super(QtBoxStyleComboBox1, self).__init__(str(Path(__file__)))
        self.setFixedSize(150, 30)
        self.addItems(['1', '2', '3', '4', '5', '6'])
        self.setStyleSheet("""
        QComboBox {
            background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #555555, stop:1 #313131);
            border: 1px solid lightgray;
            border-radius: 3px;
            font-weight: bold;
            color: white;
            padding-left: 15px;
        }
        
        QComboBox::drop-down {
            width: 22px;
            border-left: 1px solid darkgray;
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        
        QComboBox::down-arrow {
            width: 16px;
            height: 16px;
            image: url(%s);
        }
        
        QComboBox::down-arrow:on {
            image: url(%s);
        }
        
        QComboBox QAbstractItemView {
            color: white;
            border: none;
            outline: none;
            background-color: #313131;
        }
        
        QComboBox QScrollBar:vertical {
            width: 2px;
            background-color: white;
        }
        
        QComboBox QScrollBar::handle:vertical {
            background-color: #b2bdaf;
        }
        """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PyQt

# PySide
# from PySide2.QtWidgets import QComboBox


# class QtBoxStyleComboBox1(QComboBox):
#     def __init__(self):
#         super(QtBoxStyleComboBox1, self).__init__()
#         self.setFixedSize(150, 30)
#         self.addItems(['1', '2', '3', '4', '5', '6'])
#         self.setStyleSheet("""
#         QComboBox {
#             background-color: qlineargradient(x1:1, y1:0, x2:1, y2:1, stop:0 #555555, stop:1 #313131);
#             border: 1px solid lightgray;
#             border-radius: 3px;
#             font-weight: bold;
#             color: white;
#             padding-left: 15px;
#         }

#         QComboBox::drop-down {
#             width: 22px;
#             border-left: 1px solid darkgray;
#             border-top-right-radius: 3px;
#             border-bottom-right-radius: 3px;
#         }

#         QComboBox::down-arrow {
#             width: 16px;
#             height: 16px;
#             image: url(%s);
#         }

#         QComboBox::down-arrow:on {
#             image: url(%s);
#         }

#         QComboBox QAbstractItemView {
#             color: white;
#             border: none;
#             outline: none;
#             background-color: #313131;
#         }

#         QComboBox QScrollBar:vertical {
#             width: 2px;
#             background-color: white;
#         }

#         QComboBox QScrollBar::handle:vertical {
#             background-color: #b2bdaf;
#         }
#         """ % (PATH_TO_IMG1, PATH_TO_IMG2))
# PySide