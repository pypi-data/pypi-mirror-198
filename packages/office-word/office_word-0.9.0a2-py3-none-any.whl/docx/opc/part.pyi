#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author:      thepoy
# @Email:       thepoy@163.com
# @File Name:   part.pyi
# @Created At:  2023-03-20 12:05:12
# @Modified At: 2023-03-20 12:09:19
# @Modified By: thepoy

from typing import Callable, Optional, Dict, Type
from docx.opc.constants import CONTENT_TYPE
from docx.parts.image import ImagePart
from docx.parts.story import BaseStoryPart

PartClassSelector = Callable[[str, str], Optional[Type[ImagePart]]]

class PartFactory(object):
    part_class_selector: Optional[PartClassSelector] = ...
    part_type_for: Dict[CONTENT_TYPE, Type[BaseStoryPart] | Type[XmlPart]] = ...

class Part: ...
class XmlPart(Part): ...
