import enum

import lps_ml.datasets.synthetic as ml_syn
import lps_ml.datasets.selection as ml_sel

class SyntheticExperiment(enum.Enum):
    DEPTH = enum.auto()
    BOTTOM = enum.auto()
    DYNAMIC = enum.auto()
    SEASON = enum.auto()
    VOLUME = enum.auto()

    def get_filters(self) -> dict[str, ml_sel.Filter]:

        if self == SyntheticExperiment.DEPTH:
            return {
                "shallow": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SHALLOW_WATER",
                        "value": ["yes"]
                    },
                    remove_elements_in = False
                ),
                "deep": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SHALLOW_WATER",
                        "value": ["no"]
                    },
                    remove_elements_in = False
                )
            }

        if self == SyntheticExperiment.BOTTOM:
            return {
                "basalt": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SEABED",
                        "value": ["Basalt"]
                    },
                    remove_elements_in = False
                ),
                "clay": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SEABED",
                        "value": ["Clay"]
                    },
                    remove_elements_in = False
                ),
                "gravel": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SEABED",
                        "value": ["Gravel"]
                    },
                    remove_elements_in = False
                ),
                "sand": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SEABED",
                        "value": ["Sand"]
                    },
                    remove_elements_in = False
                ),
                "silt": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SEABED",
                        "value": ["Silt"]
                    },
                    remove_elements_in = False
                ),
            }

        if self == SyntheticExperiment.DYNAMIC:
            return {
                "fixed distance": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "DYNAMIC_TYPE",
                        "value": ["fixed_distance"]
                    },
                    remove_elements_in = False
                ),
                "cpa in": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "DYNAMIC_TYPE",
                        "value": ["cpa_in"]
                    },
                    remove_elements_in = False
                ),
                "cpa out": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "DYNAMIC_TYPE",
                        "value": ["cpa_out"]
                    },
                    remove_elements_in = False
                ),
            }

        if self == SyntheticExperiment.SEASON:
            return {
                "summer": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "Season",
                        "value": ["Summer"]
                    },
                    remove_elements_in = False
                ),
                "autumn": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "Season",
                        "value": ["Autumn"]
                    },
                    remove_elements_in = False
                ),
                "winter": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "Season",
                        "value": ["Winter"]
                    },
                    remove_elements_in = False
                ),
                "spring": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "Season",
                        "value": ["Spring"]
                    },
                    remove_elements_in = False
                ),
            }

        if self == SyntheticExperiment.VOLUME:
            return {
                "reference": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SCENARIO_CATALOG_ID",
                        "value": [14, 3]
                    },
                    remove_elements_in = False
                ),
                "non reference": ml_sel.ConstraintFilter(
                    constraints={
                        "header": "SCENARIO_CATALOG_ID",
                        "value": [14, 3]
                    },
                    remove_elements_in = True
                ),
            }

        raise NotImplementedError(f"get_filters not implemented for {self}.")

    def get_dynamic_selection(self) -> ml_syn.DynamicSelection:
        return ml_syn.DynamicSelection.ALL

    def get_channel_selection(self) -> ml_syn.ChannelSelection:
        if self in [SyntheticExperiment.BOTTOM, SyntheticExperiment.SEASON]:
            return ml_syn.ChannelSelection.NON_REFERENCE_ONLY
        return ml_syn.ChannelSelection.ALL
