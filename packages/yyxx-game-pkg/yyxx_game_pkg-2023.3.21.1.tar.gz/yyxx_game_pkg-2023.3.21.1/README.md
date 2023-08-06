[TOC]
# yyxx-game-pkg

`yyxx-game-pkg` 是一个专门为 yyxx 公司开发的 Python 内部接口集合。

## 模块

### xtrace

`xtrace` 模块封装了链路追踪的帮助类，可以帮助开发人员快速地实现链路追踪功能。该模块提供了以下功能：

- 封装了调用链路追踪的相关逻辑，可以自动记录服务间的调用关系。
- 提供了统一的接口，方便开发人员在不同的应用场景中调用。

调用例子：
- 初始化
```python
from yyxx_pkg.xtrace.helper import register_to_jaeger, get_tracer
from opentelemetry.instrumentation.requests import RequestsInstrumentor


# init instrumentation.requests 
RequestsInstrumentor().instrument()

# init jaeger exporter
register_to_jaeger("your server name", "jaeger-host")

if __name__ == '__main__':
    pass
```

- 业务链路埋点
```python
from yyxx_pkg.xtrace.helper import trace_span

@trace_span()
def func_business():
    # your business function
    pass

@trace_span(ret_trace_id=True)
def func_business_with_trace_id():
    # your business function
    ret_val = "success"
    
    # real return: ret_val, trace_id
    return ret_val

@trace_span(set_attributes=True)
def func_business_on_set_attributes(**kwargs):
    # your business function
    ret_val = "success"
    
    # record **kwargs as jaeger tags
    return ret_val
```

### stat
`stat`模块包含yyxxgame内部统计业务的底层框架，目前包含`dispatch`、`submit`、`xcelery几个模块`
#### dispatch
业务分发基础模块
#### submit
任务提交基础模块
#### xcelery
celery封装层

## 生产环境配置
python3环境中执行：
```
pip install yyxx-game-pkg
```


## 开发环境配置

### clone 代码
```
git clone https://github.com/yyxxgame/yyxxgame-pkg
```

### 安装poetry

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### 配置虚拟环境并显式激活
```
- poetry env use python3
- poetry env list
- poetry shell
```

### 安装更新开发包
```
- poetry install
- poetry update
```


## 版本发布
### develop
提交注释中添加`[BUILD]`关键字并推送会触发github actions的dev版本构建并发布到[yyxx-game-pkg-dev](https://pypi.org/project/yyxx-game-pkg-dev/)

### release
新建`tag`并推送会触发github actions的正式版本构建并发布到[yyxx-game-pkg](https://pypi.org/project/yyxx-game-pkg/)

## 参考文档
- [poetry](https://python-poetry.org/docs/)
- [CodeGeeX插件](https://models.aminer.cn/codegeex/)