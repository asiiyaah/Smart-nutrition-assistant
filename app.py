from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/nutrition', methods=['POST'])
def nutrition():
    food = request.form.get("food")

    # Dummy data (temporary)
    result = {
        "calories": "420 kcal",
        "protein": "13 g",
        "category": "Moderate"
    }

    return render_template("index.html", nutrition_result=result)

@app.route('/meal', methods=['POST'])
def meal():
    ingredients = request.form.get("ingredients")

    # Dummy meal
    meal_result = "Egg Fried Rice - Easy & Protein Rich"

    return render_template("index.html", meal_result=meal_result)

if __name__ == "__main__":
    app.run(debug=True)
