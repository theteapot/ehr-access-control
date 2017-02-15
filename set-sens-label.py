""" Algorithim for setting the sensitivity label.
"""

sensitivity_tree = ["ehr",
                    ["identity_data"], 
                    ["general_health"],
                    ["sexual_health",
                        ["s1"],
                        ["s2"]
                    ], 
                    ["mental_health"],
                    ["dermatology_health"]
                    ]

access_control_list = {
                    "peter":[ ["ehr", "null"], ["general_health", "null"] ], 
                    "sandra":[ ["ehr", "sexual_health", "mental_health"],
                        ["dermatology_health", "sexual_health", "null"] ], 
                    "bill":[ ["ehr", "mental_health", "dermatology_health"], 
                        ["general_health", "sexual_health", "null"] ],
                    "matt":[ ["ehr", "sexual_health", "dermatology_health"],
                        ["general_health", "mental_health", "null"] ],
                    "david":[ ["s1", "null"], ["sexual_health", "null"] ]
                    }

def set_sens_label(user_id, access_control_list):
    """
    """
    sl = []
    
    p_sl = access_control_list[user_id][0]
    ha_sl = access_control_list[user_id][1]
    
    if bfs(p_sl[0]) <= max([bfs(x) for x in ha_sl[:-1]]):
        use_asl_p = True
    else:
        use_asl_p = False
        
    if intersect(p_sl[1:], ha_sl[:-1]) == []:
        access_conflict = False
    else:
        access_conflict = True
    
    if access_conflict:
        for conflict in intersect(p_sl[1:], ha_sl[:-1]):
            p_sl.remove(conflict)
    
    if use_asl_p:
        sl = p_sl[0], p_sl[1:]    
    elif not use_asl_p:
        sl = ha_sl[:-1], p_sl[1:]
    
    return sl


def bfs(search_term, tree = sensitivity_tree, count = 0):
    count += 1
    for element in tree:
        if element == search_term:
            return count
        elif isinstance(element, list) and element != []:
            result = bfs(search_term, element, count)
            if result != None: return result

def intersect(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result += [element]
    return result

print(set_sens_label("david", access_control_list))


