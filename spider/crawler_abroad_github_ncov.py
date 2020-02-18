#!/usr/bin/env python3
# -*_ coding:utf-8 -*-
"""
Created on Saturday February 15
@author: Fenghaoguo
"""

import requests
from lxml import etree
import pymysql


def get_url(idx):
    print("连接到Mysql数据库读入爬取网址...")
    db1 = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='fengdage',
        db='URL_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cursor1 = db1.cursor()
    sql_1 = "select url from github_ncov_url where id=" + "'" + str(idx) + "'"
    cursor1.execute(sql_1)
    result1 = cursor1.fetchall()
    result = result1[0]['url']
    db1.close()
    print("关闭Mysql数据库。")
    return result


def get_webpage(surl, stbname):

    print("爬取网页" + surl + "...")
    html = requests.get(surl).content
    selector = etree.HTML(html)
    items = selector.xpath('//*[@id="wiki-body"]/div/ul/li/ul/li/a/text()')
    print("解析网页，有效数据 " + str(len(items)) + " 条，入库...")
    # 入库
    write_database(items, stbname)
    # item_len = 0
    # for item in items:
    #     print(item)
        # if item_len < len(item):
        #     item_len = len(item)
    # print(item_len)


def create_table(tbname):
    print("连接到Mysql数据库创建表" + tbname + "...")
    db3 = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='fengdage',
        db='2020_ncov_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cursor3 = db3.cursor()
    sql_4 = "drop table if exists " + tbname
    cursor3.execute(sql_4)
    sql_3 = "create table " + tbname + " (`id` int(11) NOT NULL AUTO_INCREMENT,`title` varchar(100) DEFAULT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;"
    cursor3.execute(sql_3)
    db3.close()


def write_database(items2db, s2tbname):
    db2 = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='fengdage',
        db='2020_ncov_database',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    cursor2 = db2.cursor()
    for item2 in items2db:
        sql_2 = "insert into " + s2tbname + " (title) value(%s);"
        cursor2.execute(sql_2, item2)
        db2.commit()
    db2.close()


if __name__ == "__main__":

    create_table("Academic_nCoV_2019_nCoV_wiki")
    for midx in range(1, 2):
        murl = get_url(midx)
        get_webpage(murl, "Academic_nCoV_2019_nCoV_wiki")
