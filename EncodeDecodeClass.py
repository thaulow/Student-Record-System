# Assessment 3 @ Noroff University College
_author_ = "Thomas Thaulow"
copyright = "Thomas Thaulow"
_email_ = "thaulow@thaulow.co"

class EncodeDecodeClass:

    # Constructor
    def __init__(self):
        pass

    # Encode
    def EncodeStudentList(self, file_name, shift):
        file = open(file_name, "r")
        lines = file.readlines()
        file2 = open("Encoded" + file_name, "w")
        temp = ''
        for line in lines:
            record = line.split(",")

            idnum = encodedecode_integer(record[0])
            fname = encode(record[1], shift)
            lname = encode(record[2], shift)
            age = encodedecode_integer(record[3])
            email = encode(record[4], shift)
            course = encode(record[5], shift)

            print(fname)

            file2.write(f"{idnum},{fname},{lname},{age},{email},{course}")
        file2.close()
        file.close()

    def DecodeStudentList(self, file_name, shift):

        file = open(file_name, "r")
        lines = file.readlines()
        file2 = open(file_name.replace('Encoded', 'Decoded'), "w")

        for line in lines:
            record = line.split(",")

            idnum = encodedecode_integer(record[0])
            fname = decode(record[1], shift)
            lname = decode(record[2], shift)
            age = encodedecode_integer(record[3])
            email = decode(record[4], shift)
            course = decode(record[5], shift)

            print(fname)

            file2.write(f"{idnum},{fname},{lname},{age},{email},{course}")
        file2.close()
        file.close()


def encode(string, shift):
    temp = ''
    for ch in string:
        if ch.isalpha():

            # for small letters
            # if unicode of 'ch' is in the range of small letters
            if ord(ch) in range(97, 123):

                # take number and add shift
                # resulting number will be the encrypted number
                # which we will change to character on line 113
                val = ord(ch) + shift

                if val > ord('z'):

                    # if the value is greater than 122
                    # we will subtract 25 from the value [ ord('z') - ord('a') ] = 25
                    val -= (ord('z') - ord('a'))
                    # the above expression can be written like this...
                    # val = val - ( ord('z') - ord('a') )

                temp = temp + chr(val)

            # for capital letters
            elif ord(ch) in range(65, 91):

                val = ord(ch) + shift
                if val > ord('Z'):
                    val -= (ord('Z') - ord('A'))

                temp = temp + chr(val)
        else:
            temp = temp + ch
    return temp


def decode(string, shift):
    temp = ''
    for ch in string:
        if ch.isalpha():
            if ord(ch) in range(97, 123):
                val = ord(ch) - shift
                if val < ord('a'):
                    val += (ord('z') - ord('a'))

                temp = temp + chr(val)

            elif ord(ch) in range(65, 91):
                val = ord(ch) - shift
                if val < ord('A'):
                    val += (ord('Z') - ord('A'))

                temp = temp + chr(val)

        else:
            temp = temp + ch

    return temp


# This method does both encoding and decoding
# since it only swaps the first and last number.

def encodedecode_integer(integer):

    text = str(integer)

    length = len(text)
    string = ''

    first = text[0]
    last = text[len(text) - 1]

    for num in text:
        if len(string) == 0:
            string += last
        elif len(string) == length - 1:
            string += first
        else:
            string += num

    return string