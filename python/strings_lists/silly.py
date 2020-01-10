#! /usr/bin/python3

import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.
    while index < len(template):
        if template[index:].find("{{noun}}") == 0:
            output.append(random.choice(nouns))
            index += len("{{noun}}")
        elif template[index:].find("{{verb}}") == 0:
            output.append(random.choice(verbs))
            index += len("{{verb}}")
        else:
            output.append(template[index])
            index += 1

    # After the loop has finished, join the output and return it.
    return "".join(output)


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))

