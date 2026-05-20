# Fixed code for cell 8 - copy this into your notebook

Dataset1["Article"] = Dataset1["title"] + Dataset1["text"]
Dataset1.sample(frac = 1) #Shuffle 100%

# Fix the dtype issue by using .loc and converting to string first
Dataset1.loc[Dataset1.label == 'REAL', 'label'] = '1'
Dataset1.loc[Dataset1.label == 'FAKE', 'label'] = '0'
Dataset1['label'] = Dataset1['label'].astype(int)

Dataset1 = Dataset1.loc[:,['Article','label']]
Dataset1 = Dataset1.dropna()
