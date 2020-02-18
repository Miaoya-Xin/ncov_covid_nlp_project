# -*- coding:utf-8 -*-
"""
Created on Sunday February 16
@author Fenghaoguo
"""

from sqlalchemy import Column, String, Integer, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 定义NCovMemoryData对象:
class NCovMemoryData(Base):
    # 表的名字
    __tablename__ = 'nCovMemory_data'

    # 表的结构
    id = Column(Integer, primary_key=True, autoincrement=True)
    update = Column(String)
    category = Column(String)
    media = Column(String)
    date = Column(String)
    title = Column(String)
    title_en = Column(String)
    url = Column(String)
    translation_en = Column(String)
    is_deleted = Column(String)
    alternative = Column(String)
    archive = Column(String)
