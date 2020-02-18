# -*- coding:utf-8 -*-
"""
Created on Saturday February 16 2020
@author Fenghaoguo
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_oper.database import NCovMemoryData
import jieba
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


# 初始化数据库链接
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_USER = 'root'
DB_PWD = 'fengdage'
DB_NAME = '2020_ncov_database'

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME),
                       encoding='utf-8',
                       echo=False,
                       pool_size=100,
                       pool_recycle=10)

# 创建DBSession类型：
DBSession = sessionmaker(bind=engine)
session = DBSession()


def get_title_from_mysql():
    if session.query(NCovMemoryData).count() == 0:
        return None
    else:
        tb_lst = session.query(NCovMemoryData)
        title_lst = []
        for r in tb_lst:
            # print(r.id, end='\t')
            # print(r.update, end='\t')
            # print(r.category, end='\t')
            # print(r.media, end='\t')
            # print(r.date, end='\t')
            # print(r.title, end='\t')
            # print(r.title_en, end='\t')
            # print(r.url, end='\t')
            # print(r.translation_en, end='\t')
            # print(r.is_deleted, end='\t')
            # print(r.alternative, end='\t')
            # print(r.archive, end='\t')
            # print()
            title_lst.append(r.title)
        return title_lst


def preprocess(s_title_list):
    for title in s_title_list:
        en_words = get_english(title)
        ch_words = get_chinese(title)
        # 拼接词串
        tmp_str = ' '.join(en_words)
        if len(tmp_str) > 0:
            tmp_str += ' ' + ' '.join(ch_words)
        else:
            tmp_str += ' '.join(ch_words)
        # print(tmp_str)
        with open("data_full_ncov_memory.dat", "a+") as fo:
            fo.write(tmp_str)
            fo.write('\n')


if __name__ == "__main__":
    # 获取数据
    main_title_lst = get_title_from_mysql()
    # print(len(main_title_lst))
    # print('\n'.join(main_title_lst))
    preprocess(main_title_lst)
    session.close()
