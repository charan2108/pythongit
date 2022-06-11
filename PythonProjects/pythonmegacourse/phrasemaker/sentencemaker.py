def sentence_maker(phrase):
    interrogatives = ('how', 'what', 'why')
    capitalized = phrase.capitalize()
    if phrase.startswith(capitalized):
        return "{}".format(capitalized)
    else:
        return "{}".format(capitalized)
# empty list
results = []
# condition
while True:
    user_input = input("enter something")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
print(results)        