'''
Game Name:- KBC 
Developer:- RISHABH KUMAR - Google CSE
Version:- 0.24.3
'''

from flask import Flask, render_template, request 
import json
import random
import os

app = Flask(__name__)

file_path = os.path.join(os.path.dirname(__file__), 'questions_and_answers.json')
with open(file_path, 'r') as f:
    data = json.load(f)

question_random_index = random.randint(0,len(data))

questions_answer_options = []
indexno = [question_random_index]
QMoney = [0]

@app.route('/')
def index():
    del QMoney[0:]
    for i in data:
        data1 = {
            "Question": f"{i['question']}",
            "Options": i['options'],
            "Answer": i['answer']
        }
        style = {
            "display": "none",
            "bgcolorA": "#000080",
            "bgcolorB": "#000080",
            "bgcolorC": "#000080",
            "bgcolorD": "#000080",
            "btnA": "enabled",
            "btnB": "enabled",
            "btnC": "enabled",
            "btnD": "enabled"
        }
        ReplayData = ""
        questions_answer_options.append(data1)
    return render_template('index.html', questions_answer_options=questions_answer_options, ReplayData=ReplayData, indexno=indexno[-1], style=style)

@app.route('/nxt', methods=['POST'])
def button_click():
    random_money = random.randint(1000,3000)
    index = indexno[-1]
    optionA = request.form.get('optionA')
    optionB = request.form.get('optionB')
    optionC = request.form.get('optionC')
    optionD = request.form.get('optionD')
    nextquestion = request.form.get('next-question')
    totalprizemoney = request.form.get('total-prize-money')
    
      # Initialize Replay variable
    
    if questions_answer_options[index]['Answer'] == optionA or \
        questions_answer_options[index]['Answer'] == optionB or \
        questions_answer_options[index]['Answer'] == optionC or \
        questions_answer_options[index]['Answer'] == optionD:
        if questions_answer_options[index]['Answer']=='A':
            style = {
                "display": "block",
                "bgcolorA": "rgb(0, 255, 0)",
                "bgcolorB": "#000080",
                "bgcolorC": "#000080",
                "bgcolorD": "#000080",
                "btnA": "disabled",
                "btnB": "disabled",
                "btnC": "disabled",
                "btnD": "disabled"
            }
        if questions_answer_options[index]['Answer']=='B':
            style = {
                "display": "block",
                "bgcolorA": "#000080",
                "bgcolorB": "rgb(0, 255, 0)",
                "bgcolorC": "#000080",
                "bgcolorD": "#000080",
                "btnA": "disabled",
                "btnB": "disabled",
                "btnC": "disabled",
                "btnD": "disabled"
            }
        if questions_answer_options[index]['Answer']=='C':
            style = {
                "display": "block",
                "bgcolorA": "#000080",
                "bgcolorB": "#000080",
                "bgcolorC": "rgb(0, 255, 0)",
                "bgcolorD": "#000080",
                "btnA": "disabled",
                "btnB": "disabled",
                "btnC": "disabled",
                "btnD": "disabled"
            }
        if questions_answer_options[index]['Answer']=='D':
            style = {
                "display": "block",
                "bgcolorA": "#000080",
                "bgcolorB": "#000080",
                "bgcolorC": "#000080",
                "bgcolorD": "rgb(0, 255, 0)",
                "btnA": "disabled",
                "btnB": "disabled",
                "btnC": "disabled",
                "btnD": "disabled"
            }
        QMoney.append(random_money)
        # QMoney += random_money
        ReplayData = f"Correct Answer! You have won Rs - ₹ {QMoney[-1]}."
        # indexno.append(random.randint(0,len(data)))

    elif nextquestion == "next-question":
        style = {
            "display": "none",
            "bgcolorA": "#000080",
            "bgcolorB": "#000080",
            "bgcolorC": "#000080",
            "bgcolorD": "#000080",
        }
        ReplayData = ""
        indexno.append(random.randint(0,len(data)))
    
    elif totalprizemoney == 'total-prize-money':
        ReplayData = f"You Have Won Total Rs - ₹ {sum(QMoney)}."
        style = {
            "display": "block",
            # "btnA": "disabled",
            # "btnB": "disabled",
            # "btnC": "disabled",
            # "btnD": "disabled"
        }
        indexno.append(random.randint(0,len(data)))

    elif questions_answer_options[index]['Answer'] != optionA or \
        questions_answer_options[index]['Answer'] != optionB or \
        questions_answer_options[index]['Answer'] != optionC or \
        questions_answer_options[index]['Answer'] != optionD:
        if optionA=='A':
            user_option = 'A'
        if optionB=='B':
            user_option = 'B'
        if optionC=='C':
            user_option = 'C'
        if optionD=='D':
            user_option = 'D'
        style = {
            "display": "block",
            f"bgcolor{questions_answer_options[index]['Answer']}":"rgb(0, 255, 0)",
            f"bgcolor{user_option}":"rgb(255, 0, 0)",
            "btnA": "disabled",
            "btnB": "disabled",
            "btnC": "disabled",
            "btnD": "disabled"
        }
        try:

            ReplayData = f"Wrong Answer! You Loss Rs - ₹ {QMoney[-1]}. Correct Answer Is {questions_answer_options[index]['Answer']}. {questions_answer_options[index]['Options'][questions_answer_options[index]['Answer']]}"
        except:
            ReplayData = f"Wrong Answer! You Loss Rs - ₹ 0. Correct Answer Is {questions_answer_options[index]['Answer']}. {questions_answer_options[index]['Options'][questions_answer_options[index]['Answer']]}"

        try:
            del QMoney[-1]
        except:
            pass
        # indexno.append(random.randint(0,len(data)))
    # else:
    #     style = "none"
    #     indexno.append(indexno[-1] + 1)
    #     print("Next Questions!")
    return render_template('index.html', questions_answer_options=questions_answer_options, ReplayData=ReplayData, indexno=indexno[-1],style=style)

if __name__ == '__main__':
    app.run(debug=True)
