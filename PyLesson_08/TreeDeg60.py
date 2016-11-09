word = input("Please enter a word: ")
start = 0
stop = len(word)-1
def tree(word, start, stop):
    if start <= stop:
        start += 1
        return "{: >10}".format(word[0:start]) +"\n" + tree(word, start, stop)
    else:
        return ""
print(tree(word, start, stop))


        
    
