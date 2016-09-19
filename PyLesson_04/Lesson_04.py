print("{:-<10} {:-<10}".format("test", "newTest"))
print("{:10.2f}".format(13216.132165))
print("{:-<10}".format("test"))


def printf(word, number):
    print("{:-<10}\t{:10.2f}". format(word, number))

word = "blah"
number = 12345.678

printf(word, number)

print("{:10.3f}".format(7837234.928347))
