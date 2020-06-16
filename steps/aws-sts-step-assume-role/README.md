# aws-sts-step-assume-role

This [AWS STS](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) step container returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. This step currently does not suport MFA. Default duration is 1 hour. 

For more information on requesting temporary security credentials, check out the 
documentation [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison).   

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |
| `roleARN` || string | The Amazon Resource Name (ARN) of the role to assume. | None | True | 
| `roleSessionName` || string | User-provided identifier for the session | None | True | 

## Outputs

| Name | Child Output | Data type | Description | 
|------|--------------|-----------|-------------|
| `connection` || map | Relay connection for AWS that can be used in subsequent steps | 
|| `accessKeyID` | string | The access key ID that identifies the temporary security credentials. |
|| `secretAccessKey` | string | The secret access key that can be used to sign requests. |
|| `sessionToken` | string | The token that users must pass to the service API to use the temporary credentials. |


## Example

```yaml
steps:
# ...
- name: assume-role
  image: relaysh/aws-sts-step-assume-role
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account }
      region: us-west-2
    roleARN: arn:aws:iam::123456789012:role/demo
    roleSessionName: my-session
```

## Example Outputs
| Key | Value | 
|-----|-------|
| `connection.accessKeyID` | `AKIAIOSFODNN7EXAMPLE` |
| `connection.secretAccessKey` | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY` |
| `connection.sessionToken` | `AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQWLWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGdQrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz+scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==` |