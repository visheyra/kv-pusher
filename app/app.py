#!/usr/bin/env python3

from argparse import ArgumentParser
from adapters import Adapters


def parse_args():
    parser = ArgumentParser(description='interract with different K/Vs')
    parser.add_argument('--verbose', '-v', action='store_true', help='verbosity switch', default=False)
    parser.add_argument('--endpoint', '-e', type=str, help='endpoint of the kv', required=True)
    parser.add_argument('--port', '-p', type=str, help='port to reach the kv', required=True)
    parser.add_argument('--store', '-s', type=str, help='type of store to use', choices=Adapters.keys(), required=True)
    parser.add_argument('--command', '-c', type=str, choices=['read', 'write', 'delete'], help='action to perform', required=True)
    parser.add_argument('--key', '-k', type=str, help='key to use', required=True)
    parser.add_argument('--value', '-i', type=str, default='', help='value to write, perfix the value with @ will open a file with value name and push its content as value')
    return parser.parse_args()


def extract_value(value):
    if value.startswith('@'):
        with open(value[1:], 'rb') as fl:
            return fl.read()
    return value


def main():
    p = parse_args()
    adapter = Adapters[p.store]
    try:
        adapter.configure(p.endpoint, p.port)
        val = adapter.do(p.command, p.key, extract_value(p.value), p.verbose)
    except RuntimeError as e:
        print('Runtime error occured: {}'.format(e))
    except Exception as e:
        print('Error occured: {}'.format(e))
    else:
        if p.verbose:
            print('[{}]: succeeds'.format(p.key))
        if p.command == 'read':
            print(val)


if __name__ == '__main__':
    main()
