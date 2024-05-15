#!/usr/bin/env python3
"""Task 0: Basic Flask App"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """Hello world route"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
