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


class TxnMovementMetaDataDto(Model):
    """TxnMovementMetaDataDto.

    :param movement_types: The movement types. Possible values include:
     'Settlement', 'Traded', 'ForwardFx', 'Commitment', 'Receivable',
     'CashSettlement', 'Accrual'
    :type movement_types: str or ~lusid.models.enum
    :param side: The Side. Possible values include: 'Side1', 'Side2',
     'BondInt'
    :type side: str or ~lusid.models.enum
    :param direction:
    :type direction: int
    :param properties:
    :type properties: list[~lusid.models.PropertyDto]
    :param mappings:
    :type mappings: list[~lusid.models.TxnPropertyMappingDto]
    """

    _validation = {
        'movement_types': {'required': True},
        'side': {'required': True},
        'direction': {'required': True},
    }

    _attribute_map = {
        'movement_types': {'key': 'movementTypes', 'type': 'str'},
        'side': {'key': 'side', 'type': 'str'},
        'direction': {'key': 'direction', 'type': 'int'},
        'properties': {'key': 'properties', 'type': '[PropertyDto]'},
        'mappings': {'key': 'mappings', 'type': '[TxnPropertyMappingDto]'},
    }

    def __init__(self, movement_types, side, direction, properties=None, mappings=None):
        super(TxnMovementMetaDataDto, self).__init__()
        self.movement_types = movement_types
        self.side = side
        self.direction = direction
        self.properties = properties
        self.mappings = mappings
