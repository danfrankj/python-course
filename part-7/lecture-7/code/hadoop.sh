$HADOOP_HOME/bin/hadoop jar \
  $HADOOP_HOME/hadoop-streaming.jar \
    -input input_dir \
    -output output_dir \
    -mapper mapper.py \
    -reducer reducer.py\
    -file mapper.py  \
    -file reducer.py
