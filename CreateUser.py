import boto3


def create_user(username):
    iam_createuser = boto3.client('iam')
    response = iam_createuser.create_user(UserName=username)
    print(response)


create_user('viva.admin3')