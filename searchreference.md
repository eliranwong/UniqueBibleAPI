# SEARCHREFERENCE

Keyword: SEARCHREFERENCE

Keyword description:

* Search for a string in a bible or multiple bibles. Output bible references only.

Parameter: BIBLE_VERSIONS [optional]

Parameter description:

* Specify a bible version or multiple bible versions.
* Use underscore `_` as a separator to specify multiple bible versions.
* Perform a search in the default bible version if this parameter is not given.

Parameter: SEARCH_STRING [required]

Parameter description:

* Specify a text string for the search.

Parameter: BIBLE_BOOKS [optional]

Parameter description:

* Limit the scope of the search to the specified bible books only.

# Command Format

SEARCHREFERENCE:::[BIBLE_VERSIONS]:::[SEARCH_STRING]:::[BIBLE_BOOKS]

# Examples

Command: `SEARCHREFERENCE:::NET:::God%kind:::John,Romans`

URL: https://bible.gospelchurch.uk/json?cmd=SEARCHREFERENCE:::NET:::God%kind:::John,Romans

Output:

```
{'content': 'Search Bible NET\n'
            'SEARCHREFERENCE::: NET:::God%kind:::John,Romans\n'
            '\n'
            'x 2 verse(s)\n'
            '\n'
            'Rom 2:4; Rom 11:22',
 'keyword': 'SEARCHREFERENCE',
 'parameter_1': 'NET',
 'parameter_2': 'God%kind',
 'parameter_3': 'John,Romans'}
```
