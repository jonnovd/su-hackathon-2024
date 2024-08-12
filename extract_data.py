import pandas as pd

# Replace 'file_path.csv' with the actual path to your CSV file
df = pd.read_csv('data/train_labels.csv')

df_new = df.drop(df.index[list(range(40, 184)) + [214] + list(range(234, 237))
                          + [241] + list(range(258, 298)) + list(range(308, 311)) + [314]
                          + [317] + [321] + [330] + [331] + [348] + [355] + [356] + [385]
                          + [393] + [396] + [405] + [406] + [410] + [411] + [420] + [432]
                          + [444] + [461] + [463] + [467] + [472] + [474] + [488] + [490]
                          + [492] + [495] + [500] + [502] + [505] + [511] + [512] + [522]
                          + [527] + [536] + [537] + [546] + [547] + [553] + [557] + [563]
                          + [567] + [572] + [574] + [582] + [583] + [584] + [592] + [595]
                          + [583] + [597] + [607] + [611] + [615] + [617] + [618] + [619]
                          + [622] + [627] + [629] + [630] + [631] + [632] + [635] + [638]
                          + [640] + [641] + [643]])


for i in range(len(df_new)):
    pot_num = int(df_new.iloc[i]['Pothole number'])
    df_txt = pd.read_csv(f"data/train_annotations/p{pot_num}.txt", delimiter=' ', header=None)
    df_txt.columns = ['object-class', 'x', 'y', 'width', 'height']
    if df_txt.iloc[0].iloc[0] == 0.0:
        df_new.loc[df_new['Pothole number'] == pot_num, ['x_0', 'y_0', 'width_0', 'height_0']] = df_txt.iloc[0].iloc[[1, 2, 3, 4]].values

    if df_txt.iloc[0].iloc[0] == 1.0:
        df_new.loc[df_new['Pothole number'] == pot_num, ['x_1', 'y_1', 'width_1', 'height_1']] = df_txt.iloc[0].iloc[[1, 2, 3, 4]].values

    if df_txt.iloc[0].iloc[0] == 2.0:
        df_new.loc[df_new['Pothole number'] == pot_num, ['x_2', 'y_2', 'width_2', 'height_2']] = df_txt.iloc[0].iloc[[1, 2, 3, 4]].values

    if len(df_txt) == 2:
        if df_txt.iloc[0].iloc[0] == 1.0:
            df_new.loc[df_new['Pothole number'] == pot_num, ['x_1', 'y_1', 'width_1', 'height_1']] = df_txt.iloc[0].iloc[[1, 2, 3, 4]].values

        if df_txt.iloc[1].iloc[0] == 1.0:
            df_new.loc[df_new['Pothole number'] == pot_num, ['x_1', 'y_1', 'width_1', 'height_1']] = df_txt.iloc[1].iloc[[1, 2, 3, 4]].values

    if len(df_txt) == 3:
        df_new.loc[df_new['Pothole number'] == pot_num, ['x_0', 'y_0', 'width_0', 'height_0']] = df_txt.iloc[0].iloc[[1, 2, 3, 4]].values
        df_new.loc[df_new['Pothole number'] == pot_num, ['x_1', 'y_1', 'width_1', 'height_1']] = df_txt.iloc[1].iloc[[1, 2, 3, 4]].values
        df_new.loc[df_new['Pothole number'] == pot_num, ['x_2', 'y_2', 'width_2', 'height_2']] = df_txt.iloc[2].iloc[[1, 2, 3, 4]].values


# Print the entire DataFrame
df_new = df_new.fillna(0)
df_new = df_new.drop(columns=["Pothole number"])
print(df_new.iloc[0])
