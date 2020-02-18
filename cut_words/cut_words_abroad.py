# -*- coding:utf-8 -*-
"""
Created on Saturday February 15 2020
@author Fenghaoguo
"""

import jieba
import pymysql
import re

jieba.load_userdict("dict/dict_baidu_utf8.txt")
jieba.load_userdict("dict/dict_pangu.txt")
jieba.load_userdict("dict/dict_sougou_utf8.txt")
jieba.load_userdict("dict/dict_tencent_utf8.txt")
jieba.load_userdict("dict/SogouLabDic.txt")
jieba.load_userdict("dict/my_dict.txt")

stopwords_ch = {}.fromkeys([line.strip() for line in open("stop/stopwords_ch.txt")])
stopwords_en = {}.fromkeys([line.strip() for line in open("stop/stopwords_en.txt")])


def get_chinese(sstr):
    pattern = re.compile(u"[\u4e00-\u9fa5]+")
    ch_str = ' '.join(pattern.findall(sstr))
    ch_list = jieba.cut(ch_str)
    words = [w.strip() for w in ch_list if len(w.strip()) > 1 and w.strip() not in stopwords_ch]
    return words


def get_english(s2str):
    pattern = re.compile("[a-zA-Z\d\- ]+")
    en_str = ' '.join(pattern.findall(s2str)).split()
    re_en_list = [s.strip() for s in en_str if (not re.match("^[\d.\- ]+$", s)) and (s.strip().lower() not in stopwords_en)]
    return re_en_list


def get_data_frommysql(s_tbname):
    print("链接Mysql数据库...")
    db = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='fengdage',
        db='2020_ncov_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql_str = "select title from " + s_tbname
    cursor.execute(sql_str)
    dict_list = cursor.fetchall()
    print("正在解析数据...")
    for dt in dict_list:
        # print("all:" + dt['title'])
        # 分词，停用词处理
        # 取出英文，预处理
        en_words = get_english(dt['title'])
        # print(en_words)
        # 取出中文，预处理
        ch_words = get_chinese(dt['title'])
        # print(ch_words)
        # 拼接词串
        tmp_str = ' '.join(en_words)
        if len(tmp_str) > 0:
            tmp_str += ' ' + ' '.join(ch_words)
        else:
            tmp_str += ' '.join(ch_words)
        # print(tmp_str)
        fo = open("data_full_abroad.dat", "a+")
        fo.write(tmp_str)
        fo.write('\n')
        fo.close()
    db.close()
    print("解析完成！")


if __name__ == "__main__":

    tbname = "Academic_nCoV_2019_nCoV_wiki"
    get_data_frommysql(tbname)
