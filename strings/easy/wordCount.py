def word_count(s):
    count = 0
    
    for i in s.strip():
        if i==" ":
            count+=1
    return count+1


# this program use to count the word 

print(word_count("Hello"))