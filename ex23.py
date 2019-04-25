import sys
script, input_encoding, error = sys.argv


def main(language_file,encoding, errors):
	line = language_file.readline()
	
	if line:
		print_line(line, encoding, errors)
		return main(language_file,encoding,errors) # 重复调用本身main函数，知道if False。
	
	
def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors) # 字符（string） encode成 bytes 
	cooked_string = raw_bytes.decode(encoding, errors = errors) # bytes decode成 字符（string）
	
	print(raw_bytes, "<==>", cooked_string)
	
	
languages = open("languages.txt",encoding = "utf-8")

main(languages, input_encoding, error)
