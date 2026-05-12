import sys

sys.path.append("C:/Users/AYUSH\Desktop/FileSummarizer")
import AuthenticatorService.authenticator_service as authenticator_service
import FileService.file_service as file_service
import LLMService.llm_service as llm_service
import prompts as prompt
import config as config 

import pandas as pd
import yaml
import sys
sys.path.append("C:/Users/AYUSH\Desktop/FileSummarizer")

class FileSummarizerService :

# main method
    def generate_summary(self):
        try :

            _service = authenticator_service.AuthenticatorService().authenticate_drive()
            _files = authenticator_service.AuthenticatorService().list_files(_service, config.folder_id)
            _results = []

            for _file in _files:
                print("FILENAME:", _file)
                _file_name = _file['name']
                if not (
                    _file_name.endswith(".pdf")
                    or _file_name.endswith(".docx")
                    or _file_name.endswith(".txt")
                ):
                    continue

                _path = authenticator_service.AuthenticatorService().download_file(
                    _service,
                    _file['id'],
                    _file_name
                )
                print("path", _path)

                _text = file_service.FileService().extract_file_contentt(_path)
                _text = _text[:10000] # grok model cannot handle large context
                _prompt = yaml.safe_load(open("C:/Users/AYUSH/Desktop/FileSummarizer/prompts/file_summarizer.yml"))["file_summarizer"]
                _formatted_prompt = _prompt.format(content = _text)
                _summary = llm_service.LLMService(llm_provider = config.llm_provider).generate_result(_formatted_prompt)

                _results.append({
                    "filename": _file_name,
                    "summary": _summary
                })

            _df = pd.DataFrame(_results)
            _df.to_csv("summaries.csv", index=False)
            print("\n results", _results)
            return _results
        
        except Exception as ex:
            print("Exception is :", str(ex))
            _results.append({
                    "filename": None,
                    "summary": None
                })
            return _results
"""
FileSummarizerService().generate_summary()
"""