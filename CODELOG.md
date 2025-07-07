# Codelog

Last update July 7, 2025

This code log contains the author's notes when addressing the TR comments on the **Building-Business-Ready-Generative-AI-Systems** repository.  

➬The motivation of this document is to emphasize that *The primary goal of the code reviewing process is to verify that each example in the notebook of each chapter works as expected, as explained in Section 6 of this document, which doesn't exclude other pertinent comments on the code*. 

The notes are organized by theme.

## 0. Private token and grequests.py
 `grequests.py` is downloaded early in each notebook. It contains a download function. But to download it with curl, we need a private token.

*curl* commands are widely used, including in OpenAI's documentation.

 The GitHub repository remains private until a few days before the book's release.
 As such, a private token is temporarily required in the curl command in each notebook, which will be removed once the repository is made public.
 
 `grequests.py` contains the current private token that must be used to download files from the repository. It contains the function that must be used to download files from the repo. This private token must be the one used to download grequests.py itself, as specified in the first line(s) of each notebook. 
 
  *If grequests.py is not installed and run properly, the requirements cannot be downloaded and run, leading to missing package errors.*

## 1. Google Colab
The strategic choice of Google Colab for this book was to enable users to open a notebook with one click on GitHub while reading the book. Once the requested API keys (OpenAI, Pinecone) are configured, the user can run the notebooks with a single click. 

*Goal*: Focus on the complexity of the Generative AI Systems.
Readers are free to install the programs in any environment they prefer.

### 1.1. Paths in Google Colab
In Google Colab, /content/ is the default directory. So, the following file paths point to the same directory:
  file_path = '/content/conversation_history.json' or
 file_path = 'conversation_history.json'
In another environment, you may need absolute paths.


## 2.Python
This book is *not for beginners*. As such, there is no need to explain what numpy, matplotlib or any other Python library is beyond a few words when using
a specific library.

Additionally, the code is educational and not intended for production use. The focus is on the complexity of the architecture of Generative AI Systems. As such, the code is focused on functions and not overloaded or cluttered with controls. That is for a project, not a prototype. 

*Goal*: Build a GenAISys prototype chapter by chapter and present it in Chapter 10. Thus, comments for beginners are not necessary and can be distracting unless really
necessary to understand the architecture.


## 3.API keys
The links to the platforms are provided. OpenAI and Pinecone have comprehensive documentation. 
*Goal*: Remain focused on the architecture to upskill the readers on GenAI Systems.

🐬 The *Setting up the environment* section of Chapter 1 contains the main information on how to set up an environment, including OpenAI API keys in the  *OpenAI API key initialization*
    For Pinecone and any other API Key, the same process is described in the *Setting up the environment* section of a Chapter. 

## 4. Copilots

The author's strategy is to focus on the architecture of complex GenAISys. As such, the architecture was designed first, then the main blocks of code and functions. When necessary, OpenAI and Gemini were used to fine-tune the functions. The code thus adheres to the standards that these models were trained on, as evident on GitHub and other code repositories.

*Goal*: Remain focused on the architecture of GenAISys and the narrative.

## 5.Cutting-edge LLMs
Cutting-edge LLMs such as OpenAI GPT-4o and the Ox series are advanced. We are not in the initial stages of Generative AI. They can produce sophisticated, formatted responses and tasks. *However, an LLM will not systematically produce the exact same, though acceptable, result in complex cases because the LLM controllers are designed to produce a diversity of responses*. 

We're in a new era, and we must evolve with the LLMs, push the boundaries, and explore uncharted territory.

# 6.About the code structure 

It's important to clarify the primary objective of the code presented in the book. This code is educational and designed to serve as a learning tool for aspiring AI architects, rather than a production-ready codebase for immediate deployment.

Our goal is to train readers to become proficient architects who understand the fundamental design principles of Generative AI Systems, rather than just operators who can implement pre-existing solutions. To achieve this, the code intentionally highlights core architectural concepts, design patterns, and the rationale behind specific structural choices, even if those choices may differ from what is ideal in a highly optimized, scalable production environment.
For example, aspects like:

**Modular Design**: The use of a `commons` directory and separate Python files clearly demonstrates the importance of modularity, reusability, and separation of concerns—key architectural principles.

**Explicit Memory Management**: The code meticulously illustrates how to design and implement different types of memory (short-term, long-term), which is crucial for building stateful conversational AI systems, providing a direct lesson in architectural decision-making for contextual awareness.
API Abstraction: The functions that abstract API calls teach architects how to create clean interfaces, isolate dependencies, and design for future extensibility.

**Adaptive Orchestration and Chain of Thought**: 
These sections are designed to convey how to architect intelligent decision-making and complex reasoning pipelines within a GenAISys.


While we've made efforts to ensure the code is functional and illustrative, certain choices prioritize clarity and direct demonstration of architectural concepts over production-level robustness, advanced error handling, or extreme optimization. 

These are areas that an architect, having understood the core principles from this book, would then further refine in a real-world production setting.


We believe this approach effectively equips readers with the foundational architectural knowledge necessary to design their own sophisticated GenAISys, which they can then build upon with more advanced engineering practices.


## Building a production-level program 

The existing code, designed for educational purposes, demonstrates core architectural principles of a GenAISys. Transforming this into a production-ready system requires a substantial additional investment, primarily due to requirements for robustness, scalability, comprehensive testing, and enterprise-grade security that are intentionally simplified for learning.

Based on the book's architectural descriptions and industry standards for production systems:
 * Cost of Transition: Expect an additional 9 to 60+ person-months of highly specialized engineering effort. This translates to an estimated €72,000 to €900,000+ in development costs, excluding ongoing operational expenses for infrastructure and API usage.

 * Key Additional Efforts: This estimate accounts for building robust error handling, implementing comprehensive testing (unit, integration, end-to-end), optimizing for performance and scalability (e.g., advanced memory management beyond text files, asynchronous processing), establishing full DevOps pipelines (containerization, CI/CD, monitoring), enhancing security layers (authentication, authorization, data encryption), and developing a production-grade user interface beyond educational widgets.

This is beyond the scope of an educational book. 

## Book title 

The "cognitive dissonance" the TRs are experiencing is a common point of confusion when reviewing the development of complex systems.

The book's title, "Building Business-Ready Generative AI Systems," refers to training the reader to understand and implement the architectural foundations and strategic design choices that make a GenAISys truly ready for a business environment. It focuses on the "why" and "how" of designing components, such as robust memory, adaptive controllers, integrated security, and scalable RAG, which are essential for a system to be fit for business purposes.

The code is therefore an educational tool to demonstrate these architectural principles, illustrating the concepts required to design a system capable of handling business needs, rather than providing the fully hardened, production-optimized, and endlessly tested code that would represent the final operational product.

In essence, the book equips the reader to be the architect who designs the business-ready blueprint, not the operator who finalizes the construction for immediate deployment.

## ➬Primary TR goal

*The primary goal to help the author is to verify each scenario and example in each chapter, section, and line of code in a chapter that contains an input and output*. 

Though this does not exclude other controls, it remains the primary objective. 

In practical terms, this means that for each output in a chapter, two types of TR comments add value :
- "works as expected" 
- "doesn't work as expected because:" + explanation.
- 

## Code Optimization

### 1.Unifiying Google Colab Paths or not
Status: decision pending

Section 1.1. explains that Google Colab's default directory is `/content`. So /content/filename = filename. However, the reviewers
and probably many readers will run their notebooks locally and will have to clarify this. If the developer is not a beginner, this is no problem.
Maybe I should unify this or simply add a note at the top of the notebook or not.


### 2.Pre-installing the resquired version of `click` when installing gTTs
Status: decision pending

gTTs requires a version of `click` that is not 8.1.8. 
Google Colab's version is higher
So presently, a restart is required in the middle of the *Setting up the environment process*
I'm thinking of inserting the  following cell in cell 2 of the notebooks so that the user just *run all* during the session. The program will 
automatically uninstall click, kill the session, trigger and auto-restart. The user just has to presse *run all* again.

This cell solves the issue:

# Cell 2: Conditional 'click' setup and auto-restart.
# This cell will only modify 'click' and restart the runtime IF the 'click' version is not 8.1.8.
# After the restart (if it occurs), Colab will reconnect, and you can simply "Run All" from the top.

import importlib.metadata
import os
import time

required_click_version = '8.1.8'
current_click_version = None

print("--- Checking 'click' package version... ---")

try:
    current_click_version = importlib.metadata.version('click')
    print(f"Currently installed 'click' version: {current_click_version}")
except importlib.metadata.PackageNotFoundError:
    print("'click' package not found.")

# Check if current click version is not the required one
if current_click_version != required_click_version:
    print(f"\n--- 'click' version is not {required_click_version}. Initiating setup... ---")

    # Uninstall any existing 'click' version
    print("Uninstalling any existing 'click' installation...")
    !pip uninstall -y click

    # Install the specific 'click' version required by gTTS
    print(f"Installing 'click=={required_click_version}' for compatibility...")
    !pip install click=={required_click_version}

    print("\n--- 'click' setup complete. ---")
    print("!!! Initiating runtime restart to load the correct 'click' version. !!!")
    print("!!! Please wait for Colab to reconnect, then simply click 'Run All' from the top. !!!")

    # Give a brief moment for print statements to flush
    time.sleep(2)

    # Force a runtime restart. Colab will detect this.
    os.kill(os.getpid(), 9)

else:
    print(f"--- 'click' is already at the correct version ({required_click_version}). No action needed. ---")

# IMPORTANT: If a restart happens above, this part of the code will NOT be executed
# until the notebook is re-run AFTER the restart.

