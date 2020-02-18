# -*- coding:utf-8 -*-
"""
Created on Saturday February 15
@author Fenghaoguo
"""

import jieba.analyse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='Songti.ttc')


# 词云
def generage_wordcloud_abroad(infile, outfile):
    lyric = ''
    keywords = dict()
    with open(infile, "r") as fr:
        for ly in fr:
            lyric += fr.read()

        result = jieba.analyse.textrank(lyric, topK=100, withWeight=True)

        for i in result:
            keywords[i[0]] = i[1]
        print(keywords)

    image = Image.open("lung.jpeg")
    graph = np.array(image)
    wc = WordCloud(font_path='Songti.ttc',
                   background_color='White',
                   max_words=100,
                   mask=graph)
    wc.generate_from_frequencies(keywords)
    image_color = ImageColorGenerator(graph)
    plt.title("海外", fontproperties=font, fontsize=30)
    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()
    wc.to_file(outfile)


def generage_wordcloud_domestic(infile, outfile):
    lyric = ''
    keywords = dict()
    with open(infile, "r") as fr:
        for ly in fr:
            lyric += fr.read()

        result = jieba.analyse.textrank(lyric, topK=128, withWeight=True)

        for i in result:
            keywords[i[0]] = i[1]
        print(keywords)

    image = Image.open("lung.jpeg")
    graph = np.array(image)
    wc = WordCloud(font_path='Songti.ttc',
                   background_color='White',
                   max_words=128,
                   mask=graph)
    wc.generate_from_frequencies(keywords)
    image_color = ImageColorGenerator(graph)
    plt.title("国内", fontproperties=font, fontsize=30)
    plt.imshow(wc)
    plt.imshow(wc.recolor(color_func=image_color))
    plt.axis("off")
    plt.show()
    wc.to_file(outfile)


if __name__ == '__main__':
    # 海外信息
    m_infile = "data_keywords_abroad.dat"
    m_outfile = "word_cloud_abroad.jpg"
    generage_wordcloud_abroad(m_infile, m_outfile)
    # 国内信息
    m_infile = "data_keywords_ncov_memory.dat"
    m_outfile = "word_cloud_domestic.jpg"
    generage_wordcloud_abroad(m_infile, m_outfile)
