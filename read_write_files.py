import json
import csv
from fpdf import FPDF
from docx import Document
import pandas as pd

# === 1. TXT FILE ===
txt_path = "sample.txt"
with open(txt_path, "w") as f:
    f.write("Hello from TXT file!\nThis is line 2.")

with open(txt_path, "r") as f:
    print("TXT CONTENT:\n", f.read())


# === 2. MD FILE ===
md_path = "sample.md"
with open(md_path, "w") as f:
    f.write("# Hello from Markdown\n\nThis is a **bold** line.")

with open(md_path, "r") as f:
    print("\nMD CONTENT:\n", f.read())


# === 3. JSON FILE ===
json_path = "sample.json"
data = {"name": "Alice", "age": 30, "skills": ["Python", "FastAPI"]}
with open(json_path, "w") as f:
    json.dump(data, f, indent=4)

with open(json_path, "r") as f:
    print("\nJSON CONTENT:\n", json.load(f))


# === 4. CSV FILE ===
csv_path = "sample.csv"
csv_data = [
    ["name", "age", "city"],
    ["Bob", 25, "Paris"],
    ["Eva", 28, "Berlin"]
]
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(csv_data)

with open(csv_path, "r") as f:
    print("\nCSV CONTENT:")
    print(f.read())
