# Unique Bible App API

This repository is created for documentating the API references of the [UniqueBible App](https://github.com/eliranwong/UniqueBible).

# UniqueBible App Commands and APIs

UniqueBible App offers a built-in set of commands for retrieving bible data from databases.

These commands work with most [running modes](https://github.com/eliranwong/UniqueBible/wiki/UBA-Run-Modes) that UnqiueBible App supports.

In particular, our web API endpoints work directly with UniqueBible App commands.

For example, to retrieve commentaries on John 2:4-7, the UniqueBible command is `Commentary:::John 2:4-7`.

To retrieve the commentary via the web APIs:

   Raw html output - https://bible.gospelchurch.uk/html?cmd=Commentary:::John%202:4-7

   JSON output - https://bible.gospelchurch.uk/json?cmd=Commentary:::John%202:4-7

   Plain text output - https://bible.gospelchurch.uk/plain?cmd=Commentary:::John%202:4-7

   Remarks: API outputs use `utf-8` encoding.

Therefore, you can master UniqueBible APIs with UniqueBible App commands.

This repository aims to provide detailed documentation on how to formulate UniqueBible App commands that work with UniqueBible App web APIs.
