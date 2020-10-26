import pandas as pd
# path = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

pd.set_option("display.max_columns",20)
pd.set_option('display.width', 1000)
# chipo = pd.read_csv(path,sep='\t')

# print(chipo.head(10))
# print(chipo.shape[0])
# print(chipo.shape[1])
# for i in chipo.columns:
#     print(i,end=' ')
#
# print()
# print(chipo.index)
#
# most_ord = chipo['item_name'][0]
# max_c = chipo['quantity'][0]
# dic = {chipo['item_name'][0]:chipo['quantity'][0]}
#
# for i in range(1,chipo.shape[0]):
#     try:
#         dic[(chipo['item_name'][i])] += chipo['quantity'][i]
#     except:
#         dic[(chipo['item_name'][i])] = chipo['quantity'][i]
#
#     if (dic[(chipo['item_name'][i])] > max_c):
#         max_c = dic[(chipo['item_name'][i])]
#         most_ord = chipo['item_name'][i]
#
# print(most_ord)
# print(max_c)
#
# print(chipo['quantity'].sum())
# print(type(chipo['item_price'][0]))
# chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
# print(type(chipo['item_price'][0]))
#
# chipo['revenue'] = chipo['quantity']*chipo['item_price']
# print(chipo['revenue'].sum())
#
# print(len(chipo['order_id'].unique()))
#
# print(chipo['revenue'].sum()/(len(chipo['order_id'].unique())))
# print(len(chipo['item_name'].unique()))
#
#
# print(chipo.groupby('item_name'))
# df = chipo.iloc[:,[2,4]]
# print(df.sort_values(by="item_name"))
#
# df = df.sort_values(by='item_price',ascending=False)
# print(df)
# print(chipo.iloc[df.head(1).index[0],1])
#
# print((chipo['quantity'].loc[chipo['item_name']=='Veggie Salad Bowl']).sum())
# print((chipo.loc[(chipo['item_name']=='Canned Soda') & (chipo['quantity']>1)]).shape[0])




# path = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
# users = pd.read_csv(path,sep='\t',delimiter='|')
# users.index = users['user_id']
# users.drop(['user_id'],axis=1,inplace=True)
# # print(users.head(25))
# # print(users.tail(10))
# print(users.shape[0])
# print(users.shape[1])
# print(users.columns.values)
# print(users.index)
# print(users.dtypes)
# # print(users['occupation'])
# print(len(users['occupation'].unique()))
# # print(users['occupation'].value_counts())
# print(users['occupation'].value_counts().head(1).index[0])
# print(users.info())
#
# print(users.describe(include='all'))
# print(users.occupation.describe())
# print(users.age.mean())
# print(users.age.value_counts().tail(5))
#
# print(users.columns.values[3])
# print(users.dtypes[3])


# path = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
# euro12 = pd.read_csv(path,sep='\t',delimiter=',')
# print(euro12.Goals)
# print(euro12.Team.nunique())
# print(euro12.shape[1])
#
# discipline = euro12.loc[:,['Team', 'Yellow Cards','Red Cards']]
# discipline = discipline.sort_values(by=['Red Cards','Yellow Cards'])
# print(discipline)
# print(discipline['Yellow Cards'].mean())
# print(euro12.Team.loc[euro12.Goals>6])
# print(euro12.iloc[:,0:7])
# print(euro12.iloc[:,0:-3])
# print(euro12.loc[euro12.Team.isin(['England','Italy','Russia']),['Shooting Accuracy']])
# print(euro12.Team.loc[euro12.Team.str.startswith('G')])



# raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
#             'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
#             'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
#             'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
#             'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
#             'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
#             'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
#             'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
#             'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
#             'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}
#
# columns = list(raw_data.keys())
# army = pd.DataFrame.from_dict(raw_data,orient='columns')
# army.index = army.origin
# army.drop('origin',axis=1,inplace=True)
# print(army[['veterans','deaths']])
# print(army.columns.values)
#
# print(army.loc[['Maine','Alaska'],['deaths', 'size' , 'deserters']])
# print(army.iloc[2:7,2:6])
# print(army.iloc[:4])
# print(army.iloc[:,2:7])
# print(army.loc[army.deaths>50])
# print(army.loc[(army.deaths>500) | (army.deaths<50)])
# print(army.regiment.loc[army.regiment!='Dragoons'])
# print(army.loc[['Texas','Arizona']])
# print(army.loc['Arizona',army.columns.values[2]])
# print(army.deaths.iloc[2])


#
# raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
#         'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
#         'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
#         'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
#         'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
#
# regiments = pd.DataFrame.from_dict(raw_data)
# regiments.index = regiments.regiment
# regiments.drop('regiment',inplace=True,axis=1)
# regiments.company = regiments.company.apply(lambda x: int(x[:-2]))
# print(regiments)
#
# nighthawks_reg = regiments.loc['Nighthawks']
# print(nighthawks_reg.preTestScore.mean())
# print(regiments.groupby('company').describe())
#
# print(regiments.groupby(['company']).mean().loc[:,['preTestScore']])
# print(regiments.groupby(['regiment','company']).mean().loc[:,['preTestScore']].unstack())
# print(regiments.groupby(['regiment','company']).size())
#
# for n,g in regiments.groupby('regiment  '):
#     print(n)
#     print(g)
#     print("\n")


# path = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
# users = pd.read_csv(path,sep='\t',delimiter='|')
# print(users.head())
# print(users.groupby('occupation').age.mean())
# total_per_o = users.groupby(['occupation']).size()
# males_per_o = (users.loc[users.gender=='M']).groupby(['occupation']).size()
# for i in total_per_o.index.values:
#     print(i,end=" ")
#     print(males_per_o[i]/(total_per_o[i]))
#
# print(users.groupby('occupation').age.agg(['min','max']))
#
# print(users.groupby(['occupation','gender']).age.mean())
# genders_per_o = users.groupby(['occupation','gender']).size()
# perc = genders_per_o.div(total_per_o,level='occupation')*100
# print(perc)
#

#
# path = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
# df = pd.read_csv(path,sep='\t',delimiter=',')
# df = df.iloc[:,0:12]
#
#
# def capitalize(s):
#     return s.upper()
#
# df['Mjob']= df['Mjob'].apply(capitalize)
# df['Fjob']= df['Fjob'].apply(capitalize)
#
# def legal(n):
#     if(n>17):
#         return True
#     else:
#         return False
#
# df['Legal Drinker'] = df['age'].apply(legal)
# # df = df.apply(lambda x:x*10)
# print(df.head())

# path = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
# crime = pd.read_csv(path,sep='\t',delimiter=',')
# crime.Year = pd.to_datetime(crime.Year,format='%Y')
# # print(crime.dtypes)
# crime = crime.set_index(crime.Year,drop=True)
# crime.drop('Total',axis=1,inplace=True)
#
# print(crime.head())

import random
# dic = {'A': random.choices(range(1,5),k=100),
# 'B' : random.choices(range(1,4),k=100),
# 'C' : random.choices(range(10000,30001),k=100)}
#
# df = pd.DataFrame.from_dict(dic)
# namesMap = { 'A':'bedrs', 'B':'bathrs', 'C':'price_sqr_meter'}
# df = df.rename(columns=namesMap)
# print(df.head())
# print(df.shape[0])
#
# bigcolumn = pd.concat([pd.Series(dic['A']),pd.Series(dic['B']),pd.Series(dic['C'])],axis=0)
# bigcolumn = bigcolumn.to_frame()
# bigcolumn.reset_index(drop=True,inplace=True)
# print(bigcolumn)


# raw_data_1 = {
#         'subject_id': ['1', '2', '3', '4', '5'],
#         'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
#         'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
#
# raw_data_2 = {
#         'subject_id': ['4', '5', '6', '7', '8'],
#         'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
#         'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
#
# raw_data_3 = {
#         'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
#         'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
#
#
# data1 = pd.DataFrame.from_dict(raw_data_1)
# data2 = pd.DataFrame.from_dict(raw_data_2)
# data3 = pd.DataFrame.from_dict(raw_data_3)
#
# all_data = pd.concat([data1,data2],ignore_index=True)
# print(all_data)
#
# # all_data_col = pd.concat([data1,data2],axis=1,ignore_index=True)
# # print(all_data_col)
#
# all_data_tests = pd.merge(all_data,data3,on='subject_id')
# print(all_data_tests)

# import matplotlib.pyplot as plt
# path = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# chipo = pd.read_csv(path,sep='\t',delimiter='\t')
# print(chipo.head(10))
# chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
#
# chipo_orders = (chipo.groupby('order_id'))[['quantity','item_price']].sum()
# print(chipo_orders.head())
#
# plt.scatter(chipo_orders.item_price,chipo_orders.quantity,color='green',s=2)
# plt.xticks(rotation=45,size=8)
# plt.xlabel = 'Order Prices'
# plt.ylabel = 'Order Quantity'
# plt.show()
#
# chipo_items = chipo.groupby('item_name')['quantity'].sum()
# chipo_items = chipo_items.s
#
# print(chipo_items.head())
# plt.bar(chipo_items.head())
# plt.hist(chipo.item_name)
# plt.xticks(rotation=45,size=8)
# plt.show()
#

a = [1,2,3,4,5]
b = [6,7,8,9,10]
multi = lambda x,y:x*y
for i in range(5):
    print(multi(a[i],b[i]))

s = 'abcdefghi'
print(s[-1::-1])
