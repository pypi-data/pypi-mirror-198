"""Interface artificial intelligence."""

import collections
import re
import textwrap

import black
import openai
import web
import webagt

app = web.application(__name__, prefix="ai")
openai.api_key = app.cfg.get("OPENAI_KEY")


@app.control("")
class AI:
    """AI."""

    def get(self):
        """Return an index of data sources."""
        models = openai.Model.list()
        return app.view.index(models)


@app.control("chat")
class Chat:
    """OpenAI ChatGPT."""

    def get(self):
        """."""
        return app.view.chat()

    def post(self):
        """."""
        form = web.form("request")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": form.request},
            ],
            max_tokens=500,
        )
        response_text = response.choices[0].message.content

        def highlight(matchobj):
            language, _, code = matchobj.group(1).partition("\n")
            code = textwrap.dedent(code)
            filename = ".sh"
            if language == "python":
                code = black.format_str(code, mode=black.Mode())
                filename = ".py"
            return web.slrzd.highlight(code, filename)

        output = web.mkdn(
            re.sub("```(.+?)```", highlight, response_text, flags=re.DOTALL)
        )
        return app.view.chat_response(form.request, response, output)
