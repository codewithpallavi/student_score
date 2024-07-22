
import numpy as np
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")
print(df.head())
print(df.describe())
print(df.info())
print((df.isnull().sum()))

# drop unamed column
df = df.drop("Unnamed: 0", axis=1)
print(df.head())


# # change weekly study hours column
# df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("5 - 10","5-10")  #df["WklyStudyHours"] why is here
# print(df.head())

# # gender distribution
# plt.figure(figsize=(4,4))
# ax = sns.countplot(data = df, x = "Gender")  #why i ax is here
# ax.bar_label(ax.containers[0])
# plt.title("Gender Distribution")
# plt.show()


# Frome tha above chart we have analysed that:
# the number of feamales in data is more then the number males

# gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
# # print(gb)

# plt.figure(figsize=(5,5))
# sns.heatmap(gb,annot = True)
# plt.title("Relationship btween parent's educatin and student's score")
# print(plt.show())

# From the above chart we have concluded that the:
#  education of a parents have a good impacts on the score


# gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
# # print(gb1)

# plt.figure(figsize=(5,5))
# sns.heatmap(gb1,annot = True)
# plt.title("Relationship BEtween Parent's Matrial Status and Student's Score")
# print(plt.show())

# From the above chart we have concluded that there :
# is no/negligible impact on student score, due to parents, material status.


# sns.boxplot(data = df, x = "MathScore")
# print(plt.show())


# print(df["EthnicGroup"].unique())


# ethnic_counts = df['EthnicGroup'].value_counts()

# # Step 2: Create list for counts and labels
# mylist = ethnic_counts.tolist()
# labels = ethnic_counts.index.tolist()

# # Step 3: Plotting the pie chart
# plt.figure(figsize=(8, 6))  # Optional: Adjust figure size if needed
# plt.pie(mylist, labels=labels, autopct='%1.2f%%')
# plt.title('Distribution of Ethnic Groups')
# plt.show()

ax = sns.countplot(data = df, x = "EthnicGroup")
(ax.bar_label(ax.containers[0]))
print(ax)

