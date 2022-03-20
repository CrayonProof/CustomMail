import pandas as pd
import re

PH_DELIMETER = "=============================================="

#read template file
f = open("template.txt", "r")
template_text = f.read()

#get placeholders from template file
placeholders = re.findall("<(.*?)>", template_text)

#read data file
df = pd.read_csv("data.csv")

#replace every instance of a column header with it's corresponding data instance
for index, row in df.iterrows():
	col_index = 0;
	output_text = template_text
	for item in row:
		regex_string = "<" + df.columns[col_index] + ">"
		output_text = re.sub(regex_string, row[col_index], output_text)
		col_index = col_index + 1;
	print(PH_DELIMETER+ "\n" + output_text + "\n" + PH_DELIMETER + "\n")