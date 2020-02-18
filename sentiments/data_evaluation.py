# -*- coding:utf-8 -*-
"""
Created on Sunday February 16
@author Fenghaoguo
"""

from snownlp import SnowNLP
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='Songti.ttc')


def data_evaluation(infile, outfile, stitle):
    pos_count = 0
    neg_count = 0
    with open(infile) as fr:
        for line in fr:
            s = SnowNLP(line)
            rates = s.sentiments
            if rates >= 0.5:
                pos_count += 1
                print(line)
            elif rates < 0.5:
                neg_count += 1
                #print(line)
            else:
                pass

    labels = 'Positive\n(eg. pray,eulogize\nand suggestion)', 'Negative\n(eg. abuse,sarcasm\nand indignation)'
    fracs = [pos_count, neg_count]
    explode = [0.1, 0]  # 凸出这部分
    plt.title(stitle, fontproperties=font, fontsize=30)
    plt.axes(aspect=1)  # set this , Figure is round, otherwise it is an ellipse
    plt.pie(x=fracs, labels=labels,
            explode=explode, autopct='%3.1f %%',
            shadow=True, labeldistance=1.1,
            startangle=90, pctdistance=0.6)
    plt.savefig(outfile, dpi=360)
    plt.show()


if __name__ == '__main__':
    # # 海外信息
    # data_evaluation("data_keywords_abroad.dat", "emotions_abroad_pie_chart.jpg", "海外")
    # 国内信息
    data_evaluation("data_keywords_ncov_memory.dat", "emotions_domestic_pie_chart.jpg", "国内")

