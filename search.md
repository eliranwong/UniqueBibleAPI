# SEARCH

Keyword: SEARCH

Keyword description:

* Search for a string in a bible or multiple bibles.

Parameter: BIBLE_VERSION [optional]

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

SEARCH:::[BIBLE_VERSIONS]:::[SEARCH_STRING]:::[BIBLE_BOOKS]

# Examples

Command: `SEARCH:::NET:::God%kind:::John,Romans`

URL: https://bible.gospelchurch.uk/json?cmd=SEARCH:::NET:::God%kind:::John,Romans

Output:

```
{'content': 'Search Bible NET\n'
            'SEARCH::: NET::: God % kind:::John,Romans\n'
            '\n'
            'x 2 verse(s)\n'
            '\n'
            '(Rom 2:4) Or do you have contempt for the wealth of his kind '
            'ness, forbearance, and patience, and yet do not know that God ’s '
            'kind ness leads you to repentance?\n'
            '(Rom 11:22) Notice therefore the kind ness and harshness of God – '
            'harshness toward those who have fallen, but God ’s kind ness '
            'toward you, provided you continue in his kind ness; otherwise you '
            'also will be cut off.',
 'keyword': 'SEARCH',
 'parameter_1': 'NET',
 'parameter_2': 'God%kind',
 'parameter_3': 'John,Romans'}
```
