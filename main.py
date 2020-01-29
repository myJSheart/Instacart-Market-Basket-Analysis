#%% All imports go here
import numpy as np
import pandas as pd
import seaborn as sns

#%% Load data
df_aisles = pd.read_csv('./data/aisles.csv')
df_departments = pd.read_csv('./data/departments.csv')
df_orders = pd.read_csv('./data/orders.csv')
df_order_products_prior = pd.read_csv('./data/order_products__prior.csv')
df_order_products_train = pd.read_csv('./data/order_products__train.csv')
df_products = pd.read_csv('./data/products.csv')

#%% Statistics