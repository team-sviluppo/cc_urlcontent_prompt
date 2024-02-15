from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin
from enum import Enum


# Plugin settings
class PluginSettings(BaseModel):
    remove_html_tags: bool = False


# hook to give the cat settings
@plugin
def settings_schema():
    return PluginSettings.schema()
