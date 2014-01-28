$HADOOP_HOME/bin/hadoop dfs -ls output_dir
$HADOOP_HOME/bin/hadoop dfs -cat output_dir/part-* > \
  local_output

