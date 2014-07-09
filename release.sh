awk -F"\t" '{print $1"\t"$6}' data/*/*.output > release
