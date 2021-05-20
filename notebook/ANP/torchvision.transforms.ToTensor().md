## torchvision.transforms.ToTensor()

pytorch在加载数据集时都需要对数据记性transforms转换，其中最常用的就是torchvision.transforms.ToTensor()函数，但初学者可以认为这个函数只是把输入数据类型转换为pytorch的Tensor（int64）类型，其实不然，该函数内部的具体转换步骤为：

1、将图片转化成内存中的存储格式；
2、将字节以流的形式输入，转化成Tensor类型；
3、对Tensor进行reshape；
4、对Tensor进行permute（2,0,1，因为pytorch的维度和图片维度不一样；
5、将Tensor中的每个元素除以255；
6、输出该Tensor数据。

注：以后用了这个函数之后别再想着给数据在除以255归一化一下了。。。

## torchvision.transforms.ToPILImage()

pytorch在将Tensor类型数据转换为图片数据时，需要用到这个torchvision.transforms.ToPILImage()函数，该函数的作用就是把Tensor数据变为完整原始的图片数据（保存后可以直接双击打开的那种），函数内部的具体转换步骤为：

1、将Tensor的每个元素乘以255；
2、将数据由Tensor转化成Uint8；
3、将Tensor转化成numpy的ndarray类型；
4、对ndarray对象做permute (1, 2, 0)的转置，因为pytorch的维度和图片维度不一样；
5、将ndarray对象转化成PILImage数据格式；
6、输出该PILImage数据（save后可以直接打开）。


原文链接：https://blog.csdn.net/weixin_44414948/article/details/110625431