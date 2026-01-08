from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

FILE_NAME = "survey.csv"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form

        row = [
            data.get("name"),
            data.get("email"),
            data.get("contact"),
            data.get("area"),
            data.get("age"),
            data.get("occupation"),
            data.get("availability"),
            data.get("pricing"),
            data.get("delivery_interest"),
            data.get("extra_pay"),
            ",".join(data.getlist("medicine_type")),
            ",".join(data.getlist("family_history")),
            ",".join(data.getlist("features")),
            data.get("comments"),
            data.get("latitude"),
            data.get("longitude")
        ]

        file_exists = os.path.isfile(FILE_NAME)

        with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow([
                    "Name","Email","Contact","Area","Age","Occupation",
                    "Availability","Pricing","Delivery Interest","Extra Pay",
                    "Medicine Types","Family History","Features",
                    "Comments","Latitude","Longitude"
                ])
            writer.writerow(row)

        return "✅ Response submitted successfully!"

    return render_template("index.html")

if __name__ == "__main__":
    app.run()
