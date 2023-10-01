meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print("OK Boomer here's your answer to the question ")
    print(word + ": " + meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("kelimenin tanımı kayıtlı değil")
