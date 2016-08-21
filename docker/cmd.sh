#!/bin/bash

#configuration to install dependences and other software


# exec all to app

set -e  # configura como parametro -e en docker es -environment
if [ "$ENV"= 'DEV' ]; then
  echo $ENV
  echo "Running Development Server"
  exec uwsgi --http 0.0.0.0:8000 --wsgi-file wsgi.py \
  --callable application --stats 0.0.0.0:8001
else
  echo "Running Production Server"
  exec python run.py
fi
