# pandas

DataFrame

字典创建D表格，用pd.DataFrame.from_dict(),orient参数默认'columns'，表示字典的键作为列标签，可以改'index'

```python
IN:
a1 = pd.DataFrame.from_dict({'第一行':[415,554,212,554],'第二行':[454,545,6856,5669],'第三行':[6565,4886,32,8565]},orient='index',columns=['二列','三列','四列','五列'])
a1
out:

      二列  三列   四列   五列
第一行	415	  554	212	  554
第二行	454	  545	6856  5669
第三行	6565  4886	32	  8565
```



### 处理缺失值

pandas中自动将series和DataFrame中的缺失值读取并归为一类NaN,数据中的缺失值不能空缺，缺失值也要占位，不能空不然出现语法错误，numpy里可以用na.nan和None来表示这个地方空缺，转化到pandas里面，Series和DataFrame自动转化为NaN，np.nan和NaN都可以参加计算，只是表示空缺值罢了，类型是数值型。

```python
IN:
import pandas as pd 
import numpy as np
s = pd.Series([1,2,9,None,5,np.nan])
s
OUT:
0    1.0
1    2.0
2    9.0
3    NaN
4    5.0
5    NaN
dtype: float64
IN:
s.sum() # 计算总和
s.mean() # 计算平均值
s.isnull() # 判断是否为空缺值，输出布尔类型的series
OUT:
17.0

4.25

0    False
1    False
2    False
3     True
4    False
5     True
dtype: bool
```

isnull()方法是判断series里面的值是否空缺，输出布尔类型的series，notnull(

)也是一样的，可以用于筛选出空缺值。

```python
in：
s[s.isnull()]
out:
3   NaN
5   NaN
dtype: float64
```

