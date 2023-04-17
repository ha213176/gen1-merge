需要安裝
$pip install opencv

//如果遇到 ssl error 解法
$pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org  opencv 


Usage:
設定 config.txt:
first line: origin video
second line: AI 產生的影片
third line:  合併完成的影片位置與名稱
R
G
B

***               注意事項                     ***
***          路徑不能有空白、中文               ***



執行程式:
$python replace.py