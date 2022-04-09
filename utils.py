"""
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

I literally do not care about this file, steal it as many times as you want.
"""


class Option:
    def __init__(self, name, option_id):
        self.name = name     # what the option will be named to the user
        self.id = option_id  # actually figure out what the user picked precisely.. hopefully


def multiple_options(notice: str, options: list[Option], display_id=False):
    print(notice + '\n')
    for index, x in enumerate(options):
        option_output = x.name
        if display_id:
            option_output += f" ({x.id})"
        print(f"{index}: {option_output}")  # list all options to the user

    option = None
    while not option:
        index = input("\nPlease pick an option: ")
        if not index.isdigit():
            print("That's, uh, not a number.")
        else:
            try:
                index = int(index)  # turn index to an int
                option = options[index]
                # try getting the option the user asked for
            except IndexError:
                print("Sorry, that's not a valid option.\n")  # that wasn't an option.
    return option