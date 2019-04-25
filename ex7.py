# 格式化字符的用法 "strings {}".format("words")

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow')) # 格式化字符串的第二种用法
print ("And everywhere that Mary went.")
print("." * 10) # what'd that do? 分隔符

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens

print(end1 + end2 + end3 + end4 + end5 + end6, end =' ') #print 是个函数，end=' '表示输出语句结尾是空格
print(end7 + end8 + end10 + end11 + end12)
