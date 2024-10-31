# COMMENTARY

Keyword: COMMENTARY

Keyword description:

* Retrieve bible commentaries on specific bible verses.

Parameter: COMMENTARY_MODULE [optional]

Parameter description:

* Specify a commentary module
* Use default commentary module if this parameter is not given.

Parameter: BIBLE_REFERENCES [required]

Parameter description:

* Specify a verse reference or multiple verse references.

# Command Format

COMMENTARY:::[COMMENTARY_MODULE]:::[BIBLE_REFERENCES]

# Examples

Command: `John 3:16`

URL: https://bible.gospelchurch.uk/json?cmd=COMMENTARY:::John%203:16

Output:

```
{'content': '# 3:16 Ver. 16. Several conservative theologians, Neander, '
            'Tholuck, Westcott, are of opinion that the words of Jesus end '
            'with ver. 15, and that from vv. 16-21 we have an addition by the '
            'evangelist. There is much to be said in favour of this idea. The '
            'thoughts of these verses are explanatory rather than progressive. '
            "Vv. 16 and 17 repeat the object of Christ's mission, which has "
            'already been stated. Vv. 18 and 19 declare the historic results '
            'in faith and unbelief, results which at the date of the '
            'conversation were not conspicuous. Vv. 20 and 21 exhibit the '
            'causes of faith and unbelief. The tenses also forbid us to refer '
            'the passage directly to Jesus. In His lips the present would have '
            'been more natural. To John looking back on the finished story '
            'aorists and perfects are natural. Also, the designation "only '
            'begotten son" is not one of the names by which Jesus designates '
            'Himself, but it is used by the evangelist, 1:18 and 1John 4:9.- '
            'οὕτω γὰρ ἠγάπησεν … ζωὴν αἰώνιον. The love of God for the world '
            "of men is the source of Christ's mission with all its blessings. "
            'It was this which prompted Him to "give," that is, to give not '
            'solely to the death of the cross alluded to in ver. 14, but to '
            'all that the world required for salvation, His only begotten Son. '
            '"The change from the aorist (ἀπόληται) to the present (ἔχῃ) is to '
            'be noted, the utter ruin being spoken of as an act, the '
            'possession of life eternal as an enduring experience" (Meyer, '
            'Weiss, Holtzmann).-',
 'keyword': 'COMMENTARY',
 'parameter_1': 'John 3:16'}
```

Command: `COMMENTARY:::CBSC:::John 3:16`

URL: https://bible.gospelchurch.uk/json?cmd=COMMENTARY:::CBSC:::John%203:16

Output:

```
{'content': '# 3:16\n'
            '\n'
            'For ] Explaining how God wills eternal life to every one that '
            'believeth.\n'
            '\n'
            'loved the world ] The whole human race: see on Joh 1:10. This '
            'would be a revelation to the exclusive Pharisee, brought up to '
            'believe that God loved only the chosen people. The word for '
            '‘love,’ agapân, is very frequent both in this Gospel and in the '
            'First Epistle, and may be considered characteristic of S. John.\n'
            '\n'
            'that he gave his only begotten ] This would be likely to remind '
            'Nicodemus of the offering of Isaac. Comp. 1Jn 4:9; Heb 11:17; Rom '
            '8:32. See note on Joh 1:14.\n'
            '\n'
            'everlasting life ] The Greek is the same as in the previous '
            'verse, and the translation should be the same, eternal life. '
            '‘Eternal life’ is one of the phrases of which S. John is fond. It '
            'occurs 17 times in the Gospel (only eight in the Synoptics) and '
            'six times in the First Epistle. In neither Gospel nor Epistle is '
            '‘eternal’ (aiônios) applied to anything but ‘life.’ On aiônios, '
            'which of itself does not necessarily mean ‘everlasting’ or '
            '‘unending,’ see note on Mat 25:46.',
 'keyword': 'COMMENTARY',
 'parameter_1': 'CBSC',
 'parameter_2': 'John 3:16'}
```

Command: `COMMENTARY:::CBSC:::John John 2:4,6-7`

URL: https://bible.gospelchurch.uk/json?cmd=COMMENTARY:::CBSC:::John%20John%202:4,6-7

Output:

```
{'content': '# 2:4\n'
            '\n'
            'Woman, what have I to do with thee? ] S. John alone of all the '
            'Evangelists never gives the Virgin’s name. Here, as so often, he '
            'assumes that his readers know the main points in the Gospel '
            'narrative: or it may be part of the reserve which he exhibits '
            'with regard to all that nearly concerns himself. Christ’s Mother '
            'had become his mother (Joh 19:26-27). He nowhere mentions his '
            'brother James.\n'
            '\n'
            'Treatises have been written to shew that these words do not '
            'contain a rebuke; for if Christ here rebukes His Mother, it '
            'cannot be maintained that she is immaculate. ‘Woman’ of course '
            'implies no rebuke; the Greek might more fairly be rendered ‘Lady’ '
            '(comp. Joh 19:26), At the same time it marks a difference between '
            'the Divine Son and the earthly parent: He does not say, ‘Mother.’ '
            'But ‘what have I to do with thee?’ does imply rebuke, as is '
            'evident from the other passages where the phrase occurs, Jdg '
            '11:12; 1Ki 17:18; 2Ki 3:13; Mat 8:29; Mar 1:24; Luk 8:28. Only in '
            'one passage does the meaning seem to vary: in 2Ch 35:21 the '
            'question seems to mean ‘why need we quarrel?’ rather than ‘what '
            'have we in common?’ But such a meaning, if possible there, would '
            'be quite inappropriate here. The further question has been '
            'asked,—what was she rebuked for? Chrysostom thinks for vanity; '
            'she wished to glorify herself through her Son. More probably for '
            'interference: He will help, but in His own way, and in His own '
            'time. Comp. Luk 2:51.\n'
            '\n'
            'mine hour ] The meaning of ‘My hour’ and ‘His hour’ in this '
            'Gospel depends in each case on the context. There cannot here be '
            'any reference to His death; rather it means His hour for '
            '‘manifesting forth His glory’ (Joh 2:11) as the Messiah by '
            'working miracles. The exact moment was still in the future. Comp. '
            'Joh 7:8, where He for the moment refuses what He soon after does; '
            'and Joh 12:23, Joh 17:1, which confirm the meaning here given to '
            '‘hour.’',
 'keyword': 'COMMENTARY',
 'parameter_1': 'CBSC',
 'parameter_2': 'John 2:4,6-7'}
```