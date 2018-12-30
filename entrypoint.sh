#!/bin/sh

case "$1" in
'api')
    gunicorn -w 4 service:app -b 0.0.0.0:8000
    ;;
'worker')
    rq worker scrapping-tasks -u $TASKS_REDIS_URI
    ;;
*)
    echo "use api or worker command"
    ;;
esac