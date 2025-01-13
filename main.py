def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	words = get_word_count(text) 
	print("--- Begin Book Report ---")
	print(f"{words} words were found in this book")
	print("")
	char_count = get_char_count(text)
	lett = get_char_sort(char_count)
	for i in range(0,len(lett)):
		print(f"The {lett[i]["letter"]} character was found {lett[i]["count"]} times.")
	print("")
	print("--- End Book Report ---")

def get_book_text(path):
	with open(path) as f:
		return f.read()

def get_word_count(text):
	words = text.split()
	words = len(words)
	return words

def get_char_count(text):
	words = text.split()
	char_count = {}
	lett = []
	#get each word into a string of characters
	for i in range(0,len(words)):
		string = words[i]
		string = string.lower()
		char = [] #individual characters of a string
		#break string into characters
		for s in string:
			char.append(s)
		#Update charcount, checking for new char, and counting each
		for c in char:
			if c.isalpha():
				if c in char_count:
					char_count[c] += 1
				else:
					char_count[c] = 1
	return char_count

def get_char_sort(char_count):
	lett = []
	#Get Dict into list of Dicts
	for key,value in char_count.items():
		lett.append({"letter":key, "count":value})
	#Sort list of Dicts
	def dict_sort(lett):
		return lett["count"]
	lett.sort(reverse=True, key=dict_sort)
	return lett

main()
