#!/usr/bin/env python3
from json import JSONEncoder, dumps
from typing import List, Dict, Iterable, Any
from .widgets import Widget

def strip_nulls(obj: Iterable[Any]) -> Iterable[Any]: 
  return {k: v for k, v in obj.items() if v is not None}

class DashboardEncoder(JSONEncoder):
  def default(self, obj: Any) -> str: # pylint: disable=E0202
    to_json_data = getattr(obj, 'to_json_data', None)

    if to_json_data:
      return strip_nulls(to_json_data())
    
    return JSONEncoder.default(self, obj)

class Dashboard(object):
  def __init__(self, start: str = None, end: str = None, periodOverride: str = None, widgets: List[Widget] = None) -> None:
    self.start: str = start
    self.end: str = end
    self.periodOverride: str = periodOverride
    self.widgets: List[Widget] = widgets
  
  @property
  def end(self) -> str:
    return self._end
  
  @end.setter
  def end(self, end: str) -> None:
    if not self.start and end:
      raise ValueError('Cannot set end without setting start')
    
    self._end = end

  @property
  def periodOverride(self) -> str:
    return self._periodOverride
  
  @periodOverride.setter
  def periodOverride(self, periodOverride: str) -> None:
    valid = ['auto', 'inherit', None]

    if periodOverride not in valid:
      raise ValueError(f'periodOverride must be one of: {valid}')
    
    self._periodOverride = periodOverride

  def add_widget(self, widget: Widget) -> None:
    if self.widgets is None:
      self.widgets = [widget]
    else:
      self.widgets.append(widget)
  
  def to_json_data(self) -> str:
    return {
      'start': self.start,
      'end': self.end,
      'periodOverride': self.periodOverride,
      'widgets': self.widgets
    }

  def to_json(self, **kwargs) -> Dict[str, Any]:
    return dumps(self, cls=DashboardEncoder, **kwargs)
  