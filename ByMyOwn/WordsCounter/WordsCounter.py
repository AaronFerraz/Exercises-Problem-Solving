text = "Lorem ipsum dolor sit amet, consectetur adipiscing " \
"elit. Nullam euismod, nisl eget ultricies aliquam, nunc nisl " \
"aliquet nunc, quis aliquam nisl nunc eu nisl. Nullam euismod, " \
"nisl eget ultricies aliquam, nunc nisl aliquet nunc, quis aliquam " \
"nisl nunc eu nisl. Lorem ipsum dolor sit amet, consectetur adipiscing " \
"elit. Nullam euismod, nisl eget ultricies aliquam, nunc nisl aliquet nunc, " \
"quis aliquam nisl nunc eu nisl. Nullam euismod, nisl eget ultricies aliquam, " \
"nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl."

dic_palavras = { }
text_bruto = text.split()
listaStrings = [palavra.strip(".!,;!?").lower() for palavra in text_bruto if palavra]

for palavra in listaStrings:
    dic_palavras[palavra] = dic_palavras.get(palavra, 0) + 1 

print(dic_palavras)