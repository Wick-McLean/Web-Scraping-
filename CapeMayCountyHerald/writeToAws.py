import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIAUMFOVDSBJHNWAFPQ'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    print (s3)
    response = s3.list_objects_v2(Bucket='nymag-scrape-articles-from-python')
    print(response)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


# uploaded = upload_to_aws('C:\\Users\\Wick\\.PyCharmCE2019.3\\config\\scratches\\scratch_2.py', 'nymag-scrape-articles-from-python', 'tester')