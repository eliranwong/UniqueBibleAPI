# SEARCHNT

Keyword: SEARCHNT

Keyword description:

* Search for a string in the New Testament of a bible or multiple bibles.

Parameter: BIBLE_VERSIONS [optional]

Parameter description:

* Specify a bible version or multiple bible versions.
* Use underscore `_` as a separator to specify multiple bible versions.
* Perform a search in the default bible version if this parameter is not given.

Parameter: SEARCH_STRING [required]

Parameter description:

* Specify a text string for the search.

# Command Format

SEARCHNT:::[BIBLE_VERSIONS]:::[SEARCH_STRING]

# Examples

Command: `SEARCHNT:::NET_KJV:::God%kind`

URL: https://bible.gospelchurch.uk/json?cmd=SEARCHNT:::NET_KJV:::God%kind

Output:

```
{'content': 'Search Bible NET\n'
            'ADVANCEDSEARCH::: NET:::Scripture LIKE "% God%kind %" AND Book >= '
            '40 AND Book <= 66\n'
            '\n'
            'x 6 verse(s)\n'
            '\n'
            '(Rom 2:4) Or do you have contempt for the wealth of his kindness, '
            'forbearance, and patience, and yet do not know that God’s '
            'kindness leads you to repentance?\n'
            '(Rom 11:22) Notice therefore the kindness and harshness of God – '
            'harshness toward those who have fallen, but God’s kindness toward '
            'you, provided you continue in his kindness; otherwise you also '
            'will be cut off.\n'
            '(1Cor 12:28) And God has placed in the church first apostles, '
            'second prophets, third teachers, then miracles, gifts of healing, '
            'helps, gifts of leadership, different kinds of tongues.\n'
            '(Col 3:12) Therefore, as the elect of God, holy and dearly loved, '
            'clothe yourselves with a heart of mercy, kindness, humility, '
            'gentleness, and patience,\n'
            '(1Tim 5:21) Before God and Christ Jesus and the elect angels, I '
            'solemnly charge you to carry out these commands without prejudice '
            'or favoritism of any kind.\n'
            '(Titus 3:4) But “when the kindness of God our Savior and his love '
            'for mankind appeared,\n'
            '--------------------\n'
            'Search Bible KJV\n'
            'ADVANCEDSEARCH::: KJV:::Scripture LIKE "% God%kind %" AND Book >= '
            '40 AND Book <= 66\n'
            '\n'
            'x 5 verse(s)\n'
            '\n'
            '(Acts 3:25) Ye are the children of the prophets, and of the '
            'covenant which God made with our fathers, saying unto Abraham, '
            'And in thy seed shall all the kindreds of the earth be blessed.\n'
            '(1Cor 6:9) Know ye not that the unrighteous shall not inherit the '
            'kingdom of God? Be not deceived: neither fornicators, nor '
            'idolaters, nor adulterers, nor effeminate, nor abusers of '
            'themselves with mankind,\n'
            '(Col 3:12) Put on therefore, as the elect of God, holy and '
            'beloved, bowels of mercies, kindness, humbleness of mind, '
            'meekness, longsuffering;\n'
            '(2Pet 1:7) And to godliness brotherly kindness; and to brotherly '
            'kindness charity.\n'
            '(Rev 5:9) And they sung a new song, saying, Thou art worthy to '
            'take the book, and to open the seals thereof: for thou wast '
            'slain, and hast redeemed us to God by thy blood out of every '
            'kindred, and tongue, and people, and nation;',
 'keyword': 'SEARCHNT',
 'parameter_1': 'NET_KJV',
 'parameter_2': 'God%kind'}
```
