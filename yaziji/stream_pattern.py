#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  stream_pattern.py
#  
#  Copyright 2020 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
from  yaziji_const import STREAMS
class streamPattern:
    """
    a class to handle pattern stream order
    """
    def __init__(self, stream_type):

        self.stream = STREAMS.get(stream_type, STREAMS.get('default',{}))
    
    def add(self, attribute, before="", after=""):
        """
        add an attribute after or before another attribute
        """
        pass
    def remove(self, name):
        """
        remove a component from stream
        """
        if name in self.stream:
            self.stream.remove(name)
    def __list__(self,):
        """
        list of content
        """
        return list(self.stream)

    def __str__(self,):
        """
        str of content
        """
        return (u"".join(["<%s>"%x for x in self.stream]))
        #~ return u" ".join(self.stream)

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
