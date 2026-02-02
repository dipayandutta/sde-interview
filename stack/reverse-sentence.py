def reverse_sentence(string):
    st = []
    result = ""

    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])
        else:
            while st:
                result += st.pop()
            result += " "

    while st:
        result += st.pop()

    return result 

if __name__ == '__main__':
    string = "Python is Great"
    print(reverse_sentence(string))
