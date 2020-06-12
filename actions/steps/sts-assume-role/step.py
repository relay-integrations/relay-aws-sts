#!/usr/bin/env python
import boto3
from nebula_sdk import Interface, Dynamic as D


relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
)

sts = sess.client('sts')

try:
  roleARN = relay.get(D.roleARN)
  roleSessionName = relay.get(D.roleSessionName)
except:
  print('Requires both roleARN and roleSessionName to be defined. Exiting.')
  exit(1)

print('Creating credentials...\n')
response = sts.assume_role(
    RoleArn=roleARN,
    RoleSessionName=roleSessionName
)
temporaryAccessKeyId = response['Credentials']['AccessKeyId']
temporarySecretAccessKey = response['Credentials']['SecretAccessKey']
temporarySessionToken = response['Credentials']['SessionToken']

print('\nAdding temporary credentials to the outputs `accessKeyId`, `secretAccessKey`, and `sessionToken`')
relay.outputs.set('accessKeyId', temporaryAccessKeyId)
relay.outputs.set('secretAccessKey', temporarySecretAccessKey)
relay.outputs.set('sessionToken', temporarySessionToken)