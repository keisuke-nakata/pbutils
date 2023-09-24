from pathlib import Path
import textwrap

from pbutils import html2md

here = Path(__file__).parent.resolve()


class TestHtml2Md:
    def test_html2md(self) -> None:
        with open(here / "bytes.html", "rb") as f:
            data = f.read()
        md = html2md.html2md(data)
        assert md == textwrap.dedent("""
            Heading 1
            =========

            test

            Heading 2
            ---------

            test

            ### Heading 3

            test

            #### Heading 4

            test

            ##### Heading 5

            test

            * bullet point A
                * bullet point B (bold)
                    * bullet point C (underline)

            * bullet point D (italic)
                * bullet point F (colored)
                    * bullet point G (striked)

            * 日本語文字


            1. ordered list 1
            1. ordered list a
            1. ordered list i


            [linked text](http://example.com)


            indented text
        """).strip()
