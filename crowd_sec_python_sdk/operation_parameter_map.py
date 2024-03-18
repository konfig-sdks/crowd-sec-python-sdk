operation_parameter_map = {
    '/decisions/stream-GET': {
        'parameters': [
            {
                'name': 'startup'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'origins'
            },
            {
                'name': 'scenarios_containing'
            },
            {
                'name': 'scenarios_not_containing'
            },
        ]
    },
    '/decisions/stream-HEAD': {
        'parameters': [
            {
                'name': 'startup'
            },
        ]
    },
    '/decisions-GET': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'value'
            },
            {
                'name': 'type'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'range'
            },
            {
                'name': 'contains'
            },
            {
                'name': 'origins'
            },
            {
                'name': 'scenarios_containing'
            },
            {
                'name': 'scenarios_not_containing'
            },
        ]
    },
    '/decisions-HEAD': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'value'
            },
            {
                'name': 'type'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'range'
            },
            {
                'name': 'contains'
            },
        ]
    },
    '/watchers/login-POST': {
        'parameters': [
            {
                'name': 'machine_id'
            },
            {
                'name': 'password'
            },
            {
                'name': 'scenarios'
            },
        ]
    },
    '/alerts-POST': {
        'parameters': [
        ]
    },
    '/alerts/{alert_id}-DELETE': {
        'parameters': [
            {
                'name': 'alert_id'
            },
        ]
    },
    '/alerts/{alert_id}-GET': {
        'parameters': [
            {
                'name': 'alert_id'
            },
        ]
    },
    '/alerts/{alert_id}-HEAD': {
        'parameters': [
            {
                'name': 'alert_id'
            },
        ]
    },
    '/alerts-GET': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'value'
            },
            {
                'name': 'scenario'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'range'
            },
            {
                'name': 'since'
            },
            {
                'name': 'until'
            },
            {
                'name': 'simulated'
            },
            {
                'name': 'has_active_decision'
            },
            {
                'name': 'decision_type'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'origin'
            },
        ]
    },
    '/watchers-POST': {
        'parameters': [
            {
                'name': 'machine_id'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/alerts-DELETE': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'value'
            },
            {
                'name': 'scenario'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'range'
            },
            {
                'name': 'since'
            },
            {
                'name': 'until'
            },
            {
                'name': 'has_active_decision'
            },
            {
                'name': 'alert_source'
            },
        ]
    },
    '/decisions/{decision_id}-DELETE': {
        'parameters': [
            {
                'name': 'decision_id'
            },
        ]
    },
    '/decisions-DELETE': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'value'
            },
            {
                'name': 'type'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'range'
            },
            {
                'name': 'scenario'
            },
        ]
    },
    '/alerts-HEAD': {
        'parameters': [
            {
                'name': 'scope'
            },
            {
                'name': 'value'
            },
            {
                'name': 'scenario'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'range'
            },
            {
                'name': 'since'
            },
            {
                'name': 'until'
            },
            {
                'name': 'simulated'
            },
            {
                'name': 'has_active_decision'
            },
            {
                'name': 'decision_type'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'origin'
            },
        ]
    },
};