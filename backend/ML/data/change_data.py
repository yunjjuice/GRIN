# -*- encoding: utf-8 -*-
f = open("after_change.txt", 'w', encoding='UTF8')
bf = open("ko_emo_befor8.txt", 'r', encoding='UTF8')

emo = ["Positive","Negative","Anger","Anticipation","Disgust","Fear","Joy","Sadness","Surprise","Trust"]
lines = bf.readlines()
for line in lines:
    sp = line.split('\t')
    word = sp[0]
    if word == "NO TRANSLATION":
        continue

    for i in range(1,11):
        f.write(word+"\t"+emo[i-1]+"\t"+sp[i]+"\n")



f.close()
bf.close()

tf = open("after_change2.txt", 'w', encoding='UTF8')
f = open("after_change.txt", 'r', encoding='UTF8')
lines = f.readlines()
for line in lines:
    if line[0] == '\n':
        continue
    tf.write(line)
f.close()
tf.close()

