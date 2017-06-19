#!venv/bin/python

from app import app

#app.run()
app.run(host='presensiuas.herokuapp.com', port=1337, workers=4)
