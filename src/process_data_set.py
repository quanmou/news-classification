import os
import re
import jieba

labels = {0: "体育", 1: "军事", 2: "娱乐", 3: "旅行", 4: "游戏", 5: "社会", 6: "科技", 7: "财经"}
ARTICLE_AMOUNT = 200

stop_words = list()
with open(r'../data_set/stop_words.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        stop_words.append(line.strip())

words_list = list()
for i in range(len(labels)):
    for root, dirs, files in os.walk(r'../data_set/' + labels[i]):
        count = 1
        for item in files:
            words_line = ""
            with open(os.path.join(root, item), 'r', encoding='utf-8') as f:
                content = f.read().split('\n', 2)[2]
                text = content.replace('\n', ' ')
                words = jieba.cut(text.strip())
                for word in words:
                    word = word.strip()
                    if word not in stop_words:
                        if not re.match('[a-zA-Z0-9\s!]', word):
                            words_line += word + ' '

            # print(words_line)
            words_list.append(words_line)
            if count == ARTICLE_AMOUNT:  # Only use the first ARTICLE_AMOUNT articles
                break
            else:
                count += 1

# Save processed texts
with open(r'../data_set/words_set.txt', 'w', encoding='utf-8') as f:
    for item in words_list:
        f.write(item + '\n')

with open(r'../data_set/labels_set.txt', 'w', encoding='utf-8') as f:
    for i in range(8 * ARTICLE_AMOUNT):
        num = int(i / ARTICLE_AMOUNT)
        f.write(str(num) + '\n')
