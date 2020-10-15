# aws-sts-step-assume-role

This [AWS STS](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) step container returns a set of temporary security credentials that you can use to access AWS resources that you might not normally have access to. These temporary credentials consist of an access key ID, a secret access key, and a security token. This step currently does not suport MFA. Default duration is 1 hour. 

For more information on requesting temporary security credentials, check out the 
documentation [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison).   

## Example Outputs
| Key | Value | 
|-----|-------|
| `connection.accessKeyID` | `AKIAIOSFODNN7EXAMPLE` |
| `connection.secretAccessKey` | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY` |
| `connection.sessionToken` | `AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQWLWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGdQrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz+scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==` |