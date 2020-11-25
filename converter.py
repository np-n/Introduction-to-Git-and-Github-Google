
def  fahrenheit_kelvin_converter(fahrenheit):
	kelvin = ((fahrenheit-32)*(5/9))+273
	return kelvin




def celsius_fahrenheit_converter(fahrenheit):
	celsius = (fahrenheit - 32)*(5/9)
	return celsius
def main():
	fahrenheit = input("Enter degree in fahrenheit : ")
	fahrenheit = int(fahrenheit)
	celsius = celsius_fahrenheit_converter(fahrenheit)
	print(f'{fahrenheit} degree fahrenheit is equivalent to {celsius} degree celsius')

	fahrenheit = int(input('Enter temperature in fahrenheit :'))
	kelvin = fahrenheit_kelvin_converter(fahrenheit)
	print(f'{fahrenheit} degree fahrenheit is equal to {kelvin} degree kelvin')






if __name__ == "__main__":
	main()
