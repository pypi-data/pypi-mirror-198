"""A collection of decorators to modify rule docstrings for Sphinx.

NOTE: All of these decorators are deprecated from SQLFluff 2.0.0 onwards.

They are still included to allow a transition period, but the functionality
is now packaged in the BaseRule class via the RuleMetaclass.
"""

from sqlfluff.core.rules.base import rules_logger  # noqa


def document_fix_compatible(cls):
    """Mark the rule as fixable in the documentation."""
    rules_logger.warning(
        f"{cls.__name__} uses the @document_fix_compatible decorator "
        "which is deprecated in SQLFluff 2.0.0. Remove the decorator "
        "to resolve this warning."
    )
    return cls


def document_groups(cls):
    """Mark the rule as fixable in the documentation."""
    rules_logger.warning(
        f"{cls.__name__} uses the @document_groups decorator "
        "which is deprecated in SQLFluff 2.0.0. Remove the decorator "
        "to resolve this warning."
    )
    return cls


def document_configuration(cls, **kwargs):
    """Add a 'Configuration' section to a Rule docstring."""
    rules_logger.warning(
        f"{cls.__name__} uses the @document_configuration decorator "
        "which is deprecated in SQLFluff 2.0.0. Remove the decorator "
        "to resolve this warning."
    )
    return cls
