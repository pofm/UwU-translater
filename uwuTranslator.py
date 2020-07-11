def translation(sentence):
    translate = ""
    for letter in sentence:
        if letter.upper() in "LR":
            if letter.isupper():
                translate = translate + "W"
            else:
                translate = translate + "w"
        else:
            translate = translate + letter
    if len(sentence):
        translate = translate + " uwu."
    return translate

print(translation(input("I wiww twanswate youw sentence \"nyotice buwge UWU\":")))