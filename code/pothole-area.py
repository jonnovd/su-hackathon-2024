import pandas as pd
import numpy as np

# In metres squared
def get_pothole_area(w0: float, h0:float, w1: float, h1:float)-> float:
    hypot = np.sqrt(w1*w1 + h1*h1)

    scale = 0.5 / hypot
    w1_actual = scale * w1
    h1_actual = scale * h1

    w_ratio = w0/w1
    h_ratio = h0/h1

    w0_actual = w_ratio*w1_actual
    h0_actual = h_ratio*h1_actual

    area = (w0_actual) * (h0_actual)
    return area


def main(df_path: str):
    print("MAIN")

    df = pd.read_csv(df_path)
    print(df)
    print(df.loc[df['x_0'] == 0, :])

    df['pothole_area'] = 0.0

    for i in df.index:
        if (df.loc[i, 'x_1'] != 0):
            w0 = df.loc[i, 'width_0']
            h0 = df.loc[i, 'height_0']
            w1 = df.loc[i, 'width_1']
            h1 = df.loc[i, 'height_1']
            df.loc[i, 'pothole_area'] = get_pothole_area(w0, h0, w1, h1)

    
    df.to_csv('df_area.csv', index=False)

    #print(df)
    print(df.loc[df['pothole_area'] != 0, :])


if __name__ == "__main__":
    path_to_dataframe = 'model_data.csv'
    main(path_to_dataframe)


