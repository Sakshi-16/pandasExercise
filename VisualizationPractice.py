import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

pd.set_option("display.width",1000)
pd.set_option("display.max_columns",10)
path = 'F:/Data Science/company_sales_data.csv'

df = pd.read_csv(path)
print(df.head())

# plt.plot(df['month_number'],df['total_profit'],linestyle = '--',color='red',marker='o',markerfacecolor='black',linewidth=3,markersize=12)
# plt.xlabel('Month Number')
# plt.ylabel('Sold units number')
# plt.xticks(df['month_number'])
# red_patch = mpatches.Patch(color='red',label='Profits in a month')
# plt.legend(handles=[red_patch],loc='lower right')
# plt.show()

x = df['month_number']
# plt.plot(x,df['facecream'],color='blue',label='Face Cream')
# plt.plot(x,df['facewash'],color='orange',label='Face Wash')
# plt.plot(x,df['toothpaste'],color='green',label='ToothPaste')
# plt.plot(x,df['bathingsoap'],color='red',label='Bathing Soap')
# plt.plot(x,df['shampoo'],color='purple',label='Shampoo')
# plt.plot(x,df['moisturizer'],color='brown',label='Moisturizer')
# plt.legend(loc='upper left')
# plt.show()
# plt.stackplot(x, df['facecream'], df['facewash'], df['toothpaste'],
#               df['bathingsoap'], df['shampoo'], df['moisturizer'],
#               colors=['blue','orange','green','red','purple','brown'],
#               labels=['Face Cream','Facewash','toothpaste','soap','shampoo','moist'])
# plt.legend(loc='upper left')
# plt.show()

# plt.scatter(x,df['toothpaste'],color='blue',label='Tooth Paste Sales Data',s=30)
# plt.xticks(x)
# plt.legend(loc='upper left')
# plt.grid(linestyle='--')

# plt.bar(x-0.125,df['facecream'],color='blue',label='Face Cream sales data',width=0.25)
# plt.bar(x+0.125,df['facewash'],color='orange',label='Face Wash sales data',width=0.25)
# plt.legend(loc='upper left')
# plt.grid(linestyle='--')
# plt.xticks(x)
# plt.savefig('F:/Data Science/facewashVSfacecream.png',dpi=150)
# plt.show()


# bins = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
# plt.hist(df['total_profit'],bins=bins)
# plt.xticks(bins,rotation=45)
# plt.show()

# fc = df.iloc[:,1].sum()
# fw = df.iloc[:,2].sum()
# tp = df.iloc[:,3].sum()
# bs = df.iloc[:,4].sum()
# sp = df.iloc[:,5].sum()
# mz = df.iloc[:,6].sum()
# x = [fc,fw,tp,bs,sp,mz]
# labels = df.columns.values[1:7]
# plt.pie(x,labels=labels,autopct='%1.1f%%',explode=(0,0,0.2,0,0,0),shadow=True)
# plt.legend(loc='lower center')
# plt.show()

plt.bar(x,df['total_profit'])
plt.show()
plt.boxplot(df['total_profit'])
plt.show()