# Regext

Regex is hard.

## Usage

There's 3 special token to identify the prompts:

1. `[DESC]` for description of the regex task
2. `[EXAM]` for the input string example
3. `[WANT]` for the wanted string output

`[DESC]` can specified alone without `[EXAM]` and `[WANT]`.

### Example

**Example 1, one line [EXAM] and [WANT] and output**

```python
from regext import Regext

r = Regext()

test1 = """\
[DESC] A string that extracts website domain name from a URL
[EXAM] https://www.google.com
[WANT] google
[EXAM] https://www.facebook.com
[WANT] facebook
[EXAM] https://www.youtube.com
[WANT] youtube
"""

answer = r(test1)
print(answer)
```

**Output 1**

```
Iteration: 1
Total: 3, True: 3, False: 0
'(?<=\\/\\/www\\.)\\w+(?=\\.com)'
```

**Example 2, multi line [EXAM] and [WANT] and output**
Multi line for `[EXAM]` should be forced to be one line since it's not really matter. Meanwhile multi line `[WANT]` needs to be seperated with double semicolon `;;`. See the third `[EXAM]` and `[WANT]` pair.

```python
from regext import Regext

r = Regext()

# long html example is from hackerrank

test2 = """\
[DESC] A string that extracts link from HTML <a> tag
[EXAM] <a href="https://www.google.com">Samsung</a>
[WANT] https://www.google.com
[EXAM] <p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a></p>
[WANT] http://www.quackit.com/html/tutorial/html_links.cfm
[EXAM] <div class="portal" role="navigation" id='p-navigation'>\
<h3>Navigation</h3>\
<div class="body">\
<ul>\
 <li id="n-mainpage-description"><a href="/wiki/Main_Page" title="Visit the main page [z]" accesskey="z">Main page</a></li>\
 <li id="n-contents"><a href="/wiki/Portal:Contents" title="Guides to browsing Wikipedia">Contents</a></li>\
 <li id="n-featuredcontent"><a href="/wiki/Portal:Featured_content" title="Featured content  the best of Wikipedia">Featured content</a></li>\
<li id="n-currentevents"><a href="/wiki/Portal:Current_events" title="Find background information on current events">Current events</a></li>\
<li id="n-randompage"><a href="/wiki/Special:Random" title="Load a random article [x]" accesskey="x">Random article</a></li>\
<li id="n-sitesupport"><a href="/donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en" title="Support us">Donate to Wikipedia</a></li>\
</ul>\
</div>\
</div>\

[WANT] /wiki/Main_Page;; /wiki/Portal:Contents;; /wiki/Portal:Featured_content;; /wiki/Portal:Current_events;; /wiki/Special:Random;; /donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&utm_medium=sidebar&utm_campaign=C13_en.wikipedia.org&uselang=en
"""

answer = r(test2)
print(answer)
```

**Output 2**

```
Iteration: 1
Total: 3, True: 3, False: 0
'(?<=href=")[^"]+(?=")'
```

**Notes:**

1. Make sure that you have .env file that specify open ai key. The variable name should be `OPENAI_KEY`.
