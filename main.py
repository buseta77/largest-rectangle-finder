from flask import Flask, render_template, request
import json
import os
import psycopg2
from calculations import get_largest_chosen, get_largest_rectangle, get_random_array


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        heights = get_random_array()
        
        return render_template("rectangles_raw.html", heights=heights)
    
    elif request.method == 'POST':
        heights = request.form.get("heights")
        guessed = request.form.get("guessed")
        heights = json.loads(heights)
        rectangle_data = get_largest_rectangle(heights)
        
        con = psycopg2.connect(
            database = os.environ.get("DB_NAME"),
            user = os.environ.get("DB_USER"),
            password = os.environ.get("DB_PASSWORD"),
            host = os.environ.get("DB_HOST")
        ) 
        cur = con.cursor()
        cur.execute(f"INSERT into LargestRectangle (area) values ({rectangle_data[0]})")  
        con.commit()
        cur.execute(f"SELECT area FROM LargestRectangle")
        areas_raw = cur.fetchall()
        con.close()
        
        areas = []
        for area in areas_raw:
            areas.append(area[0])
        max_area, avg_area = max(areas), round((sum(areas) / len(areas)), 1)
        
        correct = False
        if guessed:
            guess = json.loads(guessed)
            if rectangle_data == guess:
                correct = True

        return render_template("rectangles.html", heights=heights, data=rectangle_data, home=True, max_area=max_area, avg_area=avg_area, guessed=guessed, correct=correct)

@app.route("/guess", methods=['POST'])
def guess():
    if request.method == 'POST':
        rowIndex = int(request.form.get('rowIndex'))
        columnIndex = int(request.form.get('columnIndex'))
        values = json.loads(request.form.get('heights'))
        rectangle_data = get_largest_chosen(values, rowIndex, columnIndex)
        return render_template("rectangles_guess.html", heights=values, data=rectangle_data, home=False)


if __name__ == '__main__':
    app.run(debug=True)
