# 🧹 Web Scraping
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/licence-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/python-3-yellow.svg)](#) [![#](https://img.shields.io/badge/tweepy-3.8.0-brightgreen.svg)](#)

## Description
App to learn about working with Twitter API.

## Quick Start

> 👉 Before run these scripts make sure that you are using a Python 3 virtual environment ;)

```sh
# Before starting, you need to configure some environment variables.
# P.S. These values can be found in your app page at "developer.twitter.com"
export TWITTER_CONSUMER_KEY="YOUR_API_KEY"
export TWITTER_CONSUMER_SECRET="YOUR_API_SECRET_KEY"
export TWITTER_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
export TWITTER_ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET"

# First we need to get some data before processing it.
python src/data_streaming.py

# Next, we can process the data that we got ;)
python src/data_ingestion.py
```

## Related Links
- [Blog: Twitter Analytics](http://adilmoujahid.com/posts/2014/07/twitter-analytics/)
- [Twitter 4 Devs](https://developer.twitter.com/)

---

_You can find [@avcaliani](#) at [GitHub](https://github.com/avcaliani) or [GitLab](https://gitlab.com/avcaliani)._
