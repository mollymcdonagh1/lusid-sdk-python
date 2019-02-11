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


class ValuationsReconciliationRequest(Model):
    """Specification for the reconciliation request. Left and Right hand sides are
    constructed. Each consists of a valuation of a portfolio
    using an aggregation request. The results of this can then be compared to
    each other. The difference, which is effectively a risk based
    difference allows comparison of the effects of changing a recipe, valuation
    date, or (though it may or may not make logical sense) a portfolio.
    For instance, one might look at the difference in risk caused by the
    addition of transaction to a portfolio, or through changing the valuation
    methodology or system.

    :param left: The specification of the left hand side of the valuation
     (risk) reconciliation
    :type left: ~lusid.models.ValuationReconciliationRequest
    :param right: The specification of the right hand side of the valuation
     (risk) reconciliation
    :type right: ~lusid.models.ValuationReconciliationRequest
    :param instrument_property_keys: Instrument properties to be included with
     any identified breaks. These properties will be in the effective and AsAt
     dates of the left portfolio
    :type instrument_property_keys: list[str]
    """

    _validation = {
        'left': {'required': True},
        'right': {'required': True},
        'instrument_property_keys': {'required': True},
    }

    _attribute_map = {
        'left': {'key': 'left', 'type': 'ValuationReconciliationRequest'},
        'right': {'key': 'right', 'type': 'ValuationReconciliationRequest'},
        'instrument_property_keys': {'key': 'instrumentPropertyKeys', 'type': '[str]'},
    }

    def __init__(self, left, right, instrument_property_keys):
        super(ValuationsReconciliationRequest, self).__init__()
        self.left = left
        self.right = right
        self.instrument_property_keys = instrument_property_keys
