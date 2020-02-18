# -*- coding:utf-8 -*-
"""
Created on Saturday February 15
@author Fenghaoguo
"""

import jieba.analyse
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 根据词频生成 柱状图
font = FontProperties(fname='Songti.ttc')
bar_with = 0.5


def generate_bar_abroad(filepath, savepath):
    X = []
    Y = []
    keywords = dict()
    lyric = ''  # 重置

    with open(filepath, "r") as fr:
        for ly in fr:
            lyric += fr.read()

        result = jieba.analyse.textrank(lyric, topK=54, withWeight=True)

        for i in result:
            keywords[i[0]] = i[1]
        print(keywords)

    for key in keywords:
        X.append(key)
        Y.append(keywords[key])

    num = len(X)

    fig = plt.figure(figsize=(28, 10))
    plt.bar(range(num), Y, tick_label=X, width=bar_with)
    plt.xticks(rotation=50, fontproperties=font, fontsize=20)
    plt.yticks(fontsize=20)
    plt.title("海外信息词频图", fontproperties=font, fontsize=30)
    plt.savefig(savepath, dpi=360)
    plt.show()


def generate_bar_domestic(filepath, savepath):
    X = []
    Y = []
    keywords = dict()
    lyric = ''  # 重置

    with open(filepath, "r") as fr:
        for ly in fr:
            lyric += fr.read()

        result = jieba.analyse.textrank(lyric, topK=54, withWeight=True)

        for i in result:
            keywords[i[0]] = i[1]
        print(keywords)

    for key in keywords:
        X.append(key)
        Y.append(keywords[key])

    num = len(X)

    fig = plt.figure(figsize=(28, 10))
    plt.bar(range(num), Y, tick_label=X, width=bar_with)
    plt.xticks(rotation=50, fontproperties=font, fontsize=20)
    plt.yticks(fontsize=20)
    plt.title("国内信息词频图", fontproperties=font, fontsize=30)
    plt.savefig(savepath, dpi=360)
    plt.show()


if __name__ == "__main__":
    # 海外信息
    main_filepath = "data_keywords_abroad.dat"
    main_savepath = "bar_chart_abroad.jpg"
    generate_bar_abroad(main_filepath, main_savepath)
    # 国内信息
    main_filepath = "data_keywords_ncov_memory.dat"
    main_savepath = "bar_chart_domestic.jpg"
    generate_bar_domestic(main_filepath, main_savepath)
