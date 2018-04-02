def tag(name, *content, cls=None, **attrs):
    """

    :param name: positional
    :param content: multiple allowed
    :param cls: keyword-only, after an argument with prefix *
    :param attrs: keyword,captured as a dict
    :return: Generate one or more HTML tags
    """
    if cls is not None:
        attrs['class'] = ''
    if attrs:
        attr_str = ''.join(
            ' %s="%s"' % (attr, value)
            for attr, value
            in sorted(attrs.items())
        )
    else:
        attr_str = ''
    if content:
        return '\n'.join(
            '<%s%s>%s</%s>' %
            (name, attr_str, c, name) for c in content
        )
    else:
        return '<%s%s />' % (name, attr_str)