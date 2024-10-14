# Generative AI Agents

This repository serves as both an educational resource and a practical toolkit for rapid development of Large Language Model (LLM) agents. Our goal is to empower individuals and organizations to harness the power of generative AI by providing a structured learning path and a suite of reusable components.

This lecture is designed to bridge the gap between theoretical understanding and practical implementation of LLM-based agents. Whether you're an AI enthusiast, a developer, or a professional seeking to integrate generative AI into your workflows, this repository offers a comprehensive suite of tools and resources to accelerate your work.

## Getting Started
First, clone this repository and follow the instructions provided in each chapter. The project is organized into sequential modules, each building upon the previous to deepen your understanding and capabilities.

```bash
git clone https://github.com/yourusername/generative-ai-agents.git
cd generative-ai-agents
```

## Inference Building Blocks

The code in the chapters provide a toolset that you can use as inference building blocks for your own applications. We are also providing example applications in every chapter.

### LLM Setup and API Integration

In Chapter 00-02 we cover the basics of setting up an environment to work with large language models, including integration with popular APIs including the OpenAI API. We guide you with the installation of open source libraries which implement the OpenAI API as well as other useful tools for working with LLMs.

- LLM Installation: Learn how to install and configure local LLM servers like Ollama or llama.cpp.
- API Clients: Develop Python clients (ChatClient, ChatContext, QAPair) to interface with your LLMs.
- Configuration Management: Use config.json files to manage different models and settings.

### Workplace Enhancements like IDE Integration and Minimal Chat Applications

The Objective in chapter 03-05 is to Integrate LLM functionalities into your own development environment.

- IDE Plugins: Explore how to use LLMs within popular IDEs for code assistance.
- Minimal Chat Applications: Build simple chatbots to understand the basics of conversational AI.

## Structured Data Generation

The most obvious application for Generative AI Agents is to generate data out of the Large Language Model (LLM) itself. In Chapter 10 we cover this most complete to have generators for the following data types:

- Text: extract knowledge from LLMs (unstructured data)
- Tables: generate structured data
- Time-Series Data: a special version of tables which have time-markers as keys
- Decisions: data which is related to binary or tenary logic
- Classifications: catgorization of text, i.e., sentiment and profanity.
- Prompts: generate the building blocks for instruct training
- Translation: tranformation of text into different languages
- Enrichment: purpose-oriented text augmentation, i.e. SEO tasks
- Reduction: summarization and keyword generation, i.e. for query or filename production

---

*** So far this project has implemented the documented libraries. The following chapters are for future implementations, their implementation has to be done in the future. ***

---

## Agents with Internal Data

In Chapter 20 we implement the basic harvesting data structures and methods to collect and store information from various sources like system information, project information etc. We also cover how to integrate these data into our LLM agents using search engines.

## Agents with External Data

In Chapter 30 we extend the capabilities of our AI agents by integrating external data sources such as APIs, databases, or web scraping techniques. Using the archetypes from chapter 10 and the storage/retrieval functions of chapter 20, we are able to handle a wide variety of information sources in a generalized way.

## Embedded Agents with Local Data

In chapter 40 we consider that LLM agents are not external from existing systems/tools, but internal inside an existing application. We describe how the internal data can be made available for AI agents and how to integrate them into workflows seamlessly. This is particularly useful in environments where security and privacy are paramount.

## Process Automation

In chapter 50 we discuss systems that have a fixed order of operation and where generative AI agents may automate operations to enhance quality and speed of the complete process chain. We will use the Inference Building Blocks as described so far. To provide such building blocks in an existing environment requires that those are “pluggable”, i.e., they can be integrated using a client-server architecture. Therefore we implement the Inference Building Blocks as Inference Microservices.

## Reasoning and Decision Making

While the building blocks so far only provided services for linear systems in process automation, we now consider that processes may have a nonlinear structure and are interconnected using decision points. In chapter 60 we introduce reasoning methods that can help in the creation of such complex system.

## Steering

Robots or other autonomous agents need to make decisions based on their environment. In chapter 70 we explore options to collect “perception” data from sensors and use it for decision making, steering, and navigation. We will introduce a machine operation language that a LLM must speak, to operate the robot in its environment. Furthermore, we need an abstraction of a rule set which explains which target the agent should aim, what the agent is allowed to do and what not to do.

## Autonomous Agents

In chapter 80 we consider autonomous agents as those which can act without or with minimal human intervention. We consider Autonomous Agens as Robots without a physical body but with an internal language that describes a behavior model and interaction logic. 

