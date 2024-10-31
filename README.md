# Unique Bible App API

This repository is created for documentating the API references of the [UniqueBible App](https://github.com/eliranwong/UniqueBible).

# UniqueBible App Commands and APIs

UniqueBible App offers a built-in set of commands for retrieving bible data from databases.

These commands work with most [running modes](https://github.com/eliranwong/UniqueBible/wiki/UBA-Run-Modes) that UnqiueBible App supports.

In particular, our web API endpoints work directly with UniqueBible App commands.

For example, we are running an UniqueBible App web server at https://bible.gospelchurch.uk.

The command to read commentary on John 2:4-7, the UniqueBible command that uses default commentary is `commentary:::John 2:4-7`.

You can launch the UniqueBible GUI app to navigate to it via GUI menu or enter the command in the command field directly to open the commentary.

You can use the same command in other running modes, for example, in the stream mode:

> uniquebible stream commentary:::John 2:4-7

With UniqueBible web mode, you can both browse the content via web browser and retrieve the data via built-in web API endpoints: `/html`, `/json`, and `/plain`.

For example, we have an UniqueBible App web server set up at https://bible.gospelchurch.uk

You can read the commentary by opening https://bible.gospelchurch.uk/index.html?cmd=commentary:::John%202:4-7 in a web browser.

You can also retrieve the data via the web APIs in three formats:

Raw html output - https://bible.gospelchurch.uk/html?cmd=commentary:::John%202:4-7

JSON output - https://bible.gospelchurch.uk/json?cmd=commentary:::John%202:4-7

Plain text output - https://bible.gospelchurch.uk/plain?cmd=commentary:::John%202:4-7

Remarks: Web API outputs use `utf-8` encoding. You may want to decode non-English characters, e.g.:

```
import requests
r = requests.get("https://bible.gospelchurch.uk/plain?cmd=commentary:::John%202:4-7")
r.encoding = "utf-8"
print(r.text)
```

As UniqueBible App commands are consistent across different running modes that UniqueBible App supports, you can master UniqueBible APIs by mastering these commands.

This repository aims to provide detailed documentation on how to formulate UniqueBible App commands that work with UniqueBible App web APIs.

# UniqueBible App Command Format

You need to understand briefly about the format of an UniqueBible App command.

UniqueBible App commands use triple colons `:::` as separators in its built-in commands.

The first element is the command keyword, followed by optional or required parameters.

If keyword is not explicitly stated in the command, the default keyboard `bible` is used by default.

Before going into details, we would like to add a few more remarks.

# Access to Private Data

...

