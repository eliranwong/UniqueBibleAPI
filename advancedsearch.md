# ADVANCEDSEARCH

Keyword: ADVANCEDSEARCH

Keyword description:

* Search bible / bibles with a sql filter.
* It offers flexibility for advanced users to customise a search.

Parameter: BIBLE_VERSIONS [optional]

Parameter description:

* Specify a bible version or multiple bible versions.
* Use underscore `_` as a separator to specify multiple bible versions.
* Perform a search in the default bible version if this parameter is not given.

Parameter: SQL_FILTER [required]

Parameter description:

* Specify a sql filter for the search.
* The given filter fills up content after the `WHERE` keyword in the sql statment for a search.
* Use `|` as a separator to specify multiple items for a combination search

Parameter: BIBLE_BOOKS [optional]

Parameter description:

* Limit the scope of the search to the specified bible books only.

# Command Format

ADVANCEDSEARCH:::[BIBLE_VERSIONS]:::[SQL_FILTER]:::[BIBLE_BOOKS]

# Examples

Command: `ADVANCEDSEARCH:::KJV:::Book = 1 AND Scripture LIKE '%love%'`

URL: https://bible.gospelchurch.uk/json?cmd=ADVANCEDSEARCH:::KJV:::Book%20=%201%20AND%20Scripture%20LIKE%20'%love%'

Output:

```
{'content': 'Search Bible KJV\n'
            "ADVANCEDSEARCH::: KJV:::Book = 1 AND Scripture LIKE '% love %'\n"
            '\n'
            'x 14 verse(s)\n'
            '\n'
            '(Gen 22:2) And he said, Take now thy son, thine only [son] Isaac, '
            'whom thou love st, and get thee into the land of Moriah; and '
            'offer him there for a burnt offering upon one of the mountains '
            'which I will tell thee of.\n'
            "(Gen 24:67) And Isaac brought her into his mother Sarah's tent, "
            'and took Rebekah, and she became his wife; and he love d her: and '
            "Isaac was comforted after his mother's [death].\n"
            '(Gen 25:28) And Isaac love d Esau, because he did eat of [his] '
            'venison: but Rebekah love d Jacob.\n'
            '(Gen 27:4) And make me savory meat, such as I love, and bring '
            '[it] to me, that I may eat; that my soul may bless thee before I '
            'die.\n'
            '(Gen 27:9) Go now to the flock, and fetch me from thence two good '
            'kids of the goats; and I will make them savory meat for thy '
            'father, such as he love th:\n'
            '(Gen 27:14) And he went, and fetched, and brought [them] to his '
            'mother: and his mother made savory meat, such as his father love '
            'd.\n'
            '(Gen 29:18) And Jacob love d Rachel; and said, I will serve thee '
            'seven years for Rachel thy younger daughter.\n'
            '(Gen 29:20) And Jacob served seven years for Rachel; and they '
            'seemed unto him [but] a few days, for the love he had to her.\n'
            '(Gen 29:30) And he went in also unto Rachel, and he love d also '
            'Rachel more than Leah, and served with him yet seven other '
            'years.\n'
            '(Gen 29:32) And Leah conceived, and bore a son, and she called '
            'his name Reuben: for she said, Surely the LORD hath looked upon '
            'my affliction; now therefore my husband will love me.\n'
            '(Gen 34:3) And his soul cleaved unto Dinah the daughter of Jacob, '
            'and he love d the damsel, and spoke kindly unto the damsel.\n'
            '(Gen 37:3) Now Israel love d Joseph more than all his children, '
            'because he [was] the son of his old age: and he made him a coat '
            'of [many] colors.\n'
            '(Gen 37:4) And when his brethren saw that their father love d him '
            'more than all his brethren, they hated him, and could not speak '
            'peaceably unto him.\n'
            '(Gen 44:20) And we said unto my lord, We have a father, an old '
            'man, and a child of his old age, a little one; and his brother is '
            'dead, and he alone is left of his mother, and his father love th '
            'him.',
 'keyword': 'ADVANCEDSEARCH',
 'parameter_1': 'KJV',
 'parameter_2': "Book = 1 AND Scripture LIKE '%love%'"}
```
