# Python异常处理

## 什么是异常

 程序语言定义了这么多的规则，如果你希望程序能正常运行起来并且达到你的目标，就需要了解、遵守和按规则使用它。如果你不这么做，会如何呢？程序会执行不下去，报错。这些错误分为两种：
 
一种是语法错误，比如关键字拼写出错、没有正确缩进。Python解析的时候就会报错。会提示`“SyntaxError: invalid syntax”`，这个没什么好说的，必须改对程序才能执行。
    
另一种是语法没错，但运行时候才发现，比如该传的参数没有传，使用了没有定义的变量等等，这些统称为异常。

### SyntaxError : Python的语法错误

```python
>>> print "hello world." 
  File "<stdin>", line 1
    print "hello world."
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello world.")?
```

### AssertionError : 断言语句(assert)失败

linux
windows
macos

