"""Data models for twitter-lyr.

Defines Tweet, Author, Metrics, TweetMedia, and new models for DMs, Lists, Polls, Communities.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Author:
    id: str
    name: str
    screen_name: str
    profile_image_url: str = ""
    verified: bool = False


@dataclass
class Metrics:
    likes: int = 0
    retweets: int = 0
    replies: int = 0
    quotes: int = 0
    views: int = 0
    bookmarks: int = 0


@dataclass
class TweetMedia:
    type: str  # "photo" | "video" | "animated_gif"
    url: str
    width: int | None = None
    height: int | None = None


@dataclass
class Tweet:
    id: str
    text: str
    author: Author
    metrics: Metrics
    created_at: str
    media: list[TweetMedia] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)
    is_retweet: bool = False
    lang: str = ""
    retweeted_by: str | None = None
    quoted_tweet: Tweet | None = None
    score: float | None = None
    article_title: str | None = None
    article_text: str | None = None
    is_subscriber_only: bool = False
    is_promoted: bool = False


@dataclass
class BookmarkFolder:
    id: str
    name: str


@dataclass
class UserProfile:
    id: str
    name: str
    screen_name: str
    bio: str = ""
    location: str = ""
    url: str = ""
    followers_count: int = 0
    following_count: int = 0
    tweets_count: int = 0
    likes_count: int = 0
    verified: bool = False
    profile_image_url: str = ""
    created_at: str = ""


@dataclass
class DMParticipant:
    id: str
    name: str
    screen_name: str
    profile_image_url: str = ""


@dataclass
class DMMessage:
    id: str
    conversation_id: str
    sender_id: str
    sender_screen_name: str
    text: str
    created_at: str
    media: list[TweetMedia] = field(default_factory=list)


@dataclass
class DMConversation:
    id: str
    participants: list[DMParticipant] = field(default_factory=list)
    last_message: DMMessage | None = None
    updated_at: str = ""


@dataclass
class TwitterList:
    id: str
    name: str
    description: str = ""
    private: bool = False
    member_count: int = 0
    subscriber_count: int = 0
    owner: UserProfile | None = None
    created_at: str = ""


@dataclass
class PollOption:
    position: int
    text: str
    count: int = 0


@dataclass
class Poll:
    options: list[PollOption] = field(default_factory=list)
    duration_minutes: int = 0
    end_datetime: str = ""
    voting_status: str = ""  # "open" | "closed"


@dataclass
class Community:
    id: str
    name: str
    description: str = ""
    member_count: int = 0
    private: bool = False
    owner_id: str = ""
    created_at: str = ""
