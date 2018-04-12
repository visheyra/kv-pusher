# kv-pusher

Simple python utility that allows you to easily write / read / delete data in different kv providers

## Support

* etcd v2
* redis

## How to use

The helper explains itself pretty well.

```
[visheyra@linuxbox]$ python app.py -h
usage: app.py [-h] [--verbose] --endpoint ENDPOINT --port PORT --store
              {etcdv2,redis} --command {read,write,delete} --key KEY
              [--value VALUE]

interract with different K/Vs

optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v         verbosity switch
  --endpoint ENDPOINT, -e ENDPOINT
                        endpoint of the kv
  --port PORT, -p PORT  port to reach the kv
  --store {etcdv2,redis}, -s {etcdv2,redis}
                        type of store to use
  --command {read,write,delete}, -c {read,write,delete}
                        action to perform
  --key KEY, -k KEY     key to use
  --value VALUE, -i VALUE
                        value to store / update, perfix the value with @ will
                        open a file with value name and push its content as
                        value
```

## Features

* Put an `@` in front of the value will make the value be extracted from a file with the same name

## Roadmap

* [ ] pretty json output
* [x] redis server support
* [ ] redis cluster support
* [ ] redis sentinel cluster support
* [x] etcd v2 support
* [ ] etcd v3 support
* [ ] consul
* [ ] support batch mode
