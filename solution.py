##Function to remove punction marks from words/sentences
def strip_punctuation(str):
    lst_chars = list(str)
    lst_chars_new = []
    word_new = ""
       
    for char in lst_chars:
        if char not in punctuation_chars:
            lst_chars_new.append(char)
     
    return word_new.join(lst_chars_new)


##Function to get count of positive words in sentence
def get_pos(str):
    print(str)
    pos_words_count = 0
    lst_word_new=[]
    
    str_splitted = str.lower().split(" ")
    print(str_splitted)
    
    for word in str_splitted:
        lst_word_new.append(strip_punctuation(word))
    
    print(lst_word_new)
        
    for word in lst_word_new:
        if word in positive_words:
            pos_words_count +=1
    print("Positive words count is =", pos_words_count) 
    
    return pos_words_count


##Function to get count of negative words in sentence
def get_neg(str):
    str_splitted = str.lower().split(" ")
    lst_word_new = []
    neg_words_count = 0
    
    for word in str_splitted:
        lst_word_new.append(strip_punctuation(word))
        
    print(lst_word_new)
    
    for word in lst_word_new:
        if word in negative_words:
            neg_words_count +=1
            
    print("Negative words count is = ", neg_words_count)
    
    return neg_words_count


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

##Read twitter data from file            
file_twitter_data = open("project_twitter_data.csv ","r")

##Write to resultant csv file
file_resultant_data_w = open("resulting_data.csv","w")
file_resultant_data_w.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
file_resultant_data_w.write("\n")

for line in file_twitter_data.readlines()[1:]:
    #print(line)
    line_stripped = line.strip()
    twitter_text = line_stripped.split(",")[0]
    #print(twitter_text)
    pos_score = get_pos(twitter_text)
    #print(pos_score)
    neg_score = get_neg(twitter_text)
    #print(neg_score)
    net_score = pos_score - neg_score
    #print(neg_score)
    retweet_count = line_stripped.split(",")[1]
    #print(retweet_count)
    replies_count = line_stripped.split(",")[2]
    print(replies_count)
    
    file_resultant_data_w.write(retweet_count)
    file_resultant_data_w.write(",")
    
    file_resultant_data_w.write(replies_count)
    file_resultant_data_w.write(",")
    
    file_resultant_data_w.write(pos_score)
    file_resultant_data_w.write(",")
    
    file_resultant_data_w.write(neg_score)
    file_resultant_data_w.write(",")
    
    file_resultant_data_w.write(net_score)
    file_resultant_data_w.write("\n")
    
file_resultant_data_w.close()

file_resultant_data_r = open("resulting_data.csv","r")
#print(file_resultant_data_r.read())

