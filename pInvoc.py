#!/usr/bin/python

from hzdiag.invocationplotter import InvocationPlotter

invocation_history_template = """
<html>
    <head>
        <title>Invocations Analysis</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
    <body>
        <h1> Invocation History per Member </h1>
        {{#data}}
            <h2>{{name}}</h2>
            {{{plot}}}
        {{/data}}
    </body>
</html>
"""

InvocationPlotter().plot(invocation_history_template)