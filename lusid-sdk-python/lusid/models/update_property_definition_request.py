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


class UpdatePropertyDefinitionRequest(Model):
    """UpdatePropertyDefinitionRequest.

    :param value_required:
    :type value_required: bool
    :param display_name:
    :type display_name: str
    :param data_format_id:
    :type data_format_id: ~lusid.models.ResourceId
    :param sort:
    :type sort: str
    :param life_time: Possible values include: 'Perpetual', 'TimeVariant'
    :type life_time: str or ~lusid.models.enum
    """

    _attribute_map = {
        'value_required': {'key': 'valueRequired', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'data_format_id': {'key': 'dataFormatId', 'type': 'ResourceId'},
        'sort': {'key': 'sort', 'type': 'str'},
        'life_time': {'key': 'lifeTime', 'type': 'str'},
    }

    def __init__(self, value_required=None, display_name=None, data_format_id=None, sort=None, life_time=None):
        super(UpdatePropertyDefinitionRequest, self).__init__()
        self.value_required = value_required
        self.display_name = display_name
        self.data_format_id = data_format_id
        self.sort = sort
        self.life_time = life_time
