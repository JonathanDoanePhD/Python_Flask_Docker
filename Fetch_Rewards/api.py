"""Flask demonstration of rectangle corner interpolation."""

import ast

import numpy as np
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


def Organize_Corners(in_corners):
    left = min(corner[0] for corner in in_corners)
    right = max(corner[0] for corner in in_corners)
    top = max(corner[1] for corner in in_corners)
    bottom = min(corner[1] for corner in in_corners)
    return [(left, top), (right, top), (left, bottom), (right, bottom)]


def Display(in_list):
    print("[")
    length_item = len(in_list[0])
    for item in in_list:
        print("[", end="")
        for subitem in item:
            print(
                "[",
                "{:.2f}".format(subitem[0]),
                ", ",
                "{:.2f}".format(subitem[1]),
                "]",
                sep="",
                end="",
            )
            if item.index(subitem) != length_item - 1:
                print(", ", end="")
        print("]")
    return print("]")


def Dimensions_and_Corners_to_Pixels(in_dimensions, in_corners):
    corners = Organize_Corners(in_corners)
    left = corners[0][0]
    right = corners[1][0]
    top = corners[0][1]
    bottom = corners[2][1]

    x_values = list(np.linspace(left, right, in_dimensions[1]))
    y_values = list(np.linspace(top, bottom, in_dimensions[0]))

    solution = []
    for index_y in range(len(y_values)):
        solution.append([])
        for x in x_values:
            solution[index_y].append([x, y_values[index_y]])
    return solution


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/join", methods=["GET", "POST"])
def my_form_post():
    in_dimensions = ast.literal_eval(request.form["text1"])
    in_corners = ast.literal_eval(request.form["text2"])
    solution = Dimensions_and_Corners_to_Pixels(in_dimensions, in_corners)

    result_rows = {"0": "[", "-1": "]"}
    for index in range(len(solution)):
        result_rows.update({str(index + 1): str(solution[index])})
    return jsonify(result=result_rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
