# 混合时钟下的可微亚采样曝光积分

`data/record.json` 是 混合时钟下的可微亚采样曝光积分 使用的本地合成交换样本。数组按 JSON 的下标顺序排列。本文的坐标、单位和枚举约定与该记录配套。记录中如果有 `scale` 或 `limits`，对应同一输入协议的部署规格。

knots 的每行是特征时钟秒数、通道值和有效表示。clock.points 每行是相机秒和特征秒，点间线性，超出可标定区间属于未知。window 四点依次是起沿、权重达到一、权重离开一、止沿，权重在相机时间轴。积分的测度用相机时钟秒，平均分母为有效覆盖权重。事件中 knots 的起止是对源行列表的半开区间。gap_after 声明该特征时钟之后无更多观测。梯度针对 clock 各节点的特征时间值，相机轴控制点保持不变。

## 读取样本

使用 Python 3.11 或 3.12，并在虚拟环境安装锁定依赖。读取入口返回原始记录。作为命令运行时，它会列出各顶层输入项目以及 NumPy 版本。

```sh
python -m pip install -r requirements.txt
python -m fractional_exposure_input
python -m unittest discover -s tests -v
```

测试读取交换样本，核对其中的张量尺寸、标识与数据约定。
