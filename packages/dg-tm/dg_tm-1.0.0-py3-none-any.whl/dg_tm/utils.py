import os
import json
import re
import numpy as np
from pdf2txt_decoder.pdf2txt_decoder import Pdf2TxtDecoder



def read_jieba_dict(filename="dict.txt"):
    di = dict()
    with open(filename, "r") as f:
        for line in f:
            temp = line.strip().split()
            word, freq = temp[0], int(temp[1])
            di[word] = freq
    return di



def read_txt(filename):
    sentences = []
    with open(filename, "r") as f:
        for line in f:
            res = re.split("[,，。.、;；\'\"\(\)“（）【】\[\]\?？:：!！\\s+]", line)
            sentences.extend(res)
    sentences = list(set(sentences))
    return sentences




