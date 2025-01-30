ConvertFrom=input("Enter the unit you are converting from: ")
ConvertTo=input("Enter the unit you are converting to: ")
Temp=float(input(f"Enter the temperature in {ConvertFrom}: "))
if ConvertTo=="Fahrenheit":
    if ConvertFrom=="Celsius":
        TempConvert=Temp*1.8+32
    elif ConvertFrom=="Kelvin":
        TempConvert=(Temp-273.15)*1.8+32
    else: TempConvert=Temp
elif ConvertTo=="Celsius":
    if ConvertFrom=="Fahrenheit":
        TempConvert=(Temp-32)*(5/9)
    elif ConvertFrom=="Kelvin":
        TempConvert=Temp+273.15
    else: TempConvert=Temp
else:
    if ConvertFrom=="Fahrenheit":
        TempConvert=(Temp-32)*(5/9)+273.15
    elif ConvertFrom=="Celsius":
        TempConvert=Temp-273.15
    else: TempConvert=Temp
print(f"That is {TempConvert:.1f} degrees {ConvertTo}.")
