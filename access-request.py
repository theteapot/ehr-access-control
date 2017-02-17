
int_purp_list = {
                "sexual_health": 
                    {
                        "d1": ["p6", "p7"],
                        "d2": ["p7"]
                    },
                "identity_data":
                    {
                        "d1": ["p1"],
                        "d2": ["p6", "p7"],
                        "d3": ["p3", "p4", "p5"]
                    }
                }

acc_pur_list = [
                ["sexual_health", ["p6"]],
                ["identity_data", ["p3", "p1"]]
               ]

def access_request(user_id, sl, apl, acl, ipl):
    
    purpose_response = {}
    
    for request in acc_pur_list:
        data_type = request[0]
        purposes = request[1]
        for data_element in ipl[data_type].keys():
            for purpose in purposes:
                if purpose in ipl[data_type][data_element]:
                    purpose_response[data_type] = data_element
    
    return purpose_response          


print(access_request("1234", "sl", acc_pur_list, "acl", int_purp_list))
    
    
    
