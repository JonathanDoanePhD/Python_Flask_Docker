from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


# START(My solution)

import numpy as np

def Organize_Corners(in_corners):
    left   = min([l[0] for l in in_corners])
    right  = max([l[0] for l in in_corners])
    top    = max([l[1] for l in in_corners])
    bottom = min([l[1] for l in in_corners])
    return [(left, top), (right, top), (left, bottom), (right, bottom)]

def Display(in_list):
    print('[')
    length_item = len(in_list[0])
    for item in in_list:
        print('[', end='')
        for subitem in item:
            print('[', '{:.2f}'.format(subitem[0]), ', ', '{:.2f}'.format(subitem[1]), ']', sep='', end='')
            if item.index(subitem) != length_item - 1:
                print(', ', end='')
        print(']')
    return print(']')

def Dimensions_and_Corners_to_Pixels(in_dimensions, in_corners):
    corners = Organize_Corners(in_corners)
    left   = corners[0][0]
    right  = corners[1][0]
    top    = corners[0][1]
    bottom = corners[2][1]
    x_values = list(np.linspace(left, right, in_dimensions[1]))
    y_values = list(np.linspace(top, bottom, in_dimensions[0]))
    solution = []
    for index_y in range(len(y_values)):
        solution.append([])
        for x in x_values:
            solution[index_y].append([x,y_values[index_y]])
    return solution

import ast

# END(My solution)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    in_dimensions = ast.literal_eval(request.form['text1'])
    in_corners = ast.literal_eval(request.form['text2'])
    solution = Dimensions_and_Corners_to_Pixels(in_dimensions, in_corners)
    dict = {
        '0': '[',
	'-1': ']'
    }
    for i in range(len(solution)):
        dict.update({str(i+1): str(solution[i])})
    return jsonify(result=dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)