import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 负号显示

covid_data = pd.read_csv("full_data.csv")
# 练习
covid_data.head(5)
covid_data.info()

print(covid_data.iloc[0,1])
print(covid_data.iloc[2,0:5])
print(covid_data.iloc[0:2,:])
print(covid_data.iloc[0:10:2,0:5])
print(covid_data.iloc[0:3,[0,1,3]])

print(covid_data["location"])
print(covid_data["location"]=="Afghanistan")
print(covid_data[covid_data["location"]=="Afghanistan"])
print(covid_data.loc[0:81,"total_cases"])

# 测试
# 显示前三列，且隔行输出
print(covid_data.iloc[0:10:2,0:3])
# 计算new cases的均值
covid_data["new_cases"].mean()
# 计算new_deaths的均值
covid_data["new_deaths"].mean()

list1 = []
list2 = []
for index,row in covid_data[["new_cases","new_deaths"]].iterrows():
    list1.append(row[0])
    list2.append(row[1])
# 绘制new cases的箱线图
df1 = pd.DataFrame(list1)
df1.plot.box(title="new_cases")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

# 绘制new_deaths的箱线图
df2 = pd.DataFrame(list2)
df2.plot.box(title="new_deaths")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

# 随着时间的推移，西班牙的新病例和总病例是如何发展的？
dff = covid_data[covid_data["location"]=="Spain"][["date","new_cases","total_cases"]]
x = dff["date"]
y1 = dff["new_cases"]
y2 = dff["total_cases"]

plt.plot(x, y1, c='r', ls='--', lw=3, label='new_cases')
plt.plot(x, y2, c='b', ls='-.',label='total_cases')
plt.title("西班牙的新病例和总病例变化趋势图")
plt.xlabel("date")
plt.ylabel("number")
plt.legend()
plt.show()
