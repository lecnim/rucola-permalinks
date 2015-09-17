import os
import re
import posixpath


class Permalinks:

    def __init__(self, style='pretty'):
        self.style = style

    def __call__(self, app):

        for f in app.find('**/*.html'):

            p = f.get('permalink', self.style)
            if not p:
                continue

            f.path = self.permalink(p, f)

    def permalink(self, style, file):
        """Set new item url."""

        style = self._get_build_style(style, file)

        # { foo }
        style = style.format(**file)

        keywords = re.findall("(:[a-zA-z]*)", style)
        url = posixpath.normpath(style)

        # foo/bar.html => foo, bar.html
        basename, filename = os.path.split(file.path)
        title, ext = os.path.splitext(filename)

        items = {
            'basename': basename,   # foo
            'filename': filename,   # bar.html
            'title': title,         # bar
            'extension': ext[1:],   # html
            'ext': ext[1:]          # html
        }

        for key in keywords:
            if key[1:] in items:
                # :filename => filename
                url = url.replace(key, str(items[key[1:]]))

        # //home/a.html => home/a.html
        return url.lstrip(posixpath.sep)

    def _get_build_style(self, permalink, file):

        if permalink == 'pretty':

            # Prevent 'index.html' => 'index/index.html'
            if os.path.split(file.path)[1] == 'index.html':
                return ':basename/:title.html'
            return ':basename/:title/index.html'

        return permalink
