class vernamEncrypt():
    def __init__(self, key, message):
        if len(key) < len(message):
            raise Exception("The length of the key cannot be shorter than the message.")
        else:
           encryptedMessage = self.binaryValueGen((list(key)), (list(message)))
           print(encryptedMessage)

    def mapToAscii(self, charList):
        newList = []
        for i in charList:
            mappedAsciiValue = (i % 52)
            if mappedAsciiValue <= 26:
                mappedAsciiValue += 65
            else:
                mappedAsciiValue -= 26
                mappedAsciiValue += 96
            newList.append(mappedAsciiValue)
        encryptedMessage = "".join([str(chr(char)) for char in newList])
        return encryptedMessage

    def xorValues(self, keyList, messageList):
        encryptedCharList = []
        for i in range(0, len(messageList)):
            key, message = int(keyList[i], 2), int(messageList[i], 2)
            encryptedChar = key ^ message
            encryptedCharList.append(encryptedChar)
        return self.mapToAscii(encryptedCharList)

            
    def binaryValueGen(self, key, message):
        keyBinList, messageBinList = [], []
        for i in range(len(message)):
            keyBin, messageBin = (bin(ord(key[i]))), (bin(ord(message[i])))
            keyBinList.append(keyBin[:1] + keyBin[2:])
            messageBinList.append(messageBin[:1] + messageBin[2:])
        return self.xorValues(keyBinList, messageBinList)
            



while True:
    key = input("Please enter key: ")
    message = input("Please enter message: ")
    vernamEncrypt(key, message)

