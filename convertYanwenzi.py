# coding=utf8
# python 3

"""
用法：
把 yanwenzi-raw-for-sogou.json 文件放到当前 shell 工作目录；执行 python3 convertYanwenzi.py

注意：
1. 会覆盖 phrases-yanwenzi.ini 文件！
2. 输出的配置文件是 UTF-16 LE 编码的（因为搜狗拼音 Mac 版导出是这个编码；UTF-8 导入不认；这部分有问题请告诉我）

输入文件 yanwenzi-raw-for-sogou.json 的格式：
（使用例暨 A 岛 87 颜文字 https://gist.github.com/SnowOnion/920a7f13a817b521fd292db6f8f8a953）
{
    "edition":"raw-for-sogou",
    "version":"1.0",
    "hacfun":[
        ["|∀ﾟ","ha",1,"瞪眼全称嘴偷看"], # 颜文字，自定义短语字符串，排序位置，备注（不会转到自定义短语配置文件里）
        ...
"""

import json

with open("yanwenzi-raw-for-sogou.json", mode="r", encoding="utf-8") as fin:
    json_str = fin.read()

json_obj = json.loads(json_str, encoding="utf-8")
kaomoji_entries = json_obj["hacfun"]

with open("phrases-yanwenzi.ini", mode="w", encoding="utf-16 LE") as fout:
    for e in kaomoji_entries:
        fout.write("%s,%d=%s\r\n"%(e[1],e[2],e[0]))
    
print("Convertion complete! See phrases-yanwenzi.ini")