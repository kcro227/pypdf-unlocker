import tkinter
from tkinter import filedialog
import pikepdf
import os


# Windows
print("Version : V1.0")
print('请选择PDF文件。 Please choose PDF.\n')

# 打开一个文件选择对话框
root = tkinter.Tk()
root.withdraw() # 隐藏多余的窗口

# 选择文件路径
filePath = filedialog.askopenfilename()


# 获取所选文件的文件名
fileNameWithExtension = os.path.basename(filePath)
fileNameWithoutExtension  = os.path.splitext(fileNameWithExtension)[0]

# 用pikepdf破解，并以unlocked.pdf保存在当前程序所在路径下
pdf = pikepdf.open(filePath)

# 解密完成，选择保存路径
folder_selected = filedialog.askdirectory()

# 打印用户选择的文件夹路径

newFileName = folder_selected + "/"+ fileNameWithoutExtension + '_unloked.pdf'
# 保存文件
pdf.save(newFileName)
print('解密完成。 Unloked done.')
