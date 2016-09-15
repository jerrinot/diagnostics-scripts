#!/usr/bin/python

from hzdiag.simplemtricplotter import SimpleMetricPlotter

pending_invocations_template = """
<html>
    <head>
        <title>Simple Metrics</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        </head>
    <body>
        <a id="toc">
            <h1>Metrics</h1>
        <a/>
        <ul>
            {{#data}}
                <li><a href="#{{name}}">{{name}}</a>
            {{/data}}
        </ul>
        {{#data}}
            <a id="{{name}}"><h2>{{name}}</h2></a>
            {{{plot}}}
            <a href="#toc">[Table of Content]</a>
        {{/data}}
    </body>
</html>t
"""

# SimpleMetricPlotter('operation.invocations.pending').plot(pending_invocations_template)
SimpleMetricPlotter([   'operation.completedCount',
                        'operation.queueSize',
                        'operation.priorityQueueSize',
                        'operation.responseQueueSize',
                        'operation.runningPartitionCount',
                        'operation.runningGenericCount',
                        'operation.invocations.responses[normal]',
                        'operation.invocations.responses[backup]',
                        'operation.invocations.responses[error]',
                        'operation.invocations.responses[missing]',
                        'operation.invocations.responses[timeout]',
                        'operation.invocations.heartbeatPacketsReceived',
                        'operation.invocations.backupTimeouts',
                        'cluster.clock.clusterTimeDiff',
                        'event.eventQueueSize',
                        'event.totalFailureCount',
                        'executor.[hz:async].completedTaskCount',
                        'executor.[hz:client].completedTaskCount',
                        'executor.[hz:scheduled].completedTaskCount',
                        'partitions.replicaSyncRequestsCounter',
                        'gc.majorTime',

                        'tcp.inputThread[hz._hzInstance_1_workers.IO.thread-in-0].eventCount',
                        'tcp.inputThread[hz._hzInstance_1_workers.IO.thread-in-1].eventCount',
                        'tcp.inputThread[hz._hzInstance_1_workers.IO.thread-in-2].eventCount',
                        'tcp.outputThread[hz._hzInstance_1_workers.IO.thread-out-0].eventCount',
                        'tcp.outputThread[hz._hzInstance_1_workers.IO.thread-out-1].eventCount',
                        'tcp.outputThread[hz._hzInstance_1_workers.IO.thread-out-2].eventCount',

                        'operation.thread[hz._hzInstance_1_workers.generic-operation.thread-0].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.generic-operation.thread-1].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.generic-operation.thread-2].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.generic-operation.thread-3].completedTotalCount',

                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-0].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-1].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-2].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-3].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-4].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-5].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-6].completedTotalCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-7].completedTotalCount',

                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-0].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-1].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-2].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-3].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-4].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-5].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-6].normalPendingCount',
                        'operation.thread[hz._hzInstance_1_workers.partition-operation.thread-7].normalPendingCount'



                     ]).plot(pending_invocations_template)
