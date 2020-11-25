def  fahrenheit_kelvin_converter(fahrenheit):
	kelvin = ((fahrenheit-32)*(5/9))+273
	return kelvin


fahrenheit = int(input('Enter temperature in fahrenheit :'))
kelvin = fahrenheit_kelvin_converter(fahrenheit)
print(f'{fahrenheit} degree fahrenheit is equal to {kelvin} degree kelvin')
