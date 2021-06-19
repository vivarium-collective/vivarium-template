"""
================================================
Toy Injected Glucose Phosphorylation Compartment
================================================

This is a toy example referenced in the documentation.
"""

# TODO: Delete this file before publishing your project.

from vivarium.core.engine import Engine
from vivarium.core.composer import Composer
from vivarium.library.pretty import format_dict
from vivarium.processes.injector import Injector

from template.processes.glucose_phosphorylation import GlucosePhosphorylation


class InjectedGlcPhosphorylation(Composer):

    defaults = {
        'glucose_phosphorylation': {
            'k_cat': 1e-2,
        },
        'injector': {
            'substrate_rate_map': {
                'GLC': 1e-4,
                'ATP': 1e-3,
            },
        },
    }

    def __init__(self, config):
        super().__init__(config)

    def generate_processes(self, config):
        injector = Injector(self.config['injector'])
        glucose_phosphorylation = GlucosePhosphorylation(
            self.config['glucose_phosphorylation'])

        return {
            'injector': injector,
            'glucose_phosphorylation': glucose_phosphorylation,
        }

    def generate_topology(self, config):
        return {
            'injector': {
                'internal': ('cell', ),
            },
            'glucose_phosphorylation': {
                'cytoplasm': ('cell', ),
                'nucleoside_phosphates': ('cell', ),
                'global': ('global', ),
            },
        }
