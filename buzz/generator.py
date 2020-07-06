import random

buzz = ('continuous testing', 'continuous integration', 'continuous development', 'continuous improvment', 'devops')
adjectives = ('complete', 'modern', 'self-services', 'integrated', 'end-to-end')
adverbs = ('remakable', 'enormously', 'substationaly', 'significantly')
verbs = ('accelerates', 'improves', 'enchance', 'revamps', 'boosts')

def sample(l, n = 1):
	result = random.sample(l,n)
	if n == 1:
		return result[0]
	return result

def generate_buzz():
	buzz_terms = sample(buzz, 2)
	phraze = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs), sample(verbs), buzz_terms[1]])
	return phraze.title()

if __name__ == "__main__":
	print(generate_buzz()) 

