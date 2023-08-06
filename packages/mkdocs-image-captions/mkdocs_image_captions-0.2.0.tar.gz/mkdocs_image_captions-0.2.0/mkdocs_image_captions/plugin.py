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

        match = re.search(pattern, markdown)

        # no match for pattern means images are not present in MD
        if match is None:
            return markdown

        # taking image params
        caption = match.group(1)
        image = match.group(2)
        size = match.group(3)

        if size:
            size = size.split(";")
            size = f"style='width:{size[0]}px;height:{size[1]}px;'"
        else:
            size = ""

        # substituting MD image with HTML
        markdown = re.sub(
            pattern,
            r'<figure class="figure-image">\n' +
            fr'  <img src="{image}" alt="{caption}" {size}>\n' +
            fr'  <figcaption>{caption}</figcaption>\n' +
            r'</figure>',
            markdown
        )

        return markdown
