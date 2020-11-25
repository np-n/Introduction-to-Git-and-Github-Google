def celsius_fahrenheit_converter(fahrenheit):
	celsius = (fahrenheit - 32)*(5/9)
	return celsius
def main():
	fahrenheit = input("Enter degree in fahrenheit : ")
	fahrenheit = int(fahrenheit)
	celsius = celsius_fahrenheit_converter(fahrenheit)
	print(f'{fahrenheit} degree fahrenheit is equivalent to {celsius} degree celsius')






if __name__ == "__main__":
	main()
