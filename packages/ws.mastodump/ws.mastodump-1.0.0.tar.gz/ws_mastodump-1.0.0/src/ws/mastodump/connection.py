from mastodon import Mastodon
import os
import sys


# Adapted from <https://github.com/kensanata/mastodon-archive
#   /blob/main/mastodon_archive/core.py>
class Connection:

    configdir = os.path.expanduser('~/.config/mastodump/')

    def __init__(self, user, scopes=('read',), name='mastodump'):
        self.username, self.domain = user.split('@')
        self.url = 'https://' + self.domain
        self.name = name
        self.scopes = scopes
        if not os.path.exists(self.configdir):
            os.makedirs(self.configdir)
        configdir = self.configdir + self.domain
        self.client_secret = configdir + '.client.secret'
        self.user_secret = configdir + '.user.' + self.username + '.secret'

    def register(self):
        print('Registering app at %s' % self.domain)
        Mastodon.create_app(
            self.name,
            api_base_url=self.url,
            scopes=self.scopes,
            to_file=self.client_secret
        )

    def authorize(self):
        print('This app needs access to your Mastodon account.')
        mastodon = Mastodon(
            client_id=self.client_secret, api_base_url=self.url)
        url = mastodon.auth_request_url(
            client_id=self.client_secret, scopes=self.scopes)

        print('Visit the following URL and authorize the app:')
        print(url)
        print('Then paste the access token here:')
        token = sys.stdin.readline().rstrip()

        mastodon.log_in(
            code=token, to_file=self.user_secret, scopes=self.scopes)
        return mastodon

    def login(self):
        if not os.path.isfile(self.client_secret):
            self.register()
        if not os.path.isfile(self.user_secret):
            return self.authorize()

        return Mastodon(
            client_id=self.client_secret, access_token=self.user_secret,
            api_base_url=self.url)
