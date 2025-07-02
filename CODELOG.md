# Codelog

Last update July 2, 2025

This codelog contains the author's notes when addressing the TR comments on **Building-Business-Ready-Generative-AI-Systems** repository.   

🐬 Indicates *new notes since the last update* 

The notes are organized by theme.


## 0.Private token and grequests.py
 `grequests.py` is downloaded early in each notebook. It contains a download function. But to download it with curl, we need a private token.

*curl* commands are widely used including in OpenAI's documentation.

 The GitHub repository remains private until a few days before the book is released.
 As such, a private token is *temporarily* required in the curl command in each notebook which will be removed when the repository is made public.
 
 `grequests.py` contains the current private token that must be used to download files from the repository. It contains the function that must be used to download files from the repo. This private token must be the one used to download grequests.py itself in the first line(s) of each notebook. 
 
  *If grequests.py is not installed and run properly, the requirements cannot be downloaded and run, leading to missing package errors.*

## 1.Google Colab
The strategic choice of Google Colab for this book was to enable users to open a notebook with one click on GitHub while reading the book. Once the requested API keys (OpenAI, Pinecone) are configured, the user can run the notebooks with a single click. 

*Goal*: Focus on the complexity of the Generative AI Systems.
Readers are free to install the programs in any environment they prefer.

## 2.Python
This book is *not for beginners*.As such, there is no need to explain what numpy, matplotlib or any other Python library is beyond a few words when using
a specific library.

Also, the code is educational and not meant for production. The focus is on the complexity of the architecture of Generative AI Systems. As such, the code is focused on the functions and not overloaded or drowned in controls. That is for a project, not a prototype. 

*Goal*: Build a GenAISys prototype chapter by chapter and present it in Chapter 10. Thus, comments for beginners are not necessary and can be distractful unless really
necessary to understand the architecture.


## 3.API keys
The links to the platforms are provided. OpenAI and Pinecone have comprehensive documentation. 
*Goal*: Remain focused on the architecture to upskill the readers on GenAI Systems.

## 4.Copilots

The author's strategy is to focus on the architecture of complex GenAISys. As such, the architecture was designed first, then the main blocks of code and functions. When necessary, OpenAI and Gemini were used to fine-tune the functions. The code thus follows the standards that these models were trained on, as seen on GitHub and other code repositories.

*Goal*: Remain focused on the architecture of GenAISys and the narrative.

## 5.Cutting-edge LLMs
Cutting-edge LLMs such as OpenAI GPT-4o and the Ox series are advanced. We are not in the initial stages of Generative AI. They can produce sophisticated formatted responses and tasks. However, an LLM will not systematically produce the exact same, though acceptable, result in complex cases because the LLM controllers are designed to produce a diversity of responses.
We're in a new era, and we must evolve with the LLMs, push the boundaries, and explore unchartered territory.

# 6.🐬About the code structure 

It's important to clarify the primary objective of the code presented in the book. This code is educational and designed to serve as a learning tool for aspiring AI architects, rather than a production-ready codebase for immediate deployment.

Our goal is to train readers to become proficient architects who understand the fundamental design principles of Generative AI Systems, rather than just operators who can implement pre-existing solutions. To achieve this, the code intentionally highlights core architectural concepts, design patterns, and the rationale behind specific structural choices, even if those choices might differ from what's ideal in a highly optimized, scalable production environment.
For example, aspects like:

**Modular Design**: The use of a commons directory and separate Python files clearly demonstrates the importance of modularity, reusability, and separation of concerns—key architectural principles.

**Explicit Memory Management**: The code meticulously illustrates how to design and implement different types of memory (short-term, long-term), which is crucial for building stateful conversational AI systems, providing a direct lesson in architectural decision-making for contextual awareness.
API Abstraction: The functions that abstract API calls teach architects how to create clean interfaces, isolate dependencies, and design for future extensibility.

**Adaptive Orchestration and Chain of Thought**: 
These sections are designed to convey how to architect intelligent decision-making and complex reasoning pipelines within a GenAISys.


While we've made efforts to ensure the code is functional and illustrative, certain choices prioritize clarity and direct demonstration of architectural concepts over production-level robustness, advanced error handling, or extreme optimization. 

These are areas that an architect, having understood the core principles from this book, would then further refine in a real-world production setting.


We believe this approach effectively equips readers with the foundational architectural knowledge necessary to design their own sophisticated GenAISys, which they can then build upon with more advanced engineering practices


## Building a production-level program 

The existing code, designed for educational purposes, demonstrates core architectural principles of a GenAISys. Transforming this into a production-ready system requires a substantial additional investment, primarily due to requirements for robustness, scalability, comprehensive testing, and enterprise-grade security that are intentionally simplified for learning.

Based on the book's architectural descriptions and industry standards for production systems:
 * Cost of Transition: Expect an additional 9 to 60+ person-months of highly specialized engineering effort. This translates to an estimated €72,000 to €900,000+ in development costs, excluding ongoing operational expenses for infrastructure and API usage.

 * Key Additional Efforts: This estimate accounts for building robust error handling, implementing comprehensive testing (unit, integration, end-to-end), optimizing for performance and scalability (e.g., advanced memory management beyond text files, asynchronous processing), establishing full DevOps pipelines (containerization, CI/CD, monitoring), enhancing security layers (authentication, authorization, data encryption), and developing a production-grade user interface beyond educational widgets.

This is beyond the scope of an educational book. 

## Book title 

The "cognitive dissonance" the TRs are experiencing is a common point of confusion when reviewing complex systems development.

The book's title, "Building Business-Ready Generative AI Systems," refers to training the reader to understand and implement the architectural foundations and strategic design choices that make a GenAISys truly ready for a business environment. It focuses on the "why" and "how" of designing components like robust memory, adaptive controllers, integrated security, and scalable RAG, which are essential for a system to be fit for business purpose.

The code is therefore an educational tool to demonstrate these architectural principles, illustrating the concepts required to design a system capable of handling business needs, rather than providing the fully hardened, production-optimized, and endlessly tested code that would represent the final operational product.

In essence, the book equips the reader to be the architect who designs the business-ready blueprint, not the operator who finalizes the construction for immediate deployment.

## Primary TR goal

*Verify each scenario in each chapter in each section, each line of code described: input/output.*
