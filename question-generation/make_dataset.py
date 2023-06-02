
import numpy as np  
import pandas as pd 
import json         



train_input_file_path = r"Enter path to train data"  # Json File
dev_input_file_path   = r"Enter path to dev data"   # Json File

def make_dataframe(file):  

    f = open ( file , "r") 
    data = json.loads(f.read())               
    iid = []                                  
    tit = []                                  
    con = []
    Que = []
    Ans_st = []
    Txt = []
    
    for i in range(len(data['data'])):      
        
        title = data['data'][i]['title']

        for p in range(len(data['data'][i]['paragraphs'])):  
            
            context = data['data'][i]['paragraphs'][p]['context']

            for q in range(len(data['data'][i]['paragraphs'][p]['qas'])): 
                
                question = data['data'][i]['paragraphs'][p]['qas'][q]['question']

                Id = data['data'][i]['paragraphs'][p]['qas'][q]['id']

                for a in range(len(data['data'][i]['paragraphs'][p]['qas'][q]['answers'])): 
                    
                    ans_start = data['data'][i]['paragraphs'][p]['qas'][q]['answers'][a]['answer_start']

                    text = data['data'][i]['paragraphs'][p]['qas'][q]['answers'][a]['text']
                    
                    tit.append(title)
                    con.append(context)
                    Que.append(question)                    
                    iid.append(Id)
                    Ans_st.append(ans_start)
                    Txt.append(text)

    print('Done')      