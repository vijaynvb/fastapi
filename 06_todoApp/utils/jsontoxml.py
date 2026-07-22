from xml.etree.ElementTree import Element, SubElement, tostring

def _build_xml(parent: Element, value):
    if isinstance(value, dict):
        for key, child_value in value.items():
            child = SubElement(parent, str(key))
            _build_xml(child, child_value)
        return

    if isinstance(value, list):
        for item in value:
            child = SubElement(parent, "item")
            _build_xml(child, item)
        return

    parent.text = "" if value is None else str(value)


def _json_to_xml_bytes(data) -> bytes:
    root = Element("response")
    _build_xml(root, data)
    return tostring(root, encoding="utf-8", xml_declaration=True)


async def _read_response_body_bytes(response) -> bytes:
    if hasattr(response, "body") and response.body is not None:
        return response.body

    body_chunks = [chunk async for chunk in response.body_iterator]
    return b"".join(body_chunks)
