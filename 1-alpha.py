import base64
import json
import qrcode
x,y,n,st,dic,vdic=0,0,0,'',{},{}
print("欢迎使用芒果的制杖工具箱")
print("现在你勉为其难的面对3个选项:")
print("1 对字符串加解密")
print("2 字典反转")
print("3 生成一个二维码")
x=int(input("轮到你了！输入1,2或3--->"))
if x==1:
    y=int(input("编码输入1，解码输入2--->"))
    if y==1:
        st=input()
        encodestr=base64.b64encode(st.encode('utf-8'))
        print(str(encodestr,'utf-8'))
    elif y==2:
        try:
            st=input()
            decodestr=base64.b64decode(st.encode('utf-8'))
            print(str(decodestr,'utf-8'))
        except:
            print("你输入的字符串无法解码")
    else:
        print("这是不行的")

elif x==2:
    print("接下来请在一行中输入字典，我会把这个字典反转并输出好像没有什么卵用的变量类型--->")
    try:
        dic=eval(input())
        for key,val in dic.items():
            flag=0
            for k in vdic.keys():
                if val==k:
                    flag=1
            if flag:
                vdic[val].append(key)
            else:
                vdic[val]=[key]
        jsondic=json.dumps(vdic)
        print(jsondic)
        print(type(jsondic))
        print(type(vdic))
    except:
       print("格式不对吧")
elif x==3:
    st=input("请输入文件名xxx.txt中的xxx-->")+".txt"
    f=open(st,'r',encoding='utf-8')
    cont=f.read()
    qr=qrcode.QRCode(
        version=4,
        box_size=10,
        border=2,
    )
    qr.add_data(cont)
    img=qr.make_image()
    img.save('qrjpg.jpg')
    print("你提供的文本已生成名为qrjpg.jpg的二维码图片")
else:
    print("这是不行的")
