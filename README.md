# API 自动化测试框架

这是一个基于 Python 和 pytest 的 API 自动化测试框架。

## 项目结构

```
├── conftest.py           # Pytest 配置和 fixtures
├── pytest.ini           # Pytest 设置
├── requirements.txt     # Python 依赖
├── tests/              # 测试用例目录
│   ├── __init__.py
│   └── test_example.py
└── utils/              # 工具模块
    ├── __init__.py
    ├── api_client.py
    └── assertions.py
```

## 环境配置

1. 安装 Python 依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 配置环境变量（在 `.env` 文件中）：
   - API_BASE_URL：API 基础地址
   - API_KEY：API 认证密钥

## 运行测试

运行所有测试：
```bash
npm test
```

生成 HTML 报告：
```bash
npm run test:report
```

## 测试分类

- 冒烟测试：`pytest -m smoke`
- 回归测试：`pytest -m regression`

## 主要特性

- 模块化的测试结构
- 环境配置管理
- HTML 测试报告
- 自定义 API 客户端
- 可复用的断言工具
- 使用标记进行测试分类