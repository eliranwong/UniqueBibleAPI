# TEXT

Keyword: TEXT

Keyword description:

* Open a bible version.
* It is designed to quickly open the previously opened verse in a different bible version.

Parameter: BIBLE_VERSION [required]

Parameter description:

* Specify a bible version.

# Command Format

TEXT:::[BIBLE_VERSION]

# Examples

Command: `TEXT:::KJV`

URL: https://bible.gospelchurch.uk/json?cmd=TEXT:::KJV

Output:

```
{'content': '(John 3:16) For God so loved the world, that he gave his only '
            'begotten Son, that whosoever believeth in him should not perish, '
            'but have everlasting life.',
 'keyword': 'TEXT',
 'parameter_1': 'KJV'}
```

Command: `TEXT:::CUV`

URL: https://bible.gospelchurch.uk/json?cmd=TEXT:::KJV

Output:

```
{'content': '(John 3:16) 「上帝愛世人，甚至將他的獨生子賜給〔他們〕，叫一切信他的，不致滅亡，反得永生。',
 'keyword': 'TEXT',
 'parameter_1': 'CUV'}
```