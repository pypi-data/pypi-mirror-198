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
    if environments is None:
        environments = []

    if isinstance(environments, (str, Node)):
        environments = [environments]

    node = iolanta.string_to_node(thing)
    environment_nodes = [
        iolanta.string_to_node(environment)
        for environment in environments
    ]

    if not environment_nodes:
        environment_nodes = [IOLANTA.html]

    response, _stack = iolanta.render(
        node=node,
        environments=environment_nodes,
    )

    return response
