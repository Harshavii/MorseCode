from flask import render_template, Flask, request
from flask_bootstrap import Bootstrap

import pandas
import csv

app = Flask(__name__)
Bootstrap(app)

@app.route("/",methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        text_input = request.form.get('textInput', '')
        output = convert(text_input)
    return render_template("index.html",output=output)


# is_active = True
data = pandas.read_csv('morse.csv',sep=',',quoting=csv.QUOTE_NONE,encoding='utf-8',on_bad_lines='skip')

# {new_key:new_value for (index, row) in df.iterrows()}
new_dict = {row.character:row.value for (index,row) in data.iterrows()}
# print(new_dict)

# print("Hey there! Get any string(Alphabets & Numbers) converted to a morse code.")
# def ans():
#     while is_active:
#         inp = input("Enter a string: ").upper()
#         output = [new_dict[letter] for letter in inp]
#         print(f"MORSE CODE : {' '.join(output)}")
#
#         contd = input("Do you want to continue? Type yes or no: ").lower()
#         if contd == 'yes':
#             is_active = True
#         else:
#             is_active = False
#         return output

def convert(input_text):
    data = pandas.read_csv('morse.csv', sep=',', quoting=csv.QUOTE_NONE, encoding='utf-8', on_bad_lines='skip')
    new_dict = {row.character: row.value for (index, row) in data.iterrows()}
    inp = input_text.upper()
    output = [new_dict[letter] for letter in inp]

    return ' '.join(output)

app.run()
