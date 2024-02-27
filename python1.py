def my_function():
    word = str(input())
    rword = word[::-1]
    if rword == word:
        print("correct")
    else: 
        print("false")

my_function()