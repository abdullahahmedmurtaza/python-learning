def locate_cards(cards, query):
    position = 0
    while True:
        if(cards[position] == query):
            return position;
        position+=1
        if(position == len(cards)-1):
            return -1
# Always create test cases in 1-3 minutes, not 8 but 4 useful test cases are enough and label them with comments
tests = []
test1 = {
    "input" : {
        "cards" : [1,2,3,7,12,33,21,6],
        "query" : 7
    },
    "output" : 3 
}


test2 = {
    "input" : {
        "cards" : [1,2,12,12,44,32,1,6,88],
        "query" : 7
    },
    "output" : 3 
}

tests.append(test1)
tests.append(test2)

for test in tests:
        if(locate_cards(**test["input"]) == test["output"]):
            print(f"Test case passed, Element found at position {locate_cards(**test["input"])}")
        else:
            print(f"Test case failed with exit code {locate_cards(**test["input"])}")
    