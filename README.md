# 接口自动化测试练习项目

基于DummyJSON公开接口，练习接口测试用例设计、/Apifox手工测试、以及Python + pytest自动化测试的完整流程。

## 技术栈

- **接口调试工具**：Apifox（对标Postman，支持接口设计+调试+测试）
- **编程语言**：Python 3.11
- **HTTP请求库**：requests
- **测试框架**：pytest
- **测试报告**：pytest-html

## 项目结构
├── test_login.py # 登录接口测试用例（5条）
├── test_products.py # 商品CRUD接口测试用例（4条）
├── test_auth.py # 接口鉴权测试用例（3条）
├── report.html # pytest自动生成的测试报告
└── README.md

## Apifox 手工测试

使用Apifox完成了接口调试和手工测试，涵盖以下操作：
- 请求发送（GET/POST/PUT/DELETE）
- 环境变量配置
- 接口关联（登录成功后自动提取token，供后续接口使用）
- 断言编写（状态码校验、响应字段校验）
- 批量执行测试用例集


## 运行方式

```bash
# 安装依赖
pip install requests pytest pytest-html

# 运行全部测试并生成报告
pytest test_login.py test_products.py test_auth.py -v --html=report.html
```

## 测试结果

12条测试用例，全部通过。
