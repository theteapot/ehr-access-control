
int_purp_list = [   
                    ["sexual_health", ["d1", ["p6", "p7"]], ["d2", ["p7"]]]
                    ["identity_data", ["d1", ["p1"]], ["d2", ["p2", "p3"]], ["d3", ["p3", "p4", "p5"]]]
                ]

acc_pur_list = [
                ["sexual_health", ["p6"]],
                ["identity_data", ["p3", "p1"]]
               ]

def access-request(user_id, sl, apl, acl, ipl):
    num_req = len(apl)
    access_state = [False for x in range(num_req)]
    permit_data = [False for x in range(num_req)]
    check_purpose = [[False for x in range(len(ipl))] for x in range(num_req)]
    
    
