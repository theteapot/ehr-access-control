

int_pur_list =  [
                    ["sexual_health", ["p1", "p2"]],
                    ["mental_health", ["p2", "p3"]]
                ]
                
acc_pur_list =  [
                    ["sexual_health", ["p1"]],
                    ["mental_health", ["p3", "p4"]],
                ]

sens_level = ["ehr", "mental_health"] #allowed EHR, prohib mental_health

def access_request(user_id, sl, apl, acl, ipl):
    num_req = len(apl)
    access_state = [False for x in range(num_req)]
    permit_data = [False for x in range(num_req)]
    check_purpose = [[False for y in x[1]] for x in acc_pur_list]
    
    prohib_sl = sl[1:]
    for i in range(num_req):
        
        #checking if user has access to that data type
        if ipl[i][0] in prohib_sl:
            permit_data[i] = False
        else:
            permit_data[i] = True
        
        #checking if that data type allows that purpose
        for j in range(len(apl[i][1])):
            if apl[i][1][j] in int_pur_list[i][1]:
                check_purpose[i][j] = True
        
        #checking if both prior conditions are true
        if (permit_data[i] == True) and (False not in check_purpose[i]):
            access_state[i] = True

    return access_state
        
    
    


print(access_request("1234", sens_level, acc_pur_list, "acl", int_pur_list))
    
    
    
