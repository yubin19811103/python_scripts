# python_scripts
# 12万小文件上传方法
# 分割文件过程
1. find `pwd` -type f > ~/file
2. sed -i ‘#/www##g’ file
3. split -l 100 -d file 分割后的文件名前缀
