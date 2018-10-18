# CK2 Province Set-Upper
The Province Set-Upper is a small utility to make map-creating less of a tedious chore.

![screenshot][id]
___

### What It Does
Just feed it a list of names of counties with their baronies, and the tool will...
- Let you chose the ID, allowing piecemeal map generation at whatever pace you want, with as many provinces you want to be taken care of at a time.
- Create a `common\province_setup\00_province_setup.txt` file, with `max_settlements` having the proper value automatically assigned.
- Generate `common\landed_titles`, with automatic color shading; select one color and all the counties will be of a similar, but not the same colour.
- Setup `history\titles` files.
- Make `history\provinces`, including proper format, holdings (with tribal option) and culture/religion assignment.
- Generate and populate a `localisation` file.
- Spawn all needed flags in `gfx\flags` based on a random selection of the files found in the Flags folder.

For help, see the [wiki](https://github.com/Araxiel/CK2-Province_Set-Upper/wiki) and more specifically the [**Help**](https://github.com/Araxiel/CK2-Province_Set-Upper/wiki/Help) page
___

### About

Written for CK2 2.8.3.3 (SAHQ)

Tested with **CK2 2.8.3.3 (SAHQ)**

Using a comma-separated values table as a source, all necessary files and lines of codes are automatically create for all the provinces and baronies in the source file.

Written using [Python 3.7.0](https://www.python.org/downloads/release/python-370/)

### Other Info

This is a super leightweight little tool I wrote for myself using Python. It's not fancy, but it get's the job done with incredible efficiency.

It's use lies somewhere between doing everything manually, and something like CK2's StoryGen.

#### Planned:
  * Random Dynasty generator
  * Random History generator
  * For more [see `enhancement` label](https://github.com/Araxiel/CK2-Province_Set-Upper/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

Any help and contributions are welcome. Just open an issue or pull request or shot me a message or whatever.
___

Written by [Araxiel](https://github.com/Araxiel)

[id]: https://raw.githubusercontent.com/Araxiel/CK2-Province_Set-Upper/master/docs/menu_ss.JPG  "Screenshot"
