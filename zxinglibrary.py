import zxing

#creating a BarcodeReader object
reader = zxing.BarCodeReader()

#decoding the image passed to the method of the object
mytext = reader.decode("sample2.jpg")

#converting the BarCodeReader object to a string object
mystring= str(mytext)
#we will create a list object from the split method
mystring= mystring.strip("BarCode('")
mystring= mystring.split("', '",3)

encoded_text = mystring[0]
barcode_type = mystring[2]
text_type = mystring[3]

#function to process the string to get the type of text that was encoded
def ActualText(string):
    
    mytext=""
    for i in string:
        if i != "'":
        
    
            mytext += i

        else:
            break

    return mytext

text_type2 = ActualText(text_type)

print(encoded_text + "\nType of Barcode : {0} \nType of encoded text : {1}".format(barcode_type,text_type2) )
