import logging
import os
import re
from pathlib import Path
from test.data import TEST_DATA_DIR
from urllib.request import urlopen

import pytest

from rdflib import Graph, Literal, URIRef
from rdflib.plugins.parsers import ntriples

log = logging.getLogger(__name__)

NT_PATH = os.path.relpath(os.path.join(TEST_DATA_DIR, "suites", "nt_misc"), os.curdir)


def nt_file(fn):
    return os.path.join(NT_PATH, fn)


class TestNT:
    def testIssue859(self):
        graphA = Graph()
        graphB = Graph()
        graphA.parse(nt_file("quote-01.nt"), format="ntriples")
        graphB.parse(nt_file("quote-02.nt"), format="ntriples")
        for subjectA, predicateA, objA in graphA:
            for subjectB, predicateB, objB in graphB:
                assert subjectA == subjectB
                assert predicateA == predicateB
                assert objA == objB

    def testIssue78(self):
        g = Graph()
        g.add((URIRef("foo"), URIRef("foo"), Literal("R\u00E4ksm\u00F6rg\u00E5s")))
        s = g.serialize(format="nt")
        assert type(s) == str
        assert "R\u00E4ksm\u00F6rg\u00E5s" in s

    def testIssue146(self):
        g = Graph()
        g.add((URIRef("foo"), URIRef("foo"), Literal("test\n", lang="en")))
        s = g.serialize(format="nt").strip()
        assert s == '<foo> <foo> "test\\n"@en .'

    def testIssue1144_rdflib(self):
        fname = nt_file("lists-02.nt")
        g1 = Graph()
        with open(fname, "r") as f:
            g1.parse(f, format="nt")
        assert 14 == len(g1)
        g2 = Graph()
        with open(fname, "rb") as fb:
            g2.parse(fb, format="nt")
        assert 14 == len(g2)

    def testIssue1144_w3c(self):
        fname = nt_file("lists-02.nt")
        sink1 = ntriples.NTGraphSink(Graph())
        p1 = ntriples.W3CNTriplesParser(sink1)
        with open(fname, "r") as f:
            p1.parse(f)
        assert 14 == len(sink1.g)
        sink2 = ntriples.NTGraphSink(Graph())
        p2 = ntriples.W3CNTriplesParser(sink2)
        with open(fname, "rb") as f:
            p2.parse(f)
        assert 14 == len(sink2.g)

    def test_sink(self):
        s = ntriples.DummySink()
        assert s.length == 0
        s.triple(None, None, None)
        assert s.length == 1

    def test_nonvalidating_unquote(self):
        safe = """<http://example.org/alice/foaf.rdf#me> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.org/alice/foaf1.rdf> ."""
        ntriples.validate = False
        res = ntriples.unquote(safe)
        assert isinstance(res, str)

    def test_validating_unquote(self):
        quot = """<http://example.org/alice/foaf.rdf#me> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.org/alice/foaf1.rdf> ."""
        ntriples.validate = True
        res = ntriples.unquote(quot)
        # revert to default
        ntriples.validate = False
        log.debug("restype %s" % type(res))

    def test_validating_unquote_raises(self):
        ntriples.validate = True
        uniquot = """<http://www.w3.org/People/Berners-Lee/card#cm> <http://xmlns.com/foaf/0.1/name> "R\\u00E4ksm\\u00F6rg\\u00E5s" <http://www.w3.org/People/Berners-Lee/card> ."""
        with pytest.raises(ntriples.ParseError):
            ntriples.unquote(uniquot)
        uniquot = """<http://www.w3.org/People/Berners-Lee/card#cm> <http://xmlns.com/foaf/0.1/name> "R\\\\u00E4ksm\\u00F6rg\\u00E5s" <http://www.w3.org/People/Berners-Lee/card> ."""
        with pytest.raises(ntriples.ParseError):
            ntriples.unquote(uniquot)
        # revert to default
        ntriples.validate = False

    def test_nonvalidating_uriquote(self):
        ntriples.validate = False
        safe = """<http://example.org/alice/foaf.rdf#me> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://xmlns.com/foaf/0.1/Person> <http://example.org/alice/foaf1.rdf> ."""
        res = ntriples.uriquote(safe)
        assert res == safe

    def test_validating_uriquote(self):
        ntriples.validate = True
        uniquot = """<http://www.w3.org/People/Berners-Lee/card#cm> <http://xmlns.com/foaf/0.1/name> "R\\u00E4ksm\\u00F6rg\\u00E5s" <http://www.w3.org/People/Berners-Lee/card> ."""
        res = ntriples.uriquote(uniquot)
        # revert to default
        ntriples.validate = False
        assert res == uniquot

    def test_W3CNTriplesParser_fpath(self):
        fpath = os.path.join(nt_file(os.listdir(NT_PATH)[0]))
        p = ntriples.W3CNTriplesParser()
        with pytest.raises(ntriples.ParseError):
            p.parse(fpath)

    def test_W3CNTriplesParser_parsestring(self):
        p = ntriples.W3CNTriplesParser()
        data = 3
        with pytest.raises(ntriples.ParseError):
            p.parsestring(data)
        with open(nt_file("lists-02.nt"), "r") as f:
            data = f.read()
        p = ntriples.W3CNTriplesParser()
        res = p.parsestring(data)
        assert res is None

    def test_w3_ntriple_variants(self):
        uri = Path(nt_file("test.nt")).absolute().as_uri()

        parser = ntriples.W3CNTriplesParser()
        u = urlopen(uri)
        sink = parser.parse(u)
        u.close()
        # ATM we are only really interested in any exceptions thrown
        assert sink is not None

    def test_bad_line(self):
        data = (
            """<http://example.org/resource32> 3 <http://example.org/datatype1> .\n"""
        )
        p = ntriples.W3CNTriplesParser()
        with pytest.raises(ntriples.ParseError):
            p.parsestring(data)

    def test_cover_eat(self):
        data = (
            """<http://example.org/resource32> 3 <http://example.org/datatype1> .\n"""
        )
        p = ntriples.W3CNTriplesParser()
        p.line = data
        with pytest.raises(ntriples.ParseError):
            p.eat(re.compile("<http://example.org/datatype1>"))

    def test_cover_subjectobjectliteral(self):
        # data = '''<http://example.org/resource32> 3 <http://example.org/datatype1> .\n'''
        p = ntriples.W3CNTriplesParser()
        p.line = "baz"
        with pytest.raises(ntriples.ParseError):
            p.subject()
        with pytest.raises(ntriples.ParseError):
            p.object()
        # p.line = '"baz"@fr^^<http://example.org/datatype1>'
        # self.assertRaises(ntriples.ParseError, p.literal)


class TestBNodeContext:
    def test_bnode_shared_across_instances(self):
        my_sink = FakeSink()
        bnode_context = dict()
        p = ntriples.W3CNTriplesParser(my_sink, bnode_context=bnode_context)
        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000001> .
        """
        )

        q = ntriples.W3CNTriplesParser(my_sink, bnode_context=bnode_context)
        q.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000002> .
        """
        )

        assert len(my_sink.subs) == 1

    def test_bnode_distinct_across_instances(self):
        my_sink = FakeSink()
        p = ntriples.W3CNTriplesParser(my_sink)
        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000001> .
        """
        )

        q = ntriples.W3CNTriplesParser(my_sink)
        q.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000002> .
        """
        )

        assert len(my_sink.subs) == 2

    def test_bnode_distinct_across_parse(self):
        my_sink = FakeSink()
        p = ntriples.W3CNTriplesParser(my_sink)

        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000001> .
        """,
            bnode_context=dict(),
        )

        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000002> .
        """,
            bnode_context=dict(),
        )

        assert len(my_sink.subs) == 2

    def test_bnode_shared_across_parse(self):
        my_sink = FakeSink()
        p = ntriples.W3CNTriplesParser(my_sink)

        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000001> .
        """
        )

        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000002> .
        """
        )

        assert len(my_sink.subs) == 1

    def test_bnode_shared_across_instances_with_parse_option(self):
        my_sink = FakeSink()
        bnode_ctx = dict()

        p = ntriples.W3CNTriplesParser(my_sink)
        p.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000001> .
        """,
            bnode_context=bnode_ctx,
        )

        q = ntriples.W3CNTriplesParser(my_sink)
        q.parsestring(
            """
        _:0 <http://purl.obolibrary.org/obo/RO_0002350> <http://www.gbif.org/species/0000002> .
        """,
            bnode_context=bnode_ctx,
        )

        assert len(my_sink.subs) == 1


class FakeSink(object):
    def __init__(self):
        self.subs = set()

    def triple(self, s, p, o):
        self.subs.add(s)
