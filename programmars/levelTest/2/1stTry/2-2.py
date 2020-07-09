def solution(bridge_length, weight, truck_weights):    
    completed = []
    processing = []
    processingTime = []
    
    totalTime = 0

    
    while not(len(truck_weights) == 0 and len(processing) ==0) :
        for i in range(len(processing)):
            if (processingTime[i]==0):
                processing.pop(i)
                processingTime.pop(i)
                break
        
        nowTotalWeight = 0
        for i in range(len(processing)):
            nowTotalWeight = nowTotalWeight + processing[i] 
        if(len(truck_weights) != 0 and nowTotalWeight+truck_weights[0]<=weight):
            processing.append(truck_weights[0])
            processingTime.append(bridge_length)
            truck_weights.pop(0)
                
        for i in range(len(processing)):
            processingTime[i] = processingTime[i] - 1
                    
        totalTime = totalTime + 1
    
    return totalTime

def main():
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    
    print(solution(bridge_length,weight,truck_weights))
    
main()