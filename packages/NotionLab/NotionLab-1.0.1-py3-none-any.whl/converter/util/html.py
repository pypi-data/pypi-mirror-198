from typing import Dict

text_mapping: Dict = {
    "heading_1": "h1",
    "heading_2": "h2",
    "heading_3": "h3",
    "paragraph": "p"
}


def div(child: Dict, is_rich_text: bool):
    style = f"""
        style="display: inline; {style_parser(child["annotations"])}"
    """ if is_rich_text else ""
    return f"""
        {f'<a href="{child["href"]}">' if child["href"] else ""}
            <div {style}>
                {child["text"]["content"]}
            </div>
        {'</a>' if child["href"] else ""}
    """


def style_parser(annotations):
    style = ""
    if annotations["bold"]:
        style += 'font-weight: bold;'
    if annotations["italic"]:
        style += 'font-style: italic;'
    if annotations["underline"]:
        style += 'text-decoration: underline;'
    if annotations["color"]:
        style += f'color: {annotations["color"]};'
    # TODO 其他样式省略
    return style
