from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.6)

def generate_movie_name(movie):
    # Chain 1: Recommended Movie
    prompt_template_name = PromptTemplate(
        input_variables=['movie'],
        template="Recommend a popular {movie}."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="movie_name")

    # Chain 2: Suggested Movie Names
    prompt_template_items = PromptTemplate(
        input_variables=['movie_name'],
        template="""Recommend 5 movies similar to {movie_name}. Return it as a comma separated string"""
    )

    movie_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="movies")

    chain = SequentialChain(
        chains=[name_chain, movie_chain],
        input_variables=['movie'],
        output_variables=['movie_name', "movies"]
    )

    response = chain({'movie': movie})

    return response

if __name__ == "__main__":
    print(generate_movie_name("Superman"))
