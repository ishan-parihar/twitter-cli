# twitter-cli

[![CI](https://github.com/ishan-parihar/twitter-cli/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ishan-parihar/twitter-cli/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/twitter-cli.svg)](https://pypi.org/project/twitter-cli/)
[![Python](https://img.shields.io/badge/python-%3E%3D3.10-blue.svg)](https://pypi.org/project/twitter-cli/)

A terminal-first CLI for Twitter/X: read timelines, bookmarks, and user profiles without API keys. Now with **OAuth support**, **DM management**, and **media status tracking**.



### Features

**Read:**
- Timeline: fetch `for-you` and `following` feeds
- Bookmarks: list saved tweets from your account (including **bookmark folders**)
- Search: find tweets by keyword with Top/Latest/Photos/Videos tabs
- Tweet detail: view a tweet and its replies; use `show <N>` to open tweet #N from the last list output
- Article: fetch a Twitter Article and export it as Markdown
- List timeline: fetch tweets from a Twitter List
- User lookup: fetch user profile, tweets, likes, followers, and following
- **Notifications**: fetch notifications with type filtering (mentions, likes, retweets, follows, quotes)
- **Communities**: fetch tweets from Communities, join/leave Communities
- **Polls**: create and vote on polls
- **Lists**: full CRUD for Twitter Lists (create, update, delete, members, subscriptions)
- `--full-text`: disable tweet text truncation in rich table output
- Structured output: export any data as YAML or JSON for scripting and AI agent integration
- Optional scoring filter: rank tweets by engagement weights
- Structured output contract: [SCHEMA.md](./SCHEMA.md)

> **AI Agent Tip:** Prefer `--yaml` for structured output unless a strict JSON parser is required. Non-TTY stdout defaults to YAML automatically. Use `--max` to limit results.

**Write:**
- Post: create new tweets and replies, with optional image/video attachments (up to 4 images, 1 video)
- Quote: quote-tweet with optional images
- Delete: remove your own tweets
- Like / Unlike: manage tweet likes
- Retweet / Unretweet: manage retweets
- Bookmark: bookmark/unbookmark (`favorite/unfavorite` kept as compatibility aliases)
- Follow / Unfollow: manage follows
- **Block / Unblock**: block and unblock users
- **Mute / Unmute**: mute and unmute users
- **DM**: create conversations, send messages, list conversations/messages, mark read, typing indicator, rotate encryption keys
- **Polls**: create polls (2-4 options, 5 min–7 days), vote on polls
- **Lists**: create/update/delete lists, add/remove members, list members, list subscriptions
- **Communities**: join/leave communities, fetch community tweets
- Write commands also support explicit `--json` / `--yaml` output now

**Auth & Anti-Detection:**
- Cookie auth: use browser cookies or environment variables
- **OAuth 1.0a / OAuth 2.0 PKCE / App-Only**: full OAuth flows for user-context and app-only access
- Full cookie forwarding: extracts ALL browser cookies for richer browser context
- TLS fingerprint impersonation: `curl_cffi` with dynamic Chrome version matching
- `x-client-transaction-id` header generation
- Request timing jitter to avoid pattern detection
- Write operation delays (1.5–4s random) to mitigate rate limits
- Proxy support via `TWITTER_PROXY` environment variable

**Media & Utilities:**
- **Media status**: check upload processing status for images/videos
- **Auth management**: check status, clear cookies, login via OAuth flows
- **Structured errors**: consistent error codes (`not_authenticated`, `not_found`, `invalid_input`, `rate_limited`, `api_error`)

### Installation

```bash
# Recommended: uv tool (fast, isolated)
uv tool install twitter-cli

# Alternative: pipx
pipx install twitter-cli
```

Upgrade to the latest version:

```bash
uv tool upgrade twitter-cli
# Or: pipx upgrade twitter-cli
```

> **Tip:** Upgrade regularly to avoid unexpected errors from outdated API handling.

Install from source:

```bash
git clone git@github.com:ishan-parihar/twitter-cli.git
cd twitter-cli
uv sync
```

### Quick Start

```bash
# Fetch home timeline (For You)
twitter feed

# Fetch Following timeline
twitter feed -t following

# Enable ranking filter explicitly
twitter feed --filter
```

### Usage

```bash
# Feed
twitter feed --max 50
twitter feed --cursor "<next-cursor-from-previous-response>"
twitter feed --full-text
twitter feed --output tweets.json
twitter feed --input tweets.json
twitter feed --json                    # Structured stdout for scripts/agents

# Bookmarks
twitter bookmarks
twitter bookmarks --full-text
twitter bookmarks --max 30 --yaml

# Search
twitter search "Claude Code"
twitter search "AI agent" -t Latest --max 50
twitter search "AI agent" --full-text
twitter search "机器学习" --yaml
twitter search "python" --from elonmusk --lang en --since 2026-01-01
twitter search --from bbc --exclude retweets --has links
twitter search "topic" -o results.json         # Save to file
twitter search "trending" --filter              # Apply ranking filter

# Tweet detail (view tweet + replies)
twitter tweet 1234567890
twitter tweet 1234567890 --full-text
twitter tweet https://x.com/user/status/1234567890

# Open tweet by index from last list output
twitter show 2                         # Open tweet #2 from last feed/search
twitter show 2 --full-text             # Full text in reply table
twitter show 2 --json                  # Structured output

# Twitter Article
twitter article 1234567890
twitter article https://x.com/user/article/1234567890 --json
twitter article 1234567890 --markdown
twitter article 1234567890 --output article.md

# List timeline
twitter list 1539453138322673664
twitter list 1539453138322673664 --cursor "<next-cursor-from-previous-response>"
twitter list 1539453138322673664 --full-text

# User
twitter user elonmusk
twitter user-posts elonmusk --max 20
twitter user-posts elonmusk --full-text
twitter user-posts elonmusk -o tweets.json
twitter likes elonmusk --max 30          # ⚠️ own likes only (private since Jun 2024)
twitter likes elonmusk --full-text
twitter likes elonmusk -o likes.json
twitter followers elonmusk --max 50
twitter following elonmusk --max 50

# Write operations
twitter post "Hello from twitter-cli!"
twitter post "Hello!" --image photo.jpg            # Post with image
twitter post "Gallery" -i a.png -i b.jpg -i c.webp  # Up to 4 images
twitter post "reply text" --reply-to 1234567890
twitter reply 1234567890 "Nice!" -i screenshot.png  # Reply with image
twitter quote 1234567890 "Look" -i chart.png        # Quote with image
twitter post "Hello from twitter-cli!" --json
twitter delete 1234567890
twitter like 1234567890
twitter like 1234567890 --yaml
twitter unlike 1234567890
twitter retweet 1234567890
twitter unretweet 1234567890
twitter bookmark 1234567890
twitter unbookmark 1234567890
twitter follow elonmusk --json
```

### OAuth Authentication

```bash
# OAuth 2.0 PKCE (recommended for user context)
twitter auth login --oauth2

# OAuth 1.0a (legacy)
twitter auth login --oauth1

# App-Only (read-only public data)
twitter auth login --app-only

# Check auth status
twitter auth status

# Refresh OAuth2 token
twitter auth refresh <refresh_token>

# Clear stored environment cookies
twitter auth clear
```

### Media & DM Management

```bash
# Check media upload status
twitter media status <media_id>

# DM conversation management
twitter dm mark-read <conversation_id>
twitter dm typing <conversation_id>
twitter dm rotate-keys <conversation_id>
```

### Authentication

twitter-cli uses this auth priority:

1. **Environment variables**: `TWITTER_AUTH_TOKEN` + `TWITTER_CT0`
2. **Browser cookies** (recommended): auto-extract from Arc/Chrome/Edge/Firefox/Brave

Browser extraction is recommended — it forwards ALL Twitter cookies (not just `auth_token` + `ct0`) and aligns request headers with your local runtime, which is closer to normal browser traffic than minimal cookie auth.

**Chrome multi-profile**: All Chrome profiles are scanned automatically. To specify a profile:

```bash
TWITTER_CHROME_PROFILE="Profile 2" twitter feed
```

**Browser priority:** If you have multiple browsers, set `TWITTER_BROWSER` to try a specific browser first:

```bash
TWITTER_BROWSER=chrome twitter feed    # Supported: arc, chrome, edge, firefox, brave
```

After loading cookies, the CLI performs lightweight verification. Commands that require account access fail fast on clear auth errors (`401/403`).

### Proxy Support

Set `TWITTER_PROXY` to route all requests through a proxy:

```bash
# HTTP proxy
export TWITTER_PROXY=http://127.0.0.1:7890

# SOCKS5 proxy
export TWITTER_PROXY=socks5://127.0.0.1:1080
```

Using a proxy can help reduce IP-based rate limiting risks.

### Configuration

Create `config.yaml` in your working directory:

```yaml
fetch:
  count: 50

filter:
  mode: "topN"          # "topN" | "score" | "all"
  topN: 20
  minScore: 50
  lang: []
  excludeRetweets: false
  weights:
    likes: 1.0
    retweets: 3.0
    replies: 2.0
    bookmarks: 5.0
    views_log: 0.5

rateLimit:
  requestDelay: 2.5     # base delay between requests (randomized ×0.7–1.5)
  maxRetries: 3          # retry count on rate limit (429)
  retryBaseDelay: 5.0    # base delay for exponential backoff
  maxCount: 200          # hard cap on fetched items
```

Fetch behavior:

- `fetch.count` is the default item count for read commands when `--max` is omitted
- Rich table output truncates long tweet text by default; use `--full-text` to show full body text in list views

Filter behavior:

- Default behavior: no ranking filter unless `--filter` is passed
- With `--filter`: tweets are scored/sorted using `config.filter`

Scoring formula:

```text
score = likes_w * likes
      + retweets_w * retweets
      + replies_w * replies
      + bookmarks_w * bookmarks
      + views_log_w * log10(max(views, 1))
```

Mode behavior:

- `mode: "topN"` keeps the highest `topN` tweets by score
- `mode: "score"` keeps tweets where `score >= minScore`
- `mode: "all"` returns all tweets after sorting by score

### Best Practices (Avoiding Bans)

- **Use a proxy** — set `TWITTER_PROXY` to avoid direct IP exposure
- **Keep request volumes low** — use `--max 20` instead of `--max 500`
- **Don't run too frequently** — each startup fetches x.com to initialize anti-detection headers
- **Use browser cookie extraction** — provides full cookie fingerprint
- **Avoid datacenter IPs** — residential proxies are much safer

### Output Modes

- Use the default rich table for interactive reading
- Use `--full-text` when reading long posts in terminal tables
- Use `--yaml` or `--json` for scripts and agent pipelines
- Use `-c` / `--compact` when token efficiency matters more than completeness

### Troubleshooting

- `No Twitter cookies found`
  - Ensure you are logged in to `x.com` in a supported browser (Arc/Chrome/Edge/Firefox/Brave).
  - Or set `TWITTER_AUTH_TOKEN` and `TWITTER_CT0` manually.
  - Run with `-v` to see browser extraction diagnostics.

- `Cookie expired or invalid (HTTP 401/403)`
  - Re-login to `x.com` and retry.

- `Unable to get key for cookie decryption` (macOS Keychain)
  - **SSH sessions**: Keychain is locked by default over SSH. Run:
    ```bash
    security unlock-keychain ~/Library/Keychains/login.keychain-db
    ```
  - **Local terminal**: Open **Keychain Access** → search for **"\<Browser\> Safe Storage"** → **Access Control** → add your Terminal app → **Save Changes**.
  - Or click **"Always Allow"** when the Keychain authorization popup appears.

- `Twitter API error 404`
  - This can happen when upstream GraphQL query IDs rotate.
  - Retry the command; the client attempts a live queryId fallback.

- `Invalid tweet JSON file`
  - Regenerate input using `twitter feed --json > tweets.json`.

- **Windows: no output captured by pipe/subprocess** (AI agent integration)
  - This is a **ConPTY** issue, not a twitter-cli bug. Windows Terminal's ConPTY pseudo-terminal can intercept pipe output from commands with network latency.
  - **Fix**: Use **Git Bash** as your terminal shell and set `"windowsEnableConpty": false` in your terminal settings.
  - If disabling ConPTY with PowerShell, emoji output may fail with `UnicodeEncodeError: 'gbk'`. Git Bash handles UTF-8 natively.
  - Standard `subprocess.run(capture_output=True)` and file redirection (`> file 2>&1`) work correctly regardless of ConPTY.



Structured error codes commonly include `not_authenticated`, `not_found`, `invalid_input`, `rate_limited`, and `api_error`.

### Development

```bash
# Install dev dependencies
uv sync --extra dev

# Lint + tests
uv run ruff check .
uv run pytest -q
```

Current CI validates the project on Python 3.8, 3.10, and 3.12.

### Project Structure

```text
twitter_cli/
├── __init__.py
├── cli.py
├── client.py
├── graphql.py       # GraphQL query IDs, URL building, JS bundle scanning
├── parser.py        # Tweet, User, Media parsing logic
├── auth.py
├── config.py
├── constants.py
├── exceptions.py
├── filter.py
├── formatter.py
├── output.py
├── serialization.py
└── models.py
```

### Use as AI Agent Skill

twitter-cli ships with a [`SKILL.md`](./SKILL.md) so AI agents can execute common X/Twitter workflows.

#### [Skills CLI](https://github.com/vercel-labs/skills) (Recommended)

```bash
npx skills add ishan-parihar/twitter-cli
```

| Flag | Description |
| --- | --- |
| `-g` | Install globally (user-level, shared across projects) |
| `-a claude-code` | Target a specific agent |
| `-y` | Non-interactive mode |

#### Manual Install

```bash
mkdir -p .agents/skills
git clone git@github.com:ishan-parihar/twitter-cli.git .agents/skills/twitter-cli
```

#### ~~OpenClaw / ClawHub~~ (Deprecated)

> ⚠️ ClawHub install method is deprecated and no longer supported. Use [Skills CLI](#skills-cli-recommended) or Manual Install above.

