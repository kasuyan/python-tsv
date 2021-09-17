import pandas as pd


df = pd.read_csv('mid_list_a.tsv', names=['mid'])
df2 = pd.read_csv('mid_list_1.tsv', names=['mid'])
# print(df)

sorted_df = df.sort_values('mid', ascending=[1])
# print(sorted_df)

no_duplicated_df = sorted_df.drop_duplicates('mid', keep='first')

no_duplicated_df.to_csv('mid_list_b.csv', sep='\t')

tsv_list = []
tsv_list.append(no_duplicated_df)
tsv_list.append(pd.read_csv('mid_list_1.tsv', names=['mid']))
print(tsv_list)
merged_tsv = pd.concat(tsv_list)
print(merged_tsv.duplicated())
print(merged_tsv.duplicated().sum())
