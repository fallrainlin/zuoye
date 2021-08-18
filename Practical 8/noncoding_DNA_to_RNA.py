name = input("请输入基因序列的名称：")
file = open('noncoding_function.fa',"r")
text = file.readlines()

for value in text:
    if name in value:
        with open("new_file.fa","w") as fe:
            fe.write(value)
            fe.close()
file.close()
