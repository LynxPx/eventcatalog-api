from neomodel import StringProperty, StructuredNode


class Badge(StructuredNode):
    content = StringProperty(required=True)
    backgroundColor = StringProperty(required=True)
    textColor = StringProperty(required=True)


def create_badge(content, backgroundColor, textColor):
    badge = Badge(
        content=content, backgroundColor=backgroundColor, textColor=textColor
    ).save()
    return badge


def update_badge(badge_content, new_backgroundColor, new_textColor):
    badge = Badge.nodes.get(content=badge_content)
    badge.backgroundColor = new_backgroundColor
    badge.textColor = new_textColor
    badge.save()
    return badge
