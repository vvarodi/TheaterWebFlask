#!/bin/bash

# Linux
# . virtual/bin/activate
# export FLASK_APP=theater
# export FLASK_ENV=development
# flask run

# Windows
virtual\\Scripts\\activate
export FLASK_APP=theater
export FLASK_ENV=development
python -m flask run


# STOP
#netstat -ano | findstr :5000
#taskkill /PID here-pid-num /F
