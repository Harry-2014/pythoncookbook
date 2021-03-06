'''
4.13 创建数据处理管道
问题
你想以数据管道(类似Unix 管道) 的方式迭代处理数据。比如，你有个大量的数据
需要处理，但是不能将它们一次性放入内存中。
解决方案
生成器函数是一个实现管道机制的好办法
为了处理这些文件，你可以定义一个由多个执行特定任务独立任务的简单生成器
函数组成的容器

'''
'''
讨论
以管道方式处理数据可以用来解决各类其他问题，包括解析，读取实时数据，定时
轮询等。
为了理解上述代码，重点是要明白yield 语句作为数据的生产者而for 循环语句
作为数据的消费者。当这些生成器被连在一起后，每个yield 会将一个单独的数据元
素传递给迭代处理管道的下一阶段。在例子最后部分，sum() 函数是最终的程序驱动
者，每次从生成器管道中提取出一个元素。
这种方式一个非常好的特点是每个生成器函数很小并且都是独立的。这样的话就
很容易编写和维护它们了。很多时候，这些函数如果比较通用的话可以在其他场景重复
使用。并且最终将这些组件组合起来的代码看上去非常简单，也很容易理解。
使用这种方式的内存效率也不得不提。上述代码即便是在一个超大型文件目录中
也能工作的很好。事实上，由于使用了迭代方式处理，代码运行过程中只需要很小很小
的内存
'''