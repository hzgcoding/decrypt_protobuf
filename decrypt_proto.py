# coding=utf-8
from proto.ss_db_pb2 import role_base_data as RoleBaseInfo
import MySQLdb
import convert.pbjson as pbjson
import json

MYSQL_IP = "192.168.24.51"
MYSQL_USER = "root"
MYSQL_PASSWORD = "ygame123"
MYSQL_DB = "ygame_main_qa2"


# 打开数据库连接
db = MySQLdb.connect(MYSQL_IP, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

cursor.execute("select data from role_base limit 10;")

results = cursor.fetchall()

for data in results:
    role_base = RoleBaseInfo()
    role_base.ParseFromString(data[0])
    dict_result = pbjson.pb2dict(role_base)
    print json.dumps(dict_result, ensure_ascii=False, encoding='UTF-8',sort_keys=True, indent=4, separators=(',', ':'))


