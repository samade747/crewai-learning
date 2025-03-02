from crewai.flow.flow import flow, start, listen
import time

#Creating a class
class SimpleFlow(flow):

    @start()
    #inheriting the flow class
    def function1(self):
        return 'step1'
        time.sleep(3)
    
    # its wait for function1 to complete
    @listen(function1)
    def function2(self):
        return 'step2'
        time.sleep(3)


    @listen(function2)
    def function3(self):
        return 'step3'
        time.sleep(3)





def kickoff():
   obj = SimpleFlow()
   obj.kickoff() 