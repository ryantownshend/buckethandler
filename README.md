# buckethandler



	aws s3 ls | awk '{print $3}' | grep --color=never target > buckets.list

    while read -r line; do echo $line; python bucket_purge.py $line; done < buckets.list

