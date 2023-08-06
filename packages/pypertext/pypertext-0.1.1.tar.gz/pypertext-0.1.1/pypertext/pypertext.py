import typing as t
from types import FunctionType
from numbers import Number
import inspect


def is_function(x: object):
    """Return True if x is a function."""
    return isinstance(x, FunctionType)


def is_method(obj: object) -> bool:
    """Check if `obj` is a method."""
    return inspect.ismethod(obj) or inspect.isfunction(obj)


def render_element(element: t.Dict[str, t.Any]) -> str:
    """Render an element dictionary to string.

    - Elements without a tag are treated as div
    - Attributes with None values are ignored
    - Attribute c is set to class attribute
    - Attribute for_ is set to for attribute
    - If a prop value has double quotes then it is wrapped in single quotes,
        otherwise it is wrapped in double quotes
    - If a child is a callable function then call it and treat the output as
        a string

    Args:
        element (dict): A dictionary with keys `tag`, `attrs`, and `children`.
            Children can be a string, an element dict, or a list including
            instances of strings, or callable functions.

    Returns:
        (str): html representation of the element
    """
    if is_function(element) or is_method(element):
        element = element()

    if element is None:
        return ""

    if isinstance(element, (str, Number, bool)):
        return str(element)

    # self-closing tags
    # fmt: off
    sct: t.Mapping[str, bool] = {
        k: True for k in [
            "meta", "link", "img", "br", "hr", "input", "area", 
            "base", "col", "embed", "command", "keygen", "param", "source", 
            "track", "wbr",
        ]
    }
    # fmt: on
    if isinstance(element, dict):
        tag: str = element.get("tag", "div")  # default to div
        attrs: dict = element.get("attrs", {})
        children: t.Any = element.get("children", [])
    else:
        raise TypeError(
            "element must be a dict, got type %s: %r" % (type(element), element)
        )
    # replace underscores with dashes in tag name
    tag = tag.replace("_", "-")
    # children is a dict containing an element-like structure (tag, attrs, children)
    if isinstance(children, dict):
        if "tag" in children:
            children = [children]
    _attrs: t.List[t.Any] = []
    attrs_str: str = ""
    if attrs is not None:
        for k, v in attrs.items():
            # "classname", "class_", "classes", "klass" attrs are converted to "class"
            if k in ["c"]:
                k = "class"
            if k == "for_":
                k = "for"
            # prop keys with underscores are converted to dashes
            k = k.replace("_", "-")
            # evaluate values that are callable functions
            if is_function(v) or is_method(v):
                v = v()
            if isinstance(v, bool):
                # boolean value only adds the key if True
                if v:
                    _attrs.append(k)
            else:
                if v is None:
                    # None value is skipped
                    continue
                # all other value types converted to string
                if not isinstance(v, str):
                    v = str(v)
                # handle the case where value contains double quotes by using
                # single quotes
                if '"' in v:
                    _attrs.append(f"{k}='{v}'")
                else:
                    _attrs.append(f'{k}="{v}"')
        attrs_str = " ".join(_attrs)
    # if attrs is not empty, prepend a space
    if len(attrs_str) > 0:
        attrs_str = " " + attrs_str
    if tag in sct:
        # self-closing tags have no children
        return f"<{tag}{attrs_str}/>"
    else:
        innerHTML: str = ""
        if children is None:
            innerHTML = ""
        elif isinstance(children, (str, Number, bool)):
            innerHTML = str(children)
        elif is_function(children) or is_method(children):
            innerHTML += str(children())
        elif isinstance(children, (list, tuple)):
            for child in children:
                innerHTML += render_element(child)
        return f"<{tag}{attrs_str}>{innerHTML}</{tag}>"


def render_document(
    body: t.Union[t.List, t.Callable] = [],
    *,
    title: t.Union[str, None] = None,
    head: t.List[dict] = [],
    body_kwargs: t.Mapping[str, str] = {},
    css_paths: t.Union[str, t.List[str]] = None,
) -> str:
    """Render a full html document.

    Args:
        children (list): list of children elements
        title (str): title of the document
        head (list): list of elements to include in the head
        use_htmx (bool): if True, import htmx and sweetalert2

    Returns:
        str: html document
    """
    if is_function(body) or is_method(body):
        body = body()
    _head = [
        dict(tag="meta", attrs={"charset": "utf-8"}),
        dict(
            tag="meta",
            attrs={
                "name": "viewport",
                "content": "width=device-width, initial-scale=1",
            },
        ),
        dict(tag="meta", attrs={"http-equiv": "X-UA-Compatible", "content": "IE=edge"}),
    ]
    if css_paths is not None:
        if isinstance(css_paths, str):
            css_paths = [css_paths]
        for css_path in css_paths:
            _head.append(
                dict(tag="link", attrs={"rel": "stylesheet", "href": css_path})
            )
    if title:
        _head.append(dict(tag="title", children=title))
    if isinstance(head, dict):
        head = [head]
    _head.extend(head)
    container = [
        dict(tag="head", children=_head),
        dict(tag="body", children=body, attrs=body_kwargs),
    ]
    html = ["<!DOCTYPE html>"]
    html.append("<html>")
    for elem in container:
        html.append(render_element(elem))
    html.append("</html>")
    return "".join(html)
