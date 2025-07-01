Codelog {#codelog} 

Last update June 30, 2025

This codelog contains the author's notes when addressing the TR comments on Building-Business-Ready-Generative-AI-Systems repository.

🐬 Indicates new notes since the last update The notes are organized by theme.

[0.Private token and grequests.py] {#private-token-and-grequests.py}
grequests.py is downloaded early in each notebook. It contains a download function. But to download it with curl, we need a private token.

The GitHub repository remains private until a few days before the book is released.

As such, a private token is temporarily required in the curl command in each notebook which will be removed when the repository is made public.

grequests.py contains the current private token that must be used to download files from the repository. It contains the function that will be used to download files from the repo.

If grequests.py is not installed and run properly, the requirements cannot be downloaded and run, leading to missing package errors.

[1.Google Colab] {#google-colab}

The strategic choice of Google Colab for this book was to enable users to open a notebook with one click on GitHub while reading the book. Once the requested API keys (OpenAI, Pinecone) are configured, the user can run the notebooks with a single click. 
Goal: Focus on the complexity of the Generative AI Systems.

Readers are free to install the programs in any environment they prefer.

[2.Python] {#python}

This book is not for beginners.As such, there is no need to explain what numpy, matplotlib or any other Python library is beyond a few words when using
a specific library.

Also, the code is educational and not meant for production. The focus is on the complexity of the architecture of Generative AI Systems.

As such, the code is focused on the functions and not overloaded or drowned in controls. That is for a project, not a prototype.

Goal: Build a GenAISys prototype chapter by chapter and present it in Chapter 10. Thus, comments for beginners are not necessary and can be distractful unless really
necessary to understand the architecture.

[3.API keys] {#api-keys}

The links to the platforms are provided. OpenAI and Pinecone have comprehensive documentation.
Goal: Remain focused on the architecture to upskill the readers on GenAI Systems.

[4.Copilots] {#copilots}

The author's strategy is to focus on the architecture of complex GenAISys. As such, the architecture was designed first, then the main blocks of code and functions. When necessary, OpenAI and Gemini were used to fine-tune the functions. The code thus follows the standards that these models were trained on, as seen on GitHub and other code repositories.

Goal: Remain focused on the architecture of GenAISys and the narrative.

[4.Cutting-edge LLMs] {#cutting-edge-llms}

Cutting-edge LLMs such as OpenAI GPT-4o and the Ox series are advanced. We are not in the initial stages of Generative AI. They can produce sophisticated formatted responses and tasks. However, an LLM will not systematically produce the exact same, though acceptable, result in complex cases because the LLM controllers are designed to produce a diversity of responses.
We're in a new era, and we must evolve with the LLMs, push the boundaries, and explore unchartered territory.
