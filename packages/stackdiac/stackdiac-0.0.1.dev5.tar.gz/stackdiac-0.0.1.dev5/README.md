# Stackd IAC

IAC stack

## Usage

### initializing project

~~~
$ stackd init
~~~

Add --help for usage message. Initalizes new project in current directory. Clones core specifications,
terraform provider versions, setups vault. 

## Updating binaries and repos

~~~
$ stackd update
~~~

binaries and repos will be synced with stackd.yaml project file

## Building infrastructure code

~~~
$ stackd build
~~~

Builds IAC specifications for all configured clusters

## running terragrunt plan

~~~
$ stackd plan build/<cluster>/<stack>/<module>
~~~

