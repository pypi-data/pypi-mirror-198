# Stackd IAC

IAC organizer

## Usage

### initializing project

~~~
$ stackd init
~~~

Add --help for usage message. Initalizes new project in current directory. Clones core specifications,
terraform provider versions, setups vault. 



#### AWS S3 + KMS storage -- uses your own resources

- S3 buckets for terraform states and vault data files
- AWS KMS encryption key for vault unsealing and S3 server-side encryption

also, stackd can create this objects automatically, when initial credentials are provided

## Building infrastructure code

~~~
$ stackd build -c all
~~~

Builds IAC specifications for all configured clusters