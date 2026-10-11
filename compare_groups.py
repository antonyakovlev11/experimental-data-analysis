"""Descriptive calculations from report means and SD; no raw observations."""
import csv
from pathlib import Path
rows = list(csv.DictReader((Path(__file__).parent / 'bio-summary.csv').open(encoding='utf-8')))
control = rows[0]
for row in rows:
    area = float(row['leaf_area_mean_mm2'])
    height = float(row['height_mean_mm'])
    change = 100 * (area / float(control['leaf_area_mean_mm2']) - 1)
    cv_area = 100 * float(row['leaf_area_sd_mm2']) / area
    cv_height = 100 * float(row['height_sd_mm']) / height
    print(f"{row['variant']}: leaf area change={change:.2f}%; CV area={cv_area:.2f}%; CV height={cv_height:.2f}%")
