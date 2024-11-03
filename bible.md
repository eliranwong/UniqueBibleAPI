# BIBLE

Keyword: BIBLE

Keyword description:

* Retrieve a verse or multiples verses.
* Perform a search for verses if verse reference is not found.
* This is the default keyword to be used when a given command does not include any valid command keyword.

Parameter: BIBLE_VERSION [optional]

Parameter description:

* Specify a bible version.
* Use default bible version if this parameter is not given.

Parameter: SEARCH_STRING [required]

Parameter description:

* Specify either verse references or a search string.
* Retrieve a bible verse directly if a valid bible reference is given.
* Retrieve multiple bible verses directly if multiple bible references are given.
* Perform a search in the bible if no valid bible reference is given.
* If a search is performed, the default search mode is specified by the value of `bibleSearchMode` in UniqueBible App `config.py`.

# Command Format

BIBLE:::[BIBLE_VERSION]:::[SEARCH_STRING]

# Examples

Command: `John 3:16`

URL: https://bible.gospelchurch.uk/json?cmd=John%203:16

Output:

```
{'content': '(John 3:16) For God so loved the world, that he gave his only '
            'begotten Son, that whosoever believeth in him should not perish, '
            'but have everlasting life.',
 'keyword': 'bible',
 'parameter_1': 'John 3:16'}
```

Command: `BIBLE:::NET:::John 3:16`

URL: https://bible.gospelchurch.uk/json?cmd=BIBLE:::John%203:16

Output:

```
{'content': '(John 3:16) For this is the way God loved the world: He gave his '
            'one and only Son, so that everyone who believes in him will not '
            'perish but have eternal life.',
 'keyword': 'BIBLE',
 'parameter_1': 'NET',
 'parameter_2': 'John 3:16'}
```

Command: `BIBLE:::NET:::Jn 3:16; Rm 5:8; Deu 6:4`

URL: https://bible.gospelchurch.uk/json?cmd=BIBLE:::Jn%203:16;%20Rm%205:8;%20Deu%206:4

Output:

```
{'content': '(John 3:16) For this is the way God loved the world: He gave his '
            'one and only Son, so that everyone who believes in him will not '
            'perish but have eternal life.\n'
            '(Rom 5:8) But God demonstrates his own love for us, in that while '
            'we were still sinners, Christ died for us.\n'
            '(Deut 6:4) Listen, Israel: The Lord is our God, the Lord is one!',
 'keyword': 'BIBLE',
 'parameter_1': 'NET',
 'parameter_2': 'Jn 3:16; Rm 5:8; Deu 6:4'}
```

Command: `Jesus love`

URL: https://bible.gospelchurch.uk/json?cmd=Jesus%20love

Output:

```
{'content': 'REGEXSEARCH::: NET::: Jesus love\n'
            '\n'
            'x 6 verse(s)\n'
            '\n'
            '(John 11:5) (Now Jesus love d Martha and her sister and '
            'Lazarus.)\n'
            '(John 13:23) One of his disciples, the one Jesus love d, was at '
            'the table to the right of Jesus in a place of honor.\n'
            '(John 13:25) Then the disciple whom Jesus love d leaned back '
            'against Jesus’ chest and asked him, “Lord, who is it?”\n'
            '(John 20:2) So she went running to Simon Peter and the other '
            'disciple whom Jesus love d and told them, “They have taken the '
            'Lord from the tomb, and we don’t know where they have put him!”\n'
            '(John 21:7) Then the disciple whom Jesus love d said to Peter, '
            '“It is the Lord!” So Simon Peter, when he heard that it was the '
            'Lord, tucked in his outer garment (for he had nothing on '
            'underneath it), and plunged into the sea.\n'
            '(John 21:20) Peter turned around and saw the disciple whom Jesus '
            'love d following them. (This was the disciple who had leaned back '
            'against Jesus’ chest at the meal and asked, “Lord, who is the one '
            'who is going to betray you?”)',
 'keyword': 'bible',
 'parameter_1': 'Jesus love'}
```
