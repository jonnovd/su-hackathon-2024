import pandas as pd

# Assuming df is your DataFrame
df = pd.read_csv("df_area_all_data_mm_non0.csv")

# Step 1: Create bins for 'Bags used'
bins = [0, 0.35, 0.6, 0.8, 1.1, 1.35, 1.6, 1.8, 2.1, 2.35, 2.6, 2.8, 3.1]
labels = ['0-0.35', '0.35-0.6', '0.6-0.8', '0.8-1.1', '1.1-1.35', '1.35-1.6', '1.6-1.8', '1.8-2.1', '2.1-2.35', '2.35-2.6', '2.6-2.8', '2.8-3.1']
df['Bags_bin'] = pd.cut(df['Bags used'], bins=bins, labels=labels, include_lowest=True)

# Step 2: Calculate IQR and identify outliers
def calculate_iqr_and_remove_outliers(group):
    Q1 = group['pothole_area'].quantile(0.25)
    Q3 = group['pothole_area'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Filtering out the outliers
    return group[(group['pothole_area'] >= lower_bound) & (group['pothole_area'] <= upper_bound)]

# Apply the function to each group
df_filtered = df.groupby('Bags_bin').apply(calculate_iqr_and_remove_outliers).reset_index(drop=True)

# Step 3: Remove entries where 'Bags used' > 3.1
df_filtered = df_filtered[df_filtered['Bags used'] <= 3]
df_filtered.drop(['Bags_bin'], axis=1, inplace=True)

# If you want to save the result to a CSV file
df_filtered.to_csv('filtered_potholes_mm.csv', index=False)

print(df)

# Display the filtered DataFrame
print(df_filtered)