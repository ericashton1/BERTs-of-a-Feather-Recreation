#TURN HANS DATA INTO TSV

import pandas as pd

data = {'textid': [], 'text': [], 'pair': [], 'target': []}

with open('data/heuristics_evaluation_set.txt', 'r') as file:
    lines = file.readlines()
    textid = 0
    for line in lines[1:]:
        line = line.split('\t')
        #print("\nLine: ", line)
        
        data['textid'].append(textid)
        textid += 1
        i = 0
        for sent in line:
            # print("\n" + str(i))
            # print("\nSent: ", sent)
            
            if (i == 0):
                data['target'].append(sent)
            elif (i == 5):
                data['text'].append(sent)
            elif (i == 6):
                data['pair'].append(sent)
            i += 1
#print("Data: ", data)

dataframe = pd.DataFrame(data)
dataframe.to_csv('data/hans_data.tsv', sep = '\t')



#TURN MNLI DATA INTO TSV
from datasets import load_dataset
import pandas as pd

ds = load_dataset("SetFit/mnli")
#print(ds)
#using validate data because test data was unlabeled. Validate is similar size
#to test and this was not validation data used in real study
test_dataframe = ds['validation'].to_pandas()
#print(test_dataframe.head())

data_dict = {'textid': [], 'text': [], 'pair': [], 'target': []}

for i in range(len(test_dataframe['idx'])):
    data_dict['textid'].append(i)
    data_dict['text'].append(test_dataframe['text1'][i])
    data_dict['pair'].append(test_dataframe['text2'][i])
    if (test_dataframe['label'][i] == 0):
        data_dict['target'].append('entailment')
    else:
        data_dict['target'].append('non-entailment')
#print(data_dict['target'])
        
final_df=pd.DataFrame(data_dict)
final_df.to_csv('data/mnli_data.tsv', sep = '\t')