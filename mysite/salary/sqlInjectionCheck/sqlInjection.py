import sys


def main(un, p):
    username, password = sql_injection(un, p)
    return username, password


def sql_injection(username, password):
    print("before : " + username)
    tempWord = username
    tempWord = remove_problem_word(tempWord)
    tempWord = " ".join(tempWord.split())
    if tempWord.__contains__("'"):
        tempWord = delete_char(tempWord, "'")
        tempWord = " ".join(tempWord.split())  # remove the extra spaces
    if tempWord.__contains__("--"):
        w = ""
        x = 0
        while x < len(tempWord)-1:
            if tempWord[x] == "-" and tempWord[x+1] == "-":
                w = w + add_char_for_prevent(tempWord, "--") + " "
            x = x + 1
        tempWord = w
    if tempWord.__contains__("union"):
        tempWord = clean_problem_words(tempWord, "union")
        tempWord = " ".join(tempWord.split())
    if tempWord.__contains__("distinct"):
        tempWord = clean_problem_words(tempWord, "distinct")
        tempWord = " ".join(tempWord.split())
    print("after : " + tempWord)

    print("before : " + password)
    tempPass = password
    tempPass = remove_problem_word(tempPass)
    tempPass = " ".join(tempPass.split())
    if tempPass.__contains__("'"):
        tempPass = delete_char(tempPass, "'")
        tempPass = " ".join(tempPass.split())
    if tempPass.__contains__("--"):
        w = ""
        x = 0
        while x < len(tempPass)-1:
            if tempPass[x] == "-" and tempPass[x + 1] == "-":
                w = w + add_char_for_prevent(tempPass, "--") + " "
            x = x + 1
        tempPass = w
    if tempPass.__contains__("union"):
        tempPass = clean_problem_words(tempPass, "union")
        tempPass = " ".join(tempPass.split())
    if tempPass.__contains__("distinct"):
        tempPass = clean_problem_words(tempPass, "distinct")
        tempPass = " ".join(tempPass.split())
    print("after : " + tempPass)

    username = tempWord
    password = tempPass
    return username, password


def delete_char(word, char):
    # function that get word and char for deleting
    # and return word without the char.
    word = word.replace(char, '')
    return word


def clean_problem_words(word, clean):
    # function that get word and problem word for deleting
    # and return word without the problem word.
    word = word.replace(clean, '').lstrip()
    return word


def substring_after(word, char):
    return word.partition(char)[2]


def remove_problem_word(prob_word):
    # function for check if has problem word from list "ProblemWord"
    # that can to show on try to sql injection
    try:
        temp = open("D:\\Salary\\mysite\\salary\\sqlInjectionCheck\\ProblemWords.txt")
    except OSError:
        print("Could not open/read file")
        sys.exit()
    words = temp.read().splitlines()  # read from file with char \n
    prob_word = prob_word  # check word with uppercase
    for i in words:
        while i in prob_word:
            prob_word = clean_problem_words(prob_word, i)
        up_temp = i.upper()  # check case of capital letter in file ProblemWords
        while up_temp in prob_word:
            prob_word = clean_problem_words(prob_word, up_temp)
    return prob_word


def add_char_for_prevent(word, char):
    # function that get problem char in the word
    # and put "/" between for prevent try to hack
    i = 0
    beforeChar = ""
    while word[i] != char[0]:
        beforeChar = beforeChar + word[i]
        i = i + 1
    for j in range(len(char)):
        beforeChar = beforeChar + char[j] + "/"
        j = j + 1
        i = i + 1
    while i < len(word):
        beforeChar = beforeChar + word[i]
        i = i + 1
    return beforeChar


if __name__ == "__main__":
    # for example we call to function with input
    u = input("Enter Username: ")
    p = input("Enter Password: ")
    main(u, p)
