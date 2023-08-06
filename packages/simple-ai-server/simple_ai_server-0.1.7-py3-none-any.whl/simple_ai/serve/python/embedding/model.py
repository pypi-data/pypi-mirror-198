from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class LanguageModel:
    def embed(self, 
        inputs: list=[],
    ) -> str:
        # TODO : implement method for your LLM
        return []