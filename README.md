Igor
============
> The skype slave I wrote for @cohaesus


## Getting Started
To run igor, you'll need skypekit and its python wrappers and a valid licence PEM

## The Project

We desperately needed a bot at work to automate some of the more mundane rubbish we have to do on a day-to-day basis.

Skype is our primary point of contact for internal communication between different teams (Some of us tele-work and we have an offshore team as well)

So it seemed to make sense to write a bot to consume some of our common tasks - Igor was born.


### Overview
Igor consists of a main skypekit wrapper 'igor.py' a background thread 'eliza' and a number of small non-descript task scripts.

A lot of inspiration was taken from hubot but we didnt feel at the time that javascript was the correct way to go about it.

I'll expand this a lot more as time passes, but I need to get this release out!

Igor is designed to run in an isolated virtualenv, the requirements are listed in requirements.txt for easy pip installation.

## Contributing
In lieu of a formal styleguide, take care to maintain the existing coding style. Adding unit tests for any existing, new or changed functionality is strongly encouraged!
Lint and test your code using pylint, pyflakes etc.

## Changelog
* 02/05/2013 - Initial public release

## Contributers
* Nick Pack
* Daniel Portella
* Graeme Maciver

## Licence
Copyright (c) 2013 Nick Pack
Licensed under the MIT license.

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/nickpack/Igor/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

