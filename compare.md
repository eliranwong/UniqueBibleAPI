# COMPARE

Keyword: COMPARE

Keyword description:

* Compare bible versions of a single verse or multiple references.

Parameter: BIBLE_VERSIONS [optional]

Parameter description:

* Specify the bible versions to be compared.
* Compare all favourite versions if this parameter is not given.
* Use underscore `_` as a separator for specifying multiple bible versions.

Parameter: BIBLE_REFERENCES [required]

Parameter description:

* Specify a verse reference or multiple verse references.

# Command Format

COMPARE:::[BIBLE_VERSIONS]:::[BIBLE_REFERENCES]

# Examples

Command: `COMPARE:::John 3:16`

URL: https://bible.gospelchurch.uk/json?cmd=COMPARE:::John%203:16

Output:

```
{'content': 'John 3:16\n'
            '\n'
            '(MIB)\n'
            'Ουτως γαρ ηγαπησεν ο Θεος τον κοσμον, ωστε τον Υιον τον μονογενη '
            'εδωκεν, ινα πας ο πιστευων εις αυτον μη αποληται αλλ εχη ζωην '
            'αιωνιον.\n'
            '(MPB)\n'
            'Ουτως γαρ ηγαπησεν ο Θεος τον κοσμον, ωστε τον Υιον τον μονογενη '
            'εδωκεν, ινα πας ο πιστευων εις αυτον μη αποληται αλλ εχη ζωην '
            'αιωνιον.\n'
            '(NET)\n'
            'For this is the way God loved the world: He gave his one and only '
            'Son, so that everyone who believes in him will not perish but '
            'have eternal life.',
 'keyword': 'COMPARE',
 'parameter_1': 'John 3:16'}
```

Command: `COMPARE:::KJV_CUV:::John 3:16`

URL: https://bible.gospelchurch.uk/json?cmd=COMPARE:::KJV_CUV:::John%203:16

Output:

```
{'content': 'John 3:16\n'
            '\n'
            '(CUV)\n'
            '「上帝愛世人，甚至將他的獨生子賜給〔他們〕，叫一切信他的，不致滅亡，反得永生。\n'
            '(KJV)\n'
            'For God so loved the world, that he gave his only begotten Son, '
            'that whosoever believeth in him should not perish, but have '
            'everlasting life.',
 'keyword': 'COMPARE',
 'parameter_1': 'KJV_CUV',
 'parameter_2': 'John 3:16'}
```

Command: `COMPARE:::KJV_CUV:::John 3:16;Deu 6:4`

URL: https://bible.gospelchurch.uk/json?cmd=COMPARE:::KJV_CUV:::John%203:16;Deu%206:4

Output:

```
{'content': 'John 3:16\n'
            '\n'
            '(CUV)\n'
            '「上帝愛世人，甚至將他的獨生子賜給〔他們〕，叫一切信他的，不致滅亡，反得永生。\n'
            '(KJV)\n'
            'For God so loved the world, that he gave his only begotten Son, '
            'that whosoever believeth in him should not perish, but have '
            'everlasting life.\n'
            '\n'
            'Deut 6:4\n'
            '\n'
            '(CUV)\n'
            '「以色列啊，你要聽！耶和華－我們上帝是獨一的主。\n'
            '(KJV)\n'
            'Hear, O Israel: The LORD our God [is] one LORD:',
 'keyword': 'COMPARE',
 'parameter_1': 'KJV_CUV',
 'parameter_2': 'John 3:16;Deu 6:4'}
```