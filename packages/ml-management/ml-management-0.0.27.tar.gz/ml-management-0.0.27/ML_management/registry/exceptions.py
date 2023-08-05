"""Custom exception definition (necessary for RegistryManager)."""


class VersionNotFound(Exception):
    """Define Version Not Found Exception."""

    def __init__(self, model_name: str, version: str):
        self.model_name = model_name
        self.version = version
        self.message = f'There is no version "{self.version}" for model "{self.model_name}"'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (VersionNotFound, (self.model_name, self.version))


class MetricNotLogged(Exception):
    """Define Metric Not Logged exception."""

    def __init__(self, model_name: str, metric: str):
        self.model_name = model_name
        self.metric = metric
        self.message = f'Metric "{self.metric}" is not logged for model "{self.model_name}"'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (MetricNotLogged, (self.model_name, self.metric))


class ModelNotRegistered(Exception):
    """Define Model Not Registered exception."""

    def __init__(self, model_name: str):
        self.model_name = model_name
        self.message = f'Model "{self.model_name}" is not registered'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (ModelNotRegistered, (self.model_name))


class NoMetricProvided(Exception):
    """Define No Metric Provided exception."""

    def __init__(self, criteria: str):
        self.criteria = criteria
        self.message = f'Choice criteria "{self.criteria}" is passed, but no metric name is provided'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (NoMetricProvided, (self.criteria))


class UnsupportedCriteria(Exception):
    """Define Unsupported Criteria exception."""

    def __init__(self, criteria: str, supported_criteria: list):
        self.criteria = criteria
        self.supported_criteria = supported_criteria
        self.message = f'Choice criteria "{self.criteria}" is unsupported, must be one of: {self.supported_criteria}'
        super().__init__(self.message)

    def __reduce__(self):
        """Define reduce method to make exception picklable."""
        return (UnsupportedCriteria, (self.criteria, self.supported_criteria))
