import os
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'housing.data'
plots_dir  = 'plots'
plots_format = 'png'

housing_df = pd.read_csv(file_path, sep='\s+', header=0)
housing_df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV']

print(housing_df.describe().to_string())

os.makedirs(plots_dir, exist_ok=True)

for feature_idx, feature_name in enumerate(housing_df.columns):
   print('Generating ' + feature_name + ' histogram...')
   plt.hist(housing_df[feature_name], bins=3, color='g')
   plt.title(feature_name+' Histogram')
   plt.xlabel(feature_name)
   plt.ylabel('Count')
   plots_file = plots_dir + '/' + 'hist_' + feature_name + '.' + plots_format
   plt.savefig(plots_file, format=plots_format)
   plt.clf()

for feature1_idx, feature1_name in enumerate(housing_df.columns):
   for feature2_idx, feature2_name in enumerate(housing_df.columns):
      if feature1_idx != feature2_idx:
         print('Generating ' + feature1_name + ' to ' + feature2_name + ' scatter plot...')
         plt.scatter(housing_df[feature1_name], housing_df[feature2_name], color='b')
         plt.title(feature1_name + ' to ' + feature2_name)
         plt.xlabel(feature1_name)
         plt.ylabel(feature2_name)
         plots_file = plots_dir + '/' + feature1_name + '_to_' + feature2_name + '.' + plots_format
         plt.savefig(plots_file, format=plots_format)
         plt.clf()

plt.close()
