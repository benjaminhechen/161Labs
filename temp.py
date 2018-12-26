f = open("quotes.txt", "r")
lines = f.readlines()
# strip() removes the newline character: "\n"
a_line = lines[1].strip()

print(a_line[:-1])

print(a_line[:-1] + "!")
f.close()