from io import BufferedIOBase, RawIOBase
from drb.core.node import DrbNode
from drb.nodes.abstract_node import AbstractNode
from drb.core.path import ParsedPath
from drb.exceptions.core import DrbNotImplementationException
from deprecated import deprecated
from typing import Dict, List, Optional, Any, Tuple, Union, IO
import json
from pathlib import Path


class JsonNode(AbstractNode):
    """
    This class represents a single node of a tree
    of data. When a node has one or several children he has no value.

    Parameters:
            path (Union[str, Dict]): The path to the json \
            file or a dictionary representing the data.
            parent (DrbNode): The parent of this node (default: None).
            data : The json data (default: None).
    """

    def __init__(self, path: Union[str, Dict, list],
                 parent: DrbNode = None, data=None):
        super().__init__()
        if data is not None:
            self._data = data
            self.name = Path(path).name
            self._path = ParsedPath(path)
        elif isinstance(path, dict) or isinstance(path, list):
            self._data = path
            self.name = None
            self._path = ParsedPath('/')
        elif isinstance(parent, JsonNode):
            self.name = Path(path).name
            self._path = ParsedPath(path)
            self._data = None
        else:
            with open(path) as jsonFile:
                self._data = json.load(jsonFile)
                jsonFile.close()
                self.name = Path(path).name
                self._path = ParsedPath(path)

        self._available_impl += [dict, str, list]
        self.parent = parent
        self._children = None
        self.value = self._data

    @property
    def path(self) -> ParsedPath:
        return self._path

    def get_impl(self, impl: type, **kwargs) -> Any:
        if self.has_impl(impl):
            if impl == dict:
                return json.load(self._data)
            elif impl == list:
                if isinstance(self._data, list):
                    return self._data
                return [self._data]
            elif impl == BufferedIOBase:
                return json.dumps(self._data).encode('utf-8')
            else:
                return json.dumps(self._data)

        raise DrbNotImplementationException(
            f"JsonNode doesn't implement {impl}")

    def has_child(self, name: str = None, namespace: str = None) -> bool:
        if namespace:
            return False
        if name:
            if isinstance(self._data, dict):
                for e in self._data.keys():
                    if e == name:
                        return True
                    return False
            if isinstance(self._data, list):
                for e in self._data:
                    if e == name:
                        return True
                    return False
        return isinstance(self._data, dict) or isinstance(self._data, list)

    @property
    @deprecated(version='1.2.0',
                reason='Only bracket browse should be use')
    def children(self) -> List[DrbNode]:
        if self._children is None:
            self._children = []
            if self.has_child():
                if isinstance(self._data, list):
                    self._children = [
                        JsonNode(path=self.path.path,
                                 parent=self,
                                 data=e)
                        for e in self._data]
                else:
                    for e in self._data.keys():
                        if isinstance(self._data[e], list):
                            for x in self._data[e]:
                                self._children.append(
                                    JsonNode(
                                        path=Path(self.path.path).joinpath(e)
                                        .as_posix(),
                                        parent=self,
                                        data=x)
                                )
                        else:
                            self._children.append(
                                JsonNode(
                                    path=Path(self.path.path).joinpath(e)
                                    .as_posix(),
                                    parent=self,
                                    data=self._data[e])
                            )
            else:
                self._children = []
        return self._children

    def __setitem__(self, key, value):
        raise NotImplementedError(
            'Not supported in this version of drb-driver-json')

    def __delitem__(self, key):
        raise NotImplementedError(
            'Not supported in this version of drb-driver-json')


class JsonBaseNode(AbstractNode):
    """
    This class represents a single node of a tree
    of data. When the data came from another implementation.

    Parameters:
            node (DrbNode): The node where the json data came from.
            source (Union[BufferedIOBase, RawIOBase, IO]): The json data.
    """

    def __init__(self,
                 node: DrbNode,
                 source: Union[BufferedIOBase, RawIOBase, IO]):
        super().__init__()
        self.base_node = node
        self.source = source
        json_root = json.load(source)
        self.json_node = JsonNode(node.path.path, parent=self, data=json_root)

    @property
    def name(self) -> str:
        return self.base_node.name

    def impl_capabilities(self) -> List[type]:
        return self.base_node._available_impl.copy()

    def attribute_names(self):
        return self.base_node.attribute_names()

    @property
    def namespace_uri(self) -> Optional[str]:
        return self.base_node.namespace_uri

    @property
    def value(self) -> Optional[Any]:
        return self.base_node.value

    @property
    def path(self) -> ParsedPath:
        return self.base_node.path

    @property
    def parent(self) -> Optional[DrbNode]:
        return self.base_node.parent

    @property
    @deprecated(version='1.2.0',
                reason='Usage of the @ operator is recommended')
    def attributes(self) -> Dict[Tuple[str, str], Any]:
        return self.base_node.attributes

    @property
    @deprecated(version='1.2.0', reason='Only bracket browse should be use')
    def children(self) -> List[DrbNode]:
        return [self.json_node]

    def has_child(self, name: str = None, namespace: str = None) -> bool:
        if name and self.json_node.name == name:
            return True
        elif namespace:
            return False
        return True

    @deprecated(version='1.2.0',
                reason='Usage of the @ operator is recommended')
    def get_attribute(self, name: str) -> Any:
        return self.base_node.get_attribute(name)

    def has_impl(self, impl: type) -> bool:
        return self.base_node.has_impl(impl)

    def get_impl(self, impl: type, **kwargs) -> Any:
        return self.base_node.get_impl(impl)

    def __setitem__(self, key, value):
        raise NotImplementedError(
            'Not supported in this version of drb-driver-json')

    def __delitem__(self, key):
        raise NotImplementedError(
            'Not supported in this version of drb-driver-json')

    def close(self) -> None:
        if self.source:
            self.source.close()
        self.base_node.close()
