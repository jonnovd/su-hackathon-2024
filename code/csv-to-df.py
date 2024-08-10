import pandas as pd
import numpy as np
import os


def populate_df(data_dir: str, df: pd.DataFrame, cols: str) -> pd.DataFrame:
    os.chdir(data_dir)

    for file in os.listdir():
        if file.endswith(".txt"):
            pic_id = file[0 : file.index(".")]

            with open(file) as f:
                line = f.readline()

                while line != "":
                    tokens = []
                    tokens.append(pic_id)
                    tokens.extend(line.split(" "))
                    tokens = [t.strip() for t in tokens]
                    if len(tokens) == 6:
                        row_df = pd.DataFrame([tokens], columns=cols)
                        df = pd.concat([df, row_df], ignore_index=True)
                    else:
                        print(f"Invalid format data. Line skipped: {tokens}")

                    line = f.readline()

    os.chdir("../")
    return df


def main(data_dir: str, tl_csv: str):

    ta_cols = ["Pic", "Class", "X", "Y", "Width", "Height"]
    ta_df = pd.DataFrame(columns=ta_cols)

    ta_dir = f"{data_dir}/train_annotations"
    ta_df = populate_df(ta_dir, ta_df, ta_cols)

    tl_df = pd.read_csv(tl_csv)

    print(f"Training Annotations Dataframe:\n{ta_df}")
    print(f"\nTraining Labels dataframe\n{tl_df}")


if __name__ == "__main__":
    dir = "data"
    train_labels = "train_labels.csv"
    main(dir, train_labels)
