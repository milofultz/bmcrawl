# Bookmark Crawler
---

## Goal

Search engines are too broad and do not serve people who search for interesting and curated content that does not have relevant keywords. For example, searching "DIY Projects" will not yield interesting results, as those SEO search terms are saturated by bigger scale organizations and make finding smaller creators and curators much more difficult. As the internet gets larger and larger, this will only be more of a problem with modern search engines, as their algorithm rewards good SEO and Alexa rankings, which is determined not necessarily by quality of content, but by linking and optimization. 

So if you want to find interesting and curated content regarding DIY projects, how can you find them? This is an experiment that utilizes a set of URL's to create an extremely specific set of links based on the sites that you already liked enough to bookmark it. Hopefully this will provide the user with new domains and pages to explore that are related and recommended within their bookmarks. 

## How

* Take user's bookmarks (exported from Firefox as an HTML file) and create a list of URLs to scrape.
* Scrape each URL in bookmarks for links.
* Allow process to repeat up to N degrees away from initial source URL.
* Return an HTML file of new sites to explore.

## Future Implementations

I would love to see a StumbleUpon-style random button, but for now that is way beyond my capabilities.

I want to make it usable with any given site as well; where you put in a URL that you find interesting and it spits back all the sites it links to up to N degrees away. I feel like this will almost be more usable and fun than it's current implementation.

---

## Files

- **bmcrawlv3.py** - This is all you need to run it.
- **bookmarks.html** - The bookmarks file I used to test.
- **newlinks_0.html** - The result of running the program on the bookmarks file.

## Usage

1. Download the .py file.
2. Download bookmarks as an HTML file named 'bookmarks.html'.
3. Place both files in same directory.
4. ```python3 bmcrawlv3.py```