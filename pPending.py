#!/usr/bin/python

from hzdiag.pendingnvocationsplotter import PendingInvocationPlotter

pending_invocations_template = """
<html>
    <head>
        <title>Pending Invocations</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
    <body>
        <h1> Pending Invocations per Member </h1>
        {{#data}}
            <h2>{{name}}</h2>
            {{{plot}}}
        {{/data}}
    </body>
</html>
"""

PendingInvocationPlotter().plot(pending_invocations_template)