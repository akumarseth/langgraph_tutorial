from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

class LLMFactory:
    def __init__(self):
        self.llm = None


    def get_llm(self) -> AzureChatOpenAI:

        api_key = os.getenv("AZURE_OPENAI_KEY")
        api_version = os.getenv("AZURE_OPENAI_VERSION", "2024-02-15-preview")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        azure_deployment = (
            os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
            or os.getenv("AZURE_OPENAI_DEPLOYMENT")
        )

        # ---- Validation ----
        missing = []
        if not api_key:
            missing.append("AZURE_OPENAI_KEY")
        if not azure_endpoint:
            missing.append("AZURE_OPENAI_ENDPOINT")
        if not azure_deployment:
            missing.append("AZURE_OPENAI_DEPLOYMENT_NAME")

        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

        # Normalize endpoint
        azure_endpoint = azure_endpoint.rstrip("/")

        return AzureChatOpenAI(
            api_key=api_key,
            api_version=api_version,
            azure_endpoint=azure_endpoint,
            azure_deployment=azure_deployment,
            temperature=0.0,
        )
