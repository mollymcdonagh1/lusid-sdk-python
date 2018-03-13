# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReferencePortfolioConstituentDto(Model):
    """ReferencePortfolioConstituentDto.

    :param id: Identifier for this constituent
    :type id: str
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param quantity:
    :type quantity: float
    :param type: Possible values include: 'Shares', 'Weight', 'Nominal'
    :type type: str or ~lusid.models.enum
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        'quantity': {'key': 'quantity', 'type': 'float'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, id=None, properties=None, quantity=None, type=None):
        super(ReferencePortfolioConstituentDto, self).__init__()
        self.id = id
        self.properties = properties
        self.quantity = quantity
        self.type = type
