from typing import Dict

from notion_client import Client
from notion_client.api_endpoints import PagesEndpoint

from notion_lab.converter.util.html import text_mapping, div


class ConverterBase(object):
    _notion: Client
    _api_token: str = ""
    _title: str = ""
    _ctx: Dict

    def __init__(
            self,
            api_token: str,
            block_id: str,
            is_page: bool = False
    ):
        self._api_token = api_token
        self._notion: Client = Client(auth=api_token)
        if is_page:
            page: PagesEndpoint = self._notion.pages.retrieve(page_id=block_id)
            self._title = page["properties"]["title"]["title"][0]["plain_text"]
        self._ctx = self._notion.blocks.children.list(block_id=block_id)["results"]

    def convert(self):
        pass


class HtmlConverter(ConverterBase):
    _html: str = ""
    _bulleted_list_counter: int = 0

    def convert(
            self,
            is_rich_text: bool = True
    ):
        if self._title:
            self._html += f"<title>{self._title}</title>"
        for block in self._ctx:
            b_type = block["type"]
            # pprint(b_type)
            b_ctx = block[f"{b_type.lower()}"]
            if b_type in text_mapping:
                """
                H1,H2,H3,P 转换
                """
                if len(b_ctx["rich_text"]) != 0:
                    r: str = ""
                    for child in b_ctx["rich_text"]:
                        r += div(child, is_rich_text)
                    self._html += f"""
                    <{text_mapping[b_type]}>
                        {r}
                    </{text_mapping[b_type]}>
                    """
                else:
                    self._html += "<br />"
            elif b_type == "image":
                """
                Img 转换
                """
                if b_ctx["type"] == "file":
                    self._html += f"""
                        <img src="{b_ctx["file"]["url"]}" />
                    """
                elif b_ctx["type"] == "external":
                    self._html += f"""
                        <img src="{b_ctx["external"]["url"]}" />
                    """
            elif b_type == "bulleted_list_item":
                """
                无序列表转换
                """
                if self._bulleted_list_counter == 0:
                    """
                    无序列表开头
                    """
                    self._html += "<ul>"
                self._bulleted_list_counter += 1
                r: str = ""
                for child in b_ctx["rich_text"]:
                    r += div(child, is_rich_text)
                self._html += f"""
                    <li>
                        {r}
                    </li>
                """
            elif b_type == "toggle":
                """
                折叠框转换
                """
                r: str = HtmlConverter(
                    api_token=self._api_token,
                    block_id=block["id"],
                    is_page=False
                ).convert(is_rich_text)
                self._html += "<details>"
                self._html += "<summary>"
                for child in b_ctx["rich_text"]:
                    self._html += div(child, is_rich_text)
                self._html += "</summary>"
                self._html += r
                self._html += "</details>"
            if b_type != "bulleted_list_item" and self._bulleted_list_counter != 0:
                """
                无序列表封底&计数器复位
                """
                self._html += "</ul>"
                self._bulleted_list_counter = 0
        return self._html


class MDConverter(ConverterBase):
    pass
