def sentence_freq(text):
    formatted_text = text.replace('!', '.').replace('?', '.')
    sentences = [sentence.strip() for sentence in formatted_text.split('.') if sentence.strip()]
    
    freq_map = {}
    for sentence in sentences:
        freq_map[sentence] = freq_map.get(sentence, 0) + 1
    
    return freq_map

text = input("please enter your text: ")
print(sentence_freq(text))
