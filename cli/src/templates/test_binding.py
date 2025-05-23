from unittest import TestCase

import tree_sitter
import tree_sitter_LOWER_PARSER_NAME


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        try:
            tree_sitter.Language(tree_sitter_LOWER_PARSER_NAME.language())
        except Exception:
            self.fail("Error loading TITLE_PARSER_NAME grammar")
