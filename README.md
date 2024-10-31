# Unique Bible App API

This repository is created for documentating the API references of the [UniqueBible App](https://github.com/eliranwong/UniqueBible).

# UniqueBible App Commands and APIs

UniqueBible App offers a built-in set of commands for retrieving bible data from databases.

These commands work with most [running modes](https://github.com/eliranwong/UniqueBible/wiki/UBA-Run-Modes) that UnqiueBible App supports.

In particular, our web API endpoints work directly with UniqueBible App commands.

For example, we are running an UniqueBible App web server at https://bible.gospelchurch.uk.

The command to read John 3:16 in the `NET` Bible is `bible:::NET:::John 3:16`.

You can read the verse in the NET version directly by opening https://bible.gospelchurch.uk/index.html?cmd=bible:::NET:::John%203:16 in a web browser.

You can also retrieve the data via the web APIs in three formats:

   Raw html output - https://bible.gospelchurch.uk/html?cmd=bible:::NET:::John%203:16

   JSON output - https://bible.gospelchurch.uk/json?cmd=bible:::NET:::John%203:16

   Plain text output - https://bible.gospelchurch.uk/plain?cmd=bible:::NET:::John%203:16

   Remarks: API outputs use `utf-8` encoding.

Therefore, you can master UniqueBible APIs with UniqueBible App commands.

This repository aims to provide detailed documentation on how to formulate UniqueBible App commands that work with UniqueBible App web APIs.
