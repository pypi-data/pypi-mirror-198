# mastodump

Incremental export of mastodon posts and boosts to plain text,
meant for a periodic backup workflow.

## Usage

```
pip install ws.mastodump
mastodump --user yourname@example.com
```

This will output all posts of the given user since the last time it was called.
(It stores the most recent post ID in `~/.config/mastodump/last-seen` and starts the query from there.)

## Example output

```
https://sueden.social/@wosc/109451158283053826 [2022-12-03 18:28:56.888000+00:00] <p>My recommendation for an android mastodon client goes to: twidere. It&#39;s the only one I&#39;ve found that you can customize so it fits a *reasonable* amount of timeline text on the screen (show the message actions only after longpress, use a light and not-huge font).</p>
```
