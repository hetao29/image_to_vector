PY_PID=`ps -ef | grep image_to_vector | grep py | awk '{print $2}'`
if [ ! $PY_PID ];
then
        echo 'no runing'
        python3 image_to_vector.py >>/dev/null 2>&1 &
else
        echo 'is runing'
fi
