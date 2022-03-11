"""
    Documentação - https://spacy.io/api/token

    Atributos do objeto token

    text = O texto do token
    head = Qual é o token "pai"
    i = Qual posição o token está
    lemma_ = Token lemmatizado
    lower_ = Token em minusculo
    shape_ = Formato do texto

    like_num = se representa um número
    is_alpha = se é alfanúmerico
    is_digit = se é número
    is_upper = se está em maíusculo
    is_punct = se é um ponto

"""
import spacy

nlp = spacy.load("pt_core_news_sm")

doc = nlp("João pulou o rio sujo dez vezes.")

for token in doc:
    print(token.text, "|", token.i, "|", token.lemma_, "|", token.is_alpha, "|", token.is_punct, "|", token.is_digit, "|", token.like_num)