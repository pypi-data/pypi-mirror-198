from .connection import Connection
from argparse import ArgumentParser
import os


def main():
    parser = ArgumentParser()
    parser.add_argument('--user', help='@username@domain')
    options = parser.parse_args()

    mastodon = Connection(options.user).login()
    OFFSET = Connection.configdir + 'last-seen'
    if os.path.exists(OFFSET):
        with open(OFFSET) as f:
            offset = int(f.read().strip())
    else:
        offset = None

    new_offset = None
    user = mastodon.me()
    for status in mastodon.account_statuses(user['id'], since_id=offset):
        if not new_offset:
            new_offset = status['id']

        if status['reblog']:
            status = status['reblog']

        print('{url} [{created_at}] {content}'.format(**status))

    if new_offset:
        with open(OFFSET, 'w') as f:
            f.write(str(new_offset))
