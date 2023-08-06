import re

from mkdocs.plugins import BasePlugin


class ImageCaptionsPlugin(BasePlugin):

    def on_page_markdown(self, markdown: str, **kwargs) -> str:
        """
        Convert incoming MD image element into HTML <figure> with captions. The following formats are expected:
            - ![Informative image caption](/docs/assets/images/image.png) - image without size specification
            - ![Informative image caption](/docs/assets/images/image.png){100;200} - image with specification of
                width and height

        Args:
            markdown: MD source text of page

        Return:
            Formatted MD text of page
        """
        pattern = re.compile(r'!\[(.*?)\]\((.*?)\)(?:\{(.*?)\})?', flags=re.IGNORECASE)

        for match in re.finditer(pattern, markdown):
            # taking image params
            caption = match.group(1)
            image = match.group(2)
            size = match.group(3)

            # preparing HTML size settings if present
            if size:
                size = size.split(";")
                size = f"style='width:{size[0]}px;height:{size[1]}px;'"
            else:
                size = ""

            # substituting MD image with HTML
            markdown = markdown.replace(
                match.group(0),
                "<figure class='figure-image'>\n" +
                f"  <img src='{image}' alt='{caption}' {size}>\n" +
                f"  <figcaption>{caption}</figcaption>\n" +
                "</figure>"
            )

        return markdown
