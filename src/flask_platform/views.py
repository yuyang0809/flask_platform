# -*- coding: utf-8 -*-

from flask_platform import app
from flask import render_template
from systeminfo import sysinfo



@app.route('/')
def index():
	returnDict = {}
	returnDict['user'] = sysinfo.get_platform_info()
	returnDict['title'] = 'Home'
	return render_template("index.html", **returnDict)