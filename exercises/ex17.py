from sys import argv

script, from_file, to_file = argv

# we could do these two on one line, how?
indata = open(from_file).read()

out_file = open(to_file, 'w').write(indata)

out_file.close()
in_file.close()