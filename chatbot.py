import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import operator
nltk.download('punkt')
nltk.download('wordnet')

f=open('pdeu.txt','r',encoding='utf-8',errors='ignore')
raw=f.read()
raw=raw.lower()
#print(raw)
sent_tokens=nltk.sent_tokenize(raw)
sent_tokens=[x.replace('\n','') for x in sent_tokens]
word_tokens=nltk.word_tokenize(raw)
lemmer=nltk.stem.WordNetLemmatizer()
print(sent_tokens)
print(len(sent_tokens))

def lemmatize(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)

def normalize(text):
    return lemmatize(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


greet_resp=["hello welcome!!","hi how are you?","Pleasure to hear from you!!!","Hello sir","nice to  meet you sir!!!","What can I do for you?"]
greet_inp=["hi","hey","hello","howdy","how are you?"]
def greet(sent):
    for word in sent.split():
        if word.lower() in greet_inp:
            return random.choice(greet_resp)
    return None


def resp(user_inp):
    ans=[]
    ind=[]
    hue=3
    sent_tokens.append(user_inp)
    #print('Tok'sent_tokens)
    tfidvec=TfidfVectorizer(tokenizer=normalize,stop_words='english')
    tfid=tfidvec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfid[-1],tfid)
    d={}
    for i in range(0,len(vals[0])):
    	d[i]=vals[0][i]
    sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    #print("Dict",sorted_d)
    for (key,val) in sorted_d.items():
    	if(hue>0 and val>0):
    		ind.append(key)
    	else:
    		break
    	hue-=1
    #print("vals",vals[0])
    #print("indexes :: ",ind)
    
    #print(ind)
    flat=vals.flatten()
    
    flat=sorted(flat,reverse=True)
    #print('flat',flat)
    req_tfid=flat[0]
    if(req_tfid==0):
        ans=ans+"I am sorry! I don't understand you"    
    else:
        for index in ind: 
            ans.append(sent_tokens[index])
    return ans

def get_bot_resp(user_inp):
    flag=False
    while(1):
        ans=greet(user_inp.lower())
        print("got ans for query",ans,user_inp)
        if(ans!=None):
            flag=True
            return ans,flag
        return resp(user_inp.lower()),flag

'''
user_inp=input("Enter Text")
got=get_bot_resp(user_inp)
print(sent_tokens)
'''

