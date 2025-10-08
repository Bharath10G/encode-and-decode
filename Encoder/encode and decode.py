import string
from flask import Flask,render_template,request,jsonify

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/encode',methods=['POST'])
def encode():
    data = request.get_json()
    sentence = data.get('text')
    letters=string.ascii_letters
    numbers=string.digits
    spchar=string.punctuation
    sentence=sentence.split(" ")
    a=[]
    for n in sentence:
        s=""
        for i in n:
            if i.isalnum():
                if i.isdigit():
                    binary=bin(numbers.index(i))[2:]
                    if len(binary)<4:
                        binary=(4-len(binary))*"0"+binary
                    binary=binary.replace("1","5")
                    binary1=binary.replace("0","4")
                else:
                    binary=bin(letters.index(i))[2:]
                    if len(binary)<6:
                        binary=(6-len(binary))*'0'+binary
                    binary=binary.replace('1','2')
                    binary1=binary.replace('0','1')
            else:
                binary=bin(spchar.index(i))[2:]
                if len(binary)<6:
                    binary=(6-len(binary))*'0'+binary
                binary=binary.replace('1','7')
                binary1=binary.replace('0','6')
            s+=binary1
        a.append(s)
    msg="3".join(a)
    return jsonify({
        'msg': msg
    })

@app.route('/decode',methods=['POST'])
def decode():
    data = request.get_json()
    a = data.get('text')
    arr=a.split("3")
    l=string.ascii_letters
    sp=string.punctuation
    for i in range(len(arr)):
        letters=[]
        while len(arr[i])>0:
            if arr[i][0]=="1" or arr[i][0]=="2":
                s=arr[i][:6].replace("1","0")
                s=s.replace("2","1")
                s=int(s,2)
                letters.append(l[s])
                arr[i]=arr[i][6:]
            elif arr[i][0]=="6" or arr[i][0]=="7":
                s=arr[i][:6].replace("6","0")
                s=s.replace("7","1")
                s=int(s,2)
                letters.append(sp[s])
                arr[i]=arr[i][6:]
            else:
                s=arr[i][:4].replace("4","0")
                s=s.replace("5","1")
                s=int(s,2)
                letters.append(s)
                arr[i]=arr[i][4:]
        arr[i]="".join(map(str,letters))
    msg = " ".join(arr)
    return jsonify({
        'msg': msg
    })



if __name__ == "__main__":
    app.run(debug=True)