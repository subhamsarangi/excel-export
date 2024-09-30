from flask import Flask, send_file, render_template, make_response, url_for, jsonify
import pandas as pd
import os
from io import BytesIO

app = Flask(__name__)

# Create an output directory if it doesn't exist
EXCEL_FOLDER = "output"
os.makedirs(EXCEL_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download_blob")
def download_blob():
    data = pd.read_csv("data.csv", sep=",")
    df = pd.DataFrame(data)
    print(df.head())
    if df.empty:
        return "No data to write", 400
    df["Created"] = pd.to_datetime(df["Created"], errors="coerce").dt.tz_localize(None)
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Master")

    output.seek(0)
    return send_file(
        output,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="Report1.xlsx",
    )


@app.route("/download_file")
def download_file():
    data = pd.read_csv("data.csv", sep=",")
    df = pd.DataFrame(data)
    if df.empty:
        return "No data to write", 400

    df["Created"] = pd.to_datetime(df["Created"], errors="coerce").dt.tz_localize(None)
    current_dir = os.getcwd()
    uploads_folder = os.path.join(current_dir, EXCEL_FOLDER)

    file_name = "Report2.xlsx"
    file_path = os.path.join(uploads_folder, file_name)
    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="PO Master")

    # Generate download URL
    download_url = url_for("send_file_route", filename=file_name, _external=True)
    return jsonify(
        {"message": "File generated successfully.", "download_url": download_url}
    )


@app.route("/file/<filename>")
def send_file_route(filename):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, EXCEL_FOLDER, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"error": "File not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
