from .main import BinnewZ

def start():
    return BinnewZ()

config = [{
    'name': 'binnewz',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'nzb_providers',
            'name': 'binnewz',
            'description': 'Communaute francophone de referencement des newsgroups binaires. See <a href="http://www.binnews.in/">BinnewZ</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': True,
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 0,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
