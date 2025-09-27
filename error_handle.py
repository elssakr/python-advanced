
try:
    result = 10/0
except ZeroDivisionError:
    print("error,tried to divide 0")

text = "This is not a number"

try:
    text_into_int = int(text)
except Exception as e:
    print("an error uccure while persing the date:", e)


try:
    result = 10/2
except ZeroDivisionError:
    print("error,tried to divide by 0")
else:
    print("divided succsesfully: ", result)