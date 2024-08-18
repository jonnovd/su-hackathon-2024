import pandas as pd
import numpy as np
import os


def get_image_df(img_dir: str) -> pd.DataFrame:
    img_df = pd.DataFrame(columns=["Pothole number"])
    img_df["Pothole number"] = img_df["Pothole number"].astype(int)

    for i, filename in enumerate(os.listdir(img_dir)):
        img_df.loc[i, "Pothole number"] = int(filename.split(".")[0][1:])

    return img_df


def get_annotations_df(annot_dir: str) -> pd.DataFrame:
    # df = pd.DataFrame(columns=['Pothole number', 'x_0', 'y_0', 'width_0', 'height_0', 'x_1', 'y_1', 'width_1', 'height_1', 'x_2', 'y_2', 'width_2', 'height_2'])
    df = pd.DataFrame(columns=["Pothole number", "Annotations"])
    df["Pothole number"] = df["Pothole number"].astype(int)
    df["Annotations"] = df["Annotations"].astype(str)

    for i, filename in enumerate(os.listdir(annot_dir)):
        df.loc[i, "Pothole number"] = int(filename.split(".")[0][1:])
        file_path = os.path.join(annot_dir, filename)
        with open(file_path, "r") as file:
            lines = file.readlines()
        if lines:
            df.loc[i, "Annotations"] = "".join(lines).strip()
        else:
            df.loc[i, "Annotations"] = "No annotations"

    return df


def toString(img_df, labels_df, img_label_df, annotations_df, img_annot_df, complete_data_df, labeled_df):

    n_imgs = len(img_df)
    n_labels = len(labels_df)
    n_annotations = len(annotations_df)
    n_complete_data = len(complete_data_df)
    n_useful_imgs = len(img_label_df[pd.notna(img_label_df["Bags used"])])

    print("ALL IMAGES")
    print(img_label_df)
    print("\nMATCHING IMAGES AND LABELS")
    print(img_label_df[pd.notna(img_label_df["Bags used"])])
    print("\nIMAGES WITH NO LABELS")
    print(img_label_df[pd.isna(img_label_df["Bags used"])])

    print("\nALL ANNOTATIONS")
    print(annotations_df)

    print("\nMATCHING IMAGES AND ANNOTATIONS")
    print(img_annot_df[pd.notna(img_annot_df["Annotations"])])
    print("\nIMAGES WITH NO ANNOTATIONS")
    print(img_annot_df[pd.isna(img_annot_df["Annotations"])])

    print("\nIMAGES WITH LABELS AND ANNOTATIONS")
    print(complete_data_df)
    print("\nIMAGES WITH LABELS AND NO ANNOTATIONS")
    print(labeled_df[pd.isna(labeled_df["Annotations"])])
    print("\nALL IMAGES WITH LABELS")
    print(labeled_df)

    print("\nCONCLUSION")
    print(f"Number of images: {n_imgs}")
    print(f"Number of labels: {n_labels}")
    print(f"Number of Annotations: {n_annotations}")
    print(f"Number of complete data points: {n_complete_data}")
    print(f"Number of images with labels: {n_useful_imgs}")

    # print("\nUSEFUL IMAGES POTHOLE NUMBERS")
    # print(sorted(labeled_df['Pothole number'].values))

    print("\nImage missed by Dylan's code in original data")
    print(labeled_df[labeled_df["Pothole number"] == 1032])

    # List of images from original data
    # dylan = [101, 102, 106, 107, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 132, 133, 134, 135, 136, 138, 139, 140, 141, 142, 145, 146, 147, 148, 149, 150, 404, 405, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 435, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 451, 452, 453, 454, 455, 456, 460, 461, 462, 463, 465, 466, 467, 468, 469, 471, 472, 474, 475, 476, 477, 478, 497, 498, 499, 500, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1041, 1042, 1043, 1047, 1048, 1049, 1051, 1052, 1054, 1055, 1056, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1087, 1088, 1089, 1090, 1091, 1092, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1133, 1135, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1147, 1148, 1149, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1176, 1177, 1178, 1179, 1180, 1182, 1183, 1184, 1185, 1186, 1187, 1189, 1190, 1192, 1193, 1194, 1195, 1196, 1197, 1199, 1200, 1201, 1202, 1203, 1204, 1207, 1208, 1210, 1212, 1213, 1214, 1216, 1217, 1218, 1219, 1221, 1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1238, 1240, 1242, 1243, 1245, 1246, 1247, 1248, 1251, 1253, 1254, 1256, 1257, 1258, 1259, 1260, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1271, 1272, 1274, 1275, 1276, 1277, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1291, 1292, 1293, 1294, 1295, 1297, 1298, 1299, 1302, 1303, 1304, 1305, 1306, 1308, 1309, 1310, 1312, 1313, 1314, 1315, 1316, 1318, 1320, 1321, 1323, 1324, 1325, 1326, 1328, 1331, 1332, 1333, 1334, 1335, 1336, 1337, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1349, 1350, 1352, 1354, 1355, 1356, 1357, 1358, 1406, 1407, 1408, 1410, 1412, 1413, 1414, 1416, 1417, 1418, 1420, 1424, 1425, 1427, 1428, 1429, 1431, 1433, 1439, 1440, 1442, 1443, 1445, 1449]
    # jonno = [101.0, 102.0, 106.0, 107.0, 109.0, 110.0, 111.0, 112.0, 113.0, 115.0, 116.0, 117.0, 118.0, 119.0, 120.0, 121.0, 122.0, 123.0, 124.0, 125.0, 126.0, 127.0, 128.0, 129.0, 132.0, 133.0, 134.0, 135.0, 136.0, 138.0, 139.0, 140.0, 141.0, 142.0, 145.0, 146.0, 147.0, 148.0, 149.0, 150.0, 404.0, 405.0, 407.0, 408.0, 409.0, 410.0, 411.0, 412.0, 413.0, 414.0, 415.0, 416.0, 417.0, 418.0, 419.0, 420.0, 421.0, 422.0, 423.0, 424.0, 425.0, 426.0, 427.0, 428.0, 429.0, 430.0, 431.0, 432.0, 433.0, 435.0, 437.0, 438.0, 439.0, 440.0, 441.0, 442.0, 443.0, 444.0, 445.0, 446.0, 447.0, 448.0, 449.0, 451.0, 452.0, 453.0, 454.0, 455.0, 456.0, 460.0, 461.0, 462.0, 463.0, 465.0, 466.0, 467.0, 468.0, 469.0, 471.0, 472.0, 474.0, 475.0, 476.0, 477.0, 478.0, 497.0, 498.0, 499.0, 500.0, 1032.0, 1033.0, 1034.0, 1035.0, 1036.0, 1037.0, 1038.0, 1039.0, 1041.0, 1042.0, 1043.0, 1047.0, 1048.0, 1049.0, 1051.0, 1052.0, 1054.0, 1055.0, 1056.0, 1058.0, 1059.0, 1060.0, 1061.0, 1062.0, 1063.0, 1064.0, 1065.0, 1069.0, 1070.0, 1071.0, 1072.0, 1073.0, 1074.0, 1075.0, 1076.0, 1077.0, 1078.0, 1079.0, 1080.0, 1081.0, 1082.0, 1083.0, 1084.0, 1087.0, 1088.0, 1089.0, 1090.0, 1091.0, 1092.0, 1095.0, 1096.0, 1097.0, 1098.0, 1099.0, 1100.0, 1101.0, 1102.0, 1103.0, 1104.0, 1105.0, 1106.0, 1107.0, 1108.0, 1109.0, 1110.0, 1111.0, 1112.0, 1113.0, 1114.0, 1116.0, 1117.0, 1118.0, 1119.0, 1120.0, 1121.0, 1122.0, 1123.0, 1125.0, 1126.0, 1127.0, 1128.0, 1129.0, 1130.0, 1131.0, 1133.0, 1135.0, 1137.0, 1138.0, 1139.0, 1140.0, 1141.0, 1142.0, 1143.0, 1144.0, 1147.0, 1148.0, 1149.0, 1153.0, 1154.0, 1155.0, 1156.0, 1157.0, 1158.0, 1159.0, 1160.0, 1164.0, 1165.0, 1166.0, 1167.0, 1168.0, 1169.0, 1170.0, 1171.0, 1172.0, 1173.0, 1174.0, 1176.0, 1177.0, 1178.0, 1179.0, 1180.0, 1182.0, 1183.0, 1184.0, 1185.0, 1186.0, 1187.0, 1188.0, 1189.0, 1190.0, 1192.0, 1193.0, 1194.0, 1195.0, 1196.0, 1197.0, 1199.0, 1200.0, 1201.0, 1202.0, 1203.0, 1204.0, 1207.0, 1208.0, 1210.0, 1212.0, 1213.0, 1214.0, 1216.0, 1217.0, 1218.0, 1219.0, 1221.0, 1224.0, 1225.0, 1226.0, 1227.0, 1228.0, 1229.0, 1230.0, 1231.0, 1232.0, 1233.0, 1234.0, 1235.0, 1236.0, 1238.0, 1239.0, 1240.0, 1242.0, 1243.0, 1245.0, 1246.0, 1247.0, 1248.0, 1251.0, 1253.0, 1254.0, 1256.0, 1257.0, 1258.0, 1259.0, 1260.0, 1263.0, 1264.0, 1265.0, 1266.0, 1267.0, 1268.0, 1269.0, 1271.0, 1272.0, 1274.0, 1275.0, 1276.0, 1277.0, 1281.0, 1282.0, 1283.0, 1284.0, 1285.0, 1286.0, 1287.0, 1288.0, 1291.0, 1292.0, 1293.0, 1294.0, 1295.0, 1297.0, 1298.0, 1299.0, 1302.0, 1303.0, 1304.0, 1305.0, 1306.0, 1308.0, 1309.0, 1310.0, 1312.0, 1313.0, 1314.0, 1315.0, 1316.0, 1318.0, 1320.0, 1321.0, 1323.0, 1324.0, 1325.0, 1326.0, 1328.0, 1331.0, 1332.0, 1333.0, 1334.0, 1335.0, 1336.0, 1337.0, 1341.0, 1342.0, 1343.0, 1344.0, 1345.0, 1346.0, 1347.0, 1349.0, 1350.0, 1352.0, 1354.0, 1355.0, 1356.0, 1357.0, 1358.0, 1406.0, 1407.0, 1408.0, 1410.0, 1412.0, 1413.0, 1414.0, 1416.0, 1417.0, 1418.0, 1420.0, 1424.0, 1425.0, 1427.0, 1428.0, 1429.0, 1431.0, 1433.0, 1439.0, 1440.0, 1442.0, 1443.0, 1445.0, 1449.0, 1450.0]

    # diff, diff2 = [], []
    # for i in range(len(jonno)):
    #     if jonno[i] not in dylan:
    #         diff.append(jonno[i])

    # for i in range(len(dylan)):
    #     if dylan[i] not in jonno:
    #         diff2.append(dylan[i])

    # print(diff)
    # print(diff2)
    # OUTPUT: [1032.0, 1188.0, 1239.0, 1450.0] in jonno but not in dylan. ALl of dylan in jonno


def main(img_dir: str, labels_csv: str, annot_dir: str):

    labels_df = pd.read_csv(labels_csv)
    labels_df["Pothole number"] = labels_df["Pothole number"].astype(int)
    img_df = get_image_df(img_dir)
    img_label_df = pd.merge(img_df, labels_df, on="Pothole number", how="left")

    annotations_df = get_annotations_df(annot_dir)
    img_annot_df = pd.merge(img_df, annotations_df, on="Pothole number", how="left")
    label_img_annot_df = pd.merge(img_label_df, annotations_df, on="Pothole number", how="left")

    labeled_df = label_img_annot_df[pd.notna(label_img_annot_df["Bags used"])]
    complete_data_df = labeled_df[pd.notna(labeled_df["Annotations"])]

    toString(img_df, labels_df, img_label_df, annotations_df, img_annot_df, complete_data_df, labeled_df)


if __name__ == "__main__":
    # img_dir = '../data/train_images'
    # labels = '../data/train_labels.csv'
    # annot_dir = '../data/train_annotations'

    img_dir = "../../Supplementary Data/potholes_images_jpegs2"
    labels = "../../Supplementary Data/train_labels_2.csv"
    annot_dir = "../../Supplementary Data/train_annotations_2"

    main(img_dir, labels, annot_dir)


# def process_files(directory: str):
#     result = []
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)

#         # Ensure we're working with files only
#         if os.path.isfile(file_path):
#             with open(file_path, 'r') as file:
#                 lines = file.readlines()
