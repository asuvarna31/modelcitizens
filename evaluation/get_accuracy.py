import pandas as pd
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description ='eval')
parser.add_argument('--file', type = str, default=None, help='file name of responses')

args = parser.parse_args()

df = pd.read_csv(args.file)

count_in = 0
total = 0
for i in tqdm(range(len(df))):
    row = df.iloc[i]
    prediction = row['response']
    prediction = prediction.split("\n\n")[0]
    in_group_label = row['in_group_label']
        
    if not ("NO" in prediction and "YES" in prediction):
        if "YES" in prediction:
            prediction = 1
        elif "NO" in prediction:
            prediction=0
        else:
            prediction=-1

        if in_group_label == prediction:
            count_in += 1
        total += 1

print(f'total: {total} | accuracy : {100 * count_in / total}')