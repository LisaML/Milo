import string

def get_response(message):
	stopwords = ['busca','la','el','podrias','por','favor','palabra','de','definicion','definicion','que','es']
	men=message
	tokens= men.split(' ')


	#sentence cleaning

	clean_token=[]

	for token in tokens:

		#remove punctuation
		if all(char in set(string.punctuation) for char in token):
			continue

		#remove numbers
		if token.isdigit():
			continue

		#transform the token to lowcase and remove sentences
		token= token.lower()
		token = token.strip()
		#remove stopworld
		if token in stopwords:
			continue

				

		clean_token.append(token)
		re=str(clean_token)

		print(tokens)
		
    
	respuesta= ("Buscando en google la palabra:  "+ re)

	return respuesta



