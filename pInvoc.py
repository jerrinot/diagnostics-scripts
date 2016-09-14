#!/usr/bin/python

from hzdiag.hzdiag import Hzdiag

invocation_history_template = """
<html>
    <head>
        <title>Invocations Analysis</title>
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

Hzdiag().plotInvocations(invocation_history_template)