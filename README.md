# XL TestView Foodcritic plugin #

## Preface ##

This plugin will parse [Foodcritic](http://www.foodcritic.io/) results files and report them in XL TestView


## CI status ##

[![Build Status][xltv-foodcritic-plugin-travis-image] ][xltv-foodcritic-plugin-travis-url]
[![Build Status][xltv-foodcritic-plugin-codacy-image] ][xltv-foodcritic-plugin-codacy-url]
[![Build Status][xltv-foodcritic-plugin-code-climate-image] ][xltv-foodcritic-plugin-code-climate-url]


[xltv-foodcritic-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xltv-foodcritic-plugin.svg?branch=master
[xltv-foodcritic-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xltv-foodcritic-plugin
[xltv-foodcritic-plugin-codacy-image]: https://api.codacy.com/project/badge/Grade/504385334e30401f94b0280234f7530c
[xltv-foodcritic-plugin-codacy-url]: https://www.codacy.com/app/rvanstone/xltv-foodcritic-plugin
[xltv-foodcritic-plugin-code-climate-image]: https://codeclimate.com/github/xebialabs-community/xltv-foodcritic-plugin/badges/gpa.svg
[xltv-foodcritic-plugin-code-climate-url]: https://codeclimate.com/github/xebialabs-community/xltv-foodcritic-plugin


## Usage ##

To use this plugin:

* Using gradle and Docker: `./gradlew runDocker`
* Using an existing XL TestView installation:
  1. Move the [jar file](https://github.com/xebialabs-community/xltv-foodcritic-plugin/releases) into the /plugins directory of your XL TestView server installation
  2. Restart XL TestView if it's already running

You will now be able to import foodcritic results. Enter the import directory as the root folder where your foodcritic files are saved. 
For example if you have multiple results such as Res1, Res2, Res3, use the directory where those folders are stored.


## References ##
+ [Foodcritic](http://www.foodcritic.io/)
+ [Foodcritic code](https://github.com/acrmp/foodcritic)


