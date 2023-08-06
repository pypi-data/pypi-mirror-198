from smoothnlp.algorithm.phrase import extract_phrase
import re

def read_txt(filename):
    sentences = []
    with open(filename, "r") as f:
        for line in f.readlines():
            res = re.split("[,，。.、;；\'\"\(\)“（）【】\[\]\?？:：!！]", line.strip())
            #res = re.split(r'[;；.。，,！\n!?？]', line)
            sentences.extend(res)
    return sentences



res = extract_phrase(read_txt("kb.txt"))
print(res)