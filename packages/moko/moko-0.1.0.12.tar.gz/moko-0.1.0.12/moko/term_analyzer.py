     
def word_count(word_list):
    wordCount = {}
    for word in word_list:
        wordCount[word] = wordCount.get(word, 0) + 1
        sorted_dict = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

def co_occurence_count(word_lst):
    co_dic = {}
    for i,a in enumerate(word_lst):
        #for b in word_lst[i+1:i+11]:
        for b in word_lst[i+1:]:
            if a == b: continue
            #print(i,a,b)
            if a > b: c, d = b, a
            else: c, d = a, b
            co_dic[c, d] = co_dic.get((c, d), 0) + 1
    return co_dic
