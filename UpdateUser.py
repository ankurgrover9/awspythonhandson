import boto3
import json


def updateUser(olduser, newuser):
    updateIAM = boto3.client('iam')

    response = updateIAM.update_user(UserName=olduser, NewUserName=newuser)
    print(response)
    json_string = json.dumps(response, indent=2)
    # y = json.loads(json_string)
    print(json_string)
    str1 = json_string.strip()
    print(str1)
    #print(json_string["ResponseMetadata"]["HTTPStatusCode"])

updateUser('viva.demoupdate.user', 'viva.admin3')

# updateUser('viva.admin3', 'viva.demoupdate.user')
