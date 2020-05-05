gunicorn --bind 127.0.0.1:5000 wsgi:app & APP_PID=$!
sleep 15
echo start client
pytest
sleep 5
echo $APP_PID
kill -TERM $APP_PID
exit 0
