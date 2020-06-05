import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


def register(linter):
    linter.register_checker(JflyChecker(linter))

class JflyChecker(BaseChecker):
    """ This checker makes sure you have no variables named jfly """

    __implements__ = IAstroidChecker

    name = 'j3-no-jfly'
    priority = -1
    msgs = {
        # The current largest "real" warning code is W1662
        'W5000': (
            "Has a variable named 'jfly'",  # (displayed-message, what shows up on any violations)
            'j3-no-jfly',  # (message-symbol, can be used with `pylint<colon>disable=<message-symbol>` to silence it)
            "Please do not call any of your variables 'jfly'",  # (message-help, will show in `pylint --list-msgs`)
        ),
    }
    options = (
        (
            'j3-no-jfly',
            {
                'default': True,
                'type': 'yn',
                'metavar': '<y_or_n>',
                'help': "Forbid variables named 'jfly'",
            },
        ),
    )

    def visit_assignname(self, node: astroid.node_classes.AssignName):
        """ Make sure that any callable nodes are not named print.

        Because we only have access to the AST, we technically cannot
        know if the callable named `print` is *actually* going to be
        __builtins__.print at runtime. That's fine, though, since
        `redefined-builtin` should catch any obvious reassignments
        of the print.

        For example, this checker *cannot* detect:

            say = print
            say("Hello")

        It can detect:

            print("Hello")

        If we want to forbid referencing the `print` built-in whatsoever, this
        is very possible! See the way that pylint enforces other "bad" builtins.
        """
        if not self.config.j3_no_jfly:
            return

        if node.name == "jfly":
            self.add_message('j3-no-jfly', node=node)
