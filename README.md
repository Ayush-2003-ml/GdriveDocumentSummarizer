This goal of this project is to fetch google drive documents from a particular google drive folder and summarize the content of the documents including it's main topic and key points. The code is divided into multiple modules for increasing code reproducibility and integrate plugin play features.

Steps undertaken:
1. AuthenticatorService : The purpose of this module is to authenticate with google drive service using oauth2 , list files    inside a particular folder and download the file content locally.

2. FileService: The purpose of this module is to extract file content using pymupdf library.

3. LLMService: This module generates summaries using LLM. Using LLMProvider variable in the constructor we can decide which LLM to use for generating summaries.

4. FileSummarizerService: This is the main module to generate summaries using all other modules.

5. config: Most of the code is config driven so that minimal changes are made inside the source code . API_key, Oauth Credentials, Folder Id, LLM Provider, Source are config driven.