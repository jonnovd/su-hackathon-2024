import pandas as pd

# Replace 'file_path.csv' with the actual path to your CSV file
df = pd.read_csv('data/train_labels.csv')

# Drop unwanted rows from df
indices_to_drop = list(range(40, 184)) + [214] + list(range(234, 237)) + [241] + list(range(258, 298)) + list(range(308, 311)) + [314] + [317] + [321] + [330] + [331] + [348] + [355] + [356] + [385] + [393] + [396] + [405] + [406] + [410] + [411] + [420] + [432] + [444] + [461] + [463] + [467] + [472] + [474] + [488] + [490] + [492] + [495] + [500] + [502] + [505] + [511] + [512] + [522] + [527] + [536] + [537] + [546] + [547] + [553] + [557] + [563] + [567] + [572] + [574] + [582] + [583] + [584] + [592] + [595] + [583] + [597] + [607] + [611] + [615] + [617] + [618] + [619] + [622] + [627] + [629] + [630] + [631] + [632] + [635] + [638] + [640] + [641] + [643]
df_new = df.drop(indices_to_drop)

# Iterate through the filtered DataFrame
for i in range(len(df_new)):
    pot_num = int(df_new.iloc[i]['Pothole number'])
    df_txt = pd.read_csv(f"data/train_annotations/p{pot_num}.txt", delimiter=' ', header=None)
    df_txt.columns = ['object-class', 'x', 'y', 'width', 'height']

    # Sort df_txt by 'object-class'
    df_txt = df_txt.sort_values(by='object-class')

    # Update df_new based on sorted df_txt
    for class_id in range(3):  # Assuming 'object-class' ranges from 0 to 2
        if len(df_txt[df_txt['object-class'] == class_id]) > 0:
            values = df_txt[df_txt['object-class'] == class_id].iloc[0][['x', 'y', 'width', 'height']].values
            df_new.loc[df_new['Pothole number'] == pot_num, [f'x_{class_id}', f'y_{class_id}', f'width_{class_id}', f'height_{class_id}']] = values

# Fill NaN values with 0 and drop the 'Pothole number' column
df_new = df_new.fillna(0)
#df_new = df_new.drop(columns=["Pothole number"])

# Print the entire DataFrame
print(df_new)
df_new.to_csv('df_new.csv', index=False)
