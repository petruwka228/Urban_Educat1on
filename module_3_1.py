calls = 0
def count_calls():
    global calls
    calls+=1
def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a
def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
    return False



