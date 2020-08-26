c.KubeSpawner.profile_list = [
    {
        'display_name': 'Minimal Notebook (RHEL 7 / Python 3.6)',
        'kubespawner_override': {
            'image': 's2i-minimal-notebook-py36:2.5.1-rc1'
        }
    },
    {
        'display_name': 'Minimal Notebook (Fedora 31 / Python 3.7)',
        'kubespawner_override': {
            'image': 's2i-minimal-notebook-py37:2.5.1-rc1'
        }
    },
    {
        'display_name': 'Minimal Notebook (Fedora 32 / Python 3.8)',
        'default': True,
        'kubespawner_override': {
            'image': 's2i-minimal-notebook-py38:2.5.1-rc1',
            'supplemental_gids': [0, 100, 1000, 1001, 1002]
        }
    }
]
