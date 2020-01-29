#%% All imports go here
import numpy as np
import pandas as pd
import pickle

#%% Load data
print('loading files...')
df_aisles = pd.read_csv('./data/aisles.csv')
df_departments = pd.read_csv('./data/departments.csv')
df_orders = pd.read_csv('./data/orders.csv')
df_order_products_prior = pd.read_csv('./data/order_products__prior.csv')
df_order_products_train = pd.read_csv('./data/order_products__train.csv')
df_products = pd.read_csv('./data/products.csv')

#%% Preprocessing
print('preprocessing data...')
# concatenate previous contents and train data
df_order_products = pd.concat([df_order_products_prior, df_order_products_train])
# merge order and order_products
df_merged_orders = pd.merge(df_orders, df_order_products, on='order_id')
# sort by user_id and order_number
df_merged_orders = df_merged_orders.sort_values(by=['user_id', 'order_number'], ascending=[True, True])
# get the user whose id is in the test dataset
df_merged_orders = df_merged_orders[df_merged_orders['user_id'].isin(df_orders[df_orders['eval_set'] == 'test']['user_id'].values)]

#%% add a day index for each user
print('adding data index...')
day_index = []
last_user = ''
last_order_number = 1
for index, row in df_merged_orders.iterrows():
    if row['order_number'] == 1 and last_user != row['user_id']:
        day_count = 0
        last_user = row['user_id']
        last_order_number = row['order_number']

    if last_order_number == row['order_number']:
        day_index.append(day_count)
    else:
        day_count += row['days_since_prior_order']
        last_order_number = row['order_number']
        day_index.append(day_count)

df_merged_orders['day_index'] = day_index

print(df_merged_orders.head())
df_merged_orders.to_pickle('./tmp/merged_orders')
#%% add the average purchase period, the days since last purchase, 5 reordered items
df_merged_orders[df_merged_orders['user_id'] & df_merged_orders['reordered'] == 1]['user_id'].unique()