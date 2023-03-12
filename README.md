心血来潮实现的循环引用检查：



- 使用 `python` 的 `gc` 库查找引用；
- 使用 `dfs` 作为检查的主要算法。



使用 `id` 作为实例标识进行检查，同 `id` 的实例视作同一实例，在属性引用路径上若出现同样 `id` 的两个实例则判断为循环引用。



目前测试用例很简单，逻辑不一定完备，待进一步测试实际使用中的效果。