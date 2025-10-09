#implementation Cesar Encryption

#this function do encryption
def encrypt()->str:
    klar_text = input ("Enter your text to encrypt: ")
    key = input("Please enter enycryption key: ")
    return "it is encrypted from " + klar_text + " with key " + key

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