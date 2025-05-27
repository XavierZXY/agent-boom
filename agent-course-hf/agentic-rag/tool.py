import os

import datasets
from dotenv import load_dotenv
from langchain.docstore.document import Document
from langchain_community.retrievers import BM25Retriever
from smolagents import CodeAgent, InferenceClientModel, OpenAIServerModel, Tool

# Load the dataset
guest_dataset = datasets.load_dataset(
    "agents-course/unit3-invitees", split="train"
)

# Convert the dataset to a list of Document objects
docs = [
    Document(
        page_content="\n".join(
            [
                f"Name:{guest['name']}",
                f"Relation: {guest['relation']}",
                f"Description: {guest['description']}",
                f"Email: {guest['email']}",
            ]
        )
    )
    for guest in guest_dataset
]


# Create the retriever tool
class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = (
        "Retrieves information about guests based on their name or relation."
    )
    inputs = {
        "query": {
            "type": "string",
            "description": "The name or relation of the guest to search for.",
        }
    }
    output_type = "string"

    def __init__(self, docs):
        self.is_initialized = False
        self.retriever = BM25Retriever.from_documents(docs)

    def forward(self, query: str):
        results = self.retriever.get_relevant_documents(query)
        if results:
            return "\n\n".join([doc.page_content for doc in results[:3]])
        else:
            return "No matching guest information found."


# Initialize the tool with the documents
guest_info_tool = GuestInfoRetrieverTool(docs)


def main():
    # get the .env config
    load_dotenv()
    model_id = os.getenv(
        "HUGGINGFACE_MODEL_ID", "Qwen/Qwen2.5-Coder-32B-Instruct"
    )
    api_key = os.getenv("HUGGINGFACE_API_KEY")
    base_url = os.getenv(
        "HUGGINGFACE_BASE_URL", "https://api-inference.huggingface.co/models/"
    )
    # Initialize the Hugging Face model
    # model = InferenceClientModel(
    #     model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    #     api_key=api_key,
    #     base_url=base_url,
    # )
    model = OpenAIServerModel(
        model_id=model_id,
        api_key=api_key,
        api_base=base_url,
    )

    # Create Alfred, our gala agent, with the guest info tool
    alfred = CodeAgent(tools=[guest_info_tool], model=model)

    # Example query Alfred might receive during the gala
    response = alfred.run("Tell me about our guest named 'Lady Ada Lovelace'.")

    print("🎩 Alfred's Response:")
    print(response)


if __name__ == "__main__":
    main()
