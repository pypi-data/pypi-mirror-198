import re
import typing

from john import is_numeric, is_integer

# crz: the clever regex magic below is lifted verbatim from the KiCad repo here:
# https://gitlab.com/kicad/libraries/kicad-library-utils/-/blob/master/common/sexpr.py

term_regex = r"""(?mx)
    \s*(?:
        (?P<brackl>\()|
        (?P<brackr>\))|
        (?P<num>[+-]?\d+\.\d+(?=[\ \)])|\-?\d+(?=[\ \)]))|
        (?P<sq>"([^"]|(?<=\\)")*")|
        (?P<s>[^(^)\s]+)
       )"""

# crz: here I have modified it a bit to make it more readable

# open_bracket_pattern = r"""\("""
# close_bracket_pattern = r"""\)"""
# number_pattern = r"""[+-]?\d+\.\d+(?=[\ \)])|\-?\d+(?=[\ \)])"""
# quoted_string_pattern = r""""([^"]|(?<=\\)")*""""
# string_pattern = r"""[^(^)\s]+"""

# term_regex = fr"""(?mx)
#     \s*(?:
#         (?P<open_bracket>{open_bracket_pattern})|
#         (?P<close_bracket>\))|
#         (?P<number>[+-]?\d+\.\d+(?=[\ \)])|\-?\d+(?=[\ \)]))|
#         (?P<quoted_string>"([^"]|(?<=\\)")*")|
#         (?P<string>[^(^)\s]+)
#        )"""

# crz: ...and the rest is heavily based on same:


def parse_sexpr(sexp: str) -> typing.Any:
    stack = []
    out = []

    all = re.findall(term_regex, sexp)
    # print(all)

    for i, item in enumerate(all):
        # print(f"{i}: '{item[0]}'-'{item[1]}'-'{item[2]}'-'{item[3]}'-'{item[4]}'-'{item[5]}'")

        if '(' == item[0]:
            stack.append(out)
            out = []
        elif ')' == item[1]:
            assert stack, "Trouble with nesting of brackets"
            tmpout, out = out, stack.pop(-1)
            out.append(tmpout)
        elif '' != item[2]:
            if is_integer(item[2]):
                out.append(int(item[2]))
            else:
                out.append(float(item[2]))
        elif '' != item[3]:
            out.append(item[3][1:-1].replace(r"\"", '"'))
        elif '' != item[4]:
            out.append(item[4])
        elif '' != item[5]:
            out.append(item[5])
        else:
            pass

    return out[0]


def build_sexpr(exp, level: int = 0) -> str:

    if isinstance(exp, list):
        indent = '  ' * level
        content = " ".join(build_sexpr(x, level=level+1) for x in exp)
        return f"\n{indent}({content})"

    if isinstance(exp, float) or isinstance(exp, int):
        return str(exp)

    if isinstance(exp, str):
        exp = exp.replace("\"", "\\\"")

        if len(exp) == 0 or (' ' in exp) or ('.' in exp) or ('(' in exp) or ('\n' in exp) or is_numeric(exp):
            exp = f'"{exp}"'

        exp = exp.replace("\n", "\\n")

        return exp

    raise RuntimeError("bad sexpr type")
