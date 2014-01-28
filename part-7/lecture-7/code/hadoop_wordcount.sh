$HADOOP_HOME/bin/hadoop jar \
  $HADOOP_HOME/hadoop-streaming.jar \
    -input input_dir \
    -output output_dir \
    -mapper python_mapper.py \
    -reducer /bin/cat # executable\
    -file python_mapper.py # make file available \
    -file auxiliary_data.txt
