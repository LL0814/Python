# _*_ coding:utf-8 _*_
def encrypt(text, offset):
    #字母ascll码 以offset值 增减 
    return getOffsetResut(text, offset, 'encrypt')

def decrypt(encrypted_text, offset):
    #字母ascll码 以offset值 增减 
    return getOffsetResut(encrypted_text, offset, 'decrypt')
    
def getOffsetResut(text, offset, type):
    if type == 'decrypt':
        #如果是解密操作 offset取反
        offset = -offset
    space = ' '
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    upers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowersList = list(lowers)
    uperList = list(upers)
    result = ''
    for i in text:
        if i != space:
            if i in lowersList:
                index = lowersList.index(i)
                offsetIndex = index
                modValue = divmod(offset, 26)
                if modValue[1] == 0:
                    pass
                else:
                    offsetIndex = index + modValue[1]
                    if offsetIndex > 25:
                        offsetIndex = offsetIndex - 26
                    elif offsetIndex < 0:
                        offsetIndex = offsetIndex + 26
                    else:
                        pass
                i = lowersList[offsetIndex]
            elif i in uperList:
                index = uperList.index(i)
                offsetIndex = index
                modValue = divmod(offset, 26)
                if modValue[1] == 0:
                    pass
                else:
                    offsetIndex = index + modValue[1]
                    if offsetIndex > 25:
                        offsetIndex = offsetIndex - 26
                    elif offsetIndex < 0:
                        offsetIndex = offsetIndex + 26
                    else:
                        pass
                i = uperList[offsetIndex]
        result += i
    return result

def find_encryption_offsets(encrypted_text):
    offsetResult = []
    matchKeywords = serializeKeyWords() #获取words.txt文本内容 转换成列表
    encryptedTexts = encrypted_text.split(' ') #获取加密文本内容 转换成列表
    firstKeyword = encryptedTexts[0] #获取加密文本内容列表第一个元素
    for tmpOffset in range(1, 26): #循环25个偏移量
        firstDecryptKeyword = decrypt(firstKeyword, tmpOffset) #获取加密文本内容列表第一个元素的解密文本
        index = matchFirstKeyword(firstDecryptKeyword, matchKeywords) #查找第一个元素的解密文本在words文本列表中的索引
        if index != None:
            if matchAllKeywords(encryptedTexts, tmpOffset, matchKeywords): #匹配加密文本的全部内容
                offsetResult.append(tmpOffset) #如果全部匹配成功，偏移量+1
    return tuple(offsetResult);

def serializeKeyWords():
    #序列化words.txt文本内容 转换成列表
    with open('words.txt', 'r') as keywords:
        matchKeywords = keywords.read().splitlines()
    return matchKeywords

def matchFirstKeyword(keyword, matchKeywords):
    #匹配解密内容的第一个单词 匹配成功 返回该单词在words.txt序列化的列表中的位置 否则返回none
    return matchKeywords.index(keyword) if keyword in matchKeywords else None

def matchAllKeywords(keywords, offset, matchKeywords):
    #匹配解密内容的所有单词 全部匹配成功 返回true 否则返回false
    for keyword in keywords:
        keyword = decrypt(keyword, offset)
        if keyword not in matchKeywords:
            return False
    return True


if __name__==  '__main__':
    while True:
        actionType = raw_input('选择类型： 1（加密）、2（解密）、3（自动解密）4(退出): ')
        #try:
        if actionType == '1':
            encryptText = raw_input('加密内容: ')
            offset = raw_input('offset: ')
            result = encrypt(encryptText, int(offset))
            print('Encrypt Result: ')
            print(result)
        elif actionType == '2':
            decryptText = raw_input('解密内容: ')
            offset = raw_input('offset: ')
            result = decrypt(decryptText, int(offset))
            print('Decrypt Result:')
            print(result)
        elif actionType == '3':
            autodecryptText = raw_input('自动解密内容: ')
            result = find_encryption_offsets(autodecryptText)
            print('Encrypt Result:')
            print(result)
        elif actionType == '4':
            quit()
        else:
            pass
        #except Exception as e:
         #  print(e)
            
    # result1 = encrypt('you will aways remember this as the day', 7)
    # result2 = decrypt('a bmkl kso lzw sv sfv lzgmyzl al dggcwv xmf', 18)
    # result3 = find_encryption_offsets('nmd')
    # result4 = find_encryption_offsets('iynjo fuhsudj ev jxu yj mehai qbb jxu jycu')
    # print(result1)
    # print(result2)
    # print(result3)
    # print(result4)