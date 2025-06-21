---
url: https://js.langchain.com.cn/docs/modules/schema/chat-messages
crawled_at: 2025-06-22T02:00:25.902882
---

聊天消息
终端用户与LLMs互动的主要界面是聊天界面。因此，一些模型提供商已经开始以期望聊天消息的方式提供对底层API的访问。这些消息具有内容字段（通常是文本)，并与用户（或角色)相关联。当前支持的用户有System， Human，和AI。
SystemChatMessage
​
表示应为AI系统提供说明的聊天消息。
import { SystemChatMessage } from "langchain/schema";
new SystemChatMessage("You are a nice assistant");
HumanChatMessage
​
表示来自与AI系统交互的人的信息的聊天消息。
import { HumanChatMessage } from "langchain/schema";
new HumanChatMessage("Hello, how are you?");
AIChatMessage
​
表示来自AI系统的消息的聊天消息。
import
{
AIChatMessage
}
from
"langchain/schema"
;
new
AIChatMessage
(
"I am doing well, thank you!"
)
;