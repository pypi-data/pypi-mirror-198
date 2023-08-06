import numpy as np
from entities.calculation_models import Footprintable
from entities.const import Scopes


class FootprintExecutor():
    """
    the *only* purpose of this class is to calculate intensity & contribution at COMPANY LEVEL

    NOTE:
    for WACI: attribution=weight
    for TCE: attribution=position / attribution
    for OE: attribution=ownership
    """
    def __init__(self, footprintable: Footprintable) -> None:
        self.footprintable = footprintable

    def contribution(self):
        # run intensity calc
        self.intensity()
        # calculate contribution
        for scope in Scopes.to_list():
            contribution = None
            try:
                contribution = getattr(self.footprintable.intensity, scope) * self.footprintable.attribution
            except TypeError:
                contribution = np.nan
            setattr(self.footprintable.contribution, scope, contribution)


class WACI(FootprintExecutor):
    """
    at company level:
        intensity = emissions / fundamental
        contribution = weighted * intensity
    """
    def __init__(self, footprintable: Footprintable) -> None:
        super().__init__(footprintable)

    def _set_attribution(self):
        self.footprintable.attribution = None
        self.footprintable.attribution = self.footprintable.weight

    def intensity(self):
        self._set_attribution()

        for scope in Scopes.to_list():
            intensity = None
            emissions = None
            try:
                emissions = getattr(self.footprintable.emissions, scope)
                intensity = emissions / self.footprintable.fundamental
            except (TypeError, ZeroDivisionError):
                intensity = getattr(self.footprintable.intensity, scope)

            # intensity being nan or None means that some value emissions or fundamental is missing. 
            # use median intensity
            if not intensity or np.isnan(intensity):
                pass
            else:
                setattr(self.footprintable.intensity, scope, intensity)


class TCE(FootprintExecutor):
    """
    NOTE: this isn't technically the right terminology but it works for standardising the calculations in this class:
        "intensity" = emissions
        attribution_factor = nav nok / evic
        contribution = attribution_factor * "intensity"
    """
    def __init__(self, footprintable: Footprintable) -> None:
        super().__init__(footprintable)

    def _set_attribution(self):
        self.footprintable.attribution = None
        attribution = None
        try:
            # nav nok = outstanding amount, fundamental = evic or mcap
            attribution = self.footprintable.nav_nok / self.footprintable.fundamental
            # if evic is not availabe, ownership alltogether needs to be replaced with pf_ownership
        except (TypeError, ZeroDivisionError):
            attribution = self.footprintable.ownership

        if attribution is None or np.isnan(attribution):
            attribution = self.footprintable.ownership

        self.footprintable.attribution = attribution
        return

    def intensity(self):
        self._set_attribution()

        for scope in Scopes.to_list():
            intensity = None
            intensity = getattr(self.footprintable.emissions, scope, np.nan)
            setattr(self.footprintable.intensity, scope, intensity)


class OE(FootprintExecutor):
    """
    at company level:
    ownership = ownership as calculated in data model
    NOTE: this isn't technically the right terminology but it works for standardising the calcs:
        intensity = emissions
        contribution = ownership * intensity
    """
    def __init__(self, footprintable: Footprintable) -> None:
        super().__init__(footprintable)

    def _set_attribution(self):
        self.footprintable.attribution = self.footprintable.ownership
        return

    def intensity(self):
        self._set_attribution()

        for scope in Scopes.to_list():
            intensity = None
            intensity = getattr(self.footprintable.emissions, scope, np.nan)
            setattr(self.footprintable.intensity, scope, intensity)
