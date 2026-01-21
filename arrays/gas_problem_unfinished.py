gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

gas_in_tank = 0
gas_tota_used = 0 
start_index = 0
curent_gas = 0 


for i in gas:
    if i == 0:
        start_index = gas[0]
        gas_in_tank += i
    else:
        gas_in_tank += i


for i in cost:
    gas_tota_used += i

if gas_tota_used > gas_in_tank:
    print("There is no valid soulution")
else:
    print("theres a valid soultion")

print(start_index)
