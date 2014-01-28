$HADOOP_HOME/bin/hadoop dfs -copyFromLocal \
  course_description.txt input_dir
$HADOOP_HOME/bin/hadoop dfs -ls input_dir
