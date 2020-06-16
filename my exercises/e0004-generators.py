

with open("sample_file.txt") as infile:
    for line in infile:
        print(line.strip())


def gen():

    with open("sample_file.txt") as infile:
        for line in infile:
            yield line

for i in gen():
    print(i.strip())

