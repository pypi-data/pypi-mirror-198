def _build_slot_sequence_name_dict(slotSequenceJSON):
    """
    Utility method to construct a dictionary of the slot sequence.
    """
    slot_sequence = {}

    for definition in slotSequenceJSON:
        param = definition['slotParameter']
        key = param['key']
        value = param['value']
        slot_sequence[key] = value

    return slot_sequence

def _build_slot_sequence_name_array(slot_sequence):
    """
    Utility method to construct an array of the slot sequence for
    submitting to the API.
    """
    name = []
    position = 0
    for k, v in slot_sequence.items():
        name.append({'position': position,
                     'key': k,
                     'value': v})
        position += 1

    return name

def _build_param_dict(paramGroupsJSON):
    """
    Utility method to collate slot parameters and slot parameter
    groups into a dictionary.
    """
    groups = {}
    for group in paramGroupsJSON:
        name = group['slotParameterGroupName']
        
        params = {}
        for param in group['slotParameters']:
            params[param['key']] = param['value']

        groups[name] = params

    return groups