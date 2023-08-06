OpenAI API Wrapper for Advanced ChatGPT Development
===================================================

This Python package provides a comprehensive and efficient wrapper for the OpenAI API, designed to support advanced application development based on ChatGPT. The package simplifies the integration process and offers additional functionalities such as conversation management, model fine-tuning, retrieval of embeddings, automatic question generation, and offline model execution.

Features
--------

* Easy interaction with the OpenAI API for ChatGPT applications
* Conversation management for multiple chat sessions
* Support for fine-tuning the ChatGPT model
* Retrieval of embeddings for specific text passages
* Automatic question generation for given paragraphs
* Offline model execution with compatible models

Installation
------------

You can install the package using pip:

`pip install openai-api-wrapper`

Usage
-----

Here is a basic example of how to use the OpenAI API Wrapper:

python

```python
    from openai_api_wrapper import Chatbot

    # Initialize the Chatbot instance
    chatbot = ChatBot()

    # Generate a reply_contentto the given prompt.
    conversation_id = "conversation_1"
    prompt = "What is the capital of France?"
    print(f"[{conversation_id}] User message: {prompt}")

    reply_content= chatbot.ask(conversation_id, prompt)

    print(f"[{conversation_id}] AI Response: {reply_content}")
    conversation_turns = chatbot.get_conversation_turns(conversation_id)
    print(f"[{conversation_id}] Conversation turns: {conversation_turns}")

    # Generate a reply_contentto the given prompt using streaming API.
    conversation_id = "conversation_2"
    prompt = "Tell me a joke."
    print(f"[{conversation_id}] User message: {prompt}")

    unfinished_reply_content= ""
    for chunked_reply_content in chatbot.ask_stream(conversation_id, prompt):
        unfinished_reply_content+= chunked_reply_content
        print(unfinished_reply_content)
    reply_content= chatbot.get_last_reply_content(conversation_id)

    print(f"[{conversation_id}] AI Response: {reply_content}")
    conversation_turns = chatbot.get_conversation_turns(conversation_id)
    print(f"[{conversation_id}] Conversation turns: {conversation_turns}")
```

For a more detailed example with all the available features, check out the `example.py` file in the repository.

Documentation
-------------

You can find the complete documentation for this package in the `docs` folder, or check out the source code for more details on the implementation.

Roadmap
-------

We plan to continually improve and expand the functionality of this package. Some of the upcoming features include:

* Integration with various machine learning frameworks
* Support for multi-modal inputs (e.g., text, images, audio)
* Expansion of available pre-trained models
* Simplified deployment options for various platforms

Contributing
------------

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your changes (`git checkout -b my-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push the branch (`git push origin my-feature`)
5. Create a new pull request

Please make sure to add tests and documentation for any new features or changes.

License
-------

This project is licensed under the MIT License. See the `LICENSE` file for more details.
