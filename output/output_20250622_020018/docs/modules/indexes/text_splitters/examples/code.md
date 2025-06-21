---
url: https://js.langchain.com.cn/docs/modules/indexes/text_splitters/examples/code
crawled_at: 2025-06-22T02:00:23.572722
---

代码和标记文本分割器
LangChain支持各种不同的标记和编程语言特定的文本分割器，以基于语言特定的语法分割文本。
​这将导致更具有语义的自包含块，更适用于矢量存储或其他检索器。
流行的语言，如JavaScript， Python，和Rust，以及Latex，HTML，和Markdown都受到支持。
用法
​
使用“fromLanguage”工厂方法初始化标准的“RecursiveCharacterTextSplitter”。以下是各种语言的示例。
JavaScript
​
import
{
SupportedTextSplitterLanguages
,
RecursiveCharacterTextSplitter
,
}
from
"langchain/text_splitter"
;
console
.
log
(
SupportedTextSplitterLanguages
)
;
// Array of supported languages
/*
[
'cpp',      'go',
'java',     'js',
'php',      'proto',
'python',   'rst',
'ruby',     'rust',
'scala',    'swift',
'markdown', 'latex',
'html'
]
*/
const
jsCode
=
`
function helloWorld() {
console.log("Hello, World!");
}
// Call the function
helloWorld();
`
;
const
splitter
=
RecursiveCharacterTextSplitter
.
fromLanguage
(
"js"
,
{
chunkSize
:
32
,
chunkOverlap
:
0
,
}
)
;
const
jsOutput
=
await
splitter
.
createDocuments
(
[
jsCode
]
)
;
console
.
log
(
jsOutput
)
;
/*
[
Document {
pageContent: 'function helloWorld() {',
metadata: { loc: [Object] }
},
Document {
pageContent: 'console.log("Hello, World!");',
metadata: { loc: [Object] }
},
Document {
pageContent: '}\n// Call the function',
metadata: { loc: [Object] }
},
Document {
pageContent: 'helloWorld();',
metadata: { loc: [Object] }
}
]
*/
Python
​
import
{
RecursiveCharacterTextSplitter
}
from
"langchain/text_splitter"
;
const
pythonCode
=
`
def hello_world():
print("Hello, World!")
# Call the function
hello_world()
`
;
const
splitter
=
RecursiveCharacterTextSplitter
.
fromLanguage
(
"python"
,
{
chunkSize
:
32
,
chunkOverlap
:
0
,
}
)
;
const
pythonOutput
=
await
splitter
.
createDocuments
(
[
pythonCode
]
)
;
console
.
log
(
pythonOutput
)
;
/*
[
Document {
pageContent: 'def hello_world():',
metadata: { loc: [Object] }
},
Document {
pageContent: 'print("Hello, World!")',
metadata: { loc: [Object] }
},
Document {
pageContent: '# Call the function',
metadata: { loc: [Object] }
},
Document {
pageContent: 'hello_world()',
metadata: { loc: [Object] }
}
]
*/
HTML
​
import
{
RecursiveCharacterTextSplitter
}
from
"langchain/text_splitter"
;
const
text
=
`
<!DOCTYPE html>
<html>
<head>
<title>🦜️🔗 LangChain</title>
<style>
body {
font-family: Arial, sans-serif;
}
h1 {
color: darkblue;
}
</style>
</head>
<body>
<div>
<h1>🦜️🔗 LangChain</h1>
<p>⚡ Building applications with LLMs through composability ⚡</p>
</div>
<div>
As an open source project in a rapidly developing field, we are extremely open to contributions.
</div>
</body>
</html>
`
;
const
splitter
=
RecursiveCharacterTextSplitter
.
fromLanguage
(
"html"
,
{
chunkSize
:
175
,
chunkOverlap
:
20
,
}
)
;
const
output
=
await
splitter
.
createDocuments
(
[
text
]
)
;
console
.
log
(
output
)
;
/*
[
Document {
pageContent: '<!DOCTYPE html>\n<html>',
metadata: { loc: [Object] }
},
Document {
pageContent: '<head>\n    <title>🦜️🔗 LangChain</title>',
metadata: { loc: [Object] }
},
Document {
pageContent: '<style>\n' +
'      body {\n' +
'        font-family: Arial, sans-serif;\n' +
'      }\n' +
'      h1 {\n' +
'        color: darkblue;\n' +
'      }\n' +
'    </style>\n' +
'  </head>',
metadata: { loc: [Object] }
},
Document {
pageContent: '<body>\n' +
'    <div>\n' +
'      <h1>🦜️🔗 LangChain</h1>\n' +
'      <p>⚡ Building applications with LLMs through composability ⚡</p>\n' +
'    </div>',
metadata: { loc: [Object] }
},
Document {
pageContent: '<div>\n' +
'      As an open source project in a rapidly developing field, we are extremely open to contributions.\n' +
'    </div>\n' +
'  </body>\n' +
'</html>',
metadata: { loc: [Object] }
}
]
*/
Latex
​
import
{
RecursiveCharacterTextSplitter
}
from
"langchain/text_splitter"
;
const
text
=
`
\\begin{document}
\\title{🦜️🔗 LangChain}
⚡ Building applications with LLMs through composability ⚡
\\section{Quick Install}
\\begin{verbatim}
Hopefully this code block isn't split
yarn add langchain
\\end{verbatim}
As an open source project in a rapidly developing field, we are extremely open to contributions.
\\end{document}
`
;
const
splitter
=
RecursiveCharacterTextSplitter
.
fromLanguage
(
"latex"
,
{
chunkSize
:
100
,
chunkOverlap
:
0
,
}
)
;
const
output
=
await
splitter
.
createDocuments
(
[
text
]
)
;
console
.
log
(
output
)
;
/*
[
Document {
pageContent: '\\begin{document}\n' +
'\\title{🦜️🔗 LangChain}\n' +
'⚡ Building applications with LLMs through composability ⚡',
metadata: { loc: [Object] }
},
Document {
pageContent: '\\section{Quick Install}',
metadata: { loc: [Object] }
},
Document {
pageContent: '\\begin{verbatim}\n' +
"Hopefully this code block isn't split\n" +
'yarn add langchain\n' +
'\\end{verbatim}',
metadata: { loc: [Object] }
},
Document {
pageContent: 'As an open source project in a rapidly developing field, we are extremely open to contributions.',
metadata: { loc: [Object] }
},
Document {
pageContent: '\\end{document}',
metadata: { loc: [Object] }
}
]
*/