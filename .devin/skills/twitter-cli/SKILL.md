name: Twitter/X CLI
description: Twitter/X automation with timeline reading, search, posting, and engagement features
triggers:
  - "twitter post"
  - "twitter search"
  - "twitter timeline"
  - "twitter automation"
  - "social media posting"
  - "content creation"
  - "x twitter"

## Overview
Twitter CLI provides comprehensive Twitter/X automation:
- Timeline reading (home, following, bookmarks)
- Search tweets and users
- Post tweets, replies, and quote tweets
- Engagement (like, retweet, bookmark, follow)
- User profiles and analytics
- Article and media support

## Quick Start
```bash
# Show home timeline
twitter feed

# Search tweets
twitter search "query"

# Post a tweet
twitter post "Hello world"

# Get user profile
twitter user elonmusk

# Get tweet details
twitter tweet 1234567890
```

## Commands

### Reading
- `twitter feed` - Home timeline (For You)
- `twitter feed -t following` - Following feed
- `twitter bookmarks` - Bookmarks
- `twitter search "query"` - Search tweets
- `twitter user <handle>` - User profile
- `twitter user-posts <handle>` - User tweets
- `twitter tweet <id>` - Tweet detail + replies
- `twitter list <id>` - List timeline

### Writing
- `twitter post "text"` - Post a tweet
- `twitter post "text" -i photo.jpg` - Post with image(s)
- `twitter reply <id> "text"` - Reply to a tweet
- `twitter quote <id> "text"` - Quote-tweet
- `twitter delete <id>` - Delete a tweet
- `twitter like/unlike <id>` - Like/unlike
- `twitter retweet/unretweet <id>` - Retweet/unretweet
- `twitter follow/unfollow <handle>` - Follow/unfollow

### Output Formats
- `--format toon` - TOON format (default, token-efficient)
- `--format json` - JSON format
- `--format yaml` - YAML format
- `--format table` - Rich table format
- `--fields id,author,text` - Custom field selection
- `--full-text` - Show full tweet text (no truncation)

## Session Integration
Twitter CLI supports ObscuraCookieManager for browser cookie extraction:
```bash
# Automatic cookie extraction from browser
twitter feed
```

The CLI will automatically extract cookies from your browser when needed.

## Filtering
Enable score-based filtering:
```bash
twitter feed --filter
```

Configure filters in `~/.twitter/config.yaml`:
```yaml
filter:
  min_score: 50
  max_age_hours: 24
```
