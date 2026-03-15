import os
import json
import requests
import pytest
from pathlib import Path

from langchain_openai import ChatOpenAI
from ragas.metrics import ContextPrecision
from ragas.llms import LangchainLLMWrapper
from ragas.dataset_schema import SingleTurnSample


os.environ["OPENAI_API_KEY"] = "your_api_key"


@pytest.fixture
def llm_wrapper():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    llm_langwrapper = LangchainLLMWrapper(llm)
    return llm_langwrapper


@pytest.fixture
def getData(request):
    test_data = request.param

    responseDict = get_llm_response(test_data)

    sample = SingleTurnSample(
        user_input=responseDict["question"],
        response=responseDict["answer"],
        retrieved_contexts=[
            responseDict["retrieved_documents"][0]["page_content"]
        ]
    )

    return sample


@pytest.mark.parametrize("getData", load_test_data("testdata.json"), indirect=True)
@pytest.mark.asyncio
async def test_context_precision(llm_wrapper, getData):

    context_precision = ContextPrecision(llm=llm_wrapper)

    score = await context_precision.single_turn_ascore(getData)

    assert score > 0.7


def load_test_data(filename):
    project_directory = Path(__file__).parent.absolute()
    test_data_path = project_directory / "testdata" / filename

    with open(test_data_path, "r") as f:
        return json.load(f)


def get_llm_response(test_data):

    response = requests.post(
        "https://rahulshettyacademy.com/llm",
        json={
            "question": test_data["question"],
            "chat_history": []
        }
    )

    return response.json()
