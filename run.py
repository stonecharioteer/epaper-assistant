#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import logging
import argparse

from flask import Flask, render_template

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %I:%M:%S %p")

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/home")
def serve_index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, 
            threaded=True,
            host="0.0.0.0", 
            port=8080)

