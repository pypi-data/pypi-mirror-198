import re
import sys
from pathlib import PurePosixPath

import configargparse
import hvac
from hvac.exceptions import InvalidPath


def parse_args():
    parser = configargparse.ArgumentParser(
        add_env_var_help=True,
        auto_env_var_prefix='VAULT_',
    )
    parser.add_argument('--addr', help='Vault address', required=True)
    parser.add_argument('--token', help='Vault token', required=True)
    parser.add_argument('--namespace', help='Vault namespace', default=None)
    parser.add_argument('--pattern', help='Pattern to search for', default=r'''vault:([^\s'"]+)''')
    parser.add_argument('--prefix', help='Common vault key prefix', default='')
    parser.add_argument('files', help='Files to decrypt or \'-\' to read from stdin', nargs='+')

    return parser.parse_args()


def main():
    args = parse_args()

    client = hvac.Client(url=args.addr, token=args.token, namespace=args.namespace)

    for file_name in args.files:
        if file_name != '-':
            with open(file_name, 'r', encoding='utf8') as f_in:
                data = f_in.read()
        else:
            data = sys.stdin.read()

        for match in re.finditer(
            pattern=args.pattern,
            string=data,
        ):
            substr = match.group(0)
            path_group = match.group(1)
            if args.prefix and not path_group.startswith('/'):
                path_group = str(PurePosixPath('/') / args.prefix / path_group)

            _, mount_point, path_segment = path_group.split('/', maxsplit=2)

            if ':' in path_segment:
                path, key = path_segment.split(':')
            else:
                path, key = path_segment, 'value'

            full_path = f'{path}:{key}'

            try:
                value = client.secrets.kv.v2.read_secret_version(path=path, mount_point=mount_point)
            except InvalidPath:
                print(f'ERROR: Value for key "{full_path}" is not set', file=sys.stderr)
                sys.exit(1)

            value = value.get('data', {}).get('data', {}).get(key)
            if value is None:
                print(f'ERROR: Value for key "{full_path}" is not set', file=sys.stderr)
                sys.exit(1)

            data = data.replace(substr, value, 1)

            print(f'Replaced "{full_path}" value', file=sys.stderr)

        if file_name != '-':
            with open(file_name, 'w', encoding='utf8') as f_out:
                f_out.write(data)
        else:
            sys.stdout.write(data)


if __name__ == '__main__':
    sys.exit(main())
