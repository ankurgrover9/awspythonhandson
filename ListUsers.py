import boto3


def list_users():
    iam = boto3.client("iam")
    response = iam.list_users()
    #for response in paginator.paginate():
    print(response)

    for user in response['Users']:
        print('UserName: {}'.format(user['UserName']))
        #    print(f"Username: {user['UserName']}, Arn: {user['Arn']}")


def list_bbuckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    print(response)
    for bucket in response['Buckets']:
        print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))


list_users()
#list_bbuckets()
