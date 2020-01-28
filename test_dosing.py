import pandas as pd

data = pd.read_csv('t2_registry 20190619.csv').query('VISCODE == "w02" and SVDOSE == "Y"')
data2 = pd.read_csv('t2_ec 20190619.csv').query('ECSDSTXT != 280')
df = pd.DataFrame(data,columns=['ID','RID','VISCODE','SVDOSE','USERID'])
df2 =pd.DataFrame(data2,columns=['ID','RID','VISCODE','ECSDSTXT','USERID'])
keyin = ['RID','VISCODE']
df3 = pd.merge(df,df2, on=keyin, how='inner')
df3.to_csv('result.csv')
