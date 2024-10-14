# Embedded Agents Using Local Data

Consider you have a system which has the purpose to retrieve, store and provide data for a specific use case.
This system maintains it's own data structures and storage systems. In case that you want to use that data
in an AI agent, you would require to extract the data and make it available for example using RAG.
But if the AI agent is inside the data-providing system itself, there is no need to first extract the data first
just to make it available again using an outside RAG server. Here it's much easier to omit RAG and perform
context enrichment within the system itself.

