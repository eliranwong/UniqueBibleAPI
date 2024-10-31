# Unique Bible App API

This repository is created for documentating the web API references of the [UniqueBible App](https://github.com/eliranwong/UniqueBible).

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

The keyword tells UnqiueBible App what kind of bible data users want to retrieve.

If keyword is not explicitly stated in the command, the default keyboard `bible` is used by default.

Before going into details, we would like to add a few more remarks.

# Parameters Could be Optional or Required

Parameters, that follow command keywords, could be optional or required.

In command example above, `commentary:::John 2:4-7`, `commentary` is the keyword that takes `John 2:4-7` as its parameter.

You can also add an optional parameter to specify the commentary from which data is retrieved.

For example, in `commentary:::CBSC:::John 2:4-7`, `CBSC` is an abbreviation for `Cambridge Bible for Schools and Colleges (Cambridge) [57 vol.]`. The command `commentary:::CBSC:::John 2:4-7` retrieves commentaries of John 2:4-7 specifically in `Cambridge Bible for Schools and Colleges (Cambridge) [57 vol.]`.

In our documentation, we will indicate which parameters are optional.

# Unique Web APIs Commands

There are two commands that are supported ONLY in web APIs, not in other UniqueBible App running modes:

`.resources`

This command retrieves information about available resources loaded in the web server.

Read more at https://github.com/eliranwong/UniqueBibleAPI/blob/main/.resources.md

`.suggestions`

This command retrieves nested suggestions of UniqueBible App commands.

Read more at https://github.com/eliranwong/UniqueBibleAPI/blob/main/.suggestions.md

# Available Web API Endpoints

The latest UniqueBible App web APIs support three formats in outputs via three different endpoints:

`/html` raw html output

`/json` json output

`/plain` plain text output

# Request Format

Basic web API request follows the following format:

UniqueBible App http-server address + endpoint + UniqueBible App command

In example `https://bible.gospelchurch.uk/json?cmd=commentary:::John%202:4-7`

`https://bible.gospelchurch.uk` is UniqueBible App http-server address

`/json` is the endpoint

`commentary:::John%202:4-7` is the command which follows the url parameter `cmd=`

# Access to Private Data

UniqueBible App http-server offers access to private data that are not made available to the public.

This means UniqueBible App http-server can serve both public and private data.

Organisations may find this feature useful, if they want to open the private data access to a specific group of people.

To configure UniqueBible App http-server access to private data, specify the value of `webPrivateHomePage` in UniqueBible App `config.py` as the private access key.  You also need to specify the private data location in the value of `marvelDataPrivate` in UniqueBible App `config.py`.

The web API request, for accessing private data, follows the following format:

UniqueBible App http-server address + endpoint + UniqueBible App command + private key

You can use `private=` to include a the private key optionally in the url request.

For example, if you have `xxxxxxxxxxxxxxx` as your private key, formulate the request as `https://bible.gospelchurch.uk/json?cmd=.resources&private=xxxxxxxxxxxxxxx`.  The output should be different from the public request, without specifying a private key `https://bible.gospelchurch.uk/json?cmd=.resources`.

# Documentation Structure

In this repository, documentation on each command keyword is written in a single markdown file.

For example `bible.md` documents the UniqueBible App command that uses the keyword `bible`, as we use command keywords to name the files.

In each of these files, you will find description and examples of the keyword and its parameters.

In addition, we base our examples on the data retrieved from https://bible.gospelchurch.uk to demonstrate the use of the latest available web APIs, as we have the latest UniqueBible App codes running the web server to serve the site.

# Progress

We will regularly add or update the documenation in this repository.

The writings are in progress ...
