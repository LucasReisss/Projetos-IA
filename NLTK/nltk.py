import nltk

texto = "Sessenta anos atrás, eu sabia tudo. Hoje sei que nada sei. A educação é a descoberta progressiva da nossa ignorância. Will Durant"
print(texto.split('.'))

frases = nltk.tokenize.sent_tokenize(texto)
print(frases)

tokens = nltk.word_tokenize(texto, language='portuguese')
print(tokens)

tags =  nltk.pos_tag(tokens)
print(tags)

entidades = nltk.chunk.ne_chunck(tags)
print(entidades)

