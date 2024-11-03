# COUNT

Keyword: COUNT

Keyword description:

* Count the occurrences of a string in individual bible books.

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

COUNT:::[BIBLE_VERSIONS]:::[SEARCH_STRING]:::[BIBLE_BOOKS]

# Examples

Command: `COUNT:::Jesus`

URL: https://bible.gospelchurch.uk/json?cmd=COUNT:::Jesus

Output:

```
{'content': 'COUNT:::KJV:::Jesus\n'
            '\n'
            'Total: 941 verse(s) found in KJV. ***\n'
            '\n'
            'Book Verse(s)\n'
            'Gen 0\n'
            'Exod 0\n'
            'Lev 0\n'
            'Num 0\n'
            'Deut 0\n'
            'Josh 0\n'
            'Judg 0\n'
            'Ruth 0\n'
            '1Sam 0\n'
            '2Sam 0\n'
            '1Kgs 0\n'
            '2Kgs 0\n'
            '1Chr 0\n'
            '2Chr 0\n'
            'Ezra 0\n'
            'Neh 0\n'
            'Esth 0\n'
            'Job 0\n'
            'Ps 0\n'
            'Prov 0\n'
            'Eccl 0\n'
            'Song 0\n'
            'Isa 0\n'
            'Jer 0\n'
            'Lam 0\n'
            'Ezek 0\n'
            'Dan 0\n'
            'Hos 0\n'
            'Joel 0\n'
            'Amos 0\n'
            'Obad 0\n'
            'Jonah 0\n'
            'Mic 0\n'
            'Nah 0\n'
            'Hab 0\n'
            'Zeph 0\n'
            'Hag 0\n'
            'Zech 0\n'
            'Mal 0\n'
            'Matt 170\n'
            'Mark 93\n'
            'Luke 97\n'
            'John 245\n'
            'Acts 67\n'
            'Rom 38\n'
            '1Cor 24\n'
            '2Cor 16\n'
            'Gal 16\n'
            'Eph 20\n'
            'Phil 21\n'
            'Col 8\n'
            '1Thess 15\n'
            '2Thess 11\n'
            '1Tim 13\n'
            '2Tim 13\n'
            'Titus 4\n'
            'Phlm 7\n'
            'Heb 13\n'
            'Jas 2\n'
            '1Pet 10\n'
            '2Pet 8\n'
            '1John 12\n'
            '2John 2\n'
            '3John 0\n'
            'Jude 4\n'
            'Rev 12',
 'keyword': 'COUNT',
 'parameter_1': 'Jesus'}
```

Command: `COUNT:::NET:::Jesus`

URL: https://bible.gospelchurch.uk/json?cmd=COUNT:::NET:::Jesus

Output:

```
{'content': 'COUNT:::NET:::Jesus\n'
            '\n'
            'Total: 1157 verse(s) found in NET. ***\n'
            '\n'
            'Book Verse(s)\n'
            'Gen 0\n'
            'Exod 0\n'
            'Lev 0\n'
            'Num 0\n'
            'Deut 0\n'
            'Josh 0\n'
            'Judg 0\n'
            'Ruth 0\n'
            '1Sam 0\n'
            '2Sam 0\n'
            '1Kgs 0\n'
            '2Kgs 0\n'
            '1Chr 0\n'
            '2Chr 0\n'
            'Ezra 0\n'
            'Neh 0\n'
            'Esth 0\n'
            'Job 0\n'
            'Ps 0\n'
            'Prov 0\n'
            'Eccl 0\n'
            'Song 0\n'
            'Isa 0\n'
            'Jer 0\n'
            'Lam 0\n'
            'Ezek 0\n'
            'Dan 0\n'
            'Hos 0\n'
            'Joel 0\n'
            'Amos 0\n'
            'Obad 0\n'
            'Jonah 0\n'
            'Mic 0\n'
            'Nah 0\n'
            'Hab 0\n'
            'Zeph 0\n'
            'Hag 0\n'
            'Zech 0\n'
            'Mal 0\n'
            'Matt 173\n'
            'Mark 148\n'
            'Luke 215\n'
            'John 283\n'
            'Acts 73\n'
            'Rom 35\n'
            '1Cor 22\n'
            '2Cor 14\n'
            'Gal 15\n'
            'Eph 19\n'
            'Phil 21\n'
            'Col 6\n'
            '1Thess 15\n'
            '2Thess 11\n'
            '1Tim 13\n'
            '2Tim 12\n'
            'Titus 4\n'
            'Phlm 6\n'
            'Heb 15\n'
            'Jas 2\n'
            '1Pet 9\n'
            '2Pet 8\n'
            '1John 18\n'
            '2John 2\n'
            '3John 0\n'
            'Jude 6\n'
            'Rev 12',
 'keyword': 'COUNT',
 'parameter_1': 'NET',
 'parameter_2': 'Jesus'}
```

Command: `COUNT:::NET:::Jesus:::John,Romans`

URL: https://bible.gospelchurch.uk/json?cmd=COUNT:::NET:::Jesus:::John,Romans

Output:

```
{'content': 'COUNT:::NET:::Jesus:::John,Romans\n'
            '\n'
            'Total: 318 verse(s) found in NET. ***\n'
            '\n'
            'Book Verse(s)\n'
            'John 283\n'
            'Rom 35',
 'keyword': 'COUNT',
 'parameter_1': 'NET',
 'parameter_2': 'Jesus',
 'parameter_3': 'John,Romans'}
```

Command: `COUNT:::NET_KJV:::Jesus:::John,Romans`

URL: https://bible.gospelchurch.uk/json?cmd=COUNT:::NET_KJV:::Jesus:::John,Romans

Output:

```
{'content': 'COUNT:::KJV:::Jesus:::John,Romans\n'
            '\n'
            'Total: 283 verse(s) found in KJV. ***\n'
            '\n'
            'Book Verse(s)\n'
            'John 245\n'
            'Rom 38\n'
            '--------------------\n'
            'COUNT:::NET:::Jesus:::John,Romans\n'
            '\n'
            'Total: 318 verse(s) found in NET. ***\n'
            '\n'
            'Book Verse(s)\n'
            'John 283\n'
            'Rom 35',
 'keyword': 'COUNT',
 'parameter_1': 'NET_KJV',
 'parameter_2': 'Jesus',
 'parameter_3': 'John,Romans'}
```