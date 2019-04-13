---
layout: post
title: "Regex In Python"
date: 2013-07-17 13:14
comments: true
categories: [Tools, Python]
---

Regex is a important tool when dealing text. In `python` we have a library named `re`.  
Most of the *regular expression operations* are available as _module-level function and RegexObject methods_.

*import the lib*

    import re

*re.compile(pattern, flag=0)*
>Compile a regular expression pattern into a regular expression object, which can be used for matching using its `match()` and `search()` methods, described below.

    import re
    text = 'I love China'
    regexs = [re.compile(p)
            for p in ['love', 'll']
        ]
    for regex in regexs:
        print regex.pattern
        if regex.search(text):
            print "Match"
        else:
            print "Not Match"

*re.search(pattern, string)*
>Scan through string looking for a location where the regular expression pattern produces a match, and return a corresponding `MatchObject` instance.Return `None` if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

    #!/usr/bin/python
    #encoding:utf-8
    import re
    text = 'I love China'
    regexs = [re.compile(p)
            for p in ['love', 'll']
         ]
    for regex in regexs:
        print regex.pattern
        match = re.search(regex, text):
        if match:
            print "Match"
        else:
            print "Not Match"

*RegexObject.search(string)*

    #!/usr/bin/python
    #encoding:utf-8
    import re
    text = 'I love China'
    pattern = 'love'
    match = re.search(pattern, text)
    s = match.start()
    e = match.end()
    print 'Found "%s"\nin "%s"\nfrom %d to %d ("%s")' % \
          (match.re.pattern, match.string, s, e, text[s:e])

*re.match(pattern, srting)*
>If zero or more characters at the beginning of string match this regular expression, return a corresponding `MatchObject` instance. Return `None` if the string does not match the pattern; note that this is different from a zero-length match.

    #!/usr/bin/python
    #encoding:utf-8
    import re
    text = 'His phone 12345 number is 67890'
    regex = re.compile(r'.*?(\d+).*?(\d+)')
    match = re.match(regex, text)
    if match: 
        print match.group(1),match.group(2),

*RegexObject.match(string)*

    #!/usr/bin/python
    #encoding:utf-8
    import re
    text = 'His phone 12345 number is 67890'
    regex = re.compile(r'.*?(\d+).*?(\d+)')
    match = regex.match(text)
    if match: 
        print match.group(1), match.group(2),

#### Match object has many attributes:

**Match more than one**

*re.findall(pattern, string)*

    #!/usr/bin/python
    #encoding:utf-8
    import re
    text = 'this is a text'
    pattern = 'is'
    matchs = re.findall(pattern, text)
    for match in matchs:
        print match

    lo@ubuntu:~/try/regex$ python searchall.py 
    is
    is

*re.finditer(pattern, string)*

    #!/usr/bin/python
    #encoding:utf-8
    import re
    text = 'this is a text'
    pattern = 'is'
    matchs = re.finditer(pattern, text)
    for match in matchs:
        s = match.start()
        e = match.end()
        print "Found ", text[s:e], "at: ", s, e

    lo@ubuntu:~/try/regex$ python searchall.py 
    Found  is at:  2 4
    Found  is at:  5 7

**Pattern Syntax**  
*Repetition*
{a, b}

| |  |
|--|--|
|\*| equivalent to {0,}|
|+| equivalent to {1,}|
|?| equivalent to {0,1}|

    #!/usr/bin/python
    #encoding: utf-8
    import re
    text = '101000111'
    patterns = [
            '10',
            '10?',
            '10*',
            '10+',
            '10{3}',
            '10{1,3}'
            ]
    
    print 'orginal string: ', text
    
    for pattern in patterns:
        matchs = re.finditer(pattern, text)
        for match in matchs:
            s = match.start()
            e = match.end()
            substr = text[s:e]
            print 'pattern: ', pattern,' Found: ', substr, 'at', s, e


    @ubuntu:~/try/regex$ python repetition.py 
    orginal string:  101000111
    pattern:  10  Found:  10 at 0 2
    pattern:  10  Found:  10 at 2 4
    pattern:  10?  Found:  10 at 0 2
    pattern:  10?  Found:  10 at 2 4
    pattern:  10?  Found:  1 at 6 7
    pattern:  10?  Found:  1 at 7 8
    pattern:  10?  Found:  1 at 8 9
    pattern:  10*  Found:  10 at 0 2
    pattern:  10*  Found:  1000 at 2 6
    pattern:  10*  Found:  1 at 6 7
    pattern:  10*  Found:  1 at 7 8
    pattern:  10*  Found:  1 at 8 9
    pattern:  10+  Found:  10 at 0 2
    pattern:  10+  Found:  1000 at 2 6
    pattern:  10{3}  Found:  1000 at 2 6
    pattern:  10{1,3}  Found:  10 at 0 2
    pattern:  10{1,3}  Found:  1000 at 2 6

###Character set
\[a|b\]    \[a-z\]     \[0-9\]   \[a-zA-Z\]

    #!/usr/bin/python
    #encoding utf-8
    import re
    text = 'string is not 12324, 234 IS NOT STRING'
    patterns =[
            '[a-z]+',
            '[A-Z]+',
            '[0-9]+',
            '[a-zA-Z]+',
            '[a-zA-Z0-9]+'
        ]
    print "orginal string: ", text

    for pattern in patterns:
        print "pattern is: ", pattern
        matchs = re.findall(pattern, text)
        for match in matchs:
            print match
    

    lo@ubuntu:~/try/regex$ python searchset.py 
    orginal string:  string is not 12324, 234 IS NOT STRING
    pattern is:  [a-z]+
    string
    is
    not
    pattern is:  [A-Z]+
    IS
    NOT
    STRING
    pattern is:  [0-9]+
    12324
    234
    pattern is:  [a-zA-Z]+
    string
    is
    not
    IS
    NOT
    STRING
    pattern is:  [a-zA-Z0-9]+
    string
    is
    not
    12324
    234
    IS
    NOT
    STRING

**Greedy Or Non-greedy(minimal fashion)**

*Escape sequences* #TODO

| |  |
|--|---|
|\d|any decimal digit|
|\D|any character that is not a decimal digit|
|\w|any 'word' character|
|\W|any 'non-word' character|
|\s|any whitespace character|
|\S|any character that is not a whitespace character|

*Anchors*

| |  |
|--|---|
|^ |the current match point is at the start of the subject string|
|$ |the current match point is at the end of the subject string|
|\b|word boundary|
|\B|not a word boundary|
|\A|start of subject (independent of multiline mode)|
|\Z|end of subject or newline at end (independent of multiline mode)|

###Reference:
[python.org](http://docs.python.org/2/library/re.html)    
[regex php](http://www.php.net/manual/zh/reference.pcre.pattern.syntax.php)
