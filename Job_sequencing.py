#this function prints the list of jobs with maximum profit
def PrintScheduledJobs(Job_Table,n):
      length=len(Job_Table)
      for i in range(length):
            for j in range(n-1-i):
                  if Job_Table[j][2]<Job_Table[j+1][2]:
                        Job_Table[j],Job_Table[j+1]=Job_Table[j+1],Job_Table[j]
  
#to keep track of free time slots     
      Slots=[False]*n

#sequence of final jobs
      JobSequence=['1']*n

      for i in range(length):
            for j in range(min(Job_Table[i][1]-1,n-1),-1,-1):
                  if Slots[j]==False:
                        Slots[j]=True
                        JobSequence[j]=Job_Table[i][0]
                        break
      
      print(JobSequence)

if __name__=="__main__":
      Job_Table=[['a',2,100],['b',1,17],['c',2,27],['d',1,25],['e',3,15]]
      PrintScheduledJobs(Job_Table,3)
      
      
