# Getting started
Getting started should be pretty easy. First make sure you can run python notebooks, if using VSCode you might need to install an extension to support this.

After this, you can clone the documentation, as an example I used the prometheus documentation for this.
Make sure that the root of your docs ends up in `data/`

Great! You're almost ready to get started. Now, the only thing left to do is to register for Groq and get an API key.
This is a free service and has pretty high limits.

**WARNING:** Do not, I repeat **DO NOT** use the Inuits docs for this, you can try with different documentation but make sure its for an open-source project. We don't want to run the chance of leaking important information.

Once you've got this API key, set it up in the `.env` file or export it.

First open up the `create_index` notebook, and run it, after this you can run/experiment with the other notebooks.

## Explanation
First of all, we're using Llamaindex, a framework for creating RAG pipelines and other LLM-based applications.
It's not important at this point, but do know that there are different frameworks available, some notable ones include:
- Langchain: https://github.com/langchain-ai/langchain
- Promptflow: https://github.com/microsoft/promptflow
- ell: https://github.com/MadcowD/ell

They basically all work around the same concept which is augmenting the context of your model with useful data which in turn should influence the next token prediction. This workshop focuses on LlamaIndex since it's community has been really active and their documentation is one of the better ones.

The code should be self-explanatory in what it's doing, not all the details are important at this point.

In general lines we're doing the following steps:
- Loading LlamaIndex and setting up the LLM and tokenizer
- Reading all `.md` files using the `SimpleDirectoryReader`
- Indexing the docs using the tokenizer and an indexer
- Setting a response synthesizer
- Create a query engine using the index and the synthesizer
- Querying the index

## Challenges for the reader - See LlamaIndex documentation
- Try to use a different index/store (currently we're using ColBERT)
- Make it go and scrape a website instead of using the SimpleDirectoryReader
- Explore and play around with the plugins
- Try and make indexing work in parallel
