#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "USAGE: bash $0 <path-to-train_annotations>"
    exit 1
fi

count=0
# Iterate over all files in the specified directory
for file in $1/*; do
    # Use awk to check for files without any line starting with 0
    awk '
    BEGIN { has_zero = 0 }
    $1 == 0 { has_zero = 1; exit }
    END { if (has_zero == 0) print FILENAME }
    ' "$file"
    if awk 'BEGIN { has_zero = 0 } $1 == 0 { has_zero = 1; exit } END { exit (has_zero == 0) }' "$file"; then
            count=$((count + 1))
    fi
done

echo "Number of Test images with no L0 annotations: $count"