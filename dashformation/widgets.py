#!/usr/bin/env python3
from typing import Dict, Any

class Widget(object):
  def __init__(self, type: str, properties: Dict[str, Any], x: int = None, y: int = None, width: int = None, height: int = None) -> None:
    self.type: str = type
    self.properties: Dict[str, Any] = properties

    if (x is not None and y is None) or (y is not None and x is None):
      raise ValueError('x or y cannot be provided on their own')

    self.x: int = x
    self.y: int = y

    self.width: int = width
    self.height: int = height
  
  @property
  def type(self) -> str:
    return self._type
  
  @type.setter
  def type(self, type: str) -> None:
    valid = ['metric', 'text']

    if type not in valid:
      raise ValueError(f'type must be one of: {valid}')
    
    self._type = type

  @property
  def x(self) -> int:
    return self._x
  
  @x.setter
  def x(self, x: int) -> None:
    if x is not None and (x < 0 or x > 23):
      raise ValueError('x must be between 0 - 23')
    
    self._x = x
  
  @property
  def y(self) -> int:
    return self._y
  
  @y.setter
  def y(self, y: int) -> None:
    if y is not None and (y < 0):
      raise ValueError('y must be greater than 0')
    
    self._y = y
  
  @property
  def width(self) -> int:
    return self._width
  
  @width.setter
  def width(self, width: int) -> None:
    if width is not None and (width < 1 or width > 24):
      raise ValueError('width must be between 1 - 24')
    
    self._width = width
  
  @property
  def height(self) -> int:
    return self._height
  
  @height.setter
  def height(self, height: int) -> None:
    if height is not None and (height < 1 or height > 1000):
      raise ValueError('height must be between 1 - 1000')
    
    self._height = height
  
  def to_json_data(self) -> str:
    return {
      'type': self.type,
      'x': self.x,
      'y': self.y,
      'width': self.width,
      'height': self.height,
      'properties': self.properties
    }

class TextWidget(Widget):
  def __init__(self, markdown: str, type: str = 'text', **kwargs) -> None:
    properties = {
      'markdown': markdown
    }

    super().__init__(type=type, properties=properties, **kwargs)