import numpy as np
import matplotlib.pyplot as plt
import urllib.parse
from io import BytesIO
import base64
from scipy.stats import norm
from flask import Flask, render_template, request
from predict_rank import predict_rank

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
  if  request.method == 'POST':
      kcet_marks = int(request.form["kcet_marks"])
      board_marks = int(request.form["board_marks"])
      predicted_rank = predict_rank(board_marks, kcet_marks)



  return render_template("result.html", predicted_rank=predicted_rank, kcet_marks=kcet_marks, board_marks=board_marks)


if __name__ == "__main__":
    app.run(debug=True)