#implementation Cesar Encryption


ALPHABET = [
   ' ' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

ALPHABET_LEN = len(ALPHABET)
#this function gets the key from user and convert it to integer
def getKey()->int:
    #because always what user typed in cli will be saved as string
    key = input("Please enter enycryption key: ")
    #we must change the type to integer
    key = int(key)
    return key

#this function encrypts the klar_text with the key
def encrypt()->str:
    result = ""
    #klar_text is what user typed for example jojo
    klar_text = input ("Enter your text to encrypt: ")
    key = getKey()
    for charecter in klar_text:
        #we find position of char in alphabet
        #when character == j ==> aplhabet_index = 9
        alphabet_index = ALPHABET.index(charecter)
        encryptedChar_index = (alphabet_index+key) % ALPHABET_LEN
        result += ALPHABET[encryptedChar_index]
    return result

def decode()->str:
    cypher_text = input("\n please enter Text to be DECRYPTED: ")
    key = input("Please enter DECRYPTION key: ")
    return "it is decrypted from " + cypher_text + " with key " + key




def main():
    result = ""
    print("Hello, i am cesar enc and dec app!")
    userChoice = input("If you want decrypt press d or encrypt press e")
    
    if userChoice == "e":
       result = encrypt()
    elif userChoice == "d":
        result = decode()
    else:
        result = "you must enter only e or d"
        
    print(result)

if __name__ == "__main__":
    main()