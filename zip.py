import zipfile
# archive = 'images_data/archive (1).zip'
# with zipfile.ZipFile(archive, 'r') as zip_file:
#     zip_file.extractall('images_data')
import os
import pandas as pd
path_to_dataset = os.getcwd() + '/images_data/data.csv'
extension = path_to_dataset[-3:]
if extension == 'csv':
    annot = pd.read_csv(path_to_dataset)
    print('annot =', annot)

print(len(os.listdir('images_data')))
# else:
#     xml_df = self.xml_to_csv(path_to_dataset)
#     try:
#         xml_df.to_csv(self.path_to_images + '/data.csv', index=None)
#     except:
#         path_temp = self.path_to_images + '/data.csv'
#         xml_df.to_csv('/'.join(path_temp.split('/')[-2:]), index=None)