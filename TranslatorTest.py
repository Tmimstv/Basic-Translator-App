from translate import Translator

translator = Translator(to_lang="zh")

toTranslate = input("What would you like me to translate?: ")
print(translator.translate(toTranslate))
