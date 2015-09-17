from unittest import TestCase
from rucola import Rucola
from rucola_permalinks import Permalinks


class Test(TestCase):

    def setUp(self):

        self.app = Rucola()

    def test_default(self):

        f = self.app.create('a/b.html')
        b = self.app.create('a/b.txt')
        self.app.use(Permalinks())

        self.assertEqual('a/b/index.html', f.path)
        self.assertEqual('a/b.txt', b.path)

    def test_pretty(self):

        f = self.app.create('a/b.html')
        self.app.use(Permalinks('pretty'))

        self.assertEqual('a/b/index.html', f.path)

    def test_metadata(self):

        f = self.app.create('a/b.html')
        f['foo'] = 'banana'
        self.app.use(Permalinks('{foo}.html'))

        self.assertEqual('banana.html', f.path)

    def test_permalink_false(self):

        f = self.app.create('a/b.html')
        f['permalink'] = False
        self.app.use(Permalinks())

        self.assertEqual('a/b.html', f.path)

    # Style parameters

    def test_all(self):

        f = self.app.create('a/b/c.html')
        self.app.use(
            Permalinks(':basename/:title/index.:ext')
        )

        self.assertEqual('a/b/c/index.html', f.path)

    def test_filename(self):

        f = self.app.create('a/b.html')
        self.app.use(
            Permalinks('test/:filename')
        )

        self.assertEqual('test/b.html', f.path)

    def test_basename(self):

        f = self.app.create('a/b/c.html')
        self.app.use(
            Permalinks('test/:basename')
        )

        self.assertEqual('test/a/b', f.path)

    def test_extension(self):

        f = self.app.create('a/b/c.html')
        self.app.use(
            Permalinks(':extension/:ext')
        )

        self.assertEqual('html/html', f.path)

    def test_title(self):

        f = self.app.create('a/b/c.html')
        self.app.use(
            Permalinks(':title')
        )

        self.assertEqual('c', f.path)
