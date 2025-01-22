# About

This repository contains a collection of shell utilities, including small scripts, functions and aliases.

# Usage

Just clone this repo and source the utilities you want to use.

> **Warning.** The scripts were not carefully revised. So, be careful when using them.

# Utils

1. [color](./sh/color): display, convert and get ansi color codes
2. [sr](./sh/sr): search and replace content in multiple files
3. [input](./sh/input): collect user inputs from temporary files using any text editor
4. [menu](./sh/menu): generate interactive menus with pure shell
5. [gif](./sh/gif): record the screen to a `.gif` file using only basic CLI tools
6. [include](./sh/include): easily define local and global sources in your `.bashrc`
7. [is](./sh/is): a collection of bash tests
8. [mon](./sh/mon): simple CLI to manage additional monitors
9. [domain](./sh/domain): domain and TLD checks

# Criteria

The criteria I used to put something here rather than in a separated project is the following:
1. single file script with at most one or two auxiliary functions
2. it is not yaml/json configurable
3. it is not well documented
4. it has no completion script

# Dynamics

The dynamics involving the creation of this utilities is the following:
1. I need something or I have some idea
2. I sketch it, do minor tests and put in this repository
3. Anytime I want an improved or customized version of some util, I implement it in this repo, and then use the new version in some other project
4. Eventually, if I decide to really improve the utility, it will be promoted to a project, being moved to its own repository.

