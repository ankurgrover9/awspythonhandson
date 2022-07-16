import json

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

z = '{
  "ResponseMetadata": {
    "RequestId": "876b156a-1e83-4f18-9ae5-6539788d9939",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "876b156a-1e83-4f18-9ae5-6539788d9939",
      "content-type": "text/xml",
      "content-length": "200",
      "date": "Fri, 15 Jul 2022 11:59:35 GMT"
    },
    "RetryAttempts": 0
  }
}'

k = json.loads(z)

print(y["age"])
print(k["ResponseMetadata"]["HTTPStatusCode"])