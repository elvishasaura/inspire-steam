#name : Elvis Mutuma
#Date : 12/02/2026
#string formatting

#get string length
sentence = "I watch anime"

string_length = len(sentence)

print(f"The length is: {string_length}")

#spliting a string
sentence_2= "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is:", split[1])


#make everything CAPS
mpesa_code = "ubg6767dsfgh"

capitalized = mpesa_code.upper()

print(f"New mpesa code:{capitalized}")
mpesa_code = "UBG6767DSFGH"

Lower = mpesa_code.lower()

print (f"New mpesa code:{Lower}")

#Replacing characters in a string

balance = "100 kes"
amount_added = "50 kes"

cleaned_balance = balance.replace("kes", "")

print(f"Cleaned balance:{cleaned_balance}")

cleaned_amount_added = amount_added.replace("kes", "")

print(f"cleaned_amount_balance:{cleaned_amount_added}")

#Elvis' answer
new_balance = int(cleaned_balance) + int(cleaned_amount_added)
print(f"the new balance is:{new_balance}")

sentence_3 = "you have received 40kes from Kiogora"
split = sentence_3.split(" ")
print(f"New mpesa text is:" , split[3],)

balance = "12.02kes"
amount_added = "40kes"

cleaned_balance = balance.replace("kes", "")
print(f"cleaned_balance is: {cleaned_balance}")

cleaned_amount_added = amount_added.replace("kes", "")
print(f"cleaned_amount_added is: {cleaned_amount_added}")

new_balance = float(cleaned_balance) + int(cleaned_amount_added)
print(f"new_balance is: {new_balance}")