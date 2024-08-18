import pandas as pd

def main(t_labels: str, t_annots: str):
    df_new = pd.read_csv(t_labels)

    for i in range(len(df_new)):
        pot_num = int(df_new.iloc[i]['Pothole number'])
        df_txt = pd.read_csv(f"{t_annots}/p{pot_num}.txt", delimiter=' ', header=None)
        df_txt.columns = ['object-class', 'x', 'y', 'width', 'height']

        df_txt = df_txt.sort_values(by='object-class')

        for class_id in range(3):
            if len(df_txt[df_txt['object-class'] == class_id]) > 0:
                values = df_txt[df_txt['object-class'] == class_id].iloc[0][['x', 'y', 'width', 'height']].values
                df_new.loc[df_new['Pothole number'] == pot_num, [f'x_{class_id}', f'y_{class_id}', f'width_{class_id}', f'height_{class_id}']] = values

    df_new = df_new.fillna(0)

    print(df_new)
    df_new.to_csv('test_data.csv', index=False)

if __name__ == '__main__':
    t_labels = '../merged_data/test_labels.csv'
    t_annots = '../merged_data/test_annotations'
    main(t_labels, t_annots)