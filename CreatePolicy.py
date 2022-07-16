import boto3
import json


def create_policy_deny():

    iam = boto3.client('iam')

    policy_document = {
        "Version": "2012-10-17",
        "Statement":
            {
                "Effect": "Deny",
                "Action": "*",
                "Resource": "*"
            }
                    }

    response = iam.create_policy(
        PolicyName='pythonPolicy',
        PolicyDocument=json.dumps(policy_document)
    )

    print(response)


print("creating the policy")
create_policy_deny()
print("policy has been created")
