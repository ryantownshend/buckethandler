import sys
import boto3
import click
import click_log
import logging
log = logging.getLogger()
click_log.basic_config(log)
log.level = logging.INFO

def purge(bucket_name):
	session = boto3.Session()
	s3 = session.resource(service_name='s3')
	try:
		bucket = s3.Bucket(bucket_name)
		bucket.object_versions.delete()
		bucket.delete()
	except Exception as e:
		log.critical(e)
		sys.exit(1)

@click.command()
@click_log.simple_verbosity_option(log)
@click.argument(
	'bucket',
	required=True,
)
def cli(bucket):
    log.debug('cli()')
    
    purge(bucket)

if __name__ == '__main__':
    cli()

