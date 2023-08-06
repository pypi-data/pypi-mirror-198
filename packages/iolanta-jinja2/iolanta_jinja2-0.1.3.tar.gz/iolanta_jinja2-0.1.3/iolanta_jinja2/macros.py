from typing import List, Optional, Union

from iolanta.iolanta import Iolanta
from iolanta.namespaces import IOLANTA
from rdflib.term import Node, URIRef

Environments = Union[str, List[str]]


def template_render(
    thing: Union[str, Node],
    iolanta: Iolanta,
    environments: Optional[Environments] = None,
):
    """Macro to render something with Iolanta."""
    if isinstance(thing, str) and ':' not in thing:
        thing = f'local:{thing}'

    thing = iolanta.expand_qname(thing) or thing

    if isinstance(environments, str):
        environments = [environments]

    elif environments is None:
        environments = []

    environments = [
        URIRef(f'local:{environment}') if (
            isinstance(environment, str)
            and ':' not in environment
        ) else environment
        for environment in environments
    ]

    environments = [
        iolanta.expand_qname(environment) or environment
        for environment in environments
    ]

    if not environments:
        environments = [IOLANTA.html]

    response, _stack = iolanta.render(
        node=URIRef(thing) if (  # type: ignore  # noqa: WPS504
            not isinstance(thing, URIRef)
        ) else thing,
        environments=[URIRef(environment) for environment in environments],
    )

    return response
