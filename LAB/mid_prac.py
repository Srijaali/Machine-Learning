#loc func:
sample = cancer.loc[550:900, 'Gender':'Coughing of Blood']
#iloc func:
print('index of Shortness of Breath: ', cancer.columns.get_loc('Shortness of Breath'))
print('index of Frequent Cold: ', cancer.columns.get_loc('Frequent Cold'))
sample2 = cancer.iloc[-20:, 18:23]
sample2.to_csv('sample2.csv')
