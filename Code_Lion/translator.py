from googletrans import Translator

translator = Translator()

sentence = input("번역할 문장 : ")


detected = translator.detect(sentence)
result = translator.translate(sentence, 'es')

print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)