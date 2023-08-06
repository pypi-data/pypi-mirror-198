import jieba
import numpy as np
import pandas as pd
from pprint import pprint
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
from gensim import corpora, models, similarities
import networkx as nx

import wordcloud
import time
from matplotlib.pylab import datestr2num

import os
import pprint
import re
from ltp import LTP
import ltp
import torch

import numpy as np
# Plotting tools
import pyLDAvis
import pyLDAvis.gensim
import matplotlib.pyplot as plt

import jieba.analyse as analyse
from pandas import Series, DataFrame
import pandas as pd
import seaborn as sns
import hanlp
from cnsenti import Sentiment
from cnsenti import Emotion
from textrank4zh import TextRank4Keyword, TextRank4Sentence

from transformers import AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer,AutoTokenizer
from transformers import BartForConditionalGeneration
# Enable logging for gensim - optional
# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)


def time_tran(number):
    StyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(number))
    return StyleTime

#/home/bqw/gradual
def load_data(text_path):
    with open(text_path+'/body.txt', 'r', encoding='utf-8') as f:
        body_text = [i for i in list(f.readlines())]
    with open(text_path+'/title.txt', 'r', encoding='utf-8') as f:
        title_text = [i for i in list(f.readlines())]
    with open(text_path+'/time.txt', 'r', encoding='utf-8') as f:
        time_text = [i for i in list(f.readlines())]
    
    body_text=[meta.replace('\n','') for meta in body_text]
    title_text=[meta.replace('\n','') for meta in title_text]
    time_text=[int(eval(meta.replace('\n',''))) for meta in time_text]

    data_pd = {'title_text':title_text,
            'body_text':body_text,
            'time_text':time_text}
    df_data = DataFrame(data_pd)
    df_data.time_text=df_data.time_text.apply(time_tran)

    df_data=df_data.drop(df_data[(df_data['body_text'].eq('') | df_data['title_text'].eq(''))].index)
    def month_cut(text):
        return text[:7]
    def hour_cut(text):
        return text[11:13]
    df_data['month']=df_data.time_text.apply(month_cut)
    df_data['hour']=df_data.time_text.apply(hour_cut)
    
    return df_data


def trend_plot(df_data,work_dir='/home/bqw/gradual/textanalyze4sc/'):
    group1 = df_data.groupby('month')
    group1_data=group1.size()
    
    
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # x = range(len(data))
    x_date = [datestr2num(i) for i in list(group1_data.index)]
    plt.figure(figsize=(10,5))
    plt.title("三联生活周刊发布量变化图")
    plt.xlabel("时间")
    plt.xticks(rotation=45)
    plt.ylabel("发布量")
    plt.plot_date(list(group1_data.index),group1_data.values,'-',label="收盘价")
    # plt.plot_date(x_date,data['high'],'-',color='r',label="最高价")
    # plt.legend()
    plt.grid()
    plt.savefig(work_dir+'amount.jpg',bbox_inches = 'tight')
    return

def hot_plot(df_data,work_dir='/home/bqw/gradual/textanalyze4sc/'):
    group1 = df_data.groupby('month')
    group1_data=group1.size()
    
    group2 = df_data.groupby(['month', 'hour'])
    hot_matrix=np.zeros((12, 24))
    group2_data=group2.size()
    
    # month_map_dic=dict(zip(list(group2_data.index), range(12)))
    month_map_dic=dict(zip(sorted(list(set([meta[0] for meta in list(group2_data.index)]))), range(12)))
    for cur_index, cur_count in zip(list(group2_data.index), group2_data.values):
        cur_x=month_map_dic[cur_index[0]]
        cur_y=int(cur_index[1])
        hot_matrix[cur_x][cur_y]+=cur_count
        
    plot_data=pd.DataFrame(np.transpose(hot_matrix), index=list(range(24)), columns=list(group1_data.index))

    
    plt.figure(figsize=(8, 5))
    sns.heatmap(plot_data, cmap='Reds')
    plt.savefig(work_dir+'month_hour.jpg',bbox_inches = 'tight')
    plt.show()
    return

def get_keyword(df_data,work_dir='/home/bqw/gradual/textanalyze4sc/'):
    text=list(df_data.body_text)
    # 创建停用词列表
    def stopwordslist(stop_path=work_dir+'/stopwords-master/baidu_stopwords.txt'):
        stopwords = [line.strip() for line in open(stop_path, 'r', encoding='UTF-8').readlines()]
        return stopwords

    # 定义停词函数 对句子进行中文分词
    def seg_depart(sentence):
        # 对文档中的每一行进行中文分词
        sentence_depart = jieba.cut(sentence.strip())
        # 创建一个停用词列表
        stopwords = stopwordslist()
        # 输出结果为outstr
        outstr = ''
        # 去停用词
        for word in sentence_depart:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr
    # 分词后的结果
    result_fenci = []
    for i in text:
        # print(i)
        if seg_depart(i) != '':
            # print(seg_depart(i))
            result_fenci.append([i, seg_depart(i)])
    # # pd.DataFrame(result_fenci,columns=['rawtext','fencitext']).to_excel(path+'result.xlsx',index=False)
    result_fenci = [i[1].split(' ')[:-1] for i in result_fenci]
    
    def filter(text):
        return [w for w in text if len(w)>1]

    result_fenci_2gram = list(map(filter, result_fenci))
    df_data['fenci_2gram']=result_fenci_2gram
    
    keywords = analyse.textrank(''.join(result_fenci[0]), topK=50, allowPOS=('n','nz','v','vd','vn','l','a','d'))
    def extract(text):
        keywords=analyse.textrank(''.join(text), topK=50, allowPOS=('n','nz','v','vd','vn','l','a','d'))
        return keywords

    df_data['keyword_2gram']=df_data.fenci_2gram.apply(extract)
    group_key = df_data.groupby('month')

    return df_data
    
    
def word_cloud(df_data,work_dir='/home/bqw/gradual/textanalyze4sc/'):
    group1 = df_data.groupby('month')
    group1_data=group1.size()
    
    month_keyword=dict()
    for month in list(group1_data.index):
        cur_df_data=df_data[df_data['month']==month]
        #### 
        keyword_dic=dict()
        for meta in list(cur_df_data['keyword_2gram']):
            for word in meta:
                if word not in keyword_dic:
                    keyword_dic[word]=1
                else:
                    keyword_dic[word]=keyword_dic[word]+1
        cur_top=sorted(keyword_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:10]
        month_keyword[month]=cur_top

    #### 所有时间
    keyword_dic=dict()
    for meta in list(df_data['keyword_2gram']):
        for word in meta:
            if word not in keyword_dic:
                keyword_dic[word]=1
            else:
                keyword_dic[word]=keyword_dic[word]+1
    
    top50_all = sorted(keyword_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:50]

    print(top50_all)


    txt=[meta[0] for meta in top50_all]
    txt=' '.join(txt)
    # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path=work_dir+'msyh.ttc')

    # 将txt变量传入w的generate()方法，给词云输入文字
    w.generate(txt)
    # 将词云图片导出到当前文件夹
    w.to_file(work_dir+'key_cloud.png')
    
def get_entity(df_data,work_dir='/home/bqw/gradual/textanalyze4sc/'):
    tok = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)
    # hanlp.pretrained.ner.ALL # 语种见名称最后一个字段或相应语料库
    ner = hanlp.load(hanlp.pretrained.ner.MSRA_NER_ELECTRA_SMALL_ZH)
    
    
    def extract_ner(text):
        ner_list=ner(text, tasks='ner*')
        ner_list_=[meta[0] for meta in ner_list]
        ner_dict=dict()
        for cur_ner in ner_list_:
            if cur_ner not in ner_dict:
                ner_dict[cur_ner]=1
            else:
                ner_dict[cur_ner]+=1
        ner_ = sorted(ner_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:10]
        ner_ = [meta[0] for meta in ner_]
        return ner_
    df_data['ner_2gram']=df_data.fenci_2gram.apply(extract_ner)


    #### 所有时间
    keyword_dic=dict()
    for meta in list(df_data['ner_2gram']):
        for word in meta:
            if word not in keyword_dic:
                keyword_dic[word]=1
            else:
                keyword_dic[word]=keyword_dic[word]+1

    top50_all = sorted(keyword_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:100]
    top50_all=[meta[0] for meta in top50_all]
    print([meta[0] for meta in top50_all])
    return df_data
    
## 返回df_data语料库前100个实体
def entity_cloud(df_data,work_dir='/home/bqw/gradual/textanalyze4sc/'):
    tok = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)
    # hanlp.pretrained.ner.ALL # 语种见名称最后一个字段或相应语料库
    ner = hanlp.load(hanlp.pretrained.ner.MSRA_NER_ELECTRA_SMALL_ZH)
    
    
    def extract_ner(text):
        ner_list=ner(text, tasks='ner*')
        ner_list_=[meta[0] for meta in ner_list]
        ner_dict=dict()
        for cur_ner in ner_list_:
            if cur_ner not in ner_dict:
                ner_dict[cur_ner]=1
            else:
                ner_dict[cur_ner]+=1
        ner_ = sorted(ner_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:10]
        ner_ = [meta[0] for meta in ner_]
        return ner_
    df_data['ner_2gram']=df_data.fenci_2gram.apply(extract_ner)


    #### 所有时间
    keyword_dic=dict()
    for meta in list(df_data['ner_2gram']):
        for word in meta:
            if word not in keyword_dic:
                keyword_dic[word]=1
            else:
                keyword_dic[word]=keyword_dic[word]+1

    top50_all = sorted(keyword_dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)[:100]
    top50_all=[meta[0] for meta in top50_all]
    print([meta[0] for meta in top50_all])

    ##指定单词输出wordcloud
    ##过滤一部分
    ner_list_=['中国', '北京', '美国',   '三联',   '一年',   '英国',   '上海',   '晚上', '2021', '日本', '2022',    '第一个', '周末', '年代',  '欧洲', '夏天', '2020', '早上',   '世纪', '春天', '法国', '一个月', '三联生活周刊',   '云南',   '下午', '深夜', '德国', '冬天', '韩国',  '香港', '成都', '太阳', '俄罗斯', '鲁迅', '半年',   '第一人称', '春节', '地球',  '纽约', '白天', '深圳', '王海燕', '万元', '重庆', '意大利', '广东',  '第一步', '杭州', '巴黎', '四川',   '2019', '阿田', '苏州', '百年', '江南', '广州', '小贝', '一周',  '长沙',  '河南']
    ## all
    # ner_list=top50_all

    txt=' '.join(ner_list_)
    # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path=work_dir+'msyh.ttc')

    w.generate(txt)
    w.to_file(work_dir+'ner_cloud.png')
    return top50_all


##共现语义图，语料库：df_data，指定单词top50_all
def get_cosemantic(df_data, top50_all, work_dir='/home/bqw/gradual/textanalyze4sc/'):
    
    keywords = [meta[0] for meta in top50_all]
    matrix = np.zeros((len(keywords)+1)*(len(keywords)+1)).reshape(len(keywords)+1, len(keywords)+1).astype(str)
    matrix[0][0] = np.NaN
    matrix[1:, 0] = matrix[0, 1:] = keywords



    # cont_list = sum(test_list, [])
    # cont_list = result_fenci
    cont_list = list(df_data.fenci_2gram)

    for i, w1 in enumerate(keywords[:50]):
        for j, w2 in enumerate(keywords[:50]):
            count = 0
            for cont in cont_list:
                if w1 in cont and w2 in cont:
    #                 if abs(cont.index(w1)-cont.index(w2)) == 0 or abs(cont.index(w1)-cont.index(w2)) == 1:
                    if abs(cont.index(w1)-cont.index(w2)) <= 3:
                        count += 1
            matrix[i+1][j+1] = count
    df = pd.DataFrame(data=matrix)
    ## 必须，去掉表头
    df.to_csv(work_dir+'con_key.csv', index=False, header=None, encoding='utf-8-sig')
    df = pd.read_csv(work_dir+'con_key.csv')

    df.index = df.iloc[:, 0].tolist()
    df_ = df.iloc[:20, 1:21]
    df_.astype(int)


    plt.figure(figsize=(10, 10))
    graph1 = nx.from_pandas_adjacency(df_)

    options = {"node_size": 600, "node_color": "lightblue"}
    nx.draw(graph1, pos=nx.spring_layout(graph1), with_labels=True, font_size=20, edge_color='burlywood',**options)
    # nx.draw(graph1, pos=nx.spring_layout(graph1), with_labels=True, font_size=15, )
    plt.savefig('con_key.jpg',bbox_inches = 'tight')

##情感分析，text：给定文本
def get_emotion(text):
    senti = Sentiment()
    text=''.join(text)
    result = senti.sentiment_calculate(text)
    if result['pos'] > result['neg']:
        return 'pos'
    elif result['pos'] < result['neg']:
        return 'neg'
    elif result['pos'] == result['neg']:
        return 'neutral'


##细化
def get_emotion_sp(text):
    emotion = Emotion()

    text=''.join(text)
    result = emotion.emotion_count(text)
    return result


## 话题分析，df_data：给定语料
def get_topic(df_data):
    result_fenci = df_data.fenci_2gram
    id2word = corpora.Dictionary(result_fenci)
    id2word.filter_extremes(no_below=5, no_above=0.5)

    # 将字典转换为词袋,为文档中的每一个单词创建唯一的ID
    corpus = [id2word.doc2bow(doc) for doc in result_fenci]


    tfidf = gensim.models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]

    #多核并行lda模型
    tf_idf_lda_model = gensim.models.LdaMulticore(corpus_tfidf, num_topics=12, id2word=id2word, passes=2, workers=4)
    pprint(tf_idf_lda_model.print_topics(num_words=10))


    def get_topic_(text):
        tmp=tf_idf_lda_model.get_document_topics(id2word.doc2bow(text))
        tmp=sorted(tmp, key=lambda x: x[1], reverse=True)
        return tmp[0][0]

    df_data['topic']=df_data.fenci_2gram.apply(get_topic_)
    return df_data


def get_summary(text, sent_num=3, type="ext", language='en'):
    if language=='ch':
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=text, lower=True, source = 'all_filters')

        summary=[]
        # index是语句在文本中位置，weight是权重
        for item in tr4s.get_key_sentences(num=sent_num):
            # print(item.index, item.weight, item.sentence)
            summary.append(item.sentence)

        return '。'.join(summary)
    elif language=='en':
        checkpoint = "/home/bqw/.cache/torch/pytorch_transformers/bart_large_cnn"
        model = BartForConditionalGeneration.from_pretrained(checkpoint)
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        def predict(sentence):
            inputs = tokenizer([sentence],max_length = 1024, return_tensors='pt')
            summary_ids = model.generate(inputs['input_ids'], num_beams=70, max_length=150,min_length=50,early_stopping=True)
            summary = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids]
            return ' '.join(summary)
        return predict(text)



    


def get_graph(text):
    extractor = TripleExtraction()
    res = extractor.triples_main(text)
    return res


class LtpParser:
    def __init__(self):
        self.ltp = LTP()

        self.ltp_pipe = LTP("LTP/small")  # 默认加载 Small 模型
        if torch.cuda.is_available():
            # ltp.cuda()
            self.ltp_pipe.to("cuda")

    

    '''语义角色标注'''
    def format_labelrole(self, outputs):
#         roles = self.ltp.srl(hidden, keep_empty=False)
        roles = outputs.srl
        roles_dict = {}
        for role in roles[0]:
            roles_dict[role[0]] = {arg[0]: [arg[0], arg[1], arg[2]] for arg in role[1]}
        return roles_dict

    '''句法分析---为句子中的每个词语维护一个保存句法依存儿子节点的字典'''
    def build_parse_child_dict(self, words, postags, arcs):
        child_dict_list = []
        format_parse_list = []
        for index in range(len(words)):
            child_dict = dict()
            for arc_index in range(len(arcs)):
                if arcs[arc_index][1] == index+1:   # arcs的索引从1开始
                    if arcs[arc_index][2] in child_dict:
                        child_dict[arcs[arc_index][2]].append(arc_index)
                    else:
                        child_dict[arcs[arc_index][2]] = []
                        child_dict[arcs[arc_index][2]].append(arc_index)
            child_dict_list.append(child_dict)
        rely_id = [arc[1] for arc in arcs]  # 提取依存父节点id
        relation = [arc[2] for arc in arcs]  # 提取依存关系
        heads = ['Root' if id == 0 else words[id - 1] for id in rely_id]  # 匹配依存父节点词语
        for i in range(len(words)):
            # ['ATT', '李克强', 0, 'nh', '总理', 1, 'n']
            a = [relation[i], words[i], i, postags[i], heads[i], rely_id[i]-1, postags[rely_id[i]-1]]
            format_parse_list.append(a)
        return child_dict_list, format_parse_list

    '''parser主函数'''
    def parser_main(self, sentence):
#         "cws", "pos", "ner", "srl", "dep", "sdp"
        
        output = self.ltp_pipe.pipeline([sentence], tasks=["cws", "pos", "ner", "srl", "dep", "sdp"])
        words = output.cws
        postags = output.pos#
        arcs = output.dep#
        
        arc_index=1
        arc_ini=[]
        for a,b in zip(list(output.dep[0].values())[0], list(output.dep[0].values())[1]):

            arc_ini.append((arc_index,a,b))
            arc_index+=1
        arcs = arc_ini
        words, postags, arcs = words[0], postags[0], arcs
#         print(words, '\n', postags, '\n', arcs)
        child_dict_list, format_parse_list = self.build_parse_child_dict(words, postags, arcs)
        #roles_dict = self.format_labelrole(output)#
        ###########
        roles_dict={}
        for meta in output.srl[0]:
#             cur_dict={}
            cur_arg={}
            for ele in meta['arguments']:
                cur_arg[ele[0]]=ele[1]

            roles_dict[meta['predicate']]=cur_arg
#             roles_dict[meta]=(cur_dict)

        return words, postags, child_dict_list, roles_dict, format_parse_list


class TripleExtraction():
    def __init__(self):
        self.parser = LtpParser()

    '''文章分句处理, 切分长句，冒号，分号，感叹号等做切分标识'''
    def split_sents(self, content):
        #return self.parser.ltp.sent_split([content])
        #return self.parser.ltp.stn_split([content])
        #return self.parser.ltp.StnSplit().split([content])
        return ltp.StnSplit().split(content)

    
    '''利用语义角色标注,直接获取主谓宾三元组,基于A0,A1,A2'''
#     def ruler1(self, words, postags, roles_dict, role_index):
#         v = words[role_index]
#         role_info = roles_dict[role_index]
#         if 'A0' in role_info.keys() and 'A1' in role_info.keys():
#             s = ''.join([words[word_index] for word_index in range(role_info['A0'][1], role_info['A0'][2] + 1) if
#                          postags[word_index][0] not in ['w', 'u', 'x'] and words[word_index]])
#             o = ''.join([words[word_index] for word_index in range(role_info['A1'][1], role_info['A1'][2] + 1) if
#                          postags[word_index][0] not in ['w', 'u', 'x'] and words[word_index]])
#             if s and o:
#                 return '1', [s, v, o]
#         return '4', []

    def ruler1(self, cur_word, roles_dict, index):
        v = cur_word
        role_info = roles_dict[v]
        if 'A0' in role_info and 'A1' in role_info:
    #         s = ''.join([words[word_index] for word_index in range(role_info['A0'][1], role_info['A0'][2] + 1) if
    #                      postags[word_index][0] not in ['w', 'u', 'x'] and words[word_index]])
    #         o = ''.join([words[word_index] for word_index in range(role_info['A1'][1], role_info['A1'][2] + 1) if
    #                      postags[word_index][0] not in ['w', 'u', 'x'] and words[word_index]])
            s=role_info['A0']
            o=role_info['A1']
    #         s = ''.join([words[word_index] for word_index in range(role_info['A0'], role_info['A0'][2] + 1)
    #         o = ''.join([words[word_index] for word_index in range(role_info['A1'][1], role_info['A1'][2] + 1)
            if s and o:
                return '1', [s, v, o]
        return '4', []

    '''三元组抽取主函数
    关系类型	    Tag	Description	Example
    主谓关系	    SBV	subject-verb	我送她一束花 (我 <– 送)
    动宾关系	    VOB	直接宾语，verb-object	我送她一束花 (送 –> 花)
    间宾关系	    IOB	间接宾语，indirect-object	我送她一束花 (送 –> 她)
    前置宾语	    FOB	前置宾语，fronting-object	他什么书都读 (书 <– 读)
    兼语  	    DBL	double	他请我吃饭 (请 –> 我)
    定中关系	    ATT	attribute	红苹果 (红 <– 苹果)
    状中结构	    ADV	adverbial	非常美丽 (非常 <– 美丽)
    动补结构	    CMP	complement	做完了作业 (做 –> 完)
    并列关系	    COO	coordinate	大山和大海 (大山 –> 大海)
    介宾关系	    POB	preposition-object	在贸易区内 (在 –> 内)
    左附加关系	LAD	left adjunct	大山和大海 (和 <– 大海)
    右附加关系	RAD	right adjunct	孩子们 (孩子 –> 们)
    独立结构	    IS	independent structure	两个单句在结构上彼此独立
    核心关系	    HED	head	指整个句子的核心
    '''
    def ruler2(self, words, postags, child_dict_list, arcs, roles_dict):
        svos = []
        for index in range(len(postags)):
            # print(index)
            tmp = 1
            
#             if index in roles_dict:
                
            cur_word=words[index]

#             roles_dict_flag=[list(meta.keys())[0] for meta in roles_dict]
            if cur_word in roles_dict:
#                 print(cur_word)
#                 print(roles_dict)
#                 print(index)
                flag, triple = self.ruler1(cur_word, roles_dict, index)
                if flag == '1':
                    svos.append(triple)
                    tmp = 0
            if tmp == 1:
                # 如果语义角色标记为空，则使用依存句法进行抽取
                if postags[index]:
                    # 抽取以谓词为中心的事实三元组
                    child_dict = child_dict_list[index]
                    # 主谓宾
                    if 'SBV' in child_dict and 'VOB' in child_dict:
                        r = words[index]
                        e1 = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                        e2 = self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                        svos.append([e1, r, e2])

                    # 定语后置，动宾关系
                    relation = arcs[index][0]
                    head = arcs[index][2]
                    if relation == 'ATT':
                        if 'VOB' in child_dict:
                            e1 = self.complete_e(words, postags, child_dict_list, head - 1)
                            r = words[index]
                            e2 = self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0])
                            temp_string = r + e2
                            if temp_string == e1[:len(temp_string)]:
                                e1 = e1[len(temp_string):]
                            if temp_string not in e1:
                                svos.append([e1, r, e2])
                    # 含有介宾关系的主谓动补关系
                    if 'SBV' in child_dict and 'CMP' in child_dict:
                        e1 = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0])
                        cmp_index = child_dict['CMP'][0]
                        r = words[index] + words[cmp_index]
                        if 'POB' in child_dict_list[cmp_index]:
                            e2 = self.complete_e(words, postags, child_dict_list, child_dict_list[cmp_index]['POB'][0])
                            svos.append([e1, r, e2])
        return svos

    '''对找出的主语或者宾语进行扩展'''
    def complete_e(self, words, postags, child_dict_list, word_index, deep=0):
        deep += 1
        if deep == 3:
            return ""
        child_dict = child_dict_list[word_index]
        prefix = ''
        if 'ATT' in child_dict:
            for i in range(len(child_dict['ATT'])):
                prefix += self.complete_e(words, postags, child_dict_list, child_dict['ATT'][i], deep)
        postfix = ''
        if postags[word_index] == 'v':
            if 'VOB' in child_dict:
                postfix += self.complete_e(words, postags, child_dict_list, child_dict['VOB'][0], deep)
            if 'SBV' in child_dict:
                prefix = self.complete_e(words, postags, child_dict_list, child_dict['SBV'][0], deep) + prefix
        return prefix + words[word_index] + postfix

    '''程序主控函数'''

    def triples_main(self, content):
        sentences = self.split_sents(content)
        sentences = [sent for sent in sentences if len(sent.strip()) > 5]
        svos = []
        for sentence in sentences:
            words, postags, child_dict_list, roles_dict, arcs = self.parser.parser_main(sentence)

            # print(words)
            # print(postags)
            # pprint.pprint(child_dict_list)
            # pprint.pprint(roles_dict)
            # pprint.pprint(arcs)

            svo = self.ruler2(words, postags, child_dict_list, arcs, roles_dict)
            svos += svo
        return svos