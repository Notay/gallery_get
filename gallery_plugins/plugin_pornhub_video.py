# NOTE: For Pornhub use the direct link, which should look something like this: "https://www.pornhub.com/view_video.php?viewkey=blahblahblah"

# Plugin for gallery_get.
import re

# Each definition can be one of the following:
# - a string
# - a regex string
# - a function that takes source as a parameter and returns an array or a string.  (You may assume that re and urllib are already imported.)
# If you comment out a parameter, it will use the default defined in __init__.py

# identifier (default = name of this plugin after "plugin_") : If there's a match, we'll attempt to download images using this plugin.
identifier = "pornhub.com/view_video"

# title: parses the gallery page for a title.  This will be the folder name of the output gallery.
title = r'property="og:title" content="(.+?)"'

# redirect: if the links in the gallery page go to an html instead of an image, use this to parse the gallery page.

# direct_links: if redirect is non-empty, this parses each redirect page for a single image.  Otherwise, this parses the gallery page for all images.
def direct_links(source):
    links = re.findall(r'"videoUrl":"(\S+?)"',source)
    if links:
      return map(lambda x: x.replace("\/", "/"), links)[0] # highest-quality video is listed first
    else:
      return nil

# same_filename (default=False): if True, uses filename specified on remote link.  Otherwise, creates own filename with incremental index. 
same_filename = False

