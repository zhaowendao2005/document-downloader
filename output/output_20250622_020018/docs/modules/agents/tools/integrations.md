---
url: https://js.langchain.com.cn/docs/modules/agents/tools/integrations/
crawled_at: 2025-06-22T02:00:20.803960
---

集成: 工具
LangChain提供以下可立即使用的工具:
AWSLambda
- AWS Lambda API的包装器，通过Amazon Web Services Node.js SDK调用。对于触发具有您需要提供给代理的任何行为的无服务器函数很有用。
BingSerpAPI
- Bing Search API的包装器。在需要回答有关当前事件的问题时很有用。输入应该是一个搜索查询。
BraveSearch
- Brave Search API的包装器。在需要回答有关当前事件的问题时很有用。输入应该是一个搜索查询。
Calculator
- 用于获取数学表达式的结果。这个工具的输入应该是一个可以由简单计算器执行的有效的数学表达式。
GoogleCustomSearch
- Google Custom Search API的包装器。在需要回答有关当前事件的问题时很有用。输入应该是一个搜索查询。
IFTTTWebHook
- IFTTT Webhook API的包装器。用于触发IFTTT动作。
JsonListKeysTool
和
JsonGetValueTool
- 用于从JSON对象中提取数据。这些工具可在
JsonToolkit
中集体使用。
RequestsGetTool
和
RequestsPostTool
- 用于发出HTTP请求。
SerpAPI
- A wrapper around the SerpAPI API. Useful for when you need to answer questions about current events. Input should be a search query.
[
QuerySqlTool
][查询SQL工具]
，
[
InfoSqlTool
][信息SQL工具]
，
[
ListTablesSqlTool
][列出表格SQL工具]
， 和
[
QueryCheckerTool
][查询检查工具]
- 用于与SQL数据库进行交互。可以与
[
SqlToolkit
][SQL工具包]
一起使用。
[
VectorStoreQATool
][向量存储问答工具]
- 可用于从向量存储中检索相关文本数据。
[
ZapierNLARunAction
][ZapierNLA运行操作]
- 封装了Zapier NLP API。用于以自然语言输入触发Zapier操作。最好与
[
ZapierToolkit
][Zapier工具包]
一起使用。