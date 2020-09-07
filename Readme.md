## 一、MISC（杂项）
工具：binwalk 查看文件组成，-e可以分离，但分离效果不如foremost。
tips:一般下载文件后，都先用binwalk检查一下，有一次拿到一个.pcapng以为是流量分析，结果直接就是隐写。strings这个命令可以查看文件中的字符串，至少比肉眼有效，有时候效果还出奇地好。
pdfcrack爆破PDF文件密码的工具，但是不能解密。
Stegsolve.jar图片隐写工具，下载地址：http://www.caesum.com/handbook/Stegsolve.jar
zsteg 检查PNG & BMP图片隐写，https://github.com/zed-0xff/zsteg
TweakPNG 这个可以检查PNG文件是否有问题
BlindWaterMark 盲水印，理论上提取盲水印需要原图，这个就是。用Python3的脚本需要注意--oldseed参数。https://github.com/chishaxie/BlindWaterMark.git
加解密及编码工具CTFCrackTools，https://github.com/Acmesec/CTFCrackTools
压缩文件爆破工具ARCHPR 4.54速度不错
QR Research二维码识别工具，可以扫图片文件，也可以扫屏幕，非常方便。
## 二、PWN
IDA Pro 著名的反编译工具，有Free、Home、PRO三个版本，但是显然Pro最实用。
## 三、WEB
Brup Suite 神器，有企业版、专业版和社区版，社区版是免费的，但是有限制比如爆破时速度就会受限，2020.4版以后需JRE 9，Windows下安装的话会自带环境，所以几乎不影响，但是破解版不带环境就会有影响。
sqlmap SQL注入工具
## 四、REVERSE（逆向）
Easy Python Decompiler v1.3.2 Python反编译工具，可以反编译.pyc文件。
Luyten 0.5.4 Java Decompiler Gui for Procyon
## 五、CRYPTO（加密）
工具：1.RsaCtfTool https://github.com/Ganapati/RsaCtfTool.git 从名字就看得出来，解题方便，实际用来解密功能可能要差一点。
2.CTF-RSA-tool https://github.com/3summer/CTF-RSA-tool.git 跟上一个差不多。
3.ECCTOOL 椭圆密码工具
4.RSATool2 生成p、q，计算/分解N，计算d等。
5.yafu 主要用来分解质因数，分解速度比RSATool2快多了，http://factordb.com/ 这个网站不是分解而是查询，所以快。
6.Python包，RSA库，pycryptodome可以到https://pypi.org/ 下载。
https://quipqiup.com/ 一个在线词频分析网站
https://cmd5.com/ 能根据各种常见MD5加密的十六进制串找出有意义的字符串
## 六、MOBILE