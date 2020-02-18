# -*- coding:utf-8 -*-
"""
Created on Saturday February 15 2020
@author Fenghaoguo
"""

from jieba import analyse

tfidf = analyse.extract_tags


def get_keywords(data_full_file, keywords_file):
    with open(data_full_file, "r") as fr, open(keywords_file, "w") as fw:
        for line in fr:
            #print(line)
            keywords = tfidf(line)
            #print(keywords)
            fw.write(' '.join(keywords))
            fw.write('\n')

    print("关键词抽取完毕。")


if __name__ == "__main__":
    # # 海外信息
    # main_data_full_file = "data_full_abroad.dat"
    # main_keywords_file = "data_keywords_abroad.dat"
    # get_keywords(main_data_full_file, main_keywords_file)
    # 国内信息
    main_data_full_file = "data_full_ncov_memory.dat"
    main_keywords_file = "data_keywords_ncov_memory.dat"
    get_keywords(main_data_full_file, main_keywords_file)
