def say_hi(name):
    name = input()
    if name == '':
        print("you didn't enter a name")
    else:
        print ("Hi there...")
        for letter in name:
                print(letter)
    
    say_hi(name)