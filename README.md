心血来潮实现的循环引用检查：



- 使用 `__dict__` 作为引用依据
- 使用 `dfs` 作为检查的主要算法



使用 `id` 作为实例标识进行检查，同 `id` 的实例视作同一实例，在属性引用路径上若出现同样 `id` 的两个实例则判断为循环引用。



目前测试用例很简单，逻辑不一定完备，待进一步测试实际使用中的效果。


测试用例结果：
``` bash
>>>> test case no cycle <<<<
find no cycle reference!


>>>> test case has cycle <<<<
cycle reference!  root.b.c.a = root type: <class '__main__.TestCls'> id: 2002894761792
cycle reference!  root.b.c.b = root.b type: <class '__main__.TestCls'> id: 2002894761840
cycle reference!  root.c.a = root type: <class '__main__.TestCls'> id: 2002894761792
cycle reference!  root.c.b.c = root.c type: <class '__main__.TestCls'> id: 2002894761888
```

`objgraph` 的实现：


- 算法整体思路类似，依靠 `gc.get_referrers` 获取引用（和 `__dict__` 的区别应该在弱引用上，待验证）；
- 剔除了一些不需要关注的临时变量，比如 `get_chain` 这个函数逻辑使用到的 `queue` 局部变量，还有 `get_chain` 这个函数本身等等。
