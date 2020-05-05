gunicorn --bind 127.0.0.1:5000 wsgi:app & APP_PID=$!
sleep 5
pytest test.py
echo $APP_PID
kill -TERM $APP_PID
