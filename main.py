# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Url list initialization
Input = ["https://www.isb.edu", "www.google.com", "http://cyware.com",
         "https://www.gst.in", "https://www.coursera.org",
         "https://www.create.net", "https://www.ontariocolleges.ca"]
# # Using readlines()
# file1 = open('test.txt', 'r')
# Lines = file1.readlines()
#
# count = 0
# # Strips the newline character
# for line in Lines:
#     count += 1
#     print("Line{}: {}".format(count, line.strip()))

# Function to sort in tld order
def tld(Input):
    return Input.split('.')[-1]


# Internal function for reversed
def internal(string):
    return list(reversed(string.split('.')))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fn = 'uni-url.txt'
    sorted_fn = 'uni-url-sorted.txt'

    with open(fn, 'r') as first_file:
        rows = first_file.readlines()
        sorted_rows = sorted(rows, key=lambda x: x.split('.')[-1])
        with open(sorted_fn, 'w') as second_file:
            for row in sorted_rows:
                second_file.write(row)

    # print_hi('PyCharm')
    # Using sorted and calling function, key: tld|internal
    # Output = sorted(Input, key=tld)
    # Output = sorted(Input, key=lambda x: x.split('.')[-1])

    # Printing output
    # print("Initial list is :")
    # print(Input)
    # print("sorted list according to TLD is")
    # print(Output)