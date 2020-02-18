# -*- coding:utf-8 -*-
"""
Created on Sunday February 16
@author Fenghaoguo
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd
from data_oper.database import NCovMemoryData

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


def save2mysql(sdata_lst):
    try:
        session.add_all(sdata_lst)
        session.commit()
    except Exception as expt:
        print(Exception, expt)
        session.rollback()


def parse_csv2tb(csv_file):
    data_lst = []
    # 读取csv_file，进行数据处理
    df_nan = pd.read_csv(csv_file, header=0, encoding='utf-8')
    df = df_nan.astype(object).where(pd.notnull(df_nan), None)
    #print(df.count().values.max())
    # print(df.keys())
    # print(df.shape[0])
    for idx in range(0, df.shape[0]):
        row = NCovMemoryData()
        row.id = df['id'][idx]
        row.update = df['update'][idx]
        row.category = df['category'][idx]
        row.media = df['media'][idx]
        row.date = df['date'][idx]
        row.title = df['title'][idx]
        row.title_en = df['title_en'][idx]
        row.url = df['url'][idx]
        row.translation_en = df['translation_en'][idx]
        row.is_deleted = df['is_deleted'][idx]
        row.alternative = df['alternative'][idx]
        row.archive = df['archive'][idx]
        data_lst.append(row)
    return data_lst


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


if __name__ == "__main__":
    # filename = "domestic/nCovMemory_data.csv"
    # csv2lst = parse_csv2tb(filename)
    # # 查看结果
    # # print(len(csv2lst))
    # save2mysql(csv2lst)

    # 获取数据测试
    main_title_lst = get_title_from_mysql()
    print(len(main_title_lst))
    print('\n'.join(main_title_lst))
    session.close()
