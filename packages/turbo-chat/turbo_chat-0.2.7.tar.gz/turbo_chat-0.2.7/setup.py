# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['turbo_chat',
 'turbo_chat.bots',
 'turbo_chat.bots.subqueries',
 'turbo_chat.bots.tool',
 'turbo_chat.cache',
 'turbo_chat.memory',
 'turbo_chat.structs',
 'turbo_chat.types',
 'turbo_chat.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.4,<4.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'jinja2schema>=0.1.4,<0.2.0',
 'jsonschema>=4.17.3,<5.0.0',
 'lemminflect>=0.2.3,<0.3.0',
 'openai>=0.27.0,<0.28.0',
 'parse>=1.19.0,<2.0.0',
 'pydantic>=1.10.5,<2.0.0',
 'tenacity>=8.2.2,<9.0.0',
 'tiktoken>=0.3.1,<0.4.0']

setup_kwargs = {
    'name': 'turbo-chat',
    'version': '0.2.7',
    'description': 'Idiomatic way to build chatgpt apps using async generators in python',
    'long_description': '# turbo-chat\n\n> Idiomatic way to build chatgpt apps using async generators in python\n\n![turbo](https://user-images.githubusercontent.com/931887/222912628-8662fad0-091f-4cb8-92f3-6cce287716e9.jpg)\n\n## About\n\nThe [ChatGPT API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) uses a new input format called [chatml](https://github.com/openai/openai-python/blob/main/chatml.md). In openai\'s [python client](https://github.com/openai/openai-python/blob/main/chatml.md), the format is used something like this:\n\n```python\nmessages = [\n    {"role": "system", "content": "Greet the user!"},\n    {"role": "user", "content": "Hello world!"},\n]\n```\n\nThe idea here is to incrementally build the messages using an async generator and then use that to generate completions. [Async generators](https://superfastpython.com/asynchronous-generators-in-python/) are incredibly versatile and simple abstraction for doing this kind of stuff. They can also be composed together very easily.\n\n```python\n# Equivalent turbo-chat generator\nasync def example():\n    yield System(content="Greet the user!")\n    yield User(content="Hello World!")\n\n    # To run generation, just yield Generate(),\n    # the lib will take care of correctly running the app, and\n    # return the value back here.\n    output = yield Generate()\n    print(output.content)\n```\n\nSee more detailed example below.\n\n## Installation\n\n```bash\npip install turbo-chat\n```\n\n## Example\n\n```python\nfrom typing import AsyncGenerator, Union\n\nfrom turbo_chat import (\n    turbo,\n    System,\n    User,\n    Assistant,\n    GetInput,\n    Generate,\n    run,\n)\n\n# Get user\nasync def get_user(id):\n    return {"zodiac": "pisces"}\n\n# Set user zodiac mixin\n# Notice that no `@turbo()` decorator used here\nasync def set_user_zodiac(user_id: int):\n\n    user_data: dict = await get_user(user_id)\n    zodiac: str = user_data["zodiac"]\n\n    yield User(content=f"My zodiac sign is {zodiac}")\n\n\n# Horoscope app\n@turbo(temperature=0.0)\nasync def horoscope(user_id: int):\n\n    yield System(content="You are a fortune teller")\n\n    # Yield from mixin\n    async for output in set_user_zodiac(user_id):\n        yield output\n\n    # Prompt runner to ask for user input\n    input = yield GetInput(message="What do you want to know?")\n\n    # Yield the input\n    yield User(content=input)\n\n    # Generate (overriding the temperature)\n    value = yield Generate(temperature=0.9)\n\n# Let\'s run this\napp: AsyncGenerator[Union[Assistant, GetInput], str] = horoscope({"user_id": 1})\n\n_input = None\nwhile not (result := await run(app, _input)).done:\n    if result.needs_input:\n        # Prompt user with the input message\n        _input = input(result.content)\n        continue\n\n    print(result.content)\n\n# Output\n# >>> What do you want to know? Tell me my fortune\n# >>> As an AI language model, I cannot predict the future or provide supernatural fortune-telling. However, I can offer guidance and advice based on your current situation and past experiences. Is there anything specific you would like me to help you with?\n#\n\n```\n\n### Custom memory\n\nYou can also customize how the messages are persisted in-between the executions.\n\n```python\nfrom turbo_chat import turbo, BaseMemory\n\nclass RedisMemory(BaseMemory):\n    """Implement BaseMemory methods here"""\n\n    async def init(self, context) -> None:\n        ...\n\n    async def append(self, item) -> None:\n        ...\n\n    async def clear(self) -> None:\n        ...\n\n\n# Now use the memory in a turbo_chat app\n@turbo(memory_class=RedisMemory)\nasync def app():\n    ...\n```\n\n### Get access to memory object directly (just declare an additional param)\n\n```python\n@turbo()\nasync def app(some_param: Any, memory: BaseMemory):\n\n    messages = await memory.get()\n    ...\n```\n\n### Generate a response to use internally but don\'t yield downstream\n\n```python\n@turbo()\nasync def example():\n    yield System(content="You are a good guy named John")\n    yield User(content="What is your name?")\n    result = yield Generate(forward=False)\n\n    yield User(content="How are you doing?")\n    result = yield Generate()\n\nb = example()\nresults = [output async for output in b]\n\nassert len(results) == 1\n```\n\n### Add a simple in-memory cache\n\nYou can also subclass the `BaseCache` class to create a custom cache.\n\n```python\ncache = SimpleCache()\n\n@turbo(cache=cache)\nasync def example():\n    yield System(content="You are a good guy named John")\n    yield User(content="What is your name?")\n    result = yield Generate()\n\nb = example()\nresults = [output async for output in b]\n\nassert len(cache.cache) == 1\n\n```\n\n---\n\n### Latest Changes\n\n* version: 0.2.6. PR [#22](https://github.com/creatorrr/turbo-chat/pull/22) by [@creatorrr](https://github.com/creatorrr).\n* feat: Add summary memory. PR [#21](https://github.com/creatorrr/turbo-chat/pull/21) by [@creatorrr](https://github.com/creatorrr).\n* version: 0.2.5. PR [#20](https://github.com/creatorrr/turbo-chat/pull/20) by [@creatorrr](https://github.com/creatorrr).\n* version: 0.2.4. PR [#19](https://github.com/creatorrr/turbo-chat/pull/19) by [@creatorrr](https://github.com/creatorrr).\n* refactor: Move trucation logic to a separate memory class. PR [#18](https://github.com/creatorrr/turbo-chat/pull/18) by [@creatorrr](https://github.com/creatorrr).\n* version: 0.2.3. PR [#17](https://github.com/creatorrr/turbo-chat/pull/17) by [@creatorrr](https://github.com/creatorrr).\n* f/memory improvements. PR [#16](https://github.com/creatorrr/turbo-chat/pull/16) by [@creatorrr](https://github.com/creatorrr).\n* version: 0.2.2. PR [#15](https://github.com/creatorrr/turbo-chat/pull/15) by [@creatorrr](https://github.com/creatorrr).\n* f/tool bot. PR [#14](https://github.com/creatorrr/turbo-chat/pull/14) by [@creatorrr](https://github.com/creatorrr).\n* v/0.2.1. PR [#13](https://github.com/creatorrr/turbo-chat/pull/13) by [@creatorrr](https://github.com/creatorrr).\n* feat: Add count_tokens. PR [#12](https://github.com/creatorrr/turbo-chat/pull/12) by [@creatorrr](https://github.com/creatorrr).\n* Update README.md. PR [#11](https://github.com/creatorrr/turbo-chat/pull/11) by [@creatorrr](https://github.com/creatorrr).\n\n',
    'author': 'Diwank Singh Tomer',
    'author_email': 'singh@diwank.name',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
