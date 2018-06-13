# coding=utf-8
import sys
from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal
from proto.ss_db_pb2 import *
import MySQLdb
import convert.pbjson as pbjson
import json

startApp = "start.ui"
start_class, base_start_class = uic.loadUiType(startApp)

class UiStart(QtGui.QDialog, start_class):
    OnClicked = pyqtSignal([str, str])
    OnTreeClicked = pyqtSignal([str, str, str])
    db_proto = {}
    def __init__(self, *args):
        super(UiStart, self).__init__(*args)
        self.setupUi(self)
        self.ipEdit.append("192.168.24.51")
        self.userEdit.append("root")
        self.portEdit.append("3306")
        self.pswdEdit.append("ygame123")
        self.roleIdEdit.append("0")
        self.tbEdit.append("role_base")
        self.dbEdit.append("ygame_main_hzg")
        self.initProto()
        self.initpbBox()

    def initpbBox(self):
        self.pbBox.clear()
        items = self.db_proto.items()
        items.sort()
        for key, value in items:
            self.pbBox.addItem(key)

    def initProto(self):
        self.db_proto["role_base_data"] = role_base_data()
        self.db_proto["role_item_data"] = role_item_data()
        self.db_proto["role_player_data"] = role_player_data()
        self.db_proto["role_hero_data"] = role_hero_data()
        self.db_proto["role_soul_data"] = role_soul_data()
        self.db_proto["role_level_data"] = role_level_data()
        self.db_proto["role_quest_data"] = role_quest_data()
        self.db_proto["role_royal_data"] = role_royal_data()
        self.db_proto["role_show_data"] = role_show_data()
        self.db_proto["role_friend_data"] = role_friend_data()
        self.db_proto["role_shop_data"] = role_shop_data()
        self.db_proto["role_harem_data"] = role_harem_data()
        self.db_proto["role_equipment_data"] = role_shop_data()
        self.db_proto["role_flower_data"] = role_harem_data()

    def on_convert_pressed(self):
        # 打开数据库连接
        MYSQL_IP = str(self.ipEdit.toPlainText())
        MYSQL_USER = str(self.userEdit.toPlainText())
        MYSQL_PASSWORD = str(self.pswdEdit.toPlainText())
        MYSQL_DB = str(self.dbEdit.toPlainText())
        MYSQL_TABLE = str(self.tbEdit.toPlainText())
        ROLE_ID = str(self.roleIdEdit.toPlainText())

        db = MySQLdb.connect(MYSQL_IP, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        str_cmd = "select data from "+ MYSQL_TABLE+" where id = "+ ROLE_ID + " ;"
        print str_cmd
        cursor.execute(str_cmd)

        results = cursor.fetchall()

        for data in results:
            pbObj = self.db_proto[Qstring2utf(self.pbBox.currentText())]
            pbObj.ParseFromString(data[0])
            dict_result = pbjson.pb2dict(pbObj)
            str_json = json.dumps(dict_result, ensure_ascii=False, encoding='UTF-8', sort_keys=True, indent=4,
                             separators=(',', ':'))
            print str_json
            self.txtView.clear()
            self.txtView.append(str_json)

def Qstring2utf(str_):
    return unicode(str_).encode("utf-8")


if  __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui_start = UiStart()
    ui_start.show()
    sys.exit(app.exec_())