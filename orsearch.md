# ORSEARCH

Keyword: ORSEARCH

Keyword description:

* Search bible / bibles for either one of the specified items regardless of word order
* It is actually an alias of an `ADVANCEDSEARCH`.

Parameter: BIBLE_VERSIONS [optional]

Parameter description:

* Specify a bible version or multiple bible versions.
* Use underscore `_` as a separator to specify multiple bible versions.
* Perform a search in the default bible version if this parameter is not given.

Parameter: SEARCH_STRING [required]

Parameter description:

* Specify a search string for the search.
* Use `|` as a separator to specify multiple items for a combination search

Parameter: BIBLE_BOOKS [optional]

Parameter description:

* Limit the scope of the search to the specified bible books only.

# Command Format

ORSEARCH:::[BIBLE_VERSIONS]:::[SEARCH_STRING]:::[BIBLE_BOOKS]

# Examples

Command: `ORSEARCH:::KJV:::love|Jesus:::Romans`

URL: https://bible.gospelchurch.uk/json?cmd=ORSEARCH:::KJV:::love|Jesus:::Romans

Output:

```
{'content': 'Search Bible KJV\n'
            'ADVANCEDSEARCH::: KJV:::Scripture LIKE "% love %" OR Scripture '
            'LIKE "% Jesus %":::Romans\n'
            '\n'
            'x 56 verse(s)\n'
            '\n'
            '(Rom 1:1) Paul, a servant of Jesus Christ, called [to be] an '
            'apostle, separated unto the gospel of God,\n'
            '(Rom 1:3) Concerning his Son Jesus Christ our Lord, which was '
            'made of the seed of David according to the flesh;\n'
            '(Rom 1:6) Among whom are ye also the called of Jesus Christ:\n'
            '(Rom 1:7) To all that be in Rome, be love d of God, called [to '
            'be] saints: Grace to you and peace from God our Father, and the '
            'Lord Jesus Christ.\n'
            '(Rom 1:8) First, I thank my God through Jesus Christ for you all, '
            'that your faith is spoken of throughout the whole world.\n'
            '(Rom 2:16) In the day when God shall judge the secrets of men by '
            'Jesus Christ according to my gospel.\n'
            '(Rom 3:22) Even the righteousness of God [which is] by faith of '
            'Jesus Christ unto all and upon all them that believe: for there '
            'is no difference:\n'
            '(Rom 3:24) Being justified freely by his grace through the '
            'redemption that is in Christ Jesus:\n'
            '(Rom 3:26) To declare, [I say,] at this time his righteousness: '
            'that he might be just, and the justifier of him which believeth '
            'in Jesus.\n'
            '(Rom 4:24) But for us also, to whom it shall be imputed, if we '
            'believe on him that raised up Jesus our Lord from the dead;\n'
            '(Rom 5:1) Therefore being justified by faith, we have peace with '
            'God through our Lord Jesus Christ:\n'
            '(Rom 5:5) And hope maketh not ashamed; because the love of God is '
            'shed abroad in our hearts by the Holy Ghost which is given unto '
            'us.\n'
            '(Rom 5:8) But God commendeth his love toward us, in that, while '
            'we were yet sinners, Christ died for us.\n'
            '(Rom 5:11) And not only [so,] but we also joy in God through our '
            'Lord Jesus Christ, by whom we have now received the atonement.\n'
            '(Rom 5:15) But not as the offense, so also [is] the free gift. '
            'For if through the offense of one many be dead, much more the '
            'grace of God, and the gift by grace, [which] [is] by one man, '
            'Jesus Christ, hath abounded unto many.\n'
            "(Rom 5:17) For if by one man's offense death reigned by one; much "
            'more they which receive abundance of grace and of the gift of '
            'righteousness shall reign in life by one, Jesus Christ.)\n'
            '(Rom 5:21) That as sin hath reigned unto death, even so might '
            'grace reign through righteousness unto eternal life by Jesus '
            'Christ our Lord.\n'
            '(Rom 6:3) Know ye not, that so many of us as were baptized into '
            'Jesus Christ were baptized into his death?\n'
            '(Rom 6:11) Likewise reckon ye also yourselves to be dead indeed '
            'unto sin, but alive unto God through Jesus Christ our Lord.\n'
            '(Rom 6:23) For the wages of sin [is] death; but the gift of God '
            '[is] eternal life through Jesus Christ our Lord.\n'
            '(Rom 7:25) I thank God through Jesus Christ our Lord. So then '
            'with the mind I myself serve the law of God; but with the flesh '
            'the law of sin.\n'
            '(Rom 8:1) [There is] therefore now no condemnation to them which '
            'are in Christ Jesus, who walk not after the flesh, but after the '
            'Spirit.\n'
            '(Rom 8:2) For the law of the Spirit of life in Christ Jesus hath '
            'made me free from the law of sin and death.\n'
            '(Rom 8:11) But if the Spirit of him that raised up Jesus from the '
            'dead dwell in you, he that raised up Christ from the dead shall '
            'also quicken your mortal bodies by his Spirit that dwelleth in '
            'you.\n'
            '(Rom 8:28) And we know that all things work together for good to '
            'them that love God, to them who are the called according to [his] '
            'purpose.\n'
            '(Rom 8:35) Who shall separate us from the love of Christ? [shall] '
            'tribulation, or distress, or persecution, or famine, or '
            'nakedness, or peril, or sword?\n'
            '(Rom 8:37) Nay, in all these things we are more than conquerors '
            'through him that love d us.\n'
            '(Rom 8:39) Nor height, nor depth, nor any other creature, shall '
            'be able to separate us from the love of God, which is in Christ '
            'Jesus our Lord.\n'
            '(Rom 9:13) As it is written, Jacob have I love d, but Esau have I '
            'hated.\n'
            '(Rom 9:25) As he saith also in Hosea, I will call them my people, '
            'which were not my people; and her be love d, which was not be '
            'love d.\n'
            '(Rom 10:9) That if thou shalt confess with thy mouth the Lord '
            'Jesus, and shalt believe in thine heart that God hath raised him '
            'from the dead, thou shalt be saved.\n'
            '(Rom 11:28) As concerning the gospel, [they are] enemies for your '
            'sakes: but as touching the election, [they are] be love d for the '
            "fathers' sakes.\n"
            '(Rom 12:9) [Let] love be without dissimulation. Abhor that which '
            'is evil; cleave to that which is good.\n'
            '(Rom 12:10) [Be] kindly affectioned one to another with brotherly '
            'love; in honor preferring one another;\n'
            '(Rom 12:19) Dearly be love d, avenge not yourselves, but [rather] '
            'give place unto wrath: for it is written, Vengeance [is] mine; I '
            'will repay, saith the Lord.\n'
            '(Rom 13:8) Owe no man any thing, but to love one another: for he '
            'that love th another hath fulfilled the law.\n'
            '(Rom 13:9) For this, Thou shalt not commit adultery, Thou shalt '
            'not kill, Thou shalt not steal, Thou shalt not bear false '
            'witness, Thou shalt not covet; and if [there be] any other '
            'commandment, it is briefly comprehended in this saying, namely, '
            'Thou shalt love thy neighbor as thyself.\n'
            '(Rom 13:10) Love worketh no ill to his neighbor: therefore love '
            '[is] the fulfilling of the law.\n'
            '(Rom 13:14) But put ye on the Lord Jesus Christ, and make not '
            'provision for the flesh, to [fulfill] the lusts [thereof.]\n'
            '(Rom 14:14) I know, and am persuaded by the Lord Jesus, that '
            '[there is] nothing unclean of itself: but to him that esteemeth '
            'any thing to be unclean, to him [it is] unclean.\n'
            '(Rom 15:5) Now the God of patience and consolation grant you to '
            'be likeminded one toward another according to Christ Jesus:\n'
            '(Rom 15:6) That ye may with one mind [and] one mouth glorify God, '
            'even the Father of our Lord Jesus Christ.\n'
            '(Rom 15:8) Now I say that Jesus Christ was a minister of the '
            'circumcision for the truth of God, to confirm the promises [made] '
            'unto the fathers:\n'
            '(Rom 15:16) That I should be the minister of Jesus Christ to the '
            'Gentiles, ministering the gospel of God, that the offering up of '
            'the Gentiles might be acceptable, being sanctified by the Holy '
            'Ghost.\n'
            '(Rom 15:17) I have therefore whereof I may glory through Jesus '
            'Christ in those things which pertain to God.\n'
            '(Rom 15:30) Now I beseech you, brethren, for the Lord Jesus '
            "Christ's sake, and for the love of the Spirit, that ye strive "
            'together with me in your prayers to God for me;\n'
            '(Rom 16:3) Greet Priscilla and Aquila my helpers in Christ '
            'Jesus:\n'
            '(Rom 16:5) Likewise [greet] the church that is in their house. '
            'Salute my well-be love d Epaenetus, who is the firstfruits of '
            'Achaia unto Christ.\n'
            '(Rom 16:8) Greet Amplias my be love d in the Lord.\n'
            '(Rom 16:9) Salute Urbane, our helper in Christ, and Stachys my be '
            'love d.\n'
            '(Rom 16:12) Salute Tryphena and Tryphosa, who labor in the Lord. '
            'Salute the be love d Persis, which labored much in the Lord.\n'
            '(Rom 16:18) For they that are such serve not our Lord Jesus '
            'Christ, but their own belly; and by good words and fair speeches '
            'deceive the hearts of the simple.\n'
            '(Rom 16:20) And the God of peace shall bruise Satan under your '
            'feet shortly. The grace of our Lord Jesus Christ [be] with you. '
            'Amen.\n'
            '(Rom 16:24) The grace of our Lord Jesus Christ [be] with you all. '
            'Amen.\n'
            '(Rom 16:25) Now to him that is of power to establish you '
            'according to my gospel, and the preaching of Jesus Christ, '
            'according to the revelation of the mystery, which was kept secret '
            'since the world began,\n'
            '(Rom 16:27) To God only wise, [be] glory through Jesus Christ '
            'forever. Amen.',
 'keyword': 'ORSEARCH',
 'parameter_1': 'KJV',
 'parameter_2': 'love|Jesus',
 'parameter_3': 'Romans'}
```
