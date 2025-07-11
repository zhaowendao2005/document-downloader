---
url: https://js.langchain.com.cn/docs/modules/models/embeddings/integrations
crawled_at: 2025-06-22T02:00:25.483860
---

集成: 嵌入
LangChain提供了许多与各种模型提供商集成的嵌入实现。这些是:
OpenAIEmbeddings
​
OpenAIEmbeddings
类使用OpenAI API为给定文本生成嵌入。默认情况下，它会从文本中删除换行符，如OpenAI推荐的那样。但是，您可以通过将
stripNewLines: false
传递给构造函数来禁用此功能。
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
const
embeddings
=
new
OpenAIEmbeddings
(
{
openAIApiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.OPENAI_API_KEY
}
)
;
Azure
OpenAIEmbeddings
​
OpenAIEmbeddings
类使用Azure上的OpenAI API为给定文本生成嵌入。默认情况下，它会从文本中删除换行符，如OpenAI推荐的那样。但是，您可以通过将
stripNewLines: false
传递给构造函数来禁用此功能。
import
{
OpenAIEmbeddings
}
from
"langchain/embeddings/openai"
;
const
embeddings
=
new
OpenAIEmbeddings
(
{
azureOpenAIApiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_KEY
azureOpenAIApiInstanceName
:
"YOUR-INSTANCE-NAME"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_INSTANCE_NAME
azureOpenAIApiDeploymentName
:
"YOUR-DEPLOYMENT-NAME"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_DEPLOYMENT_NAME
azureOpenAIApiVersion
:
"YOUR-API-VERSION"
,
// In Node.js defaults to process.env.AZURE_OPENAI_API_VERSION
}
)
;
Google Vertex AI
​
GoogleVertexAIEmbeddings
类使用Google的Vertex AI PaLM模型为给定文本生成嵌入。
Vertex AI实现适用于Node.js，而不适用于直接在浏览器中使用，因为它需要一个服务帐户来使用。
在运行此代码之前，您应确保为您的Google Cloud仪表板中的相关项目启用了Vertex AI API，并且您已使用以下方法之一对Google Cloud进行了身份验证:
您已登录账户（使用
gcloud auth application-default login
)
enabled for the relevant project in your Google Cloud dashboard and that you've authenticated to
您正在使用被允许使用的服务帐户运行的计算机上
您已经下载了被允许使用的服务帐户的凭据
You are logged into an account (using
gcloud auth application-default login
)
permitted to that project.
You are running on a machine using a service account that is permitted
to the project.
You have downloaded the credentials for a service account that is permitted
to the project and set the
GOOGLE_APPLICATION_CREDENTIALS
environment
variable to the path of this file.
npm
Yarn
pnpm
npm
install
google-auth-library
yarn
add
google-auth-library
pnpm
add
google-auth-library
import
{
GoogleVertexAIEmbeddings
}
from
"langchain/embeddings/googlevertexai"
;
export
const
run
=
async
(
)
=>
{
const
model
=
new
GoogleVertexAIEmbeddings
(
)
;
const
res
=
await
model
.
embedQuery
(
"What would be a good company name for a company that makes colorful socks?"
)
;
console
.
log
(
{
res
}
)
;
}
;
注意:
默认的Google Vertex AI嵌入模型
textembedding-gecko
和OpenAI的
text-embedding-ada-002
模型具有不同的维度，可能不受所有向量存储提供程序的支持。
并非所有向量存储提供程序都支持它。
CohereEmbeddings
​
CohereEmbeddings
类使用Cohere API为给定文本生成嵌入向量。
npm
Yarn
pnpm
npm
install
cohere-ai
yarn
add
cohere-ai
pnpm
add
cohere-ai
import
{
CohereEmbeddings
}
from
"langchain/embeddings/cohere"
;
const
embeddings
=
new
CohereEmbeddings
(
{
apiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.COHERE_API_KEY
}
)
;
TensorFlowEmbeddings
​
此嵌入集成在您的浏览器或Node.js环境中完全运行嵌入向量，使用
TensorFlow.js
。 这意味着您的数据不会发送到任何第三方，而且您不需要注册任何API密钥。但是，它需要比其他集成更多的内存和处理能力。
npm
Yarn
pnpm
npm
install
@tensorflow/tfjs-core @tensorflow/tfjs-converter @tensorflow-models/universal-sentence-encoder @tensorflow/tfjs-backend-cpu
yarn
add
@tensorflow/tfjs-core @tensorflow/tfjs-converter @tensorflow-models/universal-sentence-encoder @tensorflow/tfjs-backend-cpu
pnpm
add
@tensorflow/tfjs-core @tensorflow/tfjs-converter @tensorflow-models/universal-sentence-encoder @tensorflow/tfjs-backend-cpu
import
"@tensorflow/tfjs-backend-cpu"
;
import
{
TensorFlowEmbeddings
}
from
"langchain/embeddings/tensorflow"
;
const
embeddings
=
new
TensorFlowEmbeddings
(
)
;
此示例使用CPU后端，适用于任何JS环境。 但是，您可以使用TensorFlow.js支持的任何后端，包括GPU和WebAssembly，它会更快。 对于Node.js，您可以使用
@tensorflow/tfjs-node
包，对于浏览器，您可以使用
@tensorflow/tfjs-backend-webgl
包。 有关更多信息，请参见
TensorFlow.js文档
。
HuggingFaceInferenceEmbeddings
​
此嵌入集成使用HuggingFace Inference API为给定文本生成嵌入向量，默认使用的是
sentence-transformers/distilbert-base-nli-mean-tokens
模型。 您可以将不同的模型名称传递给构造函数以使用不同的模型。
npm
Yarn
pnpm
npm
install
@huggingface/inference@1
yarn
add
@huggingface/inference@1
pnpm
add
@huggingface/inference@1
import
{
HuggingFaceInferenceEmbeddings
}
from
"langchain/embeddings/hf"
;
const
embeddings
=
new
HuggingFaceInferenceEmbeddings
(
{
apiKey
:
"YOUR-API-KEY"
,
// In Node.js defaults to process.env.HUGGINGFACEHUB_API_KEY
}
)
;