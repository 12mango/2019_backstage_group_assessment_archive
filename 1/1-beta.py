import base64
import json
import qrcode
print("欢迎使用芒果的制杖工具箱")
print("现在你勉为其难的面对3个选项:")
print("1 对字符串加解密")
print("2 字典反转")
print("3 生成一个二维码（目前只保证支持windows）")
firstOption=int(input("轮到你了！输入1,2或3--->"))
if firstOption==1:
    Str={}
    print("接下来在做完选择后输入需要处理的字符串哈")
    secondOption=int(input("编码输入1，解码输入2--->"))
    if secondOption==1:
        Str=input()
        encodeStr=base64.b64encode(Str.encode('utf-8'))
        print(str(encodeStr,'utf-8'))
    elif secondOption==2:
        try:
            Str=input()
            decodeStr=base64.b64decode(Str.encode('utf-8'))
            print(str(decodeStr,'utf-8'))
        except:
            print("亲，这个是不能解码的哟。我们怀疑你在用脸滚键盘这样")
    else:
        print("哎呀，只能输1或2哟")
elif firstOption==2:
    dicBefore,dicAfter={},{}
    print('接下来请在一行中输入一个字典，我会把这个字典反转并输出好像没有什么卵用的变量类型')
    print('输入这样的字典{"a":"1","b":"1","c":"2"},可以得到{"1": ["a", "b"], "2": "c"} --->')
    try:
        dicBefore=eval(input())
        for keyBefore,valBefore in dicBefore.items():
            isNotUnique=0
            for keyAfter in dicAfter.keys():
                if valBefore==keyAfter:
                    isNotUnique=1
            if isNotUnique:
                dicAfter[valBefore]=[dicAfter[valBefore]]
                dicAfter[valBefore].append(keyBefore)
            else:
                dicAfter[valBefore]=keyBefore
        dicJsonStr=json.dumps(dicAfter)
        print(dicJsonStr)
        print(type(dicJsonStr))
        print(type(dicAfter))
    except:
       print("emmmmmm好像字典输入的格式出问题了呢")
elif firstOption==3:
    Str=input('请输入文字所在文件的路径，如E:\py\qrtxt.txt 或.\py\qrtxt.txt --->')
    fileObj=open(Str,'r',encoding='utf-8')
    content=fileObj.read()
    qrObj=qrcode.QRCode(
        version=4,
        box_size=10,
        border=2,
    )
    qrObj.add_data(content)
    qrImg=qrObj.make_image()
    qrImg.save('qrjpg.jpg')
    print("我们的二维码图片qrjpg.jpg已经dun~的生成在文件夹里了")
else:
    print("乖，请你输入1,2或3，再来一遍，好不好？")