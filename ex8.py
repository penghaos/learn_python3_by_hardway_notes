# 格式化字符的用法 多参数写法"{}" .format(arg1,arg2,arg3,arg4)

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))#.format(arg1,arg2,arg3,arg4) 多个变量的写法
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
	
))
