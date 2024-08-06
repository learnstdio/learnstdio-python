#   ---------------------------------------------------------------------------------
#   Copyright (c) Learnstdio. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------
"""Usage illustration of the learnstdio."""

from learnstdio.model import load_model
from sensors import get_phase_iv

ia, va = get_phase_iv("a")
ib, vb = get_phase_iv("b")
ic, vc = get_phase_iv("c")

model = load_model('./samples/learnstdio.model.json')
ground_fault = model.predict(ia, ib, ic, va, vb, vc)

print(f'Ground fault detected: {ground_fault}')
