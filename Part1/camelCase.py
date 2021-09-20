"""
Write a program that turns a sentence into camel case.
The first word is lowercase, the rest of the words have their initial letter capitalized,
and all of the words are joined together.
"""

from re import sub
# import regEx's substring method
import re


def to_camel_case(user_input):
    try:
        # check if sentence starts with a number .replace(" ", "")
        user_input = sub(r"(_|-)+", " ", user_input).title()
        # removing special characters from string
        new_string = ''.join(filter(str.isalnum, user_input))
        return(new_string[0].lower() + new_string[1:])
    except Exception:
        return 'Error,enter a correct sentence'


def main():
    sentence = input('Enter a sentence: ').lower()
    camelCased = to_camel_case(sentence)
    print(camelCased)


# **Note**
# '__main__' = scope in which top-level code executes
# A  __name__,
if __name__ == '__main__':
    main()  # only run if script is executing when invoked directly
# else:
    # __name__ = imported module
    # print('script is getting imported by other module')
