from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.agents import initialize_agent, Tool

# 1. Setup LLM & Embeddings
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
embeddings = OpenAIEmbeddings()

# 2. Load documents
docs = open("data/sample_docs.txt").read().splitlines()
vectorstore = FAISS.from_texts(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# 3. Define RAG Tool
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
rag_tool = Tool(
    name="KnowledgeBase",
    func=qa.run,
    description="Use this tool to answer questions from the knowledge base"
)

# 4. Create Agent (ReAct style)
agent = initialize_agent(
    tools=[rag_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

# 5. Run sample queries
print(agent.run("What is RAG?"))
print(agent.run("Tell me about LangChain."))
print(agent.run("What is 25 * 14?"))
