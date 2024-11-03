# ANDSEARCH

Keyword: ANDSEARCH

Keyword description:

* Search bible / bibles for combinations of items regardless of word order
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

ANDSEARCH:::[BIBLE_VERSIONS]:::[SEARCH_STRING]:::[BIBLE_BOOKS]

# Examples

Command: `ANDSEARCH:::KJV:::love|Jesus`

URL: https://bible.gospelchurch.uk/json?cmd=ANDSEARCH:::KJV:::love|Jesus

Output:

```
{'content': 'Search Bible KJV\n'
            'ADVANCEDSEARCH::: KJV:::Scripture LIKE "% love %" AND Scripture '
            'LIKE "% Jesus %"\n'
            '\n'
            'x 38 verse(s)\n'
            '\n'
            '(Matt 22:37) Jesus said unto him, Thou shalt love the Lord thy '
            'God with all thy heart, and with all thy soul, and with all thy '
            'mind.\n'
            '(Mark 10:21) Then Jesus beholding him love d him, and said unto '
            'him, One thing thou lackest: go thy way, sell whatsoever thou '
            'hast, and give to the poor, and thou shalt have treasure in '
            'heaven: and come, take up the cross, and follow me.\n'
            '(John 8:42) Jesus said unto them, If God were your Father, ye '
            'would love me: for I proceeded forth and came from God; neither '
            'came I of myself, but he sent me.\n'
            '(John 11:5) Now Jesus love d Martha, and her sister, and '
            'Lazarus.\n'
            '(John 13:1) Now before the feast of the passover, when Jesus knew '
            'that his hour was come that he should depart out of this world '
            'unto the Father, having love d his own which were in the world, '
            'he love d them unto the end.\n'
            "(John 13:23) Now there was leaning on Jesus ' bosom one of his "
            'disciples, whom Jesus love d.\n'
            '(John 14:23) Jesus answered and said unto him, If a man love me, '
            'he will keep my words: and my Father will love him, and we will '
            'come unto him, and make our abode with him.\n'
            '(John 19:26) When Jesus therefore saw his mother, and the '
            'disciple standing by, whom he love d, he saith unto his mother, '
            'Woman, behold thy son!\n'
            '(John 20:2) Then she runneth, and cometh to Simon Peter, and to '
            'the other disciple, whom Jesus love d, and saith unto them, They '
            'have taken away the Lord out of the sepulcher, and we know not '
            'where they have laid him.\n'
            '(John 21:7) Therefore that disciple whom Jesus love d saith unto '
            'Peter, It is the Lord. Now when Simon Peter heard that it was the '
            "Lord, he girt [his] fisher's coat [unto him,] (for he was naked,) "
            'and did cast himself into the sea.\n'
            '(John 21:15) So when they had dined, Jesus saith to Simon Peter, '
            'Simon, [son] of Jona, love st thou me more than these? He saith '
            'unto him, Yea, Lord; thou knowest that I love thee. He saith unto '
            'him, Feed my lambs.\n'
            '(John 21:17) He saith unto him the third time, Simon, [son] of '
            'Jona, love st thou me? Peter was grieved because he said unto him '
            'the third time, Love st thou me? And he said unto him, Lord, thou '
            'knowest all things; thou knowest that I love thee. Jesus saith '
            'unto him, Feed my sheep.\n'
            '(John 21:20) Then Peter, turning about, seeth the disciple whom '
            'Jesus love d following; which also leaned on his breast at '
            'supper, and said, Lord, which is he that betrayeth thee?\n'
            '(Rom 1:7) To all that be in Rome, be love d of God, called [to '
            'be] saints: Grace to you and peace from God our Father, and the '
            'Lord Jesus Christ.\n'
            '(Rom 8:39) Nor height, nor depth, nor any other creature, shall '
            'be able to separate us from the love of God, which is in Christ '
            'Jesus our Lord.\n'
            '(Rom 15:30) Now I beseech you, brethren, for the Lord Jesus '
            "Christ's sake, and for the love of the Spirit, that ye strive "
            'together with me in your prayers to God for me;\n'
            '(1Cor 16:22) If any man love not the Lord Jesus Christ, let him '
            'be Anathema Maranatha.\n'
            '(1Cor 16:24) My love [be] with you all in Christ Jesus. Amen.\n'
            '(2Cor 13:14) The grace of the Lord Jesus Christ, and the love of '
            'God, and the communion of the Holy Ghost, [be] with you all. '
            'Amen.\n'
            '(Gal 5:6) For in Jesus Christ neither circumcision availeth any '
            'thing, nor uncircumcision; but faith which worketh by love.\n'
            '(Eph 1:15) Wherefore I also, after I heard of your faith in the '
            'Lord Jesus, and love unto all the saints,\n'
            '(Eph 6:23) Peace [be] to the brethren, and love with faith, from '
            'God the Father and the Lord Jesus Christ.\n'
            '(Eph 6:24) Grace [be] with all them that love our Lord Jesus '
            'Christ in sincerity. Amen.\n'
            '(Col 1:4) Since we heard of your faith in Christ Jesus, and of '
            'the love [which ye] [have] to all the saints.\n'
            '(1Thess 1:3) Remembering without ceasing your work of faith, and '
            'labor of love, and patience of hope in our Lord Jesus Christ, in '
            'the sight of God and our Father;\n'
            '(2Thess 2:16) Now our Lord Jesus Christ himself, and God, even '
            'our Father, which hath love d us, and hath given [us] everlasting '
            'consolation and good hope through grace,\n'
            '(1Tim 1:14) And the grace of our Lord was exceeding abundant with '
            'faith and love which is in Christ Jesus.\n'
            '(2Tim 1:2) To Timothy, [my] dearly be love d son: Grace, mercy, '
            '[and] peace, from God the Father and Christ Jesus our Lord.\n'
            '(2Tim 1:13) Hold fast the form of sound words, which thou hast '
            'heard of me, in faith and love which is in Christ Jesus.\n'
            '(Phlm 1:1) Paul, a prisoner of Jesus Christ, and Timothy [our] '
            'brother, unto Philemon our dearly be love d, and fellow laborer,\n'
            '(Phlm 1:5) Hearing of thy love and faith, which thou hast toward '
            'the Lord Jesus, and toward all saints;\n'
            "(Phlm 1:9) Yet for love 's sake I rather beseech [thee,] being "
            'such a one as Paul the aged, and now also a prisoner of Jesus '
            'Christ.\n'
            '(1John 3:23) And this is his commandment, That we should believe '
            'on the name of his Son Jesus Christ, and love one another, as he '
            'gave us commandment.\n'
            '(1John 5:1) Whosoever believeth that Jesus is the Christ is born '
            'of God: and every one that love th him that begat love th him '
            'also that is begotten of him.\n'
            '(2John 1:3) Grace be with you, mercy, [and] peace, from God the '
            'Father, and from the Lord Jesus Christ, the Son of the Father, in '
            'truth and love.\n'
            '(Jude 1:17) But, be love d, remember ye the words which were '
            'spoken before of the apostles of our Lord Jesus Christ;\n'
            '(Jude 1:21) Keep yourselves in the love of God, looking for the '
            'mercy of our Lord Jesus Christ unto eternal life.\n'
            '(Rev 1:5) And from Jesus Christ, [who is] the faithful witness, '
            '[and] the first begotten of the dead, and the prince of the kings '
            'of the earth. Unto him that love d us, and washed us from our '
            'sins in his own blood,',
 'keyword': 'ANDSEARCH',
 'parameter_1': 'KJV',
 'parameter_2': 'love|Jesus'}
```
