#!/usr/bin/env python
from .config import math_code

tex_begin = r'''
\documentclass[UTF8]{article}
\usepackage{xeCJK}
\usepackage{amsmath,amssymb}
\begin{document}
'''
tex_end = r'''
\end{document}
'''
char_limit = 2000


def variable_code(count):
    return math_code + '_' + '_'.join(list(str(count)))


def is_connected(line_above, line_below):
    if len(line_above) > 0 and len(line_below) > 0:
        if line_above[-1] != '.' and line_below[0].islower():
            return True
    return False


def connect_paragraphs(text):
    text_split = text.split('\n')
    i = 0
    while i < len(text_split) - 1:
        line_above = text_split[i]
        line_below = text_split[i + 1]
        if is_connected(line_above, line_below):
            text_split[i] = text_split[i] + text_split[i + 1]
            del text_split[i + 1]
        else:
            i += 1
    return '\n'.join(text_split)


def get_first_word(line):
    words = line.split(' ')
    for word in words:
        if len(word) > 0:
            return word
    return ''


def argmax(array):
    return array.index(max(array))


def split_paragraphs(text):
    text_split = []
    for paragraph in text.split('\n'):
        if len(paragraph) > char_limit:
            lines = paragraph.split('.')
            first_words = [get_first_word(line) for line in lines]
            first_length = [len(word) if (len(word) > 0 and word[0].isupper()) else 0 for word in first_words]
            first_length[0] = 0
            position = argmax(first_length)
            par1 = split_paragraphs('.'.join(lines[0:position]) + '.')
            par2 = split_paragraphs('.'.join(lines[position:]))
            text_split.extend([par1, par2])
        else:
            text_split.append(paragraph)
    return '\n'.join(text_split)


def is_title(line_above, line_below):
    if len(line_above) > 0 and len(line_below) > 0:
        if line_above[-1] != '.' and (not line_above[0].islower()) and line_below[0].isupper():
            return True
    return False


def split_titles(text):
    text_split = text.split('\n')
    i = 0
    while i < len(text_split) - 1:
        line_above = text_split[i]
        line_below = text_split[i + 1]
        if is_title(line_above, line_below):
            text_split[i] = '\n\n' + text_split[i] + '\n\n'
        i += 1
    return '\n'.join(text_split)


def convert_next(text, pattern_begin, pattern_end, count):
    position_begin = text.find(pattern_begin)
    position_end = text.find(pattern_end)
    l = len(pattern_end)
    assert not ((position_begin == -1) ^ (position_end == -1))
    before_slic = slice(0, position_begin)
    eq_slic = slice(position_begin, position_end + l)
    after_slic = slice(position_end + l, None)
    if position_begin != -1:
        eq = text[eq_slic]
        text = text[before_slic] + variable_code(count) + text[after_slic]
        return text, eq
    else:
        return None


def convert_equations(text):
    eqs = []
    count = 0
    for pattern_begin, pattern_end in [('\\(', '\\)'), ('\\[', '\\]')]:
        while True:
            result = convert_next(text, pattern_begin, pattern_end, count)
            if result is None:
                break
            else:
                text, eq = result
                eqs.append(eq)
                count += 1
    return text, eqs


def translate_by_part(translator, text, language_to, language_from, limit):
    lines = text.split('\n')
    parts = []
    part = ''
    for line in lines:
        if len(line) >= limit:
            assert False, "one line is too long"
        if len(part) + len(line) < limit - 10:
            part = part + '\n' + line
        else:
            parts.append(part)
            part = line
    parts.append(part)
    parts_translated = []
    for i, part in enumerate(parts):
        parts_translated.append(translator.translate(part, language_to, language_from))
        print(i, '/', len(parts))
    text_translated = '\n'.join(parts_translated)
    return text_translated


def translate(translator, input_path, output_path, engine, language_to, language_from, debug):
    text_original = open(input_path).read()
    text_original = connect_paragraphs(text_original)
    text_converted, eqs = convert_equations(text_original)
    text_converted = text_converted.replace('\\pm', '$\\pm$')
    text_converted = text_converted.replace('Eq.', 'equation')
    text_converted = split_paragraphs(text_converted)
    text_converted = split_titles(text_converted)
    text_translated = translate_by_part(translator, text_converted, language_to, language_from, char_limit)
    if debug:
        print(text_converted, file=open("text_old", "w"))
        print(text_translated, file=open("text_new", "w"))
    text_final = text_translated

    for count, eq in list(enumerate(eqs))[::-1]:
        text_final = text_final.replace(variable_code(count), eq)

    with open(output_path, "w") as file:
        print(tex_begin, file=file)
        print(text_final, file=file)
        print(tex_end, file=file)
