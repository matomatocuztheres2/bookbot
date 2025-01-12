def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	print(text)
	words = get_word_count(text) 
	print(f"{words} words were found in this book")

def get_book_text(path):
	with open(path) as f:
		return f.read()

def get_word_count(text):
	words = text.split()
	words = len(words)
	return words

main()
