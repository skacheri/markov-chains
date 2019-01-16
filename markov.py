"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_content = open(file_path).read()
    # return "Contents of your file as one long string"
    return file_content


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    word_list = text_string.split()
    
    chains = {}
   

    for index in range(len(word_list)-2):

        key = (word_list[index], word_list[index + 1])


        value = (word_list[index + 2])


        if key not in chains:
            chains[key] = [value]

        else:
            
            chains[key] += [value]


    # print(chains)

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []
    link = choice(list(chains.keys()))
    link_value  = choice(list(chains[link]))
    new_link = (link[1], link_value)
    words += link[0] + " " + link[1] + " " + link_value

    if new_link in chains.keys():
        words.append(chains[link_value])



    print(" ".join(words))


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
